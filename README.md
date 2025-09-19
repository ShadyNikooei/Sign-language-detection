# Sign Language Detection with Action Automation

This project uses real-time hand gesture recognition to detect simple sign language symbols via a webcam. Based on the recognized signs, it performs user-defined actions such as opening applications, playing media, visiting websites, and more.

## Features

- Real-time webcam-based hand detection
- Rule-based sign classification (no machine learning required)
- Custom action execution based on recognized signs
- Supports gesture macros (e.g., "ABC" sequence triggers a custom command)
- Voice feedback using text-to-speech
- Live display of detected signs and input sequence
- Action logging (saved to `log.txt`)
- Modular code with easy configuration via `config.json`


## Getting Started

### 1. Clone or download the project

Unzip the project files or clone via Git.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

- **Windows (PowerShell):**

  ```bash
  .venv\Scripts\Activate.ps1
  ```

- **Windows (CMD):**

  ```bash
  .venv\Scripts\activate.bat
  ```

- **Linux/macOS:**

  ```bash
  source .venv/bin/activate
  ```

### 4. Install required packages

```bash
pip install -r requirements.txt
```

---

## Running the Project

```bash
python main.py
```

A webcam window will open showing the live detection. The application will display:
- The detected sign (e.g., A, B, C)
- A sequence tracker (for macros like "ABC")
- Real-time voice feedback

Press `ESC` to exit the application.


## Configuration (`config.json`)

Customize the actions linked to each sign by editing the `config.json` file:

```json
{
  "A": { "type": "app", "value": "firefox" },
  "B": { "type": "app", "value": "notepad.exe" },
  "C": { "type": "url", "value": "https://www.python.org" },
  "D": { "type": "file", "value": "C:/Users/YourName/Desktop/file.pdf" },
  "E": { "type": "message", "value": "Sign E detected" },
  "F": { "type": "folder", "value": "C:/Users/YourName/Documents" },
  "G": { "type": "audio", "value": "C:/Users/YourName/Music/sample.mp3" },
  "H": { "type": "cmd", "value": "dir" },
  "ABC": { "type": "cmd", "value": "echo 'Macro ABC triggered'" }
}
```

Supported action types:
- `app`: Launch an application
- `url`: Open a website
- `file`: Open a file
- `folder`: Open a directory
- `audio`: Play audio or media file
- `message`: Print a custom message
- `cmd`: Execute a system command


## File Structure

```
sign_language_project/
├── main.py             # Main execution script
├── vision.py           # Image processing and sign detection
├── actions.py          # Action mapping and execution
├── utils.py            # Low-level system action handling
├── logger.py           # Logging to log.txt
├── config.json         # User-defined actions per sign
├── requirements.txt    # Python dependencies
└── log.txt             # Auto-generated on first run
```


## Notes

- This project is **rule-based** and does not use machine learning or datasets.
- Only basic geometric analysis of hand landmarks is used.
- You can expand the `classify_sign()` function in `vision.py` for more accurate or complex gestures.

## Requirements

- Python 3.8+
- Webcam
- Tested on Windows and Linux

Programmer:
Shady Nikooei - Computer Vision
