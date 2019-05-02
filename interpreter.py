# Your name: Bansri Shah
# Your SBU ID: 110335850
# Your NetID: bpshah
#
# Pep/8 Interpreter (Homework 2-1) starter code
# CSE 101, Fall 2018

# DO NOT MODIFY THE FOLLOWING HELPER FUNCTIONS AND GLOBAL VARIABLES

accumulator = 0
ram = {} # memory is initially empty

def hexToBin(h):
    h2b = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
    result = ''
    hex = h.upper().strip()
    for digit in hex:
        result += h2b[digit]
    return result

def printRam():
    global ram # use the 'ram' dictionary that was declared previously
    print('Currently active memory addresses:')
    for address in sorted(ram.keys()):
        print(address,':',ram[address])
    print()

def viewAccumulator(): # View the current contents of the accumulator register
    global accumulator
    return accumulator

# Complete the functions that follow for this assignment

def processInstruction(instruction):
    global accumulator, ram

    binary = hexToBin(instruction)

    if len(binary) < 24:
        return "ERROR"
    else:
        opcode = binary[:4]
        addr = binary[5:8]
        operand = binary[8:]
        operand = int(operand, 2)

        if opcode == "0000":
            return "HALT"
        elif opcode == "1100":
            if addr == "000":
                accumulator = operand
                return "LOAD " + str(operand) + " INTO ACCUMULATOR"
            elif addr == "001":
                if operand in ram:
                    accumulator = ram[operand]
                    return "LOAD CONTENTS OF MEMORY ADDRESS " + str(operand) + " INTO ACCUMULATOR"
                else:
                    return "ERROR"
            else:
                return "ERROR"
        elif opcode == "1110":
            if addr == "001":
                ram[operand] = accumulator
                return "STORED ACCUMULATOR INTO MEMORY ADDRESS " + str(operand)
            else:
                return "ERROR"
        elif opcode == "0111":
            if addr == "000":
                accumulator += operand
                return "ADDED " + str(operand) + " TO ACCUMULATOR"
            elif addr == "001":
                if operand in ram:
                    accumulator += ram[operand]
                    return "ADDED CONTENTS OF ADDRESS " + str(operand) + " TO ACCUMULATOR"
                else:
                    return "ERROR"
            else:
                return "ERROR"
        elif opcode == "1000":
            if addr == "000":
                accumulator -= operand
                return "SUBTRACTED " + str(operand) + " FROM ACCUMULATOR"
            elif addr == "001":
                if operand in ram:
                    accumulator -= ram[operand]
                    return "SUBTRACTED CONTENTS OF ADDRESS " + str(operand) + " FROM ACCUMULATOR"
                else:
                    return "ERROR"
            else:
                return "ERROR"
        elif opcode == "1001":
            if addr == "000":
                accumulator = accumulator * operand
                return "MULTIPLIED ACCUMULATOR BY " + str(operand)
            elif addr == "001":
                if operand in ram:
                    accumulator = accumulator * ram[operand]
                    return  "MULTIPLIED ACCUMULATOR BY CONTENTS OF ADDRESS " + str(operand)
                else:
                    return "ERROR"
            else:
                return "ERROR"
        elif opcode == "1010":
            if addr == "000":
                accumulator = accumulator // operand
                return "DIVIDED ACCUMULATOR BY " + str(operand)
            elif addr == "001":
                if operand in ram:
                    accumulator = accumulator // ram[operand]
                    return "DIVIDED ACCUMULATOR BY CONTENTS OF ADDRESS " + str(operand)
                else:
                    return "ERROR"
            else:
                return "ERROR"
        else:
            return "ERROR"
    

def executeProgram(filename):
    global ram, accumulator

    ram = {}
    accumulator = 0
    count = 0
    result = ""

    for line in open(filename):
        line = line.strip()
        result = processInstruction(line)

        if result == "ERROR":
            break
        elif result == "HALT":
            break
        else:
            count += 1
    if result == "HALT":
        count += 1
    return count


# DO NOT modify or remove the code below! You can use it to test your work.

if __name__ == "__main__":
    # Test part 1: the processInstruction() function
    ram = {141:22, 115:4}
    printRam()
    print()
    print("Processing instruction D1008D:", processInstruction("D1008D")) #invalid opcode
    print()
    print("Processing instruction 8000CB:", processInstruction("8000CB"))
    print()
    print("Processing instruction 310B4:", processInstruction("310B4")) # too few digits
    print()
    print("Processing instruction 00008D:", processInstruction("00008D"))
    print()
    print("Processing instruction A10073:", processInstruction("A10073"))
    print()
    print("Processing instruction 9000D4:", processInstruction("9000D4"))
    print()
    print("Processing instruction 7100D7:", processInstruction("7100D7")) # nonexistent memory address
    print()
    print("Processing instruction C0005F:", processInstruction("C0005F"))
    print()
    print("Processing instruction 7200F1:", processInstruction("7200F1")) # invalid address mode
    print()
    print("Processing instruction E0004D:", processInstruction("E0004D")) # invalid address mode for STORE
    print()
    print()

    # Test part 2: the executeProgram() function
    ram = {}
    accumulator = 0

    print("Testing executeProgram() with file 'program1.txt'", executeProgram("program1.txt"))
    print()

    print("Testing executeProgram() with file 'program2.txt'", executeProgram("program2.txt"))
    print()

    print("Testing executeProgram() with file 'program3.txt'", executeProgram("program3.txt"))
    print()
    
