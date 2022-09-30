# Video (.mp4) & Audio (.mp3) Youtuber Downloader

import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import youtube_dl

def clear():
    url.delete(first=0, last=50)

def browse_location():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def download_file():
    try:
        URL = url.get()
        PATH = path.get()
        # Option Selection
        if options.get() == "Video (mp4)":
            # Video Download
            ydl_opts = {}
            os.chdir(PATH)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([URL])
            noty='Video Downloaded successfully'
            Notification.configure(text=noty,fg='black', bg="light steel blue", width=30, font=('times', 18, 'bold','italic'))                
            Notification.place(x=150, y=450)
        elif options.get() == "Audio (mp3)":
            # Audio Download
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                    }],
                }
            os.chdir(PATH)
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([URL])
            noty='Audio Downloaded successfully'                
            Notification.configure(text=noty,fg='black', bg="light steel blue", width=30, font=('times', 18, 'bold','italic'))
            Notification.place(x=150, y=450)
    except Exception as e:
        print(e)

# Main Window Commands
window = tk.Tk()
window.title('Youtube Downloader')
width, height = window.winfo_screenwidth()/2, window.winfo_screenheight()/1.5
window.geometry('%dx%d+0+0' % (width,height))
window.iconbitmap('yt.ico')
window.configure(background='light steel blue')

folder_path = StringVar()

message = tk.Label(window,  text = "Youtube downloader", bg="slate blue",
            fg="black", height=2, width=int(window.winfo_screenwidth()/2), font=('times', 30, 'italic bold ')).pack()

Notification = tk.Label(window, text="Video Downloaded Successfully", bg="lime green", fg="white", width=int(window.winfo_screenwidth()/2),
                   height=2, font=('times', 18, 'bold'))

# URL Message
lbl_url = tk.Label(window, text="Enter URL :", width=10, height=2, fg="black", bg="light steel blue", font=('times', 15, ' bold '))
lbl_url.place(x=20, y=150)

url = tk.Entry(window, width=40, bg="linen", fg="gray9",font=('times', 15, ' bold '))
url.place(x=150, y=160)

# Path Message
lbl_path = tk.Label(window, text="Enter Path :", width=10, height=2, fg="black", bg="light steel blue", font=('times', 15, ' bold '))
lbl_path.place(x=20, y=270)

path = tk.Entry(window, width=40, bg="linen", fg="gray9",textvariable=folder_path, font=('times', 15, ' bold '))
path.place(x=150, y=280)

# OptionMenu Button
options = tk.StringVar(window)
options.trace_add('write', lambda *args: print(options.get()))
options.set("Video (mp4)") # default value

om1 =tk.OptionMenu(window, options, "Video (mp4)","Audio (mp3)")
om1["bg"] = "DarkGoldenrod1"
om1["highlightthickness"]=0 
om1.config(width=10, height=1, font=('times', 15, ' bold '))
om1['menu'].config(font=('times',(15)),bg='goldenrod1')
om1.place(x=600, y=160)

# Browse Button
browse = tk.Button(window, text="Browse",command=browse_location,fg='black'  ,bg="DarkGoldenrod1"  ,width=11 ,height=1 , activebackground = "Red" ,font=('times', 15, ' bold '))
browse.place(x=600, y=270)

# Decision Buttons
clearButton = tk.Button(window, text="Clear",command=clear,fg="black" ,bg="dark turquoise" ,width=10 ,height=2 , activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=180, y=350)

down = tk.Button(window, text="Download",command=download_file,fg="black" ,bg="yellow green" ,width=10 ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
down.place(x=390, y=350)

img = ImageTk.PhotoImage(Image.open("Youtube_image.PNG"))
panel = Label(window, image = img)
panel.place(x=1000, y=150)

message = tk.Label(window,  text = "", bg="slate blue",
            fg="black", height=1, width=int(window.winfo_screenwidth()/2), font=('times', 30, 'italic bold ')).pack(side = BOTTOM)


window.mainloop()
