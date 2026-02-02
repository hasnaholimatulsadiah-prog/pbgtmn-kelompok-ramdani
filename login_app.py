import tkinter as tk
from tkinter import messagebox
import mysql.connector 

# 1. Koneksi Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_login"
)
cursor = db.cursor()

# 2. Fungsi Halaman Index (Halaman Setelah Login)
def halaman_index(nama_user):
    root.withdraw() # Menyembunyikan halaman login
    
    index = tk.Toplevel() # Menggunakan Toplevel agar tidak bentrok dengan root
    index.title("Halaman Index")
    index.geometry("300x200")

    # TUGAS: Mengubah teks menjadi nama user yang login
    tk.Label(index, text=f"Selamat Datang, {nama_user}", font=("Arial", 14)).pack(pady=20)

    # TUGAS: Tambahkan messagebox logout
    def logout():
        messagebox.showinfo("Logout", "Anda telah keluar dari sistem")
        index.destroy()
        root.deiconify() # Memunculkan kembali halaman login

    tk.Button(index, text="Logout", command=logout, bg="red", fg="white").pack()

# 3. Fungsi Validasi Login
def login():
    username_input = entry_username.get()
    password_input = entry_password.get()

    # Query mencari user yang cocok 
    sql = "SELECT * FROM user WHERE username=%s AND password=%s"
    data = (username_input, password_input)
    cursor.execute(sql, data)

    hasil = cursor.fetchone() # Ambil satu data jika ada 

    if hasil:
        messagebox.showinfo("Login", "Login berhasil!")
        halaman_index(username_input) # Jalankan index dengan membawa nama user
    else:
        messagebox.showerror("Login", "Username atau Password salah!") 

# 4. Tampilan Halaman Login (GUI Utama)
root = tk.Tk()
root.title("Aplikasi Login")
root.geometry("300x250")

tk.Label(root, text="LOGIN SYSTEM", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(root, text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

tk.Label(root, text="Password").pack()
entry_password = tk.Entry(root, show="*") # Menyembunyikan password [cite: 38]
entry_password.pack(pady=5)

tk.Button(root, text="Login", command=login, bg="blue", fg="white").pack(pady=20)

root.mainloop()