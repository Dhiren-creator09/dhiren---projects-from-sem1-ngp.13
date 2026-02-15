def encode(message):
    vowels = {"a":"1","e":"45","i":"io","o":"yu","u":"kit"}
    result = ""
    
    for letter in message:
        if letter in vowels:
            result += vowels[letter]
        else:
            result += letter
            
    print("Encoded:", result)


def decoded(message):
    reverse_vowels = {"1":"a","45":"e","io":"i","yu":"o","kit":"u"}
    result = message
    
    for code in reverse_vowels:
        result = result.replace(code, reverse_vowels[code])
        
    print("Decoded:", result)


message = "enter youre message"
encode(message)
decoded(message)
