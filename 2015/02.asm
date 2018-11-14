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
               getchar, 'getchar'

section '.data' data readable writeable

strfmt db 'Wrapping paper needed %d',10,0
errfmt db 'Invalid symbol %c',10,0
error dd 0
sum dd 0
l dd 0
w dd 0
h dd 0

section '.code' code executable readable writeable

readnum:
        ; Reads number until newline, eof or 'x' is encountered
        push 0
        @@:
        call [getchar]
        cmp eax, -1
        je .eof
        cmp al, 10
        je .finish
        cmp al, 'x'
        je .finish
        cmp al, ';'
        je .eof

        ; Integer offset
        sub eax, '0'

        ; Correctly parses integer
        pop ebx
        imul ebx, 10
        add ebx, eax
        push ebx
        jmp @b
.finish:
        ; Return results in eax
        pop eax
        ret
.eof:
        ; Retuns error code -1
        pop eax
        mov [error], -1
        ret

start:
        ; Read three numbers
        call readnum
        cmp [error], -1
        je .finish
        mov [l], eax
        call readnum
        mov [w], eax
        call readnum
        mov [h], eax

        ; eax = l * h
        mov eax, [l]
        imul eax, [w]

        ; ebx = w * h
        mov ebx, [w]
        imul ebx, [h]

        ; ecx = h * l
        mov ecx, [h]
        imul ecx, [l]

        ; edx = min(eax, ebx, ecx)
        mov edx, eax
        cmp edx, ebx
        jle @f
        mov edx, ebx
        @@:
        cmp edx, ecx
        jle @f
        mov edx, ecx
        @@:

        ; sum += edx + 2*(eax + ebx + ecx)
        add eax, ebx
        add eax, ecx
        shl eax, 1
        add eax, edx
        add [sum], eax

        ; Get next line
        jmp start

.finish:
        ; Print results
        mov eax, [sum]
        push eax
        push strfmt
        call [printf]
