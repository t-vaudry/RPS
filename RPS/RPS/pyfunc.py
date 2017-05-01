import dis
def compileString(botFileName):
    #print "compiling code"
    code_str = """
print "Hello, world"
if input == "":
    x = 0
x = x+2
if input == "car":
    x = x*10
    """    
    
    f = open(botFileName, "r")
    code_str = f.read()
    f.close()
        
    #print code_str
    code_obj = compile(code_str, '<string>', 'exec')
        
    #dis.dis(code_obj)
    test2 = dict()
    test2["input"] = ""
    
    #exec code_obj in test2
      
    return [code_obj, test2]

def executeCode(code_obj, test2, moveInput):   
	test2["input"] = moveInput
	exec code_obj in test2
	#print(test2["history"])
	moveOutput = test2["output"]
	#print(test2["output"])

	return [code_obj, test2, moveOutput]



def simple():
    print "SUCCESS!"
