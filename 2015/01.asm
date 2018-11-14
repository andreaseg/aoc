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

strfmt db '%d',10,0
errfmt db 'Invalid symbol %c',10,0
acc dd 0
bas dd 0
index dd 0

section '.code' code executable readable writeable

start:

iter:
  ; Call getchar and finish if EOF
  call [getchar]
  cmp eax, -1
  je finish
  add [index], 1

  ; Check if symbol is '(' or ')'
  cmp al, '('
  je accadd
  cmp al, ')'
  je accsub

  ; Chick if lineend
  cmp al, 10
  je finish

  ; Print error message on unexpected input
  push eax
  push errfmt
  call [printf]

  ; Exit with error
  push -1
  call [ExitProcess]

accadd:
  ; Increment accumulator
  add [acc], 1
  jmp iter

accsub:
  ; Decrement accumulator
  sub [acc], 1
  cmp [acc], -1
  je setbas
  jmp iter

setbas:
  cmp [bas], 0
  jne iter
  mov eax, [index]
  mov [bas], eax
  jmp iter

finish:
  ; Print results
  mov eax, [acc]
  push eax
  push strfmt
  call [printf]

  mov eax, [bas]
  push eax
  push strfmt
  call [printf]

  ; Exit with success
  push 0
  call [ExitProcess]
