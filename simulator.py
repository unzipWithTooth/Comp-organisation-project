rv = {i: 0 for i in range(32)}   # register_values

rv[2] = 380  # stack pointer



def binary_to_decimal(binary_str):
    decimal = 0
    length = len(binary_str)
    for i in range(0,length):
        decimal+= 2**i * int(binary_str[length-i-1])
    return decimal

def decimal_to_binary( num, bits):
    binary=''
    if num==0:
        return '0'* bits
    
    while num > 0:
        binary = str(num%2) + binary
        num= num//2

    binary = (bits - len(binary))*'0' + binary

    return binary


def R_type_instruction(instruction):
    func7= instruction[0:7]
    rs2= instruction[7:12]
    rs1= instruction[12:17]
    func3= instruction[17:20]
    rd= instruction[20:25]

    def add_instruction(rs1,rs2,rd):
        rv[binary_to_decimal(rd)] = rv[binary_to_decimal(rs1)] + rv[binary_to_decimal(rs2)]

    def sub_instruction(rs1,rs2,rd):
        pass

    def slt_instruction(rs1,rs2,rd):
        pass

    def srl_instruction(rs1,rs2,rd):
        pass

    def or_instruction(rs1,rs2,rd):
        pass

    def and_instruction(rs1,rs2,rd):
        pass

    if func3 =='010':
        slt_instruction(rs1,rs2,rd)
    elif func3 =='101':
        srl_instruction(rs1,rs2,rd)
    elif func3 =='110':
        or_instruction(rs1,rs2,rd)
    elif func3 =='111':
        and_instruction(rs1,rs2,rd)
    elif func3 == '000' and func7 =='0000000':
        add_instruction(rs1,rs2,rd)
    elif func3 == '000' and func7 =='0100000':
        sub_instruction(rs1,rs2,rd)
    else :
        return "invalid func3"



def S_type_instruction(instruction):
    imm= instruction[0:7] + instruction[20:25]
    rs2= instruction[7:12]
    rs1 = instruction[12:17]



def I_type_instruction(instruction):
    imm = instruction[0:12]
    rs1 = instruction[12:17]
    rd = instruction[20:25]
    opcode = instruction[25:32]

    def addi_instruction(rs1,rd,imm):
        rv[binary_to_decimal(rd)]= rv[binary_to_decimal(rs1)] + binary_to_decimal(imm)

    def jalr_instrcution(rs1,rd,imm):
        pass
    
    def load_instruction(rs1,rd,imm):
        pass

    if opcode =='1100111':
        jalr_instrcution(rs1,rd,imm)
    
    elif opcode =='0000011':
        load_instruction(rs1,rd,imm)
    
    elif opcode =='0010011':
        addi_instruction(rs1,rd,imm)
    

def J_type_instruction(instruction):
    imm = instruction[0:12]
    rd = instruction[0:12]

def B_type_instruction(instruction):
    imm= instruction[0:7] + instruction[20:25]
    rs2= instruction[7:12]
    rs1 = instruction[12:17]
    func3 = imm= instruction[0:7] + instruction[20:25]



def decode_instruction(line):
    opcode = line[25:32]
    if opcode == '0110011':
        R_type_instruction(line)
    elif opcode in ['0000011','0010011','1100111']:
        I_type_instruction(line)
    elif opcode == '0100011':
        S_type_instruction(line)
    elif opcode =='1101111':
        J_type_instruction(line)
    elif opcode == '1100011':
        B_type_instruction(line)
    else :
        print("invalid opcode")




def main():
    f= open("input.txt",'r')
    s= f.readlines()
    for line in s:
        line = line.strip()
        decode_instruction(line)

    f.close()
    print(rv)

main()