from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
from tkinter import messagebox
import shutil

root = Tk()
root.title('Youtube Downloader')
root.configure(bg='#f0f4f8')
root.geometry('600x600')
root.resizable(True, True)


def download():
    video_path = video_url_entry.get()
    file_path = path_label.cget('text')
    messagebox.showinfo(title='Status', message='Downloading')
    try:
        mp4 = YouTube(video_path).streams.get_highest_resolution().download(output_path=file_path)
        video_clip = VideoFileClip(mp4)
        #mp3 conversion code
        audio_file = video_clip.audio
        audio_file.write_audiofile('audio.mp3')
        audio_file.close()
        shutil.move('audio.mp3', file_path)
        #mp3 conversion code
        video_clip.close()
        shutil.move(mp4, file_path)
        messagebox.showinfo("Download Complete", "✅ Your video has been downloaded successfully.")
    except Exception as e:
        messagebox.showerror("Download Failed", f"❌ Error: {e}")
    


def get_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

# Main frame for content
main_frame = Frame(root, bg='#ffffff', bd=2, relief=RIDGE)
main_frame.pack(padx=30, pady=30, fill=BOTH, expand=True)

app_label = Label(main_frame, text='Video Downloader', fg='#273b7a', 
                  font=('Arial', 24, 'bold'), bg='#ffffff')
app_label.pack(pady=(20, 10))

video_url_label = Label(main_frame, text='Enter Video url', font=('Arial', 13),
                        bg='#ffffff')
video_url_label.pack(pady=(10, 0))

video_url_entry = Entry(main_frame, font=("Arial", 13), width=30, bd=2, relief=SOLID)
video_url_entry.pack(pady=(0, 10))

#path to download videos
path_label = Label(main_frame, text='Select Path to Download', font=("Arial", 13),
                   bg='#ffffff')
path_label.pack(pady=(10, 0))

path_btn = Button(main_frame, text='Select', font=("Arial", 13, 'bold'),
                    width=20, bg='#273b7a', fg='#ffffff', command=get_path)
path_btn.pack(pady=(10, 0))

#Downlaod buttton
download_btn = Button(main_frame, text='Download', font=("Arial", 13, 'bold'),
                    width=20, bg='#273b7a', fg='#ffffff', command=download)
download_btn.pack(pady=(10, 0))

root.mainloop()