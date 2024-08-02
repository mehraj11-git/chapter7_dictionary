# d = {'a':'1','h':'2'}

def word_counter(s):
    count = {}
    for i in s:
        count[i] = s.count(i)
    return count
print(word_counter('mehraj'))    


# this method replace the same item 
# this dict method is unordered collection of items means this will give result randomly