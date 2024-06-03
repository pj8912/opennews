from constants import DATABASE_ROUTE
import sqlite3

conn  =  sqlite3.connect('myn.db', check_same_thread=False)
cursor = conn.cursor()