import os
import tkinter as tk
from tkinter import messagebox

def speak():
    text = text_input.get()
    if text.strip() == "":
        messagebox.showwarning("Warning", "Please enter text to speak")
        return

    command = (
        'powershell -Command '
        '"Add-Type -AssemblyName System.Speech; '
        '(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('
        f'\'{text}\''
        ')"'
    )
    os.system(command)

def clear_text():
    text_input.delete(0, tk.END)

def exit_app():
    root.destroy()


root = tk.Tk()
root.title("RoboSpeaker 1.20")
root.geometry("420x250")
root.resizable(False, False)
root.configure(bg="#1e1e2f")


title = tk.Label(
    root,
    text="RoboSpeaker 1.20",
    font=("Segoe UI", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=10)


subtitle = tk.Label(
    root,
    text="Created by POOJA",
    font=("Segoe UI", 10),
    bg="#1e1e2f",
    fg="#cfcfcf"
)
subtitle.pack()


text_input = tk.Entry(
    root,
    width=40,
    font=("Segoe UI", 12)
)
text_input.pack(pady=20)

btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack()


speak_btn = tk.Button(
    btn_frame,
    text="🔊 Speak",
    font=("Segoe UI", 11),
    bg="#4CAF50",
    fg="white",
    width=10,
    command=speak
)
speak_btn.grid(row=0, column=0, padx=10)


clear_btn = tk.Button(
    btn_frame,
    text="🧹 Clear",
    font=("Segoe UI", 11),
    bg="#2196F3",
    fg="white",
    width=10,
    command=clear_text
)
clear_btn.grid(row=0, column=1, padx=10)


exit_btn = tk.Button(
    root,
    text="❌ Exit",
    font=("Segoe UI", 10),
    bg="#f44336",
    fg="white",
    width=12,
    command=exit_app
)
exit_btn.pack(pady=15)

root.mainloop()
