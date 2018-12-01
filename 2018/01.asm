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

strfmt db 'Frequency is %i',10,0

section '.text' code executable readable writeable

parseint:
	; Counter
	push 0
.next:
	call [getchar]

	; Check if char is number
	cmp eax, '0'
	jl .finish
	cmp eax, '9'
	jg .finish

	; Follow decimal number rules
	mov edx, [esp]
	imul edx, 10
	sub eax, '0'
	add edx, eax
	mov [esp], edx
	jmp .next

.finish:
	pop eax
	ret	 	

start:
	; Put result on stack
	push 0

.readline:
	call [getchar]

	; Check if prefix is +
	cmp eax, '+'
	jne @f
	call parseint
	add [esp], eax
	jmp .readline
	@@:

	; Check if prefix is -
	cmp eax, '-'
	jne @f
	call parseint
	sub [esp], eax
	jmp .readline
	@@:

	cmp eax, -1
	jne .readline

	push strfmt
	call [printf]
	add esp, 8

        ; Exit with success
        push 0
        call [ExitProcess]
