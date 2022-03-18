import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

# Make connection
connection = hb.Connection()
powers_table = connection.table('powers')

for key, data in powers_table.scan(include_timestamp=True):
    print('Found: {}, {}'.format(key, data))

# Close Connection
connection.close()