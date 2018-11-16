format PE console

entry start

include 'win32a.inc'

section '.idata' data readable import
        library kernel32, 'kernel32.dll', \
                msvcrt,   'msvcrt.dll'
        import kernel32,\
               ExitProcess, 'ExitProcess'
        import msvcrt,\
               printf, 'printf',\
               getchar, 'getchar',\
               malloc, 'malloc',\
               realloc, 'realloc',\
               free, 'free'

section '.data' data readable writeable

allfmt db 'Reallocating memory at 0x%hhx (%d Bytes)',10,0
errfmt db 'Error reallocating memory',0
visfmt db 'Houses visited %d',0
x dw 0
y dw 0
list dd 0
listend dd 0
reserved dd 256

section '.code' code executable readable writeable

visit:
        ; Visit a house at (x, y) coordinates

        ; Get reference to start of heap allocated list
        mov ecx, [list]

.iter:
        ; Check if within list bounds
        cmp ecx, [listend]
        jg .oob

        ; Check if x-coordinate is equal
        mov al, [ecx]
        mov ah, [ecx+1]
        cmp ax, [x]
        jne @f

        ; Check if y-coordinate is equal
        mov al, [ecx+2]
        mov ah, [ecx+3]
        cmp ax, [y]
        je .finish

        @@:
        ; Increment pointer
        add ecx, 4
        jmp .iter

.oob:
        ; Check if realloc is needed
        mov ebx, [list]
        add ebx, [reserved]
        cmp ebx, [listend]
        jg @f

        ; Realloc
        mov eax, 2
        imul eax, [reserved]
        mov [reserved], eax
        push reserved
        push [list]
        call [realloc]
        add esp, 8
        cmp eax, 0
        je .error

        ; Update heap pointer
        mov ebx, [listend]
        sub ebx, [list]
        add ebx, eax
        mov [listend], ebx
        mov [list], eax

        ; Print message when reallocating
        push [reserved]
        push eax
        push allfmt
        call [printf]
        add esp, 12

        @@:

        ; Write value to end of list
        mov ecx, [listend]
        mov ax, [x]
        mov [ecx], al
        mov [ecx+1], ah
        mov ax, [y]
        mov [ecx+2], al
        mov [ecx+3], ah
        add [listend], 4

.finish:
        ret

.error:
        ; Print error and exit with error
        push errfmt
        call [printf]
        pop eax
        push -1
        call [ExitProcess]

start:
        ; Setup list of houses
        push [reserved]
        call [malloc]
        pop ebx
        mov [list], eax
        mov [listend], eax

.read:

        ; Visit current house
        call visit

        ; Read symbols
        call [getchar]

        cmp al, '<'
        jne @f
        dec [x]
        jmp .read
        @@:

        cmp al, '>'
        jne @f
        inc [x]
        jmp .read
        @@:

        cmp al, '^'
        jne @f
        inc [y]
        jmp .read
        @@:

        cmp al, 'v'
        jne @f
        dec [y]
        jmp .read
        @@:

        ; Print results
        mov eax, [listend]
        sub eax, [list]
        shr eax, 2
        push eax
        push visfmt
        call [printf]
        add esp, 8

        ; Free list
        push [list]
        call [free]

        ; Exit with success
        push 0
        call [ExitProcess]
