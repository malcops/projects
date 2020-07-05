// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

// R1 = n
// for (i=0, i<n, i++):
//     R2 = R2 + R0
//     

@R2 // zero result
M=0
@n
M=0
@i
M=0

@R0 // end if R0=0
D=M
@END
D;JEQ
@R1 // end if R1=0
D=M
@END
D;JEQ

@R1
D=M
@n
M=D

@LOOP
0;JMP

(LOOP)
    @i
    D=M
    @n
    D=D-M
    @END
    D;JEQ

    @R0
    D=M
    @R2
    M=D+M

    @i
    M=M+1

    @LOOP
    0; JMP

(END)
    @END
    0; JMP