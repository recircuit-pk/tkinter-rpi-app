import tkinter as tk
from tkinter import messagebox


def start_app():
    status_label.config(text="System Started")


def stop_app():
    status_label.config(text="System Stopped")


def show_message():
    messagebox.showinfo("Message", "Hello from Raspberry Pi!")


# Create window
root = tk.Tk()
root.title("Raspberry Pi Control Panel")
root.geometry("800x480")
root.configure(bg="#202124")

# Title
title = tk.Label(
    root,
    text="Raspberry Pi Control Panel",
    font=("Arial", 28, "bold"),
    bg="#202124",
    fg="white"
)
title.pack(pady=40)

# Status
status_label = tk.Label(
    root,
    text="System Ready",
    font=("Arial", 20),
    bg="#202124",
    fg="white"
)
status_label.pack(pady=20)

# Start button
start_button = tk.Button(
    root,
    text="START",
    font=("Arial", 18, "bold"),
    width=12,
    height=2,
    command=start_app
)
start_button.pack(pady=10)

# Stop button
stop_button = tk.Button(
    root,
    text="STOP",
    font=("Arial", 18, "bold"),
    width=12,
    height=2,
    command=stop_app
)
stop_button.pack(pady=10)

# Message button
message_button = tk.Button(
    root,
    text="TEST",
    font=("Arial", 14),
    width=10,
    command=show_message
)
message_button.pack(pady=20)

# Run application
root.mainloop()
