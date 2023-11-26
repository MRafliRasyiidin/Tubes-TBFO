import os
import sys

global currentChar
global line
global word

f = open("PDA.txt", "r")
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
line = 1

def ignoreBlank():
    global currentChar
    while currentChar == blank:
        currentChar = f.read(1)

def ignoreNewline():
    global currentChar
    global line
    while currentChar == newline:
        line += 1
        currentChar = f.read(1)

def ignoreBoth():
    global currentChar
    global line
    while currentChar == newline or currentChar == blank:
        if currentChar == newline:
            line += 1
        currentChar = f.read(1)

def readWord():
# I.S : berada di karakter pertama yang ingin dibaca
    global currentChar
    global word
    global line
    word = ''
    while currentChar != blank and currentChar != newline and currentChar != "":
        word += currentChar
        currentChar = f.read(1)
    return word

def readTag():
    global currentChar
    global tag
    global line
    tag = ''
    while currentChar != blank and currentChar != ">" and currentChar != newline:
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
    global f
    print("\033[1;31mSyntax Error.\033[0m")
    print("Terjadi kesalahan ekspresi pada line "+str(line-658)+":", full[line-658-1].strip(), "\n")
    f.close()
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
                if len(stack) == 0:
                    current_stack = ""
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
                if len(stack) == 0:
                    curr_stack = ""
                else:
                    current_stack = stack[len(stack)-1]
        compareTransition(current_state, input_sym,current_stack)
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
        print("Attribute-nya salah, Mas.")
        closeProgram()
    else:
        attribute += currentChar
        if attribute in special_attribute:
            currentChar = f.read(1)
            while  currentChar != "\"" and currentChar != "" and currentChar != ">":
                attribute += currentChar
                currentChar = f.read(1)
            if currentChar == ">" and currentChar == "":
                print("Attribute-nya salah, Mas.")
                closeProgram()
            else:
                attribute += currentChar
            if attribute not in full_special_attribute:
                print("Attribute-nya salah, Mas.")
                closeProgram()
        else:
            currentChar = f.read(1)
            while  currentChar != "\"" and currentChar != "" and currentChar != ">":
                currentChar = f.read(1)
            if currentChar == ">" and currentChar == "":
                print("Attribute-nya salah, Mas.")
                closeProgram()
            else:
                attribute += currentChar
    return attribute

def readFull(dir):
    global full
    full = []
    f = open(dir, "r")
    for line in f:
        full.append(line)
    f.close()
    
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

dir_valid = False

while not dir_valid: 
    nama_file = input(str("Masukkan nama file: "))
    dir = "../test/" + nama_file
    if not os.path.isfile(dir):
        print("File-nya tidak ada, Mas. Masukkan nama yang valid.\n")
    else:
        dir_valid = True

readFull(dir)

f = open(dir, "r")
currentChar = f.read(1)

while currentChar != "":
    if (current_state == "inhtml" and current_stack == "h") or (current_state == "inbody" and current_stack == "b") or (current_state == "inhead" and current_stack == "H"):
        if currentChar != "<":
            closeProgram()
    if currentChar == "<":
        x = readTag()
        if "<!--" in x:
            if currentChar == ">" and x[len(x)-1] == "-" and x[len(x)-2] == "-":
                x = "<!----"
                x += currentChar
                compareTransition(current_state, x, current_stack)
            else:
                ignoreBoth()
                closeComment = ""
                while closeComment != "-->" and currentChar != "":
                    currentChar = f.read(1)
                    closeComment += currentChar
                    if len(closeComment) > 3:
                        a = ""
                        a += closeComment[1]
                        a += closeComment[2]
                        a += closeComment[3]
                        closeComment = a
                if closeComment != "-->":
                    closeProgram()
                else:
                    x += closeComment
                    compareTransition(current_state, x, current_stack)
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
                    ignoreBoth()
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
    ignoreBoth()

    
compareTransition(current_state, "e", current_stack)
if current_state == "F":
    print("\n\033[1;32mAccepted, Mas.\033[0m\n")
f.close()