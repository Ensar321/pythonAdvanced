
import sqlite3

# Connect to database
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

# Create employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    departament TEXT NOT NULL,
    salary REAL
)
''')

connection.commit()


cursor.execute('''
    insert into employees (name, position, departament, salary)
    values (?, ?, ?, ?)
''', ('John Doe', 'Software Engineer', 'Tech', 3000.50))
# Insert first employee
# cursor.execute('''
# INSERT INTO employees (name, position, departament, salary)
# VALUES (?, ?, ?, ?)
# ''', ('John Doe', 'Software Engineer', 'Tech', 3000.50))

# Insert second employee
cursor.execute('''
INSERT INTO employees (name, position, departament, salary)
VALUES (?, ?, ?, ?)
''', ('Orges Doe', 'Software Developer', 'Tech', 15000.50))

connection.commit()

# Update employee salary
cursor.execute('''
UPDATE employees
SET salary = ?
WHERE name = ?
''', (7500.00, 'Orges Doe'))

connection.commit()

# Delete employee
cursor.execute('''
DELETE FROM employees
WHERE name = ?
''', ('John Doe',))

connection.commit()

# Display remaining employees
cursor.execute('SELECT * FROM employees')

rows = cursor.fetchall()

for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
connection.close()
