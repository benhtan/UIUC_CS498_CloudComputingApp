import happybase as hb

# Make connection
connection = hb.Connection()

tables = connection.tables()
print(tables)

# Close Connection
connection.close()