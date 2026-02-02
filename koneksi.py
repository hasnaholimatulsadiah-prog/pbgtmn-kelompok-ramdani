import mysql.connector

# 1. Membangun Koneksi
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="", # Kosongkan jika menggunakan XAMPP default
        database="sekolah"
    )

    if db.is_connected():
        print("Koneksi ke database berhasil")
        cursor = db.cursor()

        # 2. INSERT Data via Python
        sql_insert = "INSERT INTO guru (nama, mapel) VALUES (%s, %s)"
        val = ("Rina", "Multimedia")
        cursor.execute(sql_insert, val)
        db.commit() # Menyimpan perubahan
        print(f"{cursor.rowcount} data berhasil ditambahkan.")

        # 3. SELECT Data dan Tampilkan di Terminal
        cursor.execute("SELECT * FROM guru")
        hasil = cursor.fetchall()
        
        print("\n--- Data Guru ---")
        for row in hasil:
            print(f"ID: {row[0]} | Nama: {row[1]} | Mapel: {row[2]}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # 4. Menutup Koneksi
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("\nKoneksi ditutup.")