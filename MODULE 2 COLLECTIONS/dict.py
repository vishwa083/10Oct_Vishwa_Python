data={'ID':101,'Name':'Vishwa','Sub':'Python','City':'Rajkot'}
print(data)
'''print(data['Name'])
print(data.get('ID'))
print(data.keys())
print(data.values())
print(len(data))
'''
#data['ID']=102
#data['Name']='Komal'
#data.pop('City')
#del data['Name']
#data.clear()
#print(data)

'''newdata=data.copy()
print(newdata)'''

'''for i in data:
    print(i)'''

'''for i in data.values():
    print(i)'''

'''for i in data.items():
    print(i)'''

'''for i,j in data.items():
    #print(i,j)
    print(f"key={i} and values={j}")'''

'''if 'Name' in data:
    print("Yes...")
else:
    print("Noo...")'''

if 'Rajkot' in data.values():
    print("yes...")
else:
    print("No...")