from tkinter import *
from tkinter import filedialog, messagebox
from moviepy.editor import *
import yt_dlp
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS  # PyInstaller sets this at runtime
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Initialize main window
root = Tk()
root.title("🎬 YouTube Downloader")
root.geometry("600x600")
root.iconbitmap(resource_path('images/photo.ico'))
root.configure(bg="#f0f4f8")
root.resizable(True, True)

# Download logic
def download():
    video_url = video_url_entry.get().strip()
    download_path = path_label.cget("text").strip()

    if not video_url or not download_path or download_path == "Select Path to Download":
        messagebox.showerror("Missing Info", "⚠ Please enter a video URL and select a download path.")
        return

    messagebox.showinfo("Status", "⏳ Downloading...")

    try:
        ydl_opts = {
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        messagebox.showinfo("Download Complete", "✅ Your video has been downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Download Failed", f"❌ Error: {e}")

# Folder picker
def get_path():
    path = filedialog.askdirectory()
    if path:
        path_label.config(text=path)

# Main frame
main_frame = Frame(root, bg="#ffffff", bd=2, relief=RIDGE)
main_frame.pack(padx=30, pady=30, fill=BOTH, expand=True)

# Heading
heading = Label(main_frame, text="🎬 YouTube Downloader", font=("Arial", 24, "bold"), bg="#ffffff", fg="#273b7a")
heading.pack(pady=(20, 10))

# URL input
video_url_label = Label(main_frame, text="Enter YouTube Video URL", font=("Arial", 13), bg="#ffffff")
video_url_label.pack(pady=(10, 0))

video_url_entry = Entry(main_frame, font=("Arial", 13), width=40, bd=2, relief=SOLID)
video_url_entry.pack(pady=(0, 10))

# Path selection
path_label = Label(main_frame, text="Select Path to Download", font=("Arial", 13), bg="#ffffff", fg="#555555")
path_label.pack(pady=(10, 0))

path_btn = Button(main_frame, text="📁 Browse", font=("Arial", 13, "bold"), width=20,
                  bg="#273b7a", fg="#ffffff", activebackground="#1e2f5a", command=get_path)
path_btn.pack(pady=(10, 0))

# Download button
download_btn = Button(main_frame, text="⬇ Download", font=("Arial", 13, "bold"), width=20,
                      bg="#273b7a", fg="#ffffff", activebackground="#1e2f5a", command=download)
download_btn.pack(pady=(20, 10))

# Footer
footer = Label(root, text="© 2025 PhilipsTech | YouTube Video Downloader", font=("Arial", 10), bg="#f0f4f8", fg="#888")
footer.pack(pady=10)

# Run app
root.mainloop()
