# def a func contain an argument 
# return a dict contianing cube of numbers from 1 to n


def cube_finder(n):
    cube = {}
    for i in range(1,n+1):
        cube[i] = i**3
    return cube
print(cube_finder(10))    