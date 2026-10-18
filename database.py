import sqlite3

connection = sqlite3.connect('issues.db')

connection.execute('''
    CREATE TABLE IF NOT EXISTS issues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        location TEXT NOT NULL,
        category TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Open',
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
''')

connection.commit()
connection.close()

print('Database ready!')