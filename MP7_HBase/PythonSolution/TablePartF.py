import happybase as hb

# DON'T CHANGE THE PRINT FORMAT, WHICH IS THE OUTPUT
# OR YOU WON'T RECEIVE POINTS FROM THE GRADER

# Make connection
connection = hb.Connection()
powers_table = connection.table('powers')

powers_scan = []

for key, data in powers_table.scan():
    powers_scan.append(data)

print(powers_scan)

# for key, data in powers_scan:
#     # print(f'data: {data}')
#     for key1, data1 in powers_scan1:
#         color = data[b'custom:color']
#         name = data[b'professional:name']
#         power = data[b'personal:power']

#         color1 = data1[b'custom:color']
#         name1 = data1[b'professional:name']
#         power1 = data1[b'personal:power']
        
        # print(f'data1: {data1}')
        # print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))
        
        # if color == color1 and name != name1:
        #     print('{}, {}, {}, {}, {}'.format(name, power, name1, power1, color))

# Close Connection
connection.close()