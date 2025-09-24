from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Youtube Downloader')
root.configure(bg='#f0f4f8')
root.geometry('400x300')
root.resizable(True, True)


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


root.mainloop()