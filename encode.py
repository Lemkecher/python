#encode and decode string

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        
        if char != prev_char:
            
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            
            count += 1
    else:
        
        encoding += str(count) + prev_char
        return encoding
encoded_val = rle_encode( input ('write your string   '))
print(encoded_val)