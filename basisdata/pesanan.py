import sqlite3

class Pesanan:
  
  def __init__(self, username, email, password):
    self.username = username
    self.email = email
    self.password = password

  def __str__(self):
    return f"user(username:{self.username}, email:{self.email}, password:{self.password})"

  def tambahPesanan(username, email, password):
    
    koneksi = sqlite3.connect("EWS.db")

    sql = f"""INSERT INTO user(username, email, password)
            VALUES (?, ?, ?);"""
    koneksi.execute(sql, (username, email, password))
    koneksi.commit()
    koneksi.close()