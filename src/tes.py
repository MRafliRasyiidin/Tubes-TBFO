import os

global currentChar
global states
global input_symbol
global stack
global start_state
global start_stack
global final_state 
global word

f = open("PDA++++.txt", "r")
blank = " "
newline = '\n'
currentChar = f.read(1)

states = []
input_symbol = []
stack_list = []
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
    while currentChar != blank and currentChar != ">":
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

def closeProgram():
    print(current_stack)
    print(current_state)
    print(x)
    print(trans)
    print(stack)
    print("curr,", currentChar )
    print("Syntax Error")
    exit()

def compareTransition(curr_state, input_sym, curr_stack):
    global stack
    global current_state
    global current_stack
    global trans
    trans = (curr_state, input_sym, curr_stack)
    trans2 = (curr_state, "e", curr_stack)
    if trans in transition_function:
        result = transition_function[trans]
        current_state = result[0]
        stack.pop()
        if len(result[1]) == 2:
            stack.append(result[1][1])
            stack.append(result[1][0])
            current_stack = result[1][0]
        else:
            if result[1] != "e":
                stack.append(result[1])
                current_stack = result[1][0]
            else:
                current_stack = stack[len(stack)-1]
    elif trans2 in transition_function:
        result = transition_function[trans2]
        current_state = result[0]
        stack.pop()
        if len(result[1]) == 2:
            stack.append(result[1][1])
            stack.append(result[1][0])
            current_stack = result[1][0]
        else:
            if result[1] != "e":
                stack.append(result[1])
                current_stack = result[1][0]
            else:
                current_stack = stack[len(stack)-1]
        compareTransition(current_state, input_sym,current_stack)
    else:
        print(trans)
        closeProgram()

def attr():
    attr = ""
    while currentChar != "\"" or currentChar != blank:
        x = f.read(1)
        attr += x
        
    if attr != "type=\"" or attr != "method=\"":
        if currentChar == blank:
            ignoreBlank()
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
        if currentChar == blank:
            ignoreBlank()
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
                    closeProgram()
            else :
                closeProgram()
        else:
            closeProgram()

def readAttribute():
    global currentChar
    global attribute
    attribute = ''
    while  currentChar != "\"" and currentChar != "" and currentChar != ">":
        attribute += currentChar
        currentChar = f.read(1)
        if currentChar == blank:
            ignoreBlank()
    if currentChar == ">" or currentChar == "":
        print("bjir")
        closeProgram()
    else:
        attribute += currentChar
        if attribute in special_attribute:
            currentChar = f.read(1)
            while  currentChar != "\"" and currentChar != "" and currentChar != ">":
                attribute += currentChar
                currentChar = f.read(1)
            if currentChar == ">" and currentChar == "":
                closeProgram()
            else:
                attribute += currentChar
            if attribute not in full_special_attribute:
                closeProgram()
        else:
            currentChar = f.read(1)
            while  currentChar != "\"" and currentChar != "" and currentChar != ">":
                currentChar = f.read(1)
            if currentChar == ">" and currentChar == "":
                print("cokk")
                closeProgram()
            else:
                attribute += currentChar
    return attribute

    
createPDA(states, input_symbol, stack_list, start_state, start_stack, final_state, transition_function)
current_state = start_state[0]
current_stack = start_stack[0]
final_state = final_state[0]
stack = []
list = []
stack.append(current_stack)
special_attribute = ["type=\"", "method=\""]
full_special_attribute = ["type=\"text\"", "type=\"password\"", "type=\"email\"", "type=\"number\"", "type=\"checkbox\"", "type=\"text\"", "type=\"button\"","type=\"reset\"", "type=\"submit\"", "method=\"GET\"", "method=\"POST\""]
f.close()
print(full_special_attribute)

f = open("testing.html", "r")
currentChar = f.read(1)
while currentChar != "":
    if currentChar == "<":
        x = readTag()
        if x == "<!--":
            ignoreBlank()
            closeComment = ""
            while closeComment != "-->" and currentChar != "":
                closeComment += currentChar
                currentChar = f.read(1)
                if len(closeComment) > 3:
                    a = ""
                    a += closeComment[1]
                    a += closeComment[2]
                    a += closeComment[3]
                    closeComment = a
            if closeComment != "-->":
                closeProgram()
        else:
            if "/" not in x:
                compareTransition(current_state, x, current_stack)
            ignoreBlank()
            if currentChar == ">":
                if "/" in x:
                    x += currentChar
                    compareTransition(current_state, x, current_stack)
                else:
                    compareTransition(current_state, currentChar, current_stack)
            else:
                while currentChar != ">" and currentChar != "":
                    ignoreBlank()
                    p = readAttribute()
                    if p in input_symbol:
                        compareTransition(current_state, p, current_stack)
                    elif p in full_special_attribute:
                        compareTransition(current_state, p, current_stack)
                    else:
                        closeProgram()
                    currentChar = f.read(1)
                    ignoreBlank()
                if currentChar == ">":
                    compareTransition(current_state, currentChar, current_stack)
    if current_state == "ininput" or current_state == "inhr" or current_state == "inimage" or current_state == "inlink":
        compareTransition(current_state, "e", current_stack)
    currentChar = f.read(1)
    ignoreNewline()
    ignoreBlank()
    print(stack, current_state, tag)
    


print(current_state)
print(current_stack)
print(stack)
# <html id=""