
assembler = open("zadanie_13_5.txt","r")
binarnie = open("wynik.txt","w")



pc_op_dict = {'jump':'01', 'jumpi': '01', 'jz': '10', 'jnz': '11', 'add': '00', 'addi': '00', 'load': '00', 'loadi': '00', 'and':'00','andi':'00', 'nop': '00','mov':'00','movi':'00'}
imm_op_dict = {'jump': '0', 'jumpi': '1', 'jz': '1', 'jnz': '1', 'add': '0', 'addi': '1', 'load': '0', 'loadi': '1', 'and':'0','andi':'1', 'nop': '0','mov':'0','movi':'1'}
alu_op_dict = {'jump': '01', 'jumpi': '01', 'jz': '11', 'jnz': '11', 'add': '01', 'addi': '01', 'load': '01', 'loadi': '01', 'and':'00','andi':'00', 'nop': '01','mov':'01','movi':'01'}
rd_op_dict = {'jump': '0', 'jumpi': '0', 'jz': '0', 'jnz': '0', 'add': '0', 'addi': '0', 'load': '1', 'loadi': '1', 'and':1,'andi':'0', 'nop': '0','mov':'0','movi':'0'}
next_arguments ={'jump': 1, 'jumpi': 1, 'jz': 2, 'jnz': 2, 'add': 3, 'addi': 3, 'load': 2, 'loadi': 2, 'and': 3,'andi': 3,'nop':0,'mov':2,'movi':2}
registers_idx ={'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
hex_to_binary= {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110','7':'0111','8':'1000','9':'1001','a':'1010'
    ,'b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}


line_index = 0
lista_instrukcji = ['jump', 'jumpi', 'jz', 'jnz', 'add', 'addi', 'load', 'loadi', 'and','andi','nop','movi','mov']
indeksyR = ['0', '1', '2', '3', '4', '5', '6', '7']
indeksyHex= ['0', '1', '2', '3', '4', '5', '6', '7','8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

for assembler_line in assembler:

    if len(assembler_line) != 0 and assembler_line[0] != "#" and assembler_line[0] != "\n":
        argument = assembler_line.split(" ")
        liczba_argumentow = next_arguments[argument[0]]
        binary_line = "assign program[" + str(line_index) +"] = 32'b000000"
        binary_line += pc_op_dict[argument[0]]
        binary_line += '00'
        binary_line += alu_op_dict[argument[0]]
        binary_line += '0'
        if argument[0] not in lista_instrukcji:
            binary_line = "DEBILU NIE MASZ TAKIEJ INSTRUKCJI W BAZIE !!! \n\n"
        else:
            if argument[0] == 'nop':
                rx_op = registers_idx['6']
                ry_op = registers_idx['0']
                d_op = registers_idx['0']
                imm = '00000000'
            if argument[0] == 'jump':
                rx_op = registers_idx['6']
                if argument[1][1] not in indeksyR:
                    binary_line = "DEBILU POMYLEŚ INDEKS W R !!! \n\n"
                ry_op = registers_idx[argument[1][1]]
                d_op = registers_idx['7']
                imm = '00000000'
            if argument[0] == 'jumpi':
                if argument[1][2] not in indeksyHex or argument[1][3] not in indeksyHex:
                    binary_line = "DEBILU HEX POZA SKALĄ!!! \n\n"
                imm1 = hex_to_binary[argument[1][2]]
                imm2 = hex_to_binary[argument[1][3]]
                imm = str(imm1) + str(imm2)
                rx_op = registers_idx['6']
                ry_op = registers_idx['6']
                d_op = registers_idx['7']
            if argument[0] == 'jz':
                if argument[2][2] not in indeksyHex or argument[2][3] not in indeksyHex:
                    binary_line = "DEBILU HEX POZA SKALĄ!!! \n\n"
                if argument[1][1] not in indeksyR:
                    binary_line = "DEBILU POMYLEŚ INDEKS W R !!! \n\n"
                imm1 = hex_to_binary[argument[2][2]]
                imm2 = hex_to_binary[argument[2][3]]
                imm = str(imm1) + str(imm2)
                rx_op = registers_idx[argument[1][1]]
                ry_op = registers_idx['6']
                d_op = registers_idx['7']
            if argument[0] == 'jnz':
                imm1 = hex_to_binary[argument[2][2]]
                imm2 = hex_to_binary[argument[2][3]]
                imm = str(imm1) + str(imm2)
                if argument[2][2] not in indeksyHex or argument[2][3] not in indeksyHex:
                    binary_line = "DEBILU HEX POZA SKALĄ!!! \n\n"
                if argument[1][1] not in indeksyR:
                    binary_line = "DEBILU POMYLEŚ INDEKS W R !!! \n\n"
                rx_op = registers_idx[argument[1][1]]
                ry_op = registers_idx['6']
                d_op = registers_idx['7']
            if argument[0] == 'add':
                if argument[2][1] not in indeksyR or argument[3][1] not in indeksyR or argument[1][1] not in indeksyR:
                    binary_line = "DEBILU POMYLEŚ INDEKS W R !!! \n\n"
                rx_op = registers_idx[argument[2][1]]
                ry_op = registers_idx[argument[3][1]]
                d_op = registers_idx[argument[1][1]]
                imm = '00000000'
            if argument[0] == 'addi':
                if argument[3][2] not in indeksyHex or argument[3][3] not in indeksyHex:
                    binary_line = "DEBILU HEX POZA SKALĄ!!! \n\n"
                if argument[2][1] not in indeksyR or argument[1][1] not in indeksyR:
                    binary_line = "DEBILU POMYLEŚ INDEKS W R !!! \n\n"
                rx_op = registers_idx[argument[2][1]]
                ry_op = registers_idx['0']
                d_op = registers_idx[argument[1][1]]
                imm1 = hex_to_binary[argument[3][2]]
                imm2 = hex_to_binary[argument[3][3]]
                imm = str(imm1) + str(imm2)
            if argument[0] == 'and':
                if argument[2][1] not in indeksyR or argument[3][1] not in indeksyR or argument[1][1] not in indeksyR:
                    binary_line = "DEBILU POMYLEŚ INDEKS W R !!! \n\n"
                rx_op = registers_idx[argument[2][1]]
                ry_op = registers_idx[argument[3][1]]
                d_op = registers_idx[argument[1][1]]
                imm = '00000000'
            if argument[0] == 'andi':
                if argument[3][2] not in indeksyHex or argument[3][3] not in indeksyHex:
                    binary_line = "DEBILU HEX POZA SKALĄ!!! \n\n"
                if argument[2][1] not in indeksyR or argument[1][1] not in indeksyR:
                    binary_line = "DEBILU POMYLEŚ INDEKS W R !!! \n\n"
                rx_op = registers_idx[argument[2][1]]
                ry_op = registers_idx['0']
                d_op = registers_idx[argument[1][1]]
                imm1 = hex_to_binary[argument[3][2]]
                imm2 = hex_to_binary[argument[3][3]]
                imm = str(imm1) + str(imm2)
                print(imm1, imm2, argument, imm)

            if argument[0] == 'loadi':
                if argument[2][2] not in indeksyHex or argument[2][3] not in indeksyHex:
                    binary_line = "DEBILU HEX POZA SKALĄ!!! \n\n"
                if argument[1][1] not in indeksyR :
                    binary_line = "DEBILU POMYLEŚ INDEKS W R !!! \n\n"
                ry_op = registers_idx['0']
                rx_op = registers_idx['6']
                d_op = registers_idx[argument[1][1]]
                imm1 = hex_to_binary[argument[2][2]]
                imm2 = hex_to_binary[argument[2][3]]
                imm = str(imm1) + str(imm2)

            if argument[0] == 'movi':
                if argument[2][2] not in indeksyHex or argument[2][3] not in indeksyHex:
                    binary_line = "DEBILU HEX POZA SKALĄ!!! \n\n"
                if argument[1][1] not in indeksyR:
                    binary_line = "DEBILU POMYLEŚ INDEKS W R !!! \n\n"
                ry_op = registers_idx['0']
                rx_op = registers_idx['6']
                d_op = registers_idx[argument[1][1]]
                imm1 = hex_to_binary[argument[2][2]]
                imm2 = hex_to_binary[argument[2][3]]
                imm = str(imm1) + str(imm2)

            if argument[0] == 'mov':
                if argument[1][1] not in indeksyR or argument[2][1] not in indeksyR:
                    binary_line = "DEBILU POMYLEŚ INDEKS W R !!! \n\n"
                ry_op = registers_idx['6']
                rx_op = registers_idx[argument[2][1]]
                d_op = registers_idx[argument[1][1]]
                imm = '00000000'


            binary_line += rx_op
            binary_line += imm_op_dict[argument[0]]
            binary_line +=ry_op
            # print(rd_op_dict[argument[0]])
            binary_line +=str(rd_op_dict[argument[0]])

            binary_line +=d_op
            binary_line +=imm
            binary_line += ';//'
            binary_line += assembler_line


        binarnie.write(binary_line)
        line_index += 1
        # print(binary_line)
binarnie.close()
assembler.close()