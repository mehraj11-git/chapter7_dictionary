#dictionary means unordered collection of data in key : value pair
# this method use curly bracket { }
# why we use dictionaaries ??? 
# bcz of limitation of list ,lsit are  not enough to represent real data 

name = {'name' : 'mehraj' , 'age' : 23}
print(name)
print(type(name))

# second method to create dict 
user = dict(name = 'mehraj' , age = 24)

# we cannot use index method in dict 
# we use key and pair to print particular item 
#  we can store number, str ,dict inside dict 
# we can store data in more than one line 
user_info = {
'name' : 'mehraj',
'age' : 34,
'gender' : 'male'
}
# we can create a complex data structure in dict 
# how can we add data to empty dict
user_info2 = {}
user_info2['name'] = 'mehraj'
print(user_info2)