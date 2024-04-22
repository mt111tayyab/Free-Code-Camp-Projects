import sqlite3

# conect to sqlite
connection=sqlite3.connect("student.db")

# create a cursor object to insert record, create table, retrieve
cursor=connection.cursor()

# create table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

## create some meore records

cursor.execute('''Insert Into STUDENT values('Mishma','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Elisma','Data Science','A',95)''')
cursor.execute('''Insert Into STUDENT values('Manaham','DEVOPS','A',85)''')
cursor.execute('''Insert Into STUDENT values('Abigail','DEVOPS','B',70)''')

# Display results
print("The inserted records are")

data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

# commit the changes
connection.commit()

# close the connection
connection.close()