'''data={"st1":"Vishwa","st2":"Komal","st3":"kashish"}
print(data)'''

data={"st1":{'id':101,'name':'vishwa','sub':'Python'},
      "st2":{'id':102,'name':'Komal','sub':'Php'},
      "st3":{'id':103,'name':'Kashish','sub':'java'}}
#print(data)
print(data.get('st1'))
print(data['st1']['name'])
