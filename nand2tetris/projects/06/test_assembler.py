import assembler

import filecmp
import os
import pytest
import sys


def test_construct_C_instruction():
    assert assembler.construct_C_instruction("D=A") == "1110110000010000"
    assert assembler.construct_C_instruction("D=D+A") == "1110000010010000"
    assert assembler.construct_C_instruction("M=D") == "1110001100001000"

def test_parse_C_instruction():
    d,c,j = assembler.parse_C_instruction("D=A")
    assert d == "D"
    assert c == "A"
    assert j == ""

    d,c,j = assembler.parse_C_instruction("D=D+A")
    assert d == "D"
    assert c == "D+A"
    assert j == ""

    d,c,j = assembler.parse_C_instruction("M=D")
    assert d == "M"
    assert c == "D"
    assert j == ""

    d,c,j = assembler.parse_C_instruction("D;JGT")
    assert d == ""
    assert c == "D"
    assert j == "JGT"

def test_Max_asm():

    instructions = ["@R0"]
    st = assembler.SymbolTable()
    print(st.symbol_table)
    st.first_pass(instructions)