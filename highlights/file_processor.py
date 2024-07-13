import sqlite3
from highlights.models import Highlight

def bob():
    database = "KoboReader2.sqlite"

    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("select BookmarkID, Text from Bookmark")
    rows= cur.fetchall()

    # for row in rows:
        # print(row)


    id, text = rows[69]

    h = Highlight(id, text)
    h.save()


    conn.close()

def process_sqlite_db(file):
    return

def handle_uploaded_file(f):
    with open("some/file/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)