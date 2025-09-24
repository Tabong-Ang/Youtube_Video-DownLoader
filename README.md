# 🎬 YouTube Downloader (Tkinter + yt-dlp)

A sleek desktop application built with Python and Tkinter that allows users to download YouTube videos in high resolution. Powered by `yt-dlp` and styled for a modern, responsive experience.

---

## 🚀 Features

- 🔗 Download videos from any valid YouTube URL
- 📁 Choose your own download folder
- 🎥 Automatically merges best video and audio streams into `.mp4`
- ✅ Real-time feedback with success/error messages
- 🎨 Clean, responsive GUI with modern fonts and colors

---

## 🛠️ Installation

### Requirements

- Python 3.10+
- Required libraries:
  - `yt-dlp`
  - `moviepy`
  - `tkinter` (built-in)

Install dependencies via pip:

```bash
pip install yt-dlp moviepy
```

FFmpeg (Required for merging video/audio)
Download and install FFmpeg, then add it to your system PATH:

Extract FFmpeg to `C:\ffmpeg`

Add `C:\ffmpeg\bin` to your system environment variables under Path

Verify with:
```bash 
ffmpeg -version
```

📦 Usage
1. Run the app:
```bash
python ytbe.py
```
2. Paste a valid YouTube video URL
3. Click Browse to select your download folder
4. Click Download
5. Your video will be saved as .mp4 in the selected folder

📁 Project Structure
```bash
YouTube_Downloader/
├── ytbe.py
├── README.md
```

🧠 Notes
The app uses yt-dlp to fetch and merge the best video/audio streams
moviepy is included for future audio conversion or editing features
GUI is built with Tkinter and styled for clarity and responsiveness
