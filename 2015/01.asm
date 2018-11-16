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

accfmt db 'Curent floor %d',10,0
basfmt db 'First time entered basement %d',10,0
errfmt db 'Invalid symbol %c',10,0
acc dd 0
bas dd 0
index dd 0

section '.code' code executable readable writeable

start:

.iter:
        ; Call getchar and finish if EOF
        call [getchar]
        cmp eax, -1
        je .finish
        add [index], 1

        ; Check if symbol is '('
        cmp al, '('
        jne @f
        inc [acc]
        jmp .iter
        @@:

        ; Check if symbols is ')'
        cmp al, ')'
        jne @f
        dec [acc]
        cmp [acc], -1
        je .setbas
        jmp .iter
        @@:

        ; Check if lineend
        cmp al, 10
        je .finish

        ; Print error message on unexpected input
        push eax
        push errfmt
        call [printf]
        add esp, 8

        ; Exit with error
        push -1
        call [ExitProcess]

.setbas:
        ; Set bas to value of index if bas equals zero
        cmp [bas], 0
        jne .iter
        mov eax, [index]
        mov [bas], eax
        jmp .iter

.finish:
        ; Print results
        mov eax, [acc]
        push eax
        push accfmt
        call [printf]
        add esp, 8

        mov eax, [bas]
        push eax
        push basfmt
        call [printf]
        add esp, 8

        ; Exit with success
        push 0
        call [ExitProcess]
