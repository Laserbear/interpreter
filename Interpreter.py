# set up token types
INTEGER = "INTEGER"
FLOAT = "FLOAT"
MINUS = "MINUS"
PLUS = "PLUS"
MULTIPLICATION = "MULTIPLICATION"
DIVISION = "DIVISION"
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
       #tokenize  
    def tokenize(self): 
        text = self.text.replace("(", " ( ").replace(")", " ) ").replace("+", " + ").replace("-", " - ").replace("*", " * ").replace("/", " / ").split()
        if self.pos > len(text) -1 : #if at end of file
            return Token("EOF", None)
        char = text[self.pos] #get character at current position
        if char.isdigit():
            self.pos += 1
            return Token(INTEGER, int(char))
        if char == "+":
            self.pos += 1
            return Token(PLUS, char)
        if char == "-":
            self.pos += 1 
            return Token(MINUS, char)
        if char == "*":
            self.pos += 1
            return Token(MULTIPLICATION, char)
        if char == "/":
            self.pos += 1 
            return Token(DIVISION, char)
        self.error()
        
    def eat(self, token_type):
        if self.token.type == token_type:
            self.token = self.tokenize()
        else:
            self.error()
    def add(self, left_operand, right_operand):
        return left_operand.value + right_operand.value
    def subtract(self, left_operand, right_operand):
        return left_operand.value - right_operand.value
    def multiply(self, left_operand, right_operand):
        return left_operand.value * right_operand.value
    def divide(self, left_operand, right_operand):
        return left_operand.value / right_operand.value 
    def evaluate(self): #cant call it eval because it's a reserved word
        self.token = self.tokenize() #get first token
        loperand = self.token
        self.eat(INTEGER) #verify token type/get next token
        op = self.token
        if op.value == "+":
            self.eat(PLUS)
            roperand = self.token
            res = self.add(loperand, roperand)
            self.eat(INTEGER)
        if op.value == "-":
            self.eat(MINUS)
            roperand = self.token
            res = self.subtract(loperand, roperand)
            self.eat(INTEGER)
        if op.value == "*":
            self.eat(MULTIPLICATION)
            roperand = self.token
            res = self.multiply(loperand, roperand)
            self.eat(INTEGER)
        if op.value == "/":
            self.eat(DIVISION)
            roperand = self.token
            res = self.divide(loperand, roperand)
            self.eat(INTEGER)
        
        return res
while True:
    try:
        text = raw_input("calc> \n")
    except EOFError:
        break
    if not text:
        continue
    runner = Interpreter(text)
    print runner.evaluate()
    
        
            
        