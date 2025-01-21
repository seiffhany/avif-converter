
## Packaging the Application

### 1. Install PyInstaller
Install PyInstaller to package the application:
```bash
pip install pyinstaller
```

---

### 2. Package the Application
Run the following command to create a standalone macOS app:
```bash
pyinstaller --windowed --onefile --name "AVIFConverter" --icon=icon.icns avif-converter.py
```

#### Output:
- The `.app` file will be created in the `dist` folder:
  ```
  dist/AVIFConverter.app
  ```

---

## Creating a DMG File

### 1. Install `create-dmg`
Install `create-dmg` using Homebrew:
```bash
brew install create-dmg
```

---

### 2. Create the DMG File
Run the following command to create a `.dmg` file:
```bash
create-dmg \
  --volname "AVIF Converter" \
  --volicon "icon.icns" \
  --background "background.png" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "AVIFConverter.app" 200 190 \
  --hide-extension "AVIFConverter.app" \
  --app-drop-link 600 190 \
  "AVIFConverter.dmg" \
  "dist/AVIFConverter.app"
```

#### Output:
- The `.dmg` file will be created in the current directory:
  ```
  AVIFConverter.dmg
  ```

---

### 3. Optional Customizations
- **Icons**: Use `.icns` files for the app and volume icons.
- **Background**: Use a `.png` file for the DMG background.
- **Hide Extension**: The `--hide-extension` flag hides the `.app` extension in the DMG window.

Simplified command:
```bash
create-dmg \
  --volname "AVIF Converter" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "AVIFConverter.app" 200 190 \
  --app-drop-link 600 190 \
  "AVIFConverter.dmg" \
  "dist/AVIFConverter.app"
```