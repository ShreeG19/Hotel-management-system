import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from hotel import HotelManagementSystem

def validate_login():
    userid = username_entry.get().strip()
    password = password_entry.get().strip()

    users = {
        "admin": "admin@123",
        "manager": "manager@123",
        "staff": "staff@123"
    }

    if userid in users and users[userid] == password:
        messagebox.showinfo("Success", "Login successful")
        root.destroy()

        hotel_root = tk.Tk()
        hotel_app = HotelManagementSystem(hotel_root)
        hotel_root.mainloop()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Main window
root = tk.Tk()
root.title("Hotel Management System - Login")
root.geometry("1900x870+750+420")
root.minsize(1900, 1000)

BACKGROUND_PATH = '/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/background_img.jpeg'
LOGO_PATH = '/home/kalilinux/Documents/V S code files/Projects_for/hotel_foxysDolphin/images/logo.png'

canvas = tk.Canvas(root, width=1640, height=650)
canvas.pack(fill="both", expand=True)

try:
    bg_img = Image.open(BACKGROUND_PATH)
    bg_img = bg_img.resize((2000, 1000), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    canvas.bg_photo = bg_photo
except:
    canvas.create_rectangle(0, 0, 1640, 670, fill="#2c3e50")

main_frame = tk.Frame(root, bg="#f3e1a7", bd=0, relief='flat')
main_frame.place(relx=0.5, rely=0.5, anchor='center', width=600, height=650)
main_frame.lift()

try:
    logo_img = Image.open(LOGO_PATH)
    logo_img = logo_img.resize((120, 120), Image.Resampling.LANCZOS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(main_frame, image=logo_photo, bg='#f3e1a7')
    logo_label.image = logo_photo
    logo_label.pack(pady=30)
except:
    tk.Label(main_frame, text="🏨", font=('Arial', 60), bg='#f3e1a7', fg='#3498db').pack(pady=30)

tk.Label(main_frame, text="Hotel Management Login", font=('Arial', 28, 'bold'),
         bg='#f3e1a7', fg='#2c3e50').pack(pady=10)

tk.Label(main_frame, text="Username:", font=('Arial', 16),
         bg='#f3e1a7', fg='#2c3e50').pack(pady=8)

username_entry = tk.Entry(main_frame, font=('Arial', 16), width=25, bg='white', relief='solid', bd=2)
username_entry.pack(pady=8)
username_entry.focus()

tk.Label(main_frame, text="Password:", font=('Arial', 16),
         bg='#f3e1a7', fg='#2c3e50').pack(pady=8)

password_entry = tk.Entry(main_frame, font=('Arial', 16), width=25, show='*', bg='white', relief='solid', bd=2)
password_entry.pack(pady=8)

login_btn = tk.Button(main_frame, text="LOGIN",
                      font=('Arial', 18, 'bold'),
                      bg='#28a745',
                      fg='white',
                      width=22,
                      height=2,
                      cursor='hand2',
                      command=validate_login,
                      relief='raised',
                      bd=3)

login_btn.pack(pady=25)

root.bind('<Return>', lambda e: validate_login())

root.mainloop()