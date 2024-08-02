user_info = {
    'name' : 'mehraj',
    'age' : 24,
    'fav_movie' : 'agar tum sath ho'
}
more_info = {'hobby' : 'cricket',
             'fav_cricketer': 'kohli'
}
same_data = {'name':'raheem'}

# how to add data in dictionary

user_info['fav song'] = ['song1,song2']
print(user_info)

# # pop method:-
# # we can store this in variable
popped_item = user_info.pop('fav_movie')
print(f"this is pop {popped_item}")
print(user_info) 
print(type(user_info))
# poppeditem method :-
# use to delete data randomly
# this method return tuples
popped_items = user_info.popitem()
print(user_info)
# if u wanna check what item has popped 
print(popped_items)

# update() method
# we use this method to add one dictionary into other dictionary
# if both dictionary contain same key with different values it will replace it or update it .
# for ex: first name contain mehraj and other one with raheem it will give  raheem as a result
(user_info.update(more_info))
user_info.update(same_data)
print(user_info)


