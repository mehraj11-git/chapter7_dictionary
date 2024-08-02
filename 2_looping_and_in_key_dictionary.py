user_info = {
    'name' : 'mehraj',
    'age' : 24,
    'fav_movie' : 'agar tum sath ho'
}
# looping in dictionary and in keyword method

if 'name' in user_info:
    print('present')
else:
    print('not present')
# for checking key we use this method( if method)
# for checking values we use this method (.values())
# # we type data in integer or string form
# # for checking complete list then you have to put complete list.
# key present on left hand side and values present on right hand side in dictionary
if 'mehraj' in user_info.values():
        print('present')
else:
        print("not present")

for i in user_info:
      print(i) 
for i in user_info.values():
      print(i)     
for i in user_info.values():
      print(i,end= " " )    

# values method
user_info_values = user_info.values()
print(user_info_values)
print(type(user_info_values))
# if u wanna add values with the help of keys we use this method
for i in user_info:
      print(user_info[i])


# item method
user_items = user_info.items()
print(user_items)
print(type(user_items))
# this method gives tuple like result
# why this method is useful if we wanna do looping in item we will get this 
# make sure we have to write two variable otherwise it gonna gives tuple as result.
# most useful method in dictionary

for key,value in user_info.items():
      print(f"key is {key} and value is {value}")