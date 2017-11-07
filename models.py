import sqlite3 as sql
def insertUser(username, password):
    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO users(username, password ) VALUES (?,?)''', (username, password))
    conn.commit()
    conn.close()

def retreiveUsers():
    con = sql.connect('database.db')
    cur = con.cursor()
    cur.execute('''SELECT username, password FROM users''')
    users= cur.fetchall()
    con.close()
    return users


def userExists(uname):
    username= uname
    conn = sql.connect('database.db')
    c = conn.cursor()
    c.execute('''SELECT username FROM users WHERE username = ?''', (username,))
    data = c.fetchall()
    if len(data) == 0:
        return False
    else:
        print(username + "found in the database!")
        conn.close()
        return True




def getPassword(uname):
    uname = uname
    con = sql.connect('database.db')
    c = con.cursor()
    c.execute('''SELECT username FROM users WHERE username = ?''', (uname,))
    data = c.fetchall()
    if len(data) == 0:
        print(uname + "is not found in the database")
        return False
    else:
        print(uname + "is found in the database!")
        return True

    #return None