#given a word and a list of possible anagrams, selects the correct sublist.

def anagram(word , keys):
    for key in keys :
        if sorted(word ) == sorted(key):
           return key 
    return None
keys = [ 'enlists', 'google', 'inlets', 'banana'] 
print(anagram(input('write your string !')  , keys))          
