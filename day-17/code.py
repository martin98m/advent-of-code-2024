A = 0
B = 0
C = 0

program = ()
pointer = 0
output = []

def operation(opcode, literal_operand):
    global A,B,C,pointer,output

    combo_operand = literal_operand
    if literal_operand == 4:
        combo_operand = A
    elif literal_operand == 5:
        combo_operand = B
    elif literal_operand == 6:
        combo_operand = C
    elif literal_operand == 7:
        print("ERROR")
    

    if opcode == 0:
        res = int(A / (2 ** combo_operand))
        A = res
    elif opcode == 1:
        res = B ^ literal_operand
        B = res
    elif opcode == 2:
        res = combo_operand % 8
        B = res
    elif opcode == 3:
        if A == 0 : 
            pointer +=2
            return
        pointer = literal_operand
        return
    elif opcode == 4:
        res = B ^ C
        B = res
    elif opcode == 5:
        output.append(combo_operand % 8)
    elif opcode == 6:
        res = int(A / (2 ** combo_operand))
        B = res
    elif opcode == 7:
        res = int(A / (2 ** combo_operand))
        C = res
    else:
        print("ERROR opcode")
    
    pointer +=2


size = len(program)
while pointer < size:
    operation(program[pointer], program[pointer+1])

print(output)