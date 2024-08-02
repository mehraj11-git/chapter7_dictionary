# ask the user to input data in empty dict
# 

user = {}
name = input("what is your name : ")
age = input("what is your age : ")
sex = input ("what is your sex : ")
fav_movie = input("your fav movie separated by ,").split(',')
fav_song = input('your fav movie separated by ,').split(',')
user['name'] = name
user["age"] = age
user["sex"]= sex
user['fav_movie']= fav_movie
user["fav_song"] = fav_song
print(user)

#  we use item to print key value pair
# we use this method to print 1/1 means not in one line
for key,value in user.items():
    print(f"{key},and {value}")
