import string

# STRT: DO NOT ALTER THIS CLASS!
class Cipher():

    def encode(self, plaintext=None):
        # Raise an error if the inherited class doesn't implement this
        raise NotImplementedError()

    def decode(self, ciphertext=None):
        # Raise an error if the inherited class doesn't implement this
        raise NotImplementedError()

    def __eq__(self, other):
        # Raise an error if the inherited class doesn't implement thi
        raise NotImplementedError()

# END: DO NOT ALTER THIS CLASS!
# -----------------------------------------------------------------------------

# This is here to help you if you want to use it:
UPPER_CHARS = string.ascii_uppercase

# Your work begins here
class Reverse(Cipher):
    def __init__(self):
        super().__init__()    

    def encode(self, plaintext):
        self.plaintext = plaintext
        if plaintext == None:
            return Cipher().encode(plaintext=None)
        return plaintext

    def decode(self, ciphertext):
        self.ciphertext = ciphertext
        if ciphertext == None:
            return Cipher().decode(ciphertext=None)
        x = ciphertext
        ciphertext = ""
        length = len(x)
        for i in x:
            length -= 1
            ciphertext = ciphertext + x[length]
        return ciphertext

class Ceasar(Cipher):
    def __init__(self, shift):
        super().__init__()
        self.shift = shift

    def encode(self, plaintext):
        self.plaintext = plaintext
        if plaintext == None:
            return Cipher().encode(plaintext=None)
        return plaintext

    def decode(self, ciphertext):
        self.ciphertext = ciphertext
        if ciphertext == None:
            return Cipher().decode(ciphertext=None)
        x = ciphertext
        ciphertext = ""
        shiftciph = self.shift
        shiftciph = shiftciph%26
        for i in range(0,len(x)):
            if x[i].isalpha():
                y = ord(x[i])
                y = y + shiftciph
                if x[i].isupper():  
                    if y >= 91:
                        y = y - 26
                if x[i].islower():
                    if y >= 123:
                        y = y - 26
                y = chr(y)
                ciphertext = ciphertext + y
            else:
                ciphertext = ciphertext + x[i]
        return ciphertext


class Rot13(Ceasar): 
    def __init__(self):
        shift = None
        super().__init__(shift)
        super().__init__(Ceasar(self.shift))


    def encode(self, plaintext):
        self.plaintext = plaintext
        plaintext = Ceasar(shift=0).encode(plaintext)
        return plaintext

    def decode(self, ciphertext):
        self.ciphertext = ciphertext
        thirteenshift = Ceasar(shift=13).decode(ciphertext)
        return thirteenshift

class Vignere(Cipher):
    def __init__(self, key):
        self.key = key    
        
    def encode(self, plaintext):
        self.plaintext = plaintext
        if plaintext == None:
            return Cipher().encode(plaintext=None)
        return plaintext

    def decode(self, ciphertext):
        key = self.key.upper()
        self.ciphertext = ciphertext
        if ciphertext == None:
            return Cipher().decode(ciphertext=None)
        vigcipher = ""
        keylist = []
        length = len(key)
        LenCiph = len(ciphertext)
        for i in range(0, length):
            keydistance = ord(key[i]) - 65
            keylist.append(keydistance)   
        for i in range(0,LenCiph):
            var = i%length        
            if ciphertext[i].islower():
                y = ord(ciphertext[i]) + keylist[var] 
                if y >= 123:
                    y = y - 26
                y = chr(y)
                vigcipher = vigcipher + y
            if ciphertext[i].isupper():
                y = ord(ciphertext[i]) + keylist[var] 
                if y >= 91:
                    y = y - 26
                y = chr(y)
                vigcipher = vigcipher + y
        return vigcipher      


class Message():
    def __init__(self, plaintext, cipher):
        self.plaintext = plaintext
        self.cipher = cipher

    def __eq__(self, other):
        self.other = other
        if isinstance(other, self.plaintext):
            return self.plaintext
                
        if isinstance(other, self.cipher):
            return self.cipher
        
# This is extra credit!
class RailFence(Cipher):
    def __init__(self, num_rails):
        super().__init__()
        self.num_rails = num_rails

    def encode(self, plaintext):
        self.plaintext = plaintext
        if plaintext == None:
            return Cipher().encode(plaintext=None)
        return plaintext

    def decode(self, ciphertext):
        self.ciphertext = ciphertext
        if ciphertext == None:
            return Cipher().decode(ciphertext=None)
        x = self.num_rails
        length = len(ciphertext)
        RailLeng = x
        listRail = []
        while(RailLeng > 0):
            newrail = ""
            for i in range(0,(length)):
                if i%x == (x - RailLeng):
                    newrail = newrail + (ciphertext[i])
                else:
                    newrail = newrail + " "
            listRail.append(newrail)
            RailLeng -= 1
        ciphertext = ""
        for i in range(0,x):
            ciphertext = ciphertext + listRail[i] + "\n"
        return ciphertext
