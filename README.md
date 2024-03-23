# Cross-Platform Accessibility ID Injector 🚀 

## Overview 🌐
Accessibility Identifier Updater is a Python-based command-line tool designed to automatically update accessibility identifiers in Xcode and WPF project files. It processes iOS and macOS storyboard files (`.xib` and `.storyboard`), as well as WPF `.xaml` files, appending the `viewController`'s `customClass` value or the root element's `x:Class` value before each outlet property or control in the accessibility identifiers. This tool offers the functionality to exclude specific directories from the search, providing flexibility in large projects with multiple subprojects or dependencies like CocoaPods and NuGet packages.

## Features ✨
- Automatically processes `.xib`, `.storyboard`, and `.xaml` files for iOS, macOS, and WPF platforms.
- Specifically adds automation IDs to the following WPF elements for enhanced accessibility and UI testing:
  - `Button`, `TextBox`, `ComboBox`, `ListBox`, `RadioButton`, `CheckBox`,
  - `MenuItem`, `TabControl`, `ListView`, `TreeView`, `DataGrid`, `Expander`,
  - `ScrollViewer`, `Slider`, `ProgressBar`, `GroupBox`, `Label`, `Hyperlink`,
  - `Image`, `WebBrowser`, `Calendar`, `DatePicker`, `TimePicker`, `PasswordBox`,
  - `RichTextBox`, `DocumentViewer`, `MediaElement`, `UserControl`, `ContentControl`, `Border`.
- Multithreading support for efficient handling of multiple files.
- Exclusion of specific directories from the file search (e.g., Pods, Build directories, and NuGet packages).
- Command-line interface for easy usage and integration into development workflows.
- Detailed logging of the processing for easy tracking and debugging.

## Requirements
- Python 3.x

## Installation  💾 
Clone the repository to your local machine:

```bash
git clone https://github.com/munibsiddiqui/Xcode-Auto-Accessibility-Identifier-Generator-iOS.git
cd Xcode-Auto-Accessibility-Identifier-Generator-iOS
```
### For macOS Users

#### Installation

1. **Install Python 3:** Ensure Python 3 is installed on your macOS. You can check if Python is installed and its version by running `python3 --version` in the Terminal. If Python is not installed, you can install it using Homebrew with the command `brew install python`.

2. **Install `lxml`:** The script requires `lxml` for parsing XML files. Install `lxml` by running the following command in the Terminal:

   ```bash
   pip3 install lxml
   ```

   If you encounter any issues related to permissions or environments, you might need to adjust your Python environment or use virtual environments (e.g., `pyenv` or Python's built-in `venv`).

### For Windows Users

#### Installation

1. **Install Python 3:** Ensure Python 3 is installed on your Windows system. You can download Python from the official website and follow the installation instructions. During installation, make sure to select the option to add Python to the PATH.

2. **Install `lxml`:** Open Command Prompt and install `lxml` required for parsing XML files:

   ```cmd
   pip install lxml
   ```

   If you run into any issues during installation, consider using a virtual environment or consult the `lxml` documentation for Windows-specific installation tips.

## Usage 📚
Navigate to the script directory and run the script with the required project path:

```bash
python3 main.py /path/to/your/project/root/folder
```

To exclude specific directories (e.g., Pods, Build, NuGet packages), use the `--exclude` option:

```bash
python main.py /path/to/your/project --exclude Pods Build NuGetPackages
```

### Options
- `project_path`: Mandatory. The root folder of your project.
- `--exclude`: Optional. List of directories to exclude from the search.

After running the script, each UI element in your project's `.storyboard`, `.xib`, or `.xaml` files will have an accessibility identifier set based on the name of its view controller, custom class, or x:Class and the name of the property or control. This standard naming convention helps maintain consistency across your project and simplifies the process of identifying UI elements for accessibility purposes and UI testing.

## Structure
- `main.py`: The main script that orchestrates the file scanning, processing, and exclusion logic.
- `accessibility.py`: Contains the core functionality for updating the accessibility identifiers.

## Contributing
Contributions to Accessibility Identifier Updater are welcome. Please follow the standard code practices and submit a pull request for review.

## License 📄
GPLv2

## Contact
For queries or feedback, please contact Munib Siddiqui at munibsiddiqui@gmail.com.

## Credits 🙏
This project is a fork and extension of [Gini-Apps's Xcode-Auto-Accessibility-Identifier-Generator-iOS](https://github.com/Gini-Apps/Xcode-Auto-Accessibility-Identifier-Generator-iOS). Credit goes to the original authors for their foundational work on which this tool is built. Additional thanks to the contributors who have extended support for WPF applications, making this tool more versatile and useful for a broader range of developers.

---

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/munibsiddiqui)
