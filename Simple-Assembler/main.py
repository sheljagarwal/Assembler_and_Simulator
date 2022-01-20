from sys import stdin

commandlist = []
errorflag = 0
for line in stdin:
    
    if line == '': 
        break
    
    commandlist.append(line)

for i in range(len(commandlist)) :
    commandlist[i] = commandlist[i].replace("\t"," ")
    commandlist[i] = commandlist[i].strip("\n")


command_list = []
for i in range(len(commandlist)) :
    command_list.append(list(commandlist[i].split(" ")))

lineNumber = list(range(len(command_list)))
LineNumber = [i+1 for i in lineNumber]
for i in range(len(command_list)) :
    if command_list[i] != [''] :
        command_list[i].append(LineNumber[i])

commandList = [i for i in command_list if i != ['']]

for i in range(len(commandList)) :
    commandList[i] = list(filter(None, commandList[i]))

defaultLabel = "def:"
for i in range(len(commandList)) :
    if commandList[i][0][-1] == ':' :
        continue
    else :
        commandList[i].insert(0, defaultLabel)

for i in range(len(commandList)) :
    if len(commandList[i]) == 2 :
        print(f"Error in line {commandList[i][-1]}: General Syntax Error")
        exit()

for i in range(len(commandList)) :
    if commandList[i][1] == 'var' :
        if len(commandList[i]) < 3 :
            print(f'Error in line { commandList[i][-1]} : Variable declared without assigning name.')
            exit()
        else :
            continue
    else :
        continue


variableIndex = []
for i in range(len(commandList)) :
    if commandList[i][1] == 'var' :
        variableIndex.append(i)


if variableIndex != list(range(len(variableIndex))) :
    dum1 = 0
    for i in range(len(variableIndex)) :
        if variableIndex[i] != i :
            dum1 = variableIndex[i]
            break
    print(f"Error in line {commandList[dum1][-1]} : All variables not declared in the beginning")
    exit()

for i in range(len(variableIndex)) :
    commandList.append(commandList.pop(0))

for i in range(len(commandList)) :
    commandList[i].insert(0, i)

variableAddress = {}
variableNames = []
for i in range(len(commandList)) :
    if commandList[i][2] == 'var' :
        variableAddress[commandList[i][3]] = commandList[i][0]
        variableNames.append(commandList[i][3])

n = len(variableNames)

lableAddress = {}
lableNames = []
for i in range(len(commandList)) :
    if commandList[i][1] == 'def:' :
        continue
    else :
        lableAddress[commandList[i][1][ : -1]] = commandList[i][0]
        dum = commandList[i][1][ : -1]
        lableNames.append(dum)


registerAddress = {'R0' : '000','R1' : '001','R2' : '010','R3' : '011','R4' : '100','R5' : '101','R6' : '110','FLAGS' : '111'}
registerNames = ['R0' , 'R1' , 'R2' , 'R3', 'R4', 'R5', 'R6', 'FLAGS']


opcodes = { 'add' : '00000' , 'sub' : '00001' , 'movimm' : '00010' ,
            'movreg' : '00011' , 'ld' : '00100' , 'st' : '00101' ,
            'mul' : '00110' , 'div' : '00111' , 'rs' : '01000' ,
            'ls' : '01001' , 'xor' : '01010' , 'or' : '01011' ,
            'and' : '01100' , 'not' : '01101' , 'cmp' : '01110' ,
            'jmp' : '01111' , 'jlt' : '10000' , 'jgt' : '10001' ,
            'je' : '10010' , 'hlt' : '10011' }

CommandList = []
if n > 0 :
    CommandList = commandList[ : -n]
else :
    CommandList = commandList

def decimalToBinary(n):
    return format( n , '08b')

def representsInteger(str):
    try:
        int(str)
        return True
    except ValueError :
        return False

def add(command) :
    instruction = 'add'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 7 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction add')
            exit()
        else :
            registers = command[3 : -1]
            if 'FLAGS' in registers :
                print(f'Error in line {command[-1]} : FLAGS register cannot be used for add instruction')
                exit()

            check = all(item in registerNames for item in registers)
            if check is True :
                registerEncode = ''
                for i in range(len(registers)) :
                    registerEncode += registerAddress.get(registers[i])

                binaryEncode = opcodes.get('add') + '00' + registerEncode 
                return binaryEncode

            else :
                print(f'Error in line {command[-1]} : Typo in register name')
                exit()  
    
    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction add')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction add')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            
            if commandInstruction == 'and' :
                return None
            elif dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction add')
                exit()
            else :
                return None
        else :
            return None




def sub(command) :
    instruction = 'sub'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 7 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction sub')
            exit()
        else :
            registers = command[3 : -1]
            if 'FLAGS' in registers :
                print(f'Error in line {command[-1]} : FLAGS register cannot be used for sub instruction')
                exit()

            check = all(item in registerNames for item in registers)
            if check is True :
                registerEncode = ''
                for i in range(len(registers)) :
                    registerEncode += registerAddress.get(registers[i])

                binaryEncode = opcodes.get('sub') + '00' + registerEncode 
                return binaryEncode

            else :
                print(f'Error in line {command[-1]} : Typo in register name')
                exit()  
    
    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction sub')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction sub')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction sub')
                exit()
            else :
                return None
        else :
            return None

def mov(command) :
    instruction = 'mov'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 6 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction mov')
            exit()
        else :
            maybeRegisters = command[3 : -1]
            check = all(item in registerNames for item in maybeRegisters)
            if check == True :
                if maybeRegisters[0] == 'FLAGS' :
                    print(f'Error in line {command[-1]} : FLAGS register cannot be used for movimm instruction')
                    exit()
                registerEncode = registerAddress.get(maybeRegisters[0]) + registerAddress.get(maybeRegisters[1])
                binaryEncode = opcodes.get('movreg') + '00000' + registerEncode
                return binaryEncode
            elif maybeRegisters[0] in registerNames and maybeRegisters[1][0] == '$' :
                if maybeRegisters[0] == 'FLAGS' :
                    print(f'Error in line {command[-1]} : FLAGS register cannot be used for movimm instruction')
                    exit()
                immvalue = maybeRegisters[1][1 : ]
                if representsInteger(immvalue) :
                    intimmvalue = int(immvalue)
                    if intimmvalue >= 0 and intimmvalue <= 255 :
                        immEncode = decimalToBinary(intimmvalue)
                        registerEncode = registerAddress.get(maybeRegisters[0])
                        binaryEncode = opcodes.get('movimm') + registerEncode + immEncode
                        return binaryEncode
                    else :
                        print(f"Error in line {command[-1]} : Constant integer value must be less than 256")
                        exit()
                else :
                    print(f"Error in line {command[-1]} : Immediate value must be an integer")
                    exit()
            else :
                print(f"Error in line {command[-1]} : Typo in register name or immediate value")
                exit()

    
    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction mov')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction mov')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction mov')
                exit()
            else :
                return None
        else :
            return None

def ld(command) :
    instruction = 'ld'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 6 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction ld')
            exit()
        else :
            maybeRegisters = command[3 : -1]
            if 'FLAGS' in maybeRegisters :
                print(f'Error in line {command[-1]} : FLAGS register cannot be used for ld instruction')
                exit()
            elif maybeRegisters[0] in registerNames and maybeRegisters[1] in variableNames :
                registerEncode = registerAddress.get(maybeRegisters[0])
                variableEncode = decimalToBinary(variableAddress.get(maybeRegisters[1]))
                binaryEncode = opcodes.get('ld') + registerEncode + variableEncode
                return binaryEncode
            elif maybeRegisters[0] in registerNames :
                print(f"Error in line {command[-1]} : use of undefined variable")
                exit()
            elif maybeRegisters[1] in variableNames :
                print(f"Error in line {command[-1]} : Typo in register name")
                exit()
            else :
                print(f"Error in line {command[-1]} : Typo in register name or variable")
                exit()
    
    else :
        return None

def st(command) :
    instruction = 'st'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 6 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction st')
            exit()
        else :
            maybeRegisters = command[3 : -1]
            if 'FLAGS' in maybeRegisters :
                print(f'Error in line {command[-1]} : FLAGS register cannot be used for st instruction')
                exit()
            elif maybeRegisters[0] in registerNames and maybeRegisters[1] in variableNames :
                registerEncode = registerAddress.get(maybeRegisters[0])
                variableEncode = decimalToBinary(variableAddress.get(maybeRegisters[1]))
                binaryEncode = opcodes.get('st') + registerEncode + variableEncode
                return binaryEncode
            elif maybeRegisters[0] in registerNames :
                print(f"Error in line {command[-1]} : use of undefined variable")
                exit()
            elif maybeRegisters[1] in variableNames :
                print(f"Error in line {command[-1]} : Typo in register name")
                exit()
            else :
                print(f"Error in line {command[-1]} : Typo in register name or variable")
                exit()
    
    else :
        return None

def mul(command) :
    instruction = 'mul'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 7 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction mul')
            exit()
        else :
            registers = command[3 : -1]
            if 'FLAGS' in registers :
                print(f'Error in line {command[-1]} : FLAGS register cannot be used for mul instruction')
                exit()

            check = all(item in registerNames for item in registers)
            if check is True :
                registerEncode = ''
                for i in range(len(registers)) :
                    registerEncode += registerAddress.get(registers[i])

                binaryEncode = opcodes.get('mul') + '00' + registerEncode 
                return binaryEncode

            else :
                print(f'Error in line {command[-1]} : Typo in register name')
                exit()  
    
    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction mul')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction mul')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction mul')
                exit()
            else :
                return None
        else :
            return None

def div(command) :
    instruction = 'div'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 6 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction div')
            exit()
        else :
            registers = command[3 : -1]
            check = all(item in registerNames for item in registers)
            if check == True :
                if 'FLAGS' in registers :
                    print(f'Error in line {command[-1]} : FLAGS register cannot be used for div instruction')
                    exit()
                registerEncode = registerAddress.get(registers[0]) + registerAddress.get(registers[1])
                binaryEncode = opcodes.get('div') + '00000' + registerEncode
                return binaryEncode
            else :
                print(f"Error in line {command[-1]} : Typo in register name")
                exit()

    
    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction div')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction div')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction div')
                exit()
            else :
                return None
        else :
            return None

def rs(command) :
    instruction = 'rs'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 6 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction mov')
            exit()
        else :
            maybeRegisters = command[3 : -1]
            if maybeRegisters[0] in registerNames and maybeRegisters[1][0] == '$' :
                if maybeRegisters[0] == 'FLAGS' :
                    print(f'Error in line {command[-1]} : FLAGS register cannot be used for movimm instruction')
                    exit()
                immvalue = maybeRegisters[1][1 : ]
                if representsInteger(immvalue) :
                    intimmvalue = int(immvalue)
                    if intimmvalue >= 0 and intimmvalue <= 255 :
                        immEncode = decimalToBinary(intimmvalue)
                        registerEncode = registerAddress.get(maybeRegisters[0])
                        binaryEncode = opcodes.get('rs') + registerEncode + immEncode
                        return binaryEncode
                    else :
                        print(f"Error in line {command[-1]} : Constant integer value must be less than 256")
                        exit()
                else :
                    print(f"Error in line {command[-1]} : Immediate value must be an integer")
                    exit()
            else :
                print(f"Error in line {command[-1]} : Typo in register name or immediate value")
                exit()
    
    else :
        return None

def ls(command) :
    instruction = 'ls'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 6 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction mov')
            exit()
        else :
            maybeRegisters = command[3 : -1]
            if maybeRegisters[0] in registerNames and maybeRegisters[1][0] == '$' :
                if maybeRegisters[0] == 'FLAGS' :
                    print(f'Error in line {command[-1]} : FLAGS register cannot be used for movimm instruction')
                    exit()
                immvalue = maybeRegisters[1][1 : ]
                if representsInteger(immvalue) :
                    intimmvalue = int(immvalue)
                    if intimmvalue >= 0 and intimmvalue <= 255 :
                        immEncode = decimalToBinary(intimmvalue)
                        registerEncode = registerAddress.get(maybeRegisters[0])
                        binaryEncode = opcodes.get('ls') + registerEncode + immEncode
                        return binaryEncode
                    else :
                        print(f"Error in line {command[-1]} : Constant integer value must be less than 256")
                        exit()
                else :
                    print(f"Error in line {command[-1]} : Immediate value must be an integer")
                    exit()
            else :
                print(f"Error in line {command[-1]} : Typo in register name or immediate value")
                exit()
    
    else :
        return None

def xor(command) :
    instruction = 'xor'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 7 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction xor')
            exit()
        else :
            registers = command[3 : -1]
            if 'FLAGS' in registers :
                print(f'Error in line {command[-1]} : FLAGS register cannot be used for xor instruction')
                exit()

            check = all(item in registerNames for item in registers)
            if check is True :
                registerEncode = ''
                for i in range(len(registers)) :
                    registerEncode += registerAddress.get(registers[i])

                binaryEncode = opcodes.get('xor') + '00' + registerEncode 
                return binaryEncode

            else :
                print(f'Error in line {command[-1]} : Typo in register name')
                exit()  
    
    elif commandInstruction == 'or' :
        return None
    
    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction xor')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction xor')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction xor')
                exit()
            else :
                return None
        else :
            return None

def Or(command) :
    instruction = 'or'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 7 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction or')
            exit()
        else :
            registers = command[3 : -1]
            if 'FLAGS' in registers :
                print(f'Error in line {command[-1]} : FLAGS register cannot be used for or instruction')
                exit()

            check = all(item in registerNames for item in registers)
            if check is True :
                registerEncode = ''
                for i in range(len(registers)) :
                    registerEncode += registerAddress.get(registers[i])

                binaryEncode = opcodes.get('xor') + '00' + registerEncode 
                return binaryEncode

            else :
                print(f'Error in line {command[-1]} : Typo in register name')
                exit()  
    else :
        return None

def And(command) :
    instruction = 'and'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 7 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction and')
            exit()
        else :
            registers = command[3 :-1]
            if 'FLAGS' in registers :
                print(f'Error in line {command[-1]} : FLAGS register cannot be used for and instruction')
                exit()

            check = all(item in registerNames for item in registers)
            if check is True :
                registerEncode = ''
                for i in range(len(registers)) :
                    registerEncode += registerAddress.get(registers[i])

                binaryEncode = opcodes.get('and') + '00' + registerEncode 
                return binaryEncode

            else :
                print(f'Error in line {command[-1]} : Typo in register name')
                exit()  
    
    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction and')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction and')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction and')
                exit()
            else :
                return None
        else :
            return None

def Not(command) :
    instruction = 'not'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 6 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction not')
            exit()
        else :
            registers = command[3 : -1]
            check = all(item in registerNames for item in registers)
            if check == True :
                if 'FLAGS' in registers :
                    print(f'Error in line {command[-1]} : FLAGS register cannot be used for not instruction')
                    exit()
                registerEncode = registerAddress.get(registers[0]) + registerAddress.get(registers[1])
                binaryEncode = opcodes.get('not') + '00000' + registerEncode
                return binaryEncode
            else :
                print(f"Error in line {command[-1]} : Typo in register name")
                exit()

    
    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction not')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction not')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction not')
                exit()
            else :
                return None
        else :
            return None

def cmp(command) :
    instruction = 'cmp'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 6 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction mov')
            exit()
        else :
            registers = command[3 : -1]
            check = all(item in registerNames for item in registers)
            if check == True :
                if 'FLAGS' in registers :
                    print(f'Error in line {command[-1]} : FLAGS register cannot be used for movimm instruction')
                    exit()
                registerEncode = registerAddress.get(registers[0]) + registerAddress.get(registers[1])
                binaryEncode = opcodes.get('cmp') + '00000' + registerEncode
                return binaryEncode
            else :
                print(f"Error in line {command[-1]} : Typo in register name")
                exit()

    elif commandInstruction == 'jmp' :
        return None
    
    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction cmp')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction cmp')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction cmp')
                exit()
            else :
                return None
        else :
            return None

def jmp(command) :
    instruction = 'jmp'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 5 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction jmp')
            exit()
        else :
            lable = command[3]
            if lable in lableNames :
                lableEncode = decimalToBinary(lableAddress.get(lable))
                binaryEncode = opcodes.get('jmp') + '000' + lableEncode
                return binaryEncode
            else :
                print(f"Error in line {command[-1]} : Lable not defined")
                exit()
    
    elif commandInstruction == 'cmp' :
        return None

    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction jmp')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction jmp')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction jmp')
                exit()
            else :
                return None
        else :
            return None

def jlt(command) :
    instruction = 'jlt'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 5 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction jlt')
            exit()
        else :
            lable = command[3]
            if lable in lableNames :
                lableEncode = decimalToBinary(lableAddress.get(lable))
                binaryEncode = opcodes.get('jlt') + '000' + lableEncode
                return binaryEncode
            else :
                print(f"Error in line {command[-1]} : Lable not defined")
                exit()

    elif commandInstruction == 'hlt' :
        return None
    
    elif commandInstruction == 'jgt' :
        return None

    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction jlt')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction jlt')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction jlt')
                exit()
            else :
                return None
        else :
            return None

def jgt(command) :
    instruction = 'jgt'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 5 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction jgt')
            exit()
        else :
            lable = command[3]
            if lable in lableNames :
                lableEncode = decimalToBinary(lableAddress.get(lable))
                binaryEncode = opcodes.get('jgt') + '000' + lableEncode
                return binaryEncode
            else :
                print(f"Error in line {command[-1]} : Lable not defined")
                exit()

    elif commandInstruction == 'jmp' :
        return None
    
    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction jgt')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction jgt')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction jgt')
                exit()
            else :
                return None
        else :
            return None

def je(command) :
    instruction = 'je'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 5 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction je')
            exit()
        else :
            lable = command[3]
            if lable in lableNames :
                lableEncode = decimalToBinary(lableAddress.get(lable))
                binaryEncode = opcodes.get('je') + '000' + lableEncode
                return binaryEncode
            else :
                print(f"Error in line {command[-1]} : Lable not defined")
                exit()
    else :
        return None

def hlt(command) :
    instruction = 'hlt'
    commandInstruction = command[2]
    
    if instruction == commandInstruction :
        if len(command) != 4 :
            print(f'Error in line {command[-1]} : Wrong syntax used for instruction hlt')
            exit()
        else :
            binaryEncode = opcodes.get('hlt') + '00000000000'
            return binaryEncode

    elif commandInstruction == 'jlt' :
        return None

    elif instruction.find(commandInstruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction hlt')
        exit()
    
    elif commandInstruction.find(instruction) != -1 :
        print(f'Error in line {command[-1]} : Typo in instruction hlt')
        exit()
    
    else :
        if len(instruction) == len(commandInstruction) :
            dum = 0
            for i in range(len(instruction)) :
                if instruction[i] == commandInstruction[i] :
                    dum += 1
            if dum == 2 :
                print(f'Error in line {command[-1]} : Typo in instruction hlt')
                exit()
            else :
                return None
        else :
            return None



binaryOutput = []
for i in CommandList :

    if add(i) != None :
        binaryEncode = add(i)
        binaryOutput.append(binaryEncode)
    elif sub(i) != None :
        binaryEncode = sub(i)
        binaryOutput.append(binaryEncode)
    elif mov(i) != None :
        binaryEncode = mov(i)
        binaryOutput.append(binaryEncode)
    elif ld(i) != None :
        binaryEncode = ld(i)
        binaryOutput.append(binaryEncode)
    elif st(i) != None :
        binaryEncode = st(i)
        binaryOutput.append(binaryEncode)
    elif mul(i) != None :
        binaryEncode = mul(i)
        binaryOutput.append(binaryEncode)
    elif div(i) != None :
        binaryEncode = div(i)
        binaryOutput.append(binaryEncode)
    elif rs(i) != None :
        binaryEncode = rs(i)
        binaryOutput.append(binaryEncode)
    elif ls(i) != None :
        binaryEncode = ls(i)
        binaryOutput.append(binaryEncode)
    elif xor(i) != None :
        binaryEncode = xor(i)
        binaryOutput.append(binaryEncode)
    elif Or(i) != None :
        binaryEncode = Or(i)
        binaryOutput.append(binaryEncode)
    elif And(i) != None :
        binaryEncode = And(i)
        binaryOutput.append(binaryEncode)
    elif Not(i) != None :
        binaryEncode = Not(i)
        binaryOutput.append(binaryEncode)
    elif cmp(i) != None :
        binaryEncode = cmp(i)
        binaryOutput.append(binaryEncode)
    elif jmp(i) != None :
        binaryEncode = jmp(i)
        binaryOutput.append(binaryEncode)
    elif jlt(i) != None :
        binaryEncode = jlt(i)
        binaryOutput.append(binaryEncode)
    elif jgt(i) != None :
        binaryEncode = jgt(i)
        binaryOutput.append(binaryEncode)
    elif je(i) != None :
        binaryEncode = je(i)
        binaryOutput.append(binaryEncode)
    elif hlt(i) != None :
        binaryEncode = hlt(i)
        binaryOutput.append(binaryEncode)
    else :
        print(f'Error in line {i[0] + 1} : General Syntax Error')
        exit()

if len(binaryOutput) > 256 :
    print('Error : The assembler can support only 256 instructions.')
    exit()

for i in range(len(binaryOutput) - 1) :
    if binaryOutput[i][ :5] == '10011' :
        print(f'Error in line {CommandList[i][-1]} : hlt not being used as the last instruction')
        exit()

if '1001100000000000' not in binaryOutput :
    print('Error : Missing hlt instruction.')
    exit()

for i in binaryOutput :
    print(i)