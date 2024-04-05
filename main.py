import tkinter as tk
from tkinter import filedialog, messagebox
from audioTrim1 import mainTrim
from mp3toWav2 import mainWav
from transkript3 import mainTranskript
from getDuration import duration

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    print(file_path)
    return file_path

def show_popup(message):
    messagebox.showinfo("Islem tamamlandi", message)

def main():
    file_path = select_file()
    if file_path:
        #minute = duration(file_path)
        minute = 1
        mainTrim(minute, file_path)
        mainWav(minute)
        mainTranskript(minute)
        show_popup("transkript.txt dosyasina bakin.")

if __name__ == "__main__":
    main()
