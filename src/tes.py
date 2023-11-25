import os

global currentChar
global states
global input_symbol
global stack
global start_state
global start_stack
global final_state 
global word

f = open("a.txt", "r")
blank = " "
newline = '\n'
currentChar = f.read(1)

states = []
input_symbol = []
stack = []
start_state = []
start_stack = []
final_state = []
transition_function = {}

def ignoreBlank():
    global currentChar
    while currentChar == blank:
        currentChar = f.read(1)

def ignoreNewline():
    global currentChar
    while currentChar == newline:
        currentChar = f.read(1)

def readWord():
# I.S : berada di karakter pertama yang ingin dibaca
    global currentChar
    global word
    word = ''
    while currentChar != blank and currentChar != newline and currentChar != "":
        word += currentChar
        currentChar = f.read(1)
    return word

def readTag():
    global currentChar
    global tag
    tag = ''
    currentChar = f.read(1)
    if currentChar == "/":
        x = True
    while currentChar != blank or currentChar != ">":
        tag += currentChar
        currentChar = f.read(1)
    
    return tag, x
        

def createPDA(states, input_symbol, stack, start_state, start_stack, final_state, transition_function):
    global currentChar
    global word
    temp_transition = []
    while currentChar != newline:
        states.append(readWord())
        ignoreBlank()
    ignoreNewline()
    while currentChar != newline:
        input_symbol.append(readWord())
        ignoreBlank()
    ignoreNewline()
    while currentChar != newline:
        stack.append(readWord())
        ignoreBlank()
    ignoreNewline()
    while currentChar != newline:
        start_state.append(readWord())
        ignoreBlank()
    ignoreNewline()
    while currentChar != newline:
        start_stack.append(readWord())
        ignoreBlank()
    ignoreNewline()
    while currentChar != newline:
        final_state.append(readWord())
        ignoreBlank()
    ignoreNewline()
    while currentChar != "":
        temp_transition = []
        i = 0
        trans_tuple = ()
        prod = ()
        while currentChar != newline and currentChar != '' and currentChar != None:
            if i < 3:
                trans_tuple += (readWord(),)
            else:
                prod += (readWord(),)
            i += 1
            ignoreBlank()
        transition_function[trans_tuple] = prod
        ignoreNewline()
    
createPDA(states, input_symbol, stack, start_state, start_stack, final_state, transition_function)
start_state = start_state[0]
start_stack = start_stack[0]
final_state = final_state[0]
stack = []
list = []
f.close()

def attr():
    attr = ""
    while currentChar != "=" or currentChar != blank or currentChar != "":
        x = f.read(1)
        attr += x
    if currentChar == blank:
        ignoreBlank()
    if attr != "type\"" or attr != "method\"":
        if currentChar == "=":
            attr += currentChar
            x = f.read(1)
            ignoreBlank()
            if currentChar == "\"":
                attr += currentChar
                while currentChar != "\"" and currentChar != "":
                    x = f.read(1)
                if currentChar == "":
                    g = False
                attr += x
            else :
                g = False
        else:
            g = False
    else:
        if currentChar == "=":
            attr += currentChar
            x = f.read(1)
            ignoreBlank()
            if currentChar == "\"":
                attr += currentChar
                while currentChar != "\"" and currentChar != "":
                    x = f.read(1)
                    attr += x
                if currentChar == "":
                    g = False
            else :
                g = False
        else:
            g = False
    return attr

state = ""

f = open("testing.html", "r")
currentChar = f.read(1)
while currentChar != "":
    if currentChar == "<":
        x = readTag()
        stack.append(x)
        while currentChar != ">" or currentChar != "" or currentChar != "/":
            ignoreBlank()
            stack.append(attr())
        if currentChar == ">":
            stack.append(">")
        else:
            g = False

while currentChar != "":
    if state[:1] == "in" or state == "out":
        if currentChar == "<":
            currentChar,x = readTag()
            stack.append(x)
            if not x :
                ignoreBlank()
                while currentChar != ">" or currentChar != "":
                    ignoreBlank()
                    stack.append(attr())
                if currentChar == ">":
                    stack.append(">")
                else:
                    g = False
        
# <html id=""