from gtts import gTTS
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename


def convert():
    mytext = write_place.get(1.0, tk.END)
    language = 'en'
    audio = gTTS(text= mytext, lang = language, slow=False)
    audio.save("output.mp3")
    os.system("start output.mp3")

def clear():
    write_place.delete(1.0, tk.END)

def clear_all(event):
    write_place.delete(1.0, tk.END)

def open_new():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    write_place.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        write_place.insert(tk.END, text)
    window.title(f"Text To Speech - {filepath}")

def open_newer(event):
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    write_place.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        write_place.insert(tk.END, text)
    window.title(f"Text To Speech - {filepath}")

window = tk.Tk()
window.title("Text To Speech ")
window.geometry("700x500")

btn_grid = tk.Frame(window, bd=3, relief="groove")
btn_grid.grid(row =0, column=0, sticky = "ns")
text_grid = tk.Frame(window)
text_grid.grid(row=0, column=1, sticky = "nsew")

clear_btn = tk.Button(btn_grid,text="CLEAR", padx=5, pady=5, command=clear,  bg="brown", fg="white")
label1 = tk.Label(btn_grid,text='')
window.bind('<Escape>', clear_all)
convert_btn = tk.Button(btn_grid,text="CONVERT", padx=5, pady=5, command=convert,  bg="brown", fg="white")
clear_btn.pack(fill = "x")
label1.pack()
convert_btn.pack(fill = "x")
label2 = tk.Label(btn_grid,text='')
label2.pack()
open_btn = tk.Button(btn_grid,text="OPEN", padx=5, pady=5, command=open_new,  bg="brown", fg="white")
open_btn.pack(fill = "x")

write_place = tk.Text(text_grid)
write_place.pack(fill="both")

window.bind('<Control-o>', open_newer)

window.mainloop()