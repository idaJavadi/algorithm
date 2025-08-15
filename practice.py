# pip install customtkinter psycopg2-binary
import customtkinter as ctk
from tkinter import messagebox
import psycopg2

def connect_to_db():
    host = entry_host.get()
    port = entry_port.get() or "5432"
    dbname = entry_dbname.get()
    user = entry_user.get()
    password = entry_password.get()

    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        conn.close()
        messagebox.showinfo("موفقیت", "اتصال موفق بود! ✅")
    except Exception as e:
        messagebox.showerror("خطا", f"اتصال ناموفق: {e}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("PostgreSQL")
root.geometry("400x300")

entry_host = ctk.CTkEntry(root, placeholder_text="Host")
entry_host.pack(pady=5)

entry_port = ctk.CTkEntry(root, placeholder_text="Port")
entry_port.insert(0, "5432")
entry_port.pack(pady=5)

entry_dbname = ctk.CTkEntry(root, placeholder_text="Database Name")
entry_dbname.pack(pady=5)

entry_user = ctk.CTkEntry(root, placeholder_text="Username")
entry_user.pack(pady=5)

entry_password = ctk.CTkEntry(root, placeholder_text="Password", show="*")
entry_password.pack(pady=5)

btn_connect = ctk.CTkButton(root, text="اتصال", command=connect_to_db)
btn_connect.pack(pady=20)

root.mainloop()
