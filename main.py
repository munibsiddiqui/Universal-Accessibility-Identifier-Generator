import argparse
import os
import time
import logging
from accessibility import add_accessibility_identifier, add_automation_id_to_wpf_lxml
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_files(project_path, exclude_dirs):
    all_files = []
    ui_files_path = []

    # Configure logging to save in user's Library/Logs
    home_dir = os.path.expanduser('~')
    log_directory = os.path.join(home_dir, 'Library', 'Logs', 'AccessibilityUpdater')
    log_file_path = os.path.join(log_directory, 'accessibility_update.log')

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logging.basicConfig(level=logging.INFO, filename=log_file_path, filemode='w', 
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Get all files path and save, excluding specified directories
    for dirpath, _, files in os.walk(project_path):
        if any(excluded in dirpath for excluded in exclude_dirs):
            continue  # Skip excluded directories

        for file_name in files:
            if file_name.endswith('.xib') or file_name.endswith('.storyboard') or file_name.endswith('.xaml'):
                rel_file = os.path.join(dirpath, file_name)
                ui_files_path.append(rel_file)

    logging.info(f"UI files found: {ui_files_path}")

    # Check if there are UI files to process
    if not ui_files_path:
        logging.info("No .xib, .storyboard, or .xaml files found in the provided path.")
        return

    # Maximum number of workers
    max_workers = min(len(ui_files_path), 10)

    # Run "add_accessibility_if_needed" in parallel tasks
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_path = {}
        for xml_path in ui_files_path:
            if xml_path.endswith('.xaml'):
                future_to_path[executor.submit(add_automation_id_to_wpf_lxml, xml_path)] = xml_path
            else:
                future_to_path[executor.submit(add_accessibility_identifier, xml_path)] = xml_path
                
        for future in as_completed(future_to_path):
            path = future_to_path[future]
            try:
                future.result()
                logging.info(f"Successfully processed file: {path}")
            except Exception as exc:
                logging.error(f"Error processing file {path}: {exc}", exc_info=True)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Update accessibility identifiers in Xcode and WPF project files.")
    parser.add_argument("project_path", help="Path to the project directory")
    parser.add_argument("--exclude", nargs='*', default=[], 
                        help="List of directory names to exclude (e.g., --exclude Pods Build)")

    # Parsing arguments
    args = parser.parse_args()

    # Check if the path exists
    if not os.path.exists(args.project_path):
        print("The provided path does not exist.")
    else:
        start = time.time()
        process_files(args.project_path, args.exclude)
        end = time.time()
        logging.info(f"Time taken for execution: {end - start} seconds")