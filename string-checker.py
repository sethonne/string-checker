import tkinter as tk
from tkinter import messagebox

def check_string():
    s = entry.get().strip().lower()
    a_count = s.count('a')
    b_count = s.count('b')

    if not s:
        output_label.config(text="Please enter a string.")
        return

    if not all(c in 'ab' for c in s):
        output_label.config(text="Only 'a' and 'b' are allowed.")
        return

    if a_count % 2 == 0 and b_count % 2 == 1:
        output_label.config(text="✅ YES — Valid")
    else:
        output_label.config(text="❌ NO — Invalid")

# Colors & Fonts
bg_color = "#1e1e2f"
card_color = "#2a2a40"
fg_color = "#e0e0e0"
accent_color = "#00e6e6"
error_color = "#ff4c4c"
entry_bg = "#1f1f30"

font_main = ("Segoe UI", 11)
font_title = ("Segoe UI", 17, "bold")

# Root Window
root = tk.Tk()
root.title("Even A’s & Odd B’s Checker")
root.geometry("520x320")
root.configure(bg=bg_color)
root.resizable(False, False)

# Container card
card = tk.Frame(root, bg=card_color, bd=0, highlightthickness=0)
card.place(relx=0.5, rely=0.5, anchor="center", width=460, height=280)

# Title
title_label = tk.Label(card, text="Even A’s & Odd B’s Checker", font=font_title,
                       bg=card_color, fg=accent_color)
title_label.pack(pady=(20, 10))

# Entry
entry = tk.Entry(card, width=40, font=font_main, bg=entry_bg, fg=fg_color,
                 insertbackground=fg_color, relief="flat", highlightthickness=1,
                 highlightbackground=accent_color)
entry.pack(ipady=7, pady=(0, 10))

# Button styling
def on_enter(e): check_button.config(bg="#00cccc")
def on_leave(e): check_button.config(bg=accent_color)

check_button = tk.Button(card, text="Check String", command=check_string,
                         bg=accent_color, fg=bg_color, font=font_main,
                         activebackground="#00cccc", relief="flat", width=20, height=1,
                         cursor="hand2", borderwidth=0)
check_button.bind("<Enter>", on_enter)
check_button.bind("<Leave>", on_leave)
check_button.pack(pady=10)

# Output
output_label = tk.Label(card, text="", font=font_main, bg=card_color, fg=fg_color,
                        wraplength=400, justify="center")
output_label.pack(pady=(5, 0))

root.mainloop()
