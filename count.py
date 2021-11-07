#count the occurence of each word

def word_count(str):
    words = str.split()
    count = dict()
    for word in words :
        if word in count :
            count[word] += 1
        else:
            count[word] = 1 
    return count 
print (word_count (input ('write your string  :  ')))          