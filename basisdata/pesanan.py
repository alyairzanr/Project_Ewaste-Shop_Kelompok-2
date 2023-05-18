import sqlite3

class Pesanan:
  
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"user(username:{self.username}, email:{self.email}, password:{self.password})"

    def tambahPesanan(username_penjual, username_pembeli, gambar, nama_gambar, harga, deskripsi):
        
        koneksi = sqlite3.connect("EWS.db")

        sql = f"""INSERT INTO pesanan(username_penjual, username_pembeli, gambar, nama_gambar, harga, deskripsi)
                VALUES (?, ?, ?, ?, ?, ?);"""
        koneksi.execute(sql, (username_penjual, username_pembeli, gambar, nama_gambar, harga, deskripsi))
        koneksi.commit()
        koneksi.close()

    def hapusPesanan(id):
        koneksi = sqlite3.connect("EWS.db")

        sql = f"""DELETE FROM pesanan
                WHERE id=?;"""
        koneksi.execute(sql, (id,))
        koneksi.commit()

        koneksi.close()

    def ambilPesananPembeli(username_pembeli):
        conn = sqlite3.connect('EWS.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM pesanan WHERE username_pembeli = ?', (username_pembeli,))
        rows = cursor.fetchall()
        conn.close()

        return rows
    
    def tambahDipesan(username_penjual, username_pembeli, nama_pembeli, alamat, telepon, gambar, nama_gambar, harga, deskripsi):
        
        koneksi = sqlite3.connect("EWS.db")

        sql = f"""INSERT INTO dipesan(username_penjual, username_pembeli, nama_pembeli, alamat, telepon, gambar, nama_gambar, harga, deskripsi)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        koneksi.execute(sql, (username_penjual, username_pembeli, nama_pembeli, alamat, telepon, gambar, nama_gambar, harga, deskripsi))
        koneksi.commit()
        koneksi.close()

    def ambilPesananUser(username_penjual):
        conn = sqlite3.connect('EWS.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM dipesan WHERE username_penjual = ?', (username_penjual,))
        rows = cursor.fetchall()
        conn.close()

        return rows