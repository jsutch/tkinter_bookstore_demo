#!/usr/bin/env python
"""
backend interface for book app
"""

import sqlite3


def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close() 
    return rows

def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT title, author, year, isbn FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close() 
    return rows

def update(_id, title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, _id))
    conn.commit()
    conn.close() 


def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE ID = ?", (id,))
    conn.commit()
    conn.close()

def close():
    pass



# run every time
connect()
# insert("The Damned2", "Alex Jones", 1982, 8234567)
# print(view())
# print(search("The Sea"))
# delete(2)
# print(search("The Sea"))
# update(12, "The Darned", "Alice Simpson", 1982, 8234567) # borked
# print(search("The Darned"))
# print(view())