# "Database code" for the DB Forum.

import psycopg2
import bleach

DBNAME = 'forum'

def get_posts():
    db = psycopg2.connect(database = DBNAME)
    cursor = db.cursor() #create a cursor object
    cursor.execute("select content, time from posts order by time desc")
    posts = cursor.fetchall()
    db.close()
    return posts

def add_post(content):
    db = psycopg2.connect(database = DBNAME)
    c = db.cursor() #create a new cursor object
    c.execute("insert into posts values (%s)", (bleach.clean(content),))
    db.commit()
    db.close()
