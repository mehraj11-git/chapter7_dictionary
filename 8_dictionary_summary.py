#dictionary means unordered collection of data in key : value pair
# this method use curly bracket 

names = {'name' : 'mehraj' , 'age' : 23}

print(names)
print(type(names)) 
user = dict(name = 'mehraj' , age = 24)
print(user) 

# there is no indexing in dictionary 
# we use key to access about the data
# we can store number,list,string,dictionary
# we can add dictionary inside dictionary 
# we can add data to empty dictionary

user_info = {
    'name' : 'mehraj',
    'age' : 24,
    'fav_movie' : 'agar tum sath ho'
}
print(user_info,end= " ")
#  add data
data = {}
data['name'] = 'mohit'
print(data)
 
#  we use in keyword method to check for key
# to print all keys 
for i in names:
    print(i)

# to print all values 
for i in names.values():
    print(i)

# more common dict method
# get method
# this method use to access a key and checck existance#
print(names.get('age')) 
print(names.get('agess')) # no error,gives NOne as a result

# to delete item 
# pop method --->take one argument which is keyname
pooped_item = names.pop('name')
print(pooped_item)
print(names)


# popitems
# this method delete item randomly
popped_items = names.popitem()