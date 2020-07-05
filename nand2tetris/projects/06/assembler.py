#!/usr/bin/env python3
import argparse

class SymbolTable:

    # key = symbol, value = memory address
    default_symbol_table = {
        "R0": 0,
        "R1": 1, 
        "R2": 2,
        "R3": 3,
        "R4": 4, 
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11, 
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SCREEN": 16384,
        "KBD": 24576,
    }
    def __init__(self):
        print("Initializing symbol table")
        self.symbol_table = self.default_symbol_table
        self.n = 16

    def first_pass(self, instructions):
        # first pass add anything with left bracket
        # address is line following the one with '('
        print("symbol table first pass")
        symbols_added = 0 # lines containing (XXX) symbols will be removed
        for line in enumerate(instructions):
            if line[1].startswith("("):
                self.symbol_table[f"{line[1].lstrip('(').rstrip(')')}"] = line[0] - symbols_added
                symbols_added += 1
        print(self.symbol_table) 

    def second_pass(self, instructions):
        # second pass add any remaining symbols
        # starting at 16, add any symbols that are not already in the symbol table
        print("symbol table second pass")
        updated_instructions = []
        for line in instructions:
            if line.startswith("@"):
                try: 
                    # @0
                    if line.strip("@").isnumeric():
                        updated_instructions.append(line) 
                    # @LABEL
                    else:
                        addr = self.symbol_table[line.lstrip('@')]
                        updated_instructions.append("@" + str(addr)) 
                except KeyError as e:
                    # @LABEL wasn't already in symbols table
                    self.symbol_table[line.lstrip('@')] = self.n
                    updated_instructions.append("@" + str(self.n))
                    self.n = self.n + 1
            elif line.startswith("("):
                pass
            else:
                updated_instructions.append(line)
        return updated_instructions

COMP_TABLE = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
}

DEST_TABLE = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}

JUMP_TABLE = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

def parse_C_instruction(instruction):
    if "=" in instruction:
        dst = instruction.split("=")[0]
        remainder = instruction.split("=")[1]
    else:
        dst = ""
        remainder = instruction
    if ";" in remainder:
        jmp = remainder.split(";")[1]
        cmp = remainder.split(";")[0]
    else:
        jmp = ""
        cmp = remainder
    return dst, cmp, jmp

# if C instruction
def construct_C_instruction(instruction):

    dst, cmp, jmp = parse_C_instruction(instruction) 
    dst_b = DEST_TABLE[dst]
    cmp_b = COMP_TABLE[cmp]
    jmp_b = JUMP_TABLE[jmp]
    instruction_b = "111" + cmp_b + dst_b + jmp_b
    return instruction_b

# if A instruction, convert to 0 + address
def construct_A_instruction(instruction):
    # print("0" + "{0:015b}".format(int(instruction.lstrip("@"))))
    return "0" + "{0:015b}".format(int(instruction.lstrip("@")))

def remove_comments(lines):
    program_only = []
    for line in lines:
        if line and not line.startswith("//"):
            if "//" in line:
                program_only.append(line.split("//")[0].strip())
            else:
                program_only.append(line.strip())
    return program_only

def load_asm(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
    return lines

def write_hack_file(hack_code):
    with open("generated.hack", 'w+') as f:
        for line in hack_code:
            f.write(line + "\n")

def main():
    print("Starting program")
    args = parse_args()
    print(f"Loading file {args.asm_file}")
    raw_asm = load_asm(args.asm_file)
    instructions = remove_comments(raw_asm)

    # find symbols
    symbol_table = SymbolTable()
    symbol_table.first_pass(instructions)
    updated_instructions = symbol_table.second_pass(instructions)

    hack_code = []
    for instruction in updated_instructions:
        if instruction.startswith("@"):
            hack_code.append(construct_A_instruction(instruction))
        else:
            hack_code.append(construct_C_instruction(instruction))

    write_hack_file(hack_code)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("asm_file")
    return parser.parse_args()

if __name__ == "__main__":
    main()