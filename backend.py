import sqlite3
from turtle import title

class Database:

    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")    
        # self.conn.commit()
        # conn.close() #opening the connection
    # connect() 

    def insert(self, title,author,year,isbn):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title,author,year,isbn))
        #the next line too will work
        # cur.execute("INSERT INTO book(title, author,year,isbn) VALUES (?,?,?,?)", (title,author,year,isbn))
        # self.conn.commit()
        # conn.close() #you dont want to close the connection else the connection will close on the second attempt

    # insert()

    def delete(self, id):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        # self.conn.commit()
        # self.conn.close()

    def update(self, id,title,author,year,isbn):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("UPDATE book SET title=?, author=?, year=?,isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()
        # conn.close()

    def search(self, title='',author='',year='',isbn=''):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
        rows=self.cur.fetchall()
        self.conn.close()
        return rows

    def view(self):
        # conn = sqlite3.connect("books.db")
        # cur = conn.cursor()
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        # conn.close()
        return rows

    def commit(self):
        self.conn.commit()

def __del__(self): #close the connection
    self.conn.close()



    # insert("english", "afjd", 1938, 98080980)
    # print(search(author="Ola Rotimi"))
    # print(search("english"))
    # delete(2)
    # update(4, "english", "eng", 1933, 808090)
    # print(view())





