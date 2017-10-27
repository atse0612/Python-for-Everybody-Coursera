# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:52:41 2017

@author: atse
"""

import xml.etree.ElementTree as ET
    #parses the xml into element form
import sqlite3
    #creates if does not exist database for tracks/if it does just establishes connection to the db
conn = sqlite3.connect('Trackdb.sqlite')
    #establishes connection to the database/
cur = conn.cursor()

#clears all tables out so no conflicting or bad info to begin
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Track;''')

    # creates the table 'Artist' id key autoincrements and must be unique, the artists name is stored there and will be referenced by table downstream
cur.execute(''' CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );''')

cur.execute(''' CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
    );''') # each line starts with the name of the prospective column followed by the schema thats being set for it entries
    #
cur.execute(''' CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
    );''')
cur.execute(''' CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    count INTEGER
    );''')


tree = ET.parse(r'C:\Users\\atse\Documents\Python for Everybody Specialization\Using Databases with Python\Week 3\Library.xml')

root = tree.getroot()
    # . - selects current node (plist) most useful at beginning path
    #/dict/dict//dict - then goes dict branch then next child then //
    # //dict selects all child elements 'dict' within that wrung of tree (ladder)
itlist = root.findall('./dict/dict//dict')

def lookup(dic, key):
    found = False
    for child in dic:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

print('Dict count', len(itlist))
for entry in itlist:
    if (lookup(entry,'Track ID') is None) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    length = lookup(entry, 'Total Time')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')

    if name is None or artist is None or album is None or genre is None : continue


    print(name, artist, album, count, rating, length)
    #insert the new row into DB and table, then specify colum
    #to place information into, BUT b/c using variable
    #need to use ? placeholder, b/c value is in a variable
    #and not directly entered into the VALUES field
    cur.execute('''INSERT or IGNORE INTO Artist (name)
        VALUES (?)''', (artist,))
    # grabs the row with the corresponding artist name, impt ONLY 1 though
    # selects this info, this way, because no human error, computer handles
    # getting the value, and need the value because going to use it in the
    # following entry
    cur.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES (?)''', ( genre, ) )

    cur.execute('SELECT id FROM Genre WHERE name = ?', ( genre, ) )
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT or IGNORE INTO Album (title, artist_id)
        VALUES (?,?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ?', (album,))
    # good way to think here is that row is actually what the cursor is pointing at
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES (?,?,?,?,?,?)''',
        (name, album_id, genre_id, length, rating, count))

    conn.commit()