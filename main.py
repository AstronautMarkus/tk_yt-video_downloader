import webbrowser
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import video_dl as vd
from PIL import Image, ImageTk

def getData():
    url = textbox.get()
    folder = filedialog.askdirectory()

    if folder:
        global directory_path
        directory_path = folder

        result_dl = vd.download_video(url, directory_path)

        if result_dl == 1:
            messagebox.showinfo(message="Video downloaded!", title="Sucess")
        else:
            messagebox.showerror(message="Invalid URL. You must enter a valid URL!", title="Error")
    else:
        messagebox.showwarning(message="You must select a valid directory path for download a video.", title="Error")


def gitProfile(event):
    url = "https://github.com/AstronautMarkus"
    webbrowser.open(url)


root = tk.Tk()
root.title("YouTube Video downloader")


root.geometry("550x240")

root.resizable(False, False)

root.iconbitmap('317714_video_youtube_icon.ico')


main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0)


label_title = ttk.Label(main_frame, text="Youtube video downloader")
label_title.grid(row=0, column=1, columnspan=1, pady=10)

label_author = ttk.Label(main_frame, text="made by AstronautMarkus")
label_author.grid(row=2, column=0, columnspan=1, pady=10)


textbox = ttk.Entry(main_frame, width=40)
textbox.grid(row=1, column=1, padx=5, pady=5)


button = ttk.Button(main_frame, text="Download video", command=getData, cursor="hand2")
button.grid(row=1, column=2, padx=5, pady=5)


image = Image.open('img.jpeg')
image = image.resize((100, 100)) 
image = ImageTk.PhotoImage(image)


label_image = ttk.Label(main_frame, image=image)
label_image.grid(row=1, column=0, padx=5, pady=5)

label_image.bind("<Button-1>", gitProfile,)
label_author.bind("<Button-1>", gitProfile,)


root.mainloop()
