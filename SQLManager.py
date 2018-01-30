import sqlite3

class SQLManager:
  def __init__(self):
    self.conn = sqlite3.connect('shows.db')

  def create_db(self):
    c = self.conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS shows (id int, name text, episodes int, seasons int)")
    self.conn.commit()

  def close_db(self):
    self.conn.close()

  def add_show(self, idShow, nameShow):
    c = self.conn.cursor()
    c.execute("INSERT INTO shows VALUES ({}, '{}')".format(idShow, nameShow))
    self.conn.commit()

  def getAllShows(self):
    c = self.conn.cursor()
    return c.execute('SELECT * FROM shows ORDER BY name')
