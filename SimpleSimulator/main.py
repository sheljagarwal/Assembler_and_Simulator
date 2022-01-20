from sys import stdin
from matplotlib import pyplot as plt

commandlist = []

for line in stdin:
    
    if line == '': 
        break
    
    commandlist.append(line)

for i in range(len(commandlist)) :
    commandlist[i] = commandlist[i].strip("\n")

memory = []
pc = []
for i in range(256) :
    memory.append('0000000000000000')
    pc.append(format(i,'08b'))

pc = pc[ : len(commandlist)]
commandList = dict(zip(pc,commandlist))

for i in range(len(commandlist)) :
    memory[i] = commandlist[i]

registers = {'000' : '0000000000000000' , '001' : '0000000000000000' , '010' : '0000000000000000' ,
             '011' : '0000000000000000' , '100' : '0000000000000000' , '101' : '0000000000000000' , 
             '110' : '0000000000000000' , '111' : '0000000000000000'}

def decimalToBinary(n):
    return format(n,'016b')

def binaryToDecimal(b) :
    return int(b,2)

def add(instruction) :
    r1 = instruction[7:10]
    r2 = instruction[10:13]
    r3 = instruction[13:]
    val2 = registers.get(r2)
    val3 = registers.get(r3)
    int2 = binaryToDecimal(val2)
    int3 = binaryToDecimal(val3)
    int1 = int2 + int3
    val1 = decimalToBinary(int1)
    registers['111'] = '0000000000000000'
    if int1 > 65535 :
        registers['111'] = '0000000000001000'
        val1 = val1[-16:]
    registers[r1] = val1

def sub(instruction) :
    r1 = instruction[7:10]
    r2 = instruction[10:13]
    r3 = instruction[13:]
    val2 = registers.get(r2)
    val3 = registers.get(r3)
    int2 = binaryToDecimal(val2)
    int3 = binaryToDecimal(val3)
    int1 = int2 - int3
    val1 = ''
    registers['111'] = '0000000000000000'
    if int1 < 0 :
        registers['111'] = '0000000000001000'
        val1 = '0000000000000000'
    else :
        val1 = decimalToBinary(int1)
    registers[r1] = val1

def mul(instruction) :
    r1 = instruction[7:10]
    r2 = instruction[10:13]
    r3 = instruction[13:]
    val2 = registers.get(r2)
    val3 = registers.get(r3)
    int2 = binaryToDecimal(val2)
    int3 = binaryToDecimal(val3)
    int1 = int2 * int3
    val1 = decimalToBinary(int1)
    registers['111'] = '0000000000000000'
    if int1 > 65535 :
        registers['111'] = '0000000000001000'
        val1 = val1[-16:]
    registers[r1] = val1

def movimm(instruction) :
    r1 = instruction[5:8]
    immval = instruction[8:]
    registers[r1] = '00000000' + immval
    registers['111'] = '0000000000000000'

def movreg(instruction) :
    r1 = instruction[10:13]
    r2 = instruction[13:]
    val = registers.get(r2)
    registers[r1] = val
    registers['111'] = '0000000000000000'

def ld(instruction) :
    r1 = instruction[5:8]
    address = instruction[8:]
    index = binaryToDecimal(address)
    registers[r1] = memory[index]
    registers['111'] = '0000000000000000'
    return address

def st(instruction) :
    r1 = instruction[5:8]
    address = instruction[8:]
    index = binaryToDecimal(address)
    val = registers.get(r1)
    memory[index] = val
    registers['111'] = '0000000000000000'
    return address

def div(instruction) :
    r1 = instruction[10:13]
    r2 = instruction[13:]
    val1 = registers.get(r1)
    val2 = registers.get(r2)
    int1 = binaryToDecimal(val1)
    int2 = binaryToDecimal(val2)
    q , r = divmod(int1 , int2)
    quotient = decimalToBinary(q)
    remainder = decimalToBinary(r)
    registers['000'] = quotient
    registers['001'] = remainder
    registers['111'] = '0000000000000000'

def rs(instruction) :
    r1 = instruction[5:8]
    immval = instruction[8:]
    shift = binaryToDecimal(immval)
    val = registers.get(r1)
    intval = binaryToDecimal(val)
    shiftedint = intval >> shift
    shiftedval = decimalToBinary(shiftedint)
    registers[r1] = shiftedval
    registers['111'] = '0000000000000000'

def ls(instruction) :
    r1 = instruction[5:8]
    immval = instruction[8:]
    shift = binaryToDecimal(immval)
    val = registers.get(r1)
    intval = binaryToDecimal(val)
    shiftedint = intval << shift
    shiftedval = decimalToBinary(shiftedint)
    shiftedval = shiftedval[-16:]
    registers[r1] = shiftedval
    registers['111'] = '0000000000000000'

def xor(instruction) :
    r1 = instruction[7:10]
    r2 = instruction[10:13]
    r3 = instruction[13:]
    val2 = registers.get(r2)
    val3 = registers.get(r3)
    int2 = binaryToDecimal(val2)
    int3 = binaryToDecimal(val3)
    int1 = int2^int3
    val1 = decimalToBinary(int1)
    registers[r1] = val1
    registers['111'] = '0000000000000000'

def Or(instruction) :
    r1 = instruction[7:10]
    r2 = instruction[10:13]
    r3 = instruction[13:]
    val2 = registers.get(r2)
    val3 = registers.get(r3)
    int2 = binaryToDecimal(val2)
    int3 = binaryToDecimal(val3)
    int1 = int2 | int3
    val1 = decimalToBinary(int1)
    registers[r1] = val1
    registers['111'] = '0000000000000000'

def And(instruction) :
    r1 = instruction[7:10]
    r2 = instruction[10:13]
    r3 = instruction[13:]
    val2 = registers.get(r2)
    val3 = registers.get(r3)
    int2 = binaryToDecimal(val2)
    int3 = binaryToDecimal(val3)
    int1 = int2 & int3
    val1 = decimalToBinary(int1)
    registers[r1] = val1
    registers['111'] = '0000000000000000'

def Not(instruction) :
    r1 = instruction[10:13]
    r2 = instruction[13:]
    val = registers.get(r2)
    notval = val.replace('1','2')
    notval = notval.replace('0','1')
    notval = notval.replace('2','0')
    registers[r1] = notval
    registers['111'] = '0000000000000000'

def cmp(instruction) :
    r1 = instruction[10:13]
    r2 = instruction[13:]
    val1 = registers.get(r1)
    val2 = registers.get(r2)
    int1 = binaryToDecimal(val1)
    int2 = binaryToDecimal(val2)
    if int1 > int2 :
        registers['111'] = '0000000000000010'
    elif int1 == int2 :
        registers['111'] = '0000000000000001'
    else :
        registers['111'] = '0000000000000100'

def jmp(instruction) :
    address = instruction[8:]
    registers['111'] = '0000000000000000'
    return address

def jlt(instruction) :
    address = instruction[8:]
    if registers['111'] == '0000000000000100' :
        registers['111'] = '0000000000000000'
        return address
    else :
        registers['111'] = '0000000000000000'
        return None

def jgt(instruction) :
    address = instruction[8:]
    if registers['111'] == '0000000000000010' :
        registers['111'] = '0000000000000000'
        return address
    else :
        registers['111'] = '0000000000000000'
        return None

def je(instruction) :
    address = instruction[8:]
    if registers['111'] == '0000000000000001' :
        registers['111'] = '0000000000000000'
        return address
    else :
        registers['111'] = '0000000000000000'
        return None

def nextpc(pc) :
    dum = binaryToDecimal(pc)
    dum += 1
    newpc = format(dum,'08b')
    return newpc

def executor(pc) :
    instruction = commandList[pc]
    newpc = ''
    halted = False
    mem = pc
    if instruction[:5] == '00000' :
        add(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '00001' :
        sub(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '00010' :
        movimm(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '00011' :
        movreg(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '00100' :
        mem = ld(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '00101' :
        mem = st(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '00110' :
        mul(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '00111' :
        div(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '01000' :
        rs(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '01001' :
        ls(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '01010' :
        xor(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '01011' :
        Or(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '01100' :
        And(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '01101' :
        Not(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '01110' :
        cmp(instruction)
        newpc = nextpc(pc)
    elif instruction[:5] == '01111' :
        newpc = jmp(instruction)
    elif instruction[:5] == '10000' :
        if jlt(instruction) != None :
            newpc = jlt(instruction)
        else :
            newpc = nextpc(pc)
    elif instruction[:5] == '10001' :
        if jgt(instruction) != None :
            newpc = jgt(instruction)
        else :
            newpc = nextpc(pc)
    elif instruction[:5] == '10010' :
        if je(instruction) != None :
            newpc = je(instruction)
        else :
            newpc = nextpc(pc)
    else :
        halted = True

    print(pc,end=' ')
    registervalues = list(registers.values())
    for i in registervalues :
        print(i,end=' ')
    print()
    return halted,newpc,mem
    
halted = False
pc = '00000000'
cycle = 0
cycle_x = []
mem_y = []
while not halted :
    cycle_x.append(cycle)
    halted,newpc,mem = executor(pc)
    y = binaryToDecimal(mem)
    mem_y.append(y)
    pc = newpc
    cycle += 1

for i in memory :
    print(i)

plt.plot(cycle_x,mem_y)
plt.title('Memory Accesses v/s Cycles')
plt.xlabel('Cycle')
plt.ylabel('Address')
plt.tight_layout()
plt.savefig('plot.png')