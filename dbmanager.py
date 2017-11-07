import sqlite3
def create_database():
    sqlite_file= 'databases.db'
    table_name= 'users'
    id_column= 'id_column'
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

   # c.execute('''DROP TABLE  IF EXISTS users''')
    c.execute('''CREATE TABLE IF NOT EXISTS users(id  INTEGER PRIMARY KEY AUTOINCREMENT , username TEXT NOT NULL , password TEXT NOT NULL )''')
    """
     c.execute('''CREATE TABLE IF NOT EXISTS {tn}({nf}{ft})'''.format(tn = table_name, nf = id_column, ft ='INTEGER PRIMARY KEY ' ))
    #ADD NEXT COULUMN
    new_column = 'username'
    columnType = 'TEXT'
    c.execute('''ALTER TABLE {tn} ADD COLUMN "{cn}" {ct}'''.format(tn= table_name, cn= new_column, ct= columnType))
    new_column = 'password'
    columnType = 'TEXT'
    c.execute('''ALTER TABLE {tn} ADD COLUMN "{cn}"{ct}'''.format(tn = table_name, cn = new_column, ct = columnType))
    #c.execute('''Select name from table_name''')

    """

    conn.execute('''CREATE TABLE IF NOT EXISTS usersaves(id_column INTEGER , key_word TEXT, timeStap DATE,FOREIGN  KEY(id_column) REFERENCES users(id_column));''')
    print('Database and table(s) created!')
    conn.commit()
    conn.close()
def showEntries():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM users''')
    print(c.fetchall())
create_database()