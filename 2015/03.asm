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

errfmt db 'Error reallocation',0
visfmt db 'Houses visited %d',0
x dw 0
y dw 0
list dd 0
listend dd 0
reserved dd 400

section '.code' code executable readable writeable

visit:
        ; Visit a house at (x, y) coordinates

        ; Get reference to start of heap allocated list
        mov ecx, [list]

.iter:
        ; Check if within list bounds
        cmp ecx, [listend]
        jge .oob

        ; Check if x-coordinate is equal
        mov ah, [ecx]
        mov al, [ecx+1]
        cmp ax, [x]
        jne @f

        ; Check if y-coordinate is equal
        mov ah, [ecx+2]
        mov al, [ecx+3]
        cmp ax, [y]
        je .finish

        @@:
        add ecx, 4
        jmp .iter

.oob:
        ; Check if realloc is needed
        mov ebx, [listend]
        sub ebx, [list]
        cmp ebx, [reserved]
        jl @f

        ; Realloc
        add [reserved], 400
        push reserved
        push [list]
        call [realloc]
        cmp eax, 0
        je .error

        ; Update heap pointer
        mov ebx, [listend]
        sub ebx, [list]
        mov [list], eax
        mov [listend], eax
        add [listend], ebx

        @@:

        ; Write value to end of list
        mov ecx, [listend]
        mov ax, [x]
        mov [ecx], ah
        mov [ecx+1], al
        mov ax, [y]
        mov [ecx+2], ah
        mov [ecx+3], al
        add [listend], 4

.finish:
        ret

.error:
        push errfmt
        call [printf]
        push -1
        call [ExitProcess]

start:
        ; Setup list of houses
        push [reserved]
        call [malloc]
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

        ; Free list
        push [list]
        call [free]

        push 0
        call [ExitProcess]
