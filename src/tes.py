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
    while currentChar != ">":
        tag += currentChar
        currentChar = f.read(1)
    return tag

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
f.close()

f = open("testing.html", "r")
currentChar = f.read(1)
for line in f:
    if currentChar == "<":
        x = readTag()
    