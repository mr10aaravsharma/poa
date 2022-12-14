//--------------2cubeMixed
//online gdb pe lang mei choose c++(turbo)

#include<stdio.h>
#include<conio.h>

void main() {
    clrscr();
    int base = 2, power = 3, ans;
    asm MOV ax, 01H;
    asm MOV cx, base;
    asm MOV bx, power;
    UP: asm MUL cx;
    asm DEC bx;
    asm JNZ UP;
    asm MOV ans, ax;
    printf("%d^%d = %d", base, power, ans);
}


//--------------mixedModelSl.c
#include <stdio.h>

int main()
{
    int p = 100, r = 2, t = 3, interest;

    __asm__ __volatile__(
        "mul %%ebx"
        : "=a"(p)
        : "a"(p), "b"(r));

    __asm__ __volatile__(
        "mul %%ebx"
        : "=a"(p)
        : "a"(p), "b"(t));

    // div function not working for some reason
    __asm__ __volatile__(
        "div %%ebx, %%eax"
        : "=a"(p)
        : "a"(p), "b"(100));

    __asm__ __volatile__(
        "mov %%eax, %%ecx"
        : "=a"(interest)
        : "a"(p));
    printf("Simple Interest = %d\n", interest);

    return 0;
}

//-------------simpleInterestAssembly
data segment
    p dw 100
    r dw 2
    t dw 2
    i dw ?
ends

code segment
    assume ds:data cs:code
    start:
    mov ax,data
    mov ds,ax
    
    mov ax,p
    mul r
    mul t
    mov bx,0064h
    div bx
    mov i,ax
ends
end start

//-------------mRaisedTonAssembly
;EXPERIMENT 9
; PERFORMING M ^ N

DATA SEGMENT
    M DW 3
    N DW 3
    RES DW ?
DATA ENDS

CODE SEGMENT
    ASSUME CS:CODE,DS:DATA
    START:  
        MOV AX,DATA
        MOV DS,AX
        MOV AX,0001
        MOV BX,M
        MOV CX,N
        LOOP1:
        MUL BX
        DEC CX
        JNZ LOOP1
        MOV RES,AX
CODE ENDS
END START


//----------mixedMode.c
#include <stdio.h>

int main(void) {
    int num1 = 10, num2 = 15, sum = 0;
    __asm__ __volatile__(
        "addl %%ebx,%%eax"
        : "=a"(num1)
        : "a"(num1), "b"(num2));
    printf("num1 + num2=%d\n", num1);
    __asm__ __volatile__(
        "movl %%eax, %%ecx"
        : "=c"(sum)
        : "a"(num1));
    printf("num1 + num2=%d\n", sum);
    return 0;
}



//----arithemeticOpsAssembly
// ADDITION
mov ax, [1000h] 
mov bx, [1002h] 
mov cl, 00h
add ax, bx
mov [1004h], ax

JNC jump
inc cl
jump:
mov [1006h], cl 
hlt

// SUBTRACTION
mov ax, [1000h] 
mov bx, [1002h] 
mov cl, 00h
sub ax, bx
mov [1004h], ax

JNC jump
inc cl
jump:
mov [1006h], cl 
hlt

// MULTIPLICATION- mul
// DIVISION - div

// ADD & SUB USING PROCEDURE
ASSUME CS:CODE, DS:DATA, SS:STACK_SEG

DATA SEGMENT
NUM1 DB 50H
NUM2 DB 20H
ADD_RES DB ?
SUB_RES DB ?
DATA ENDS


CODE SEGMENT
START: MOV AX, DATA ; initialize data segment
MOV DS, AX

CALL ADDITION
CALL SUBTRACTION

MOV AH, 4CH
INT 21H

ADDITION PROC NEAR 
MOV AL, NUM1
MOV BL, NUM2
ADD AL, BL
MOV ADD_RES, AL 
RET
ADDITION ENDP

SUBTRACTION PROC 
MOV AL, NUM1
MOV BL, NUM2
SUB AL, BL
MOV SUB_RES, AL 
RET
SUBTRACTION ENDP

CODE ENDS
END START

//--------factorialAssembly
// FACTORIAL USING MACRO

factorial macro n
loop:
mul n
dec n
jnz loop
endm

data segment
num dw05h
result dw ?
data ends

code segment
assume ds:data,cs:code

start:
MOV AX,data
MOV DS,AX
MOV AX,0001h
factorial num
MOV result,AX

end start
code ends

// FACTORIAL USING PROCEDURE

data segment
num dw05h
result dw ?
data ends

code segment
assume ds:data,cs:code

start:
MOV AX,data
MOV DS,AX
MOV AX,0001h
CALL factorial
int21h

proc factorial near
loop:
mul num
dec num
jnz loop
MOV result,AX
factorial endp

end start
code ends

// FACTORIAL (SIMPLE)

DATA SEGMENT
A DB 5
fact DB ?
DATA ENDS
CODE SEGMENT
         ASSUME DS:DATA,CS:CODE
START:
      MOV AX,DATA
      MOV DS,AX
      MOV AH,00
      MOV AL,A
 L1:  DEC A
      MUL A
      MOV CL,A
      CMP CL,01
      JNZ L1
      MOV fact, AL 
CODE ENDS
END START


//---------transferNBlocksDataAssembly
data segment
src db0x90,0x34,0x45,0x21
data ends

extra segment
dest db ?
extra ends

code segment
assume cs:code,ds:data,es:extra

start:
mov ax,data
mov ds,ax
mov ax,extra
mov es,ax
lea si,src
lea di,dest
mov cx,0x04
cld
rep
movsb

end start
code ends


//---------minMaxNumberAssembly
// SMALLEST/MINIMUM NUMBER

data segment 
arr db 0x77, 0x27, 0x99, 0x80 
data ends

code segment 
assume cs:code, ds:data

start:
mov ax, data 
mov ds, ax 
lea si, arr 
mov cl, 0x03 
mov al, [si] 
inc si

loop_:
mov bl, [si] 
cmp al, bl 
jc cleanup 
mov al, bl
cleanup: 
inc si
dec cl 
jnz loop_

code ends 
end start

// LARGEST/MAXIMUM NUMBER

data segment 
arr db 0x77, 0x27, 0x99, 0x80 
data ends

code segment 
assume cs:code, ds:data

start:
mov ax, data 
mov ds, ax 
lea si, arr 
mov cl, 0x03 
mov al, [si] 
inc si

loop_:
mov bl, [si] 
cmp al, bl 
jnc cleanup 
mov al, bl
cleanup: 
inc si
dec cl 
jnz loop_

code ends 
end start



//--------ascDescSortAssembly
// ASCENDING
data segment
arr db 0x89, 0x45, 0x54, 0x10, 0x23 
data ends

code segment 
assume cs:code, ds:data

start:
mov ax, data
mov ds, ax

mov ch, 0x04
loop_1:
mov cl, 0x04
lea si, arr

loop_2:
mov al, [si] 
mov bl, [si + 1] 
cmp al, bl 
jc cleanup 
mov dl, [si + 1] 
xchg [si], dl 
mov [si + 1], dl
cleanup: 
inc si 
dec cl
jnz loop_2 
dec ch 
jnz loop_1
code ends
end start

// DESCENDING
data segment
arr db 0x89, 0x45, 0x54, 0x10, 0x23 
data ends

code segment 
assume cs:code, ds:data

start:
mov ax, data
mov ds, ax

mov ch, 0x04
loop_1:
mov cl, 0x04
lea si, arr

loop_2:
mov al, [si] 
mov bl, [si + 1] 
cmp al, bl 
jnc cleanup 
mov dl, [si + 1] 
xchg [si], dl 
mov [si + 1], dl
cleanup: 
inc si 
dec cl
jnz loop_2 
dec ch 
jnz loop_1
code ends
end start


//memoryAllocation
#include <stdio.h>
#include <limits.h>
#include <malloc.h>
int *worst_fit_map(int *mem_map, int *proc_map, int mem_size, int proc_size)
{
    int *mem_map_copy = (int *)malloc(sizeof(int) * mem_size);
    int *result = (int *)malloc(sizeof(int) * proc_size);
    for (int i = 0; i < mem_size; mem_map_copy[i] = mem_map[i], ++i)
        ;
    for (int i = 0; i < proc_size; result[i] = -1, ++i)
        ;
    for (int i = 0; i < proc_size; ++i)
    {
        int curr_proc = proc_map[i];
        int idx = -1, diff = INT_MIN;
        for (int j = 0; j < mem_size; ++j)
        {
            if (mem_map_copy[j] >= curr_proc && mem_map_copy[j] - curr_proc > diff && mem_map_copy[j] == mem_map[j])
            {
                idx = j;
                diff = mem_map_copy[j] - curr_proc;
            }
        }
        if (idx != -1)
        {
            mem_map_copy[idx] -= curr_proc;
            result[i] = mem_map_copy[idx];
        }
    }
    free(mem_map_copy);
    return result;
}
int *first_fit_map(int *mem_map, int *proc_map, int mem_size, int proc_size)
{
    int *mem_map_copy = (int *)malloc(sizeof(int) * mem_size);
    int *result = (int *)malloc(sizeof(int) * proc_size);
    for (int i = 0; i < mem_size; mem_map_copy[i] = mem_map[i], ++i)
        ;
    for (int i = 0; i < proc_size; result[i] = -1, ++i)
        ;
    for (int i = 0; i < proc_size; ++i)
    {
        int curr_proc = proc_map[i];
        for (int j = 0; j < mem_size; ++j)
        {
            if (mem_map_copy[j] >= curr_proc && mem_map_copy[j] == mem_map[j])
            {
                mem_map_copy[j] -= curr_proc;
                result[i] = mem_map_copy[j];
                break;
            }
        }
    }
    free(mem_map_copy);
    return result;
}
int *best_fit_map(int *mem_map, int *proc_map, int mem_size, int proc_size)
{
    int *mem_map_copy = (int *)malloc(sizeof(int) * mem_size);
    int *result = (int *)malloc(sizeof(int) * proc_size);
    for (int i = 0; i < mem_size; mem_map_copy[i] = mem_map[i], ++i)
        ;
    for (int i = 0; i < proc_size; result[i] = -1, ++i)
        ;
    for (int i = 0; i < proc_size; ++i)
    {
        int curr_proc = proc_map[i];
        int idx = -1, diff = INT_MAX;
        for (int j = 0; j < mem_size; ++j)
        {
            if (mem_map_copy[j] >= curr_proc && mem_map_copy[j] - curr_proc < diff && mem_map_copy[j] == mem_map[j])
            {
                idx = j;
                diff = mem_map_copy[j] - curr_proc;
            }
        }
        if (idx != -1)
        {
            mem_map_copy[idx] -= curr_proc;
            result[i] = mem_map_copy[idx];
        }
    }
    free(mem_map_copy);
    return result;
}
int *next_fit_map(int *mem_map, int *proc_map, int mem_size, int proc_size)
{
    int *mem_map_copy = (int *)malloc(sizeof(int) * mem_size);
    int *result = (int *)malloc(sizeof(int) * proc_size);
    int next_idx = 0;
    for (int i = 0; i < mem_size; mem_map_copy[i] = mem_map[i], ++i)
        ;
    for (int i = 0; i < proc_size; result[i] = -1, ++i)
        ;
    for (int i = 0; i < proc_size; ++i)
    {
        for (int j = next_idx, k = 0; k < mem_size; j = (j + 1) % mem_size, ++k)
        {
            if (mem_map_copy[j] >= proc_map[i] && mem_map_copy[j] == mem_map[j])
            {
                mem_map_copy[j] -= proc_map[i];
                result[i] = mem_map_copy[j];
                if (mem_map_copy[j] != 0)
                    next_idx = j;
                else
                    next_idx = (j + 1) % mem_size;
                break;
            }
        }
    }
    free(mem_map_copy);
    return result;
}
int main()
{
    int *mem_map, *proc_map;
    int mem_size, proc_size;
    printf("Enter size of memory map: \n");
    scanf("%d", &mem_size);
    printf("Enter size of process map: \n");
    scanf("%d", &proc_size);
    mem_map = (int *)malloc(sizeof(int) * mem_size);
    proc_map = (int *)malloc(sizeof(int) * proc_size);
    printf("Enter sizes of memory map: \n");
    for (int i = 0; i < mem_size; ++i)
        scanf("%d", &mem_map[i]);
    printf("Enter sizes of process map: \n");
    for (int i = 0; i < proc_size; ++i)
        scanf("%d", &proc_map[i]);
    int *best_fit = best_fit_map(mem_map, proc_map, mem_size, proc_size);
    int *first_fit = first_fit_map(mem_map, proc_map, mem_size, proc_size);
    int *worst_fit = worst_fit_map(mem_map, proc_map, mem_size, proc_size);
    int *next_fit = next_fit_map(mem_map, proc_map, mem_size, proc_size);
    // Logic to print above three arrays as table
    printf("PROC SIZE\t BEST FIT\t FIRST FIT\t WORST FIT\t NEXT FIT\n");
    for (int i = 0; i < proc_size; ++i)
        printf("%d\t\t %d\t\t %d\t\t %d\t\t %d\n", proc_map[i], best_fit[i], first_fit[i], worst_fit[i], next_fit[i]);
    free(best_fit);
    free(first_fit);
    free(worst_fit);
    free(mem_map);
    free(proc_map);
    return 0;
}