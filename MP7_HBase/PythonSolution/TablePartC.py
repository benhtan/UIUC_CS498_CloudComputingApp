import happybase as hb
import csv

# Make connection
connection = hb.Connection()
powers_table = connection.table('powers')

file = open('input.csv', 'r')
reader = csv.reader(file) # List of list ['row1', 'yes', 'fly', 'batman', '100', 'black']

batch = powers_table.batch()
for row in reader:
    batch.put( row[0], {'personal:hero': row[1], 'personal:power': row[2], 'professional:name': row[3], 'professional:xp': row[4], 'custom:color': row[5]}  )
    
batch.send()

# Close Connection
connection.close()
file.close()
