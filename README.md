# AVIF Converter

---

## Table of Contents

- [AVIF Converter](#avif-converter)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Directory Structure](#directory-structure)
  - [System Dependencies](#system-dependencies)
  - [Installation Guide](#installation-guide)
    - [macOS](#macos)
    - [Windows](#windows)
    - [Linux](#linux)
  - [Setting Up the Environment](#setting-up-the-environment)
    - [Installing Python](#installing-python)
      - [macOS:](#macos-1)
      - [Windows:](#windows-1)
      - [Linux:](#linux-1)
    - [Creating a Virtual Environment](#creating-a-virtual-environment)
      - [macOS/Linux:](#macoslinux)
      - [Windows:](#windows-2)
    - [Installing ImageMagick](#installing-imagemagick)
  - [Running the Application](#running-the-application)
    - [Troubleshooting python version](#troubleshooting-python-version)
  - [Troubleshooting](#troubleshooting)

---

## Introduction

I started to build websites that require a lot of images which, if not compressed or optimized properly, heavily affects the load time and performance of the web application.

I tried to look for free AVIF converters online that can batch convert images into AVIF but most of them are either paid or have a limit on the number of images that can be converted.

So I made this extremely basic GUI application to convert images to AVIF format using ImageMagick. It handles duplicate filenames by appending `(copy #)` to the output filenames and includes a progress bar to track conversion progress.

Supported image formats for conversion:

- JPG
- JPEG
- PNG
- GIF
- BMP
- TIFF
- WebP

I have also included the DMG file for macOS users to download and use the application.

(Windows app coming soon...)

---

## Directory Structure

```markdown
avif-converter/
├── avif-converter.py # Main Python script
├── AVIFConverter.dmg # Final DMG file (after packaging)
└── README.md # This file
```

---

## System Dependencies

| Platform    | Python 3.11.7 | ImageMagick | Package Manager       |
| ----------- | ------------- | ----------- | --------------------- |
| **macOS**   | Required      | Required    | Homebrew              |
| **Windows** | Required      | Required    | Chocolatey (Optional) |
| **Linux**   | Required      | Required    | APT (or equivalent)   |

---

## Installation Guide

### macOS

1. **Install Homebrew** (if not already installed):

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install ImageMagick**:

   ```bash
   brew install imagemagick
   ```

3. **Verify Installation**:

   ```bash
   magick --version
   ```

### Windows

1. **Using the Official Installer**:
   - Download the installer from the [ImageMagick download page](https://imagemagick.org/script/download.php).
   - Run the installer and ensure you check the box to **Add ImageMagick to PATH**.
2. **Using Chocolatey (Optional)**:
   - Install Chocolatey:
     ```powershell
     Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
     ```
   - Install ImageMagick:
     ```powershell
     choco install imagemagick
     ```
3. **Verify Installation**:
   ```cmd
   magick --version
   ```

### Linux

1. **Using APT (Debian/Ubuntu)**:
   ```bash
   sudo apt update
   sudo apt install imagemagick
   ```
2. **Using YUM (CentOS/RHEL)**:
   ```bash
   sudo yum install ImageMagick
   ```
3. **Using DNF (Fedora)**:
   ```bash
   sudo dnf install ImageMagick
   ```
4. **Verify Installation**:
   ```bash
   magick --version
   ```

---

## Setting Up the Environment

### Installing Python

#### macOS:

1. Install `pyenv`:
   ```bash
   brew install pyenv
   ```
2. Install Python 3.11.7:
   ```bash
   pyenv install 3.11.7
   ```
3. Set Python 3.11.7 as the global version:
   ```bash
   pyenv global 3.11.7
   ```

#### Windows:

1. Download Python 3.11.7 from the [official Python website](https://www.python.org/downloads/release/python-3117/).
2. Run the installer and ensure you check the box to **Add Python to PATH**.
3. Verify the installation:
   ```cmd
   python --version
   ```

#### Linux:

1. Update your package list:
   ```bash
   sudo apt update
   ```
2. Install Python 3.11.7:
   ```bash
   sudo apt install python3.11
   ```
3. Verify the installation:
   ```bash
   python3.11 --version
   ```

### Creating a Virtual Environment

#### macOS/Linux:

1. Navigate to the project directory:
   ```bash
   cd avif-converter
   ```
2. Create a virtual environment:
   ```bash
   python3.11 -m venv env
   ```
3. Activate the virtual environment:
   ```bash
   source env/bin/activate
   ```

#### Windows:

1. Navigate to the project directory:
   ```cmd
   cd avif-converter
   ```
2. Create a virtual environment:
   ```cmd
   python -m venv env
   ```
3. Activate the virtual environment:
   ```cmd
   .\env\Scripts\activate
   ```

### Installing ImageMagick

Refer to the [Installation Guide](#installation-guide) for platform-specific instructions.

---

## Running the Application

1. Activate the virtual environment:
   - macOS/Linux:
     ```bash
     source env/bin/activate
     ```
   - Windows:
     ```cmd
     .\env\Scripts\activate
     ```
2. Run the script:
   ```bash
   python avif-converter.py
   ```

### Troubleshooting python version

Make sure your python is not aliased by running this command:

```bash
which python
```

If your output does not show the path to the virtual environment (e.g. `.../env/bin/python`), and instead shows the system Python path (e.g. `/usr/bin/python`), you can temporarily unalias the Python command by running:

```bash
unalias python
```

Then, try running the script again.

---

## Troubleshooting

- **macOS**: If `magick` is not recognized, ensure Homebrew added it to your PATH. Restart your terminal or run:
  ```bash
  eval "$(brew shellenv)"
  ```
- **Windows**: If `magick` is not recognized, manually add ImageMagick to your system PATH.
- **Linux**: If `magick` is not recognized, try using `convert` instead:
  ```bash
  convert --version
  ```
