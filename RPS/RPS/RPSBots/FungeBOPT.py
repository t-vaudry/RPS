import random

def move(prevDir, cur):
    if prevDir == ">":
        if (cur % 10) == 9:
            cur -= 9
        else:
            cur += 1
    elif prevDir == "v":
        cur += 10
    elif prevDir == "<":
        if cur % 10 == 0:
            cur += 9
        else:
            cur -= 1
    elif prevDir == "^":
        cur -= 10
    if cur < 0:
        cur += 100
    if cur > 100:
        cur -= 100
    return cur

def funge(source, inp):
    cur = 0
    stack = []
    out = ""
    allDir = [">","v","<","^"]
    prevDir = ">"
    stringMode = False
    while source[cur] != "@":
        if stringMode:
            if source[cur] == '"':
                stringMode = False
            else:
                stack.append(ord(source[cur]))
        else:
            if source[cur] in allDir:
                prevDir = source[cur]
            elif source[cur] == "?":
                prevDir = random.choice(allDir)
            elif source[cur] == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif source[cur] == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(a-b)
            elif source[cur] == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif source[cur] == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(a//b)
            elif source[cur] == "%":
                a = stack.pop()
                b = stack.pop()
                stack.append(a%b)
            elif source[cur] == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(a-b)
            elif source[cur] == "!":
                if stack.pop() == 0:
                    stack.append(1)
                else:
                    stack.append(0)
            elif source[cur] == "`":
                a = stack.pop()
                b = stack.pop()
                if b > a:
                    stack.append(1)
                else:
                    stack.append(0)
            elif source[cur] == "_":
                if stack.pop() == 0:
                    prevDir = ">"
                else:
                    prevDir = "<"
            elif source[cur] == "|":
                if stack.pop() == 0:
                    prevDir = "v"
                else:
                    prevDir = "^"
            elif source[cur] == '"':
                stringMode = True
            elif source[cur] == ":":
                a = stack.pop()
                stack.append(a)
                stack.append(a)
            elif source[cur] == "\\":
                a = stack.pop()
                b = stack.pop()
                stack.append(a)
                stack.append(b)
            elif source[cur] == "$":
                stack.pop()
            elif source[cur] == ".":
                out = stack.pop()
            elif source[cur] == ",":
                out = chr(stack.pop())
            elif source[cur] == "#":
                cur = move(prevDir, cur)
            elif source[cur] == "p":
                y = stack.pop()
                x = stack.pop()
                z = stack.pop()
                source[x+(y*10)] = chr(z)
            elif source[cur] == "g":
                y = stack.pop()
                x = stack.pop()
                stack.append(ord(source[x+(y*10)]))
            elif source[cur] == "~":
                if inp:
                    stack.append(ord(inp))
                else:
                    stack.append(ord("X"))
            elif source[cur].isdigit():
                stack.append(ord(source[cur])-48)
        cur = move(prevDir, cur)
    return out

source = ['>',' ',' ',' ',' ',' ',' ','~',':','v',\
          '>',',','@',' ',' ','>','2','9','v','1',\
          '+','>','*','+','-','|',' ',' ','9','9',\
          '*','9',' ',' ',' ','1',' ',' ','*','9',\
          '9','9','@',' ',' ','9',' ',' ','+','*',\
          '9','2',',',' ',' ','9',' ',' ',',','-',\
          '2',':','^','+','*','<',' ',' ','@','-',\
          '^','|','-','+','*','9','9','1',':','_',\
          '1','<',' ',' ','@',',','-','*','9','9',\
          ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
inp = input
output = funge(source, inp)