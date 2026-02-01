import sqlite3

# Connect to database (creates if not exists)
conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

# Drop table if exists to start fresh
cur.execute('DROP TABLE IF EXISTS Counts')

# Create table with org and count
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# Prompt for file name
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'

fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    # Extract domain (organization)
    org = email.split('@')[1]

    # Check if org already exists
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

# Commit once after processing all lines (faster)
conn.commit()

# Query top 10 organizations
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
