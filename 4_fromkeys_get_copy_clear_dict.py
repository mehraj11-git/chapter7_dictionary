# fromkeys
# we use this method to create dict
# we can create the dict which contain same values with diff keys
# for ex:
# # d = {"name" : "unknown" ,"age":"unknown" ,"sex":"unknown"}
# we use  paranthesis as well
# if we add data in the form of string "abc" then it will take data separate
# we can use range func as well

d=dict.fromkeys(['name','age','sex'],'unknown')
c=dict.fromkeys("abc",'unknown')
f=dict.fromkeys(('name','age','sex'),'unknown')
r=dict.fromkeys(range(1,11),'unknown')
print(d)
print(c)
print(f)
print(r)

# get method:-
# suppose if we have dict and if we want to access key we use this method
g = {"name" : "unknown" ,"age":"unknown" ,"sex":"unknown"}
print(g['name'])
# suppose if we write key which is not in their dict it will give error
# for this we use get method
print(g['names'])
print(g.get('name'))
# suppose if we write key which is not in their dict it will give NONE as a result (get method)
print(g.get('names'))

if 'name' in g :
    print('presrnt')
else:
    print('not present')    

if g.get('name'):
    print('present')
else:
    print('not present')
 # both methods are correct
#    clear method:-
# we can clear a dict with this method

g.clear()
print(g)

# copy method:-
# we can copy the complete dict to another dict
# we cant copy like this 
g1  = g  # both are same
print(g1)
# for ex:
# print(g1.popitem())
print(g) #look both are same but we want diff dict with same values 
# # for that we use copy method

g1 = g.copy()
print(g1)
# print(g1.popitem())
print(g)
# for checking validity we use 'is' or '==' method
# when you check this make sure you comment out popitem method or pop method ,other wise it will not give correct result
print(g1 is g)
print(g1 == g)


# more about get method:-
user = {"name" : "mehraj" ,"age":"24" ,"sex":"male"}
print(user.get('name'))
print(user.get('names')) #this will give NONE as a result
# if u dont want None as a result we can do like this
print(user.get('names','not found ! '))
print(user.get('names','not present ! '))
# if we have same key with diff values it will replace with one only for ex:
# the value will be overwrite
info= {"name" : "mehraj" ,"age":"24" ,"age":"34", "sex":"male"}
print(info)