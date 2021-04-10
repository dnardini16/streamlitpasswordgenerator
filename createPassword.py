import random
import string

def createPWD(num_char=12,cases=True,getSymbol=True,getNumber=True):
    
    def split(word):
        return [char for char in word]

    if getNumber == True and getSymbol== True:
        len_char = num_char-2
    elif getNumber == True and getSymbol== False:
        len_char = num_char-1
    elif getNumber == False and getSymbol== True:
        len_char = num_char-1
    else:
        len_char = num_char
    
    password = ''.join(random.choice(string.ascii_uppercase) for _ in range(len_char))
    letters = split(password)
    
    if cases == True:
        samples = random.sample(letters, int(len(letters)/2))
        for letter in samples:
            letters.remove(letter)
            letter = letter.lower()
            letters.append(letter)
    else:
        pass
        
    if getNumber == True:
        number = random.choice(string.digits)
        letters.append(number)
        
    if getSymbol== True:
        symbol = random.choice(["?","!","^","_","@","$","%"])
        letters.append(symbol)

    random.shuffle(letters)
    
    password = "".join(letters)
    return password