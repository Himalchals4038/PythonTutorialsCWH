import sqlite3
conn = sqlite3.connect("sqlite1.db")
conn.execute('''
Create Table Student(
        st_id INT AUTO_INCREMENT PRIMARY KEY,
        st_name VARCHAR(50),
        st_class VARCHAR(10),
        st_email VARCHAR(30)
    )
''')
conn.close()