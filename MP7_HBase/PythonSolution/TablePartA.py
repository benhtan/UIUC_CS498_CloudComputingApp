import happybase as hb

# Make connection
connection = hb.Connection()

# Delete prior created tables
tables = connection.tables()
for t in tables:
    connection.delete_table(t, disable=True)

# Set families for columns
powers_families = {
    'personal': {},
    'professional': {},
    'custom': {},
}

food_families = {
    'nutrition': {},
    'taste': {},
}

# Make tables
connection.create_table('powers', powers_families)
connection.create_table('food', food_families)

# Close Connection
connection.close()