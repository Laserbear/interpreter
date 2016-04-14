# set up token types
INTEGER = "INTEGER"
PLUS = "PLUS"
EOF = "EOF"

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __str__(self):
        return "Token("+str(self.type)+", " + repr(self.value)+"}"
    def __repr__(self):
        return self.__str__()
        
class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.token = None
    def error(self):
        raise Exception("Error while parsing input")
    def tokenize(self):
        text = self.text
        if self.pos > len(text) -1 : #if at end of file
            return Token("EOF", None)
        char = text[self.pos] #get character at current position
        if char.isdigit():
            self.pos += 1
            return Token(INTEGER, int(char))
        if char == "+":
            self.pos += 1
            return Token(PLUS, char)
        self.error()
    def eat(self, token_type):
        if self.token.type == token_type:
            self.token = self.tokenize()
        else:
            self.error()
    def evaluate(self): #cant call it eval because it's a reserved word
        self.token = self.tokenize() #get first token
        loperand = self.token
        self.eat(INTEGER) #verify token type/get next token
        op = self.token 
        self.eat(PLUS) 
        roperand = self.token
        self.eat(INTEGER)
        return loperand.value + roperand.value
while True:
    try:
        text = raw_input("calc> \n")
    except EOFError:
        break
    if not text:
        continue
    runner = Interpreter(text)
    print runner.evaluate()
    
        
            
        