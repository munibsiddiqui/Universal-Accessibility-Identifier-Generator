
# Accessibility Identifier Updater

## Overview
Accessibility Identifier Updater is a Python-based command-line tool designed to automatically update accessibility identifiers in Xcode project files. It processes both iOS and macOS storyboard files (`.xib` and `.storyboard`), appending the `viewController`'s `customClass` value before each outlet property in the accessibility identifiers. The tool provides functionality to exclude specific directories from the search, allowing for greater flexibility in large projects with multiple subprojects or dependencies like CocoaPods.

## Features
- Automatically processes `.xib` and `.storyboard` files for both iOS and macOS platforms.
- Multithreading support for efficient handling of multiple files.
- Exclusion of specific directories from the file search (e.g., Pods, Build directories).
- Command-line interface for easy usage and integration into development workflows.
- Detailed logging of the processing for easy tracking and debugging.

## Requirements
- Python 3.x


## Installation
Clone the repository to your local machine:

```bash
git clone https://github.com/munibsiddiqui/Xcode-Auto-Accessibility-Identifier-Generator-iOS.git
cd Xcode-Auto-Accessibility-Identifier-Generator-iOS
```

## Usage
Navigate to the script directory and run the script with the required project path:

```bash
python3 main.py /path/to/your/xcode/project/root/folder
```

To exclude specific directories (e.g., Pods, Build), use the `--exclude` option:

```bash
python main.py /path/to/your/xcode/project --exclude Pods Build
```

### Options
- `project_path`: Mandatory. The root folder of your xcode project.
- `--exclude`: Optional. List of directories to exclude from the search.



After running the script, each UI element in your Xcode project's `.storyboard` or `.xib` files will have an accessibility identifier set based on the name of its view controller and the name of the property. 

For example, if you have a `UILabel` connected to a `ViewController` with the property name `lblName`, the tool will set the accessibility identifier to `ViewController_lblName`.

This standard naming convention helps maintain consistency across your project and simplifies the process of identifying UI elements for accessibility purposes and UI testing.

## Structure
- `main.py`: The main script that orchestrates the file scanning, processing, and exclusion logic.
- `accessibility.py`: Contains the core functionality for updating the accessibility identifiers.

## Contributing
Contributions to Accessibility Identifier Updater are welcome. Please follow the standard code practices and submit a pull request for review.

## License
GPLv2

## Contact
For queries or feedback, please contact Munib Siddiqui at munibsiddiqui@gmail.com.

## Credits
This project is a fork and extension of [Gini-Apps's Xcode-Auto-Accessibility-Identifier-Generator-iOS](https://github.com/Gini-Apps/Xcode-Auto-Accessibility-Identifier-Generator-iOS). Credit goes to the original authors for their foundational work on which this tool is built.

---

