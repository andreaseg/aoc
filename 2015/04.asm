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

strfmt db '%hhx%hhx%hhx%hhx',10,0
errfmt db 'Error reallocating memory',0

section '.code' code executable readable writeable

md5:
        ; esi should point to the string to hash.
        ; Returns result into eax, ebx, ecx,
        ; and edx registers.

        ; Setup stack
        push 0x10325476 ; D [esp+20]
        push 0x98badcfe ; C [esp+16]
        push 0xefcdab89 ; B [esp+12]
        push 0x67452301 ; A [esp+8]

.start:

        xor ecx, ecx ; i = 0

        push 3905402710
        push 12
        call .part1
        add esp, 8

        push 606105819
        push 17
        call .part1
        add esp, 8

        push 3250441966
        push 22
        call .part1
        add esp, 8

        push 4118548399
        push 7
        call .part1
        add esp, 8

        push 1200080426
        push 12
        call .part1
        add esp, 8

        push 2821735955
        push 17
        call .part1
        add esp, 8

        push 4249261313
        push 22
        call .part1
        add esp, 8

        push 1770035416
        push 7
        call .part1
        add esp, 8

        push 2336552879
        push 12
        call .part1
        add esp, 8

        push 4294925233
        push 17
        call .part1
        add esp, 8

        push 2304563134
        push 22
        call .part1
        add esp, 8

        push 1804603682
        push 7
        call .part1
        add esp, 8

        push 4254626195
        push 12
        call .part1
        add esp, 8

        push 2792965006
        push 17
        call .part1
        add esp, 8

        push 1236535329
        push 22
        call .part1
        add esp, 8

        push 4129170786
        push 5
        call .part2
        add esp, 8

        push 3225465664
        push 9
        call .part2
        add esp, 8

        push 643717713
        push 14
        call .part2
        add esp, 8

        push 3921069994
        push 20
        call .part2
        add esp, 8

        push 3593408605
        push 5
        call .part2
        add esp, 8

        push 38016083
        push 9
        call .part2
        add esp, 8

        push 3634488961
        push 14
        call .part2
        add esp, 8

        push 3889429448
        push 20
        call .part2
        add esp, 8

        push 568446438
        push 5
        call .part2
        add esp, 8

        push 3275163606
        push 9
        call .part2
        add esp, 8

        push 4107603335
        push 14
        call .part2
        add esp, 8

        push 1163531501
        push 20
        call .part2
        add esp, 8

        push 2850285829
        push 5
        call .part2
        add esp, 8

        push 4243563512
        push 9
        call .part2
        add esp, 8

        push 1735328473
        push 14
        call .part2
        add esp, 8

        push 2368359562
        push 20
        call .part2
        add esp, 8

        push 4294588738
        push 4
        call .part3
        add esp, 8

        push 2272392833
        push 11
        call .part3
        add esp, 8

        push 1839030562
        push 16
        call .part3
        add esp, 8

        push 4259657740
        push 23
        call .part3
        add esp, 8

        push 2763975236
        push 4
        call .part3
        add esp, 8

        push 1272893353
        push 11
        call .part3
        add esp, 8

        push 4139469664
        push 16
        call .part3
        add esp, 8

        push 3200236656
        push 23
        call .part3
        add esp, 8

        push 681279174
        push 4
        call .part3
        add esp, 8

        push 3936430074
        push 11
        call .part3
        add esp, 8

        push 3572445317
        push 16
        call .part3
        add esp, 8

        push 76029189
        push 23
        call .part3
        add esp, 8

        push 3654602809
        push 4
        call .part3
        add esp, 8

        push 3873151461
        push 11
        call .part3
        add esp, 8

        push 530742520
        push 16
        call .part3
        add esp, 8

        push 3299628645
        push 23
        call .part3
        add esp, 8

        push 4096336452
        push 6
        call .part4
        add esp, 8

        push 1126891415
        push 10
        call .part4
        add esp, 8

        push 2878612391
        push 15
        call .part4
        add esp, 8

        push 4237533241
        push 21
        call .part4
        add esp, 8

        push 1700485571
        push 6
        call .part4
        add esp, 8

        push 2399980690
        push 10
        call .part4
        add esp, 8

        push 4293915773
        push 15
        call .part4
        add esp, 8

        push 2240044497
        push 21
        call .part4
        add esp, 8

        push 1873313359
        push 6
        call .part4
        add esp, 8

        push 4264355552
        push 10
        call .part4
        add esp, 8

        push 2734768916
        push 15
        call .part4
        add esp, 8

        push 1309151649
        push 21
        call .part4
        add esp, 8

        push 4149444226
        push 6
        call .part4
        add esp, 8

        push 3174756917
        push 10
        call .part4
        add esp, 8

        push 718787259
        push 15
        call .part4
        add esp, 8

        push 3951481745
        push 21
        call .part4
        add esp, 8

        ; Check if string has ended
        cmp [esi+512], 0
        je @f
        add esi, 512
        jmp .start
        @@:

        pop eax
        pop ebx
        pop ecx
        pop edx

        ret


.part1:
        mov eax, [esp+12]
        not eax
        and eax, [esp+20]
        mov edx [esp+12]
        and edx, [esp+16]
        or eax, edx

        mov ebx, ecx

        jmp .common

.part2:
        mov eax, [esp+20]
        not eax
        and eax, [esp+16]
        mov edx, [esp+20]
        and edx, [esp+12]
        or eax, edx

        lea ebx, [5*ecx + 1]
        and ebx, 0xf

        jmp .common

.part3:
        mov eax, [esp+20]
        xor eax, [esp+16]
        xor eax, [exp+12]

        lea ebx, [3*ecx+5]
        and ebx, 0xf

        jmp .common

.part4:
        mov eax, [esp+20]
        not eax
        or eax, [esp+12]
        xor eax, [esp+16]

        lea ebx, [7*ecx]
        and ebx, 0xf

.common:
        ; eax = F
        ; ebx = g
        add eax, [esp+8]
        add eax, [esp+4]

        ; Load correct 32-bit word
        mov dh, [esi+4*ebx]
        mov dl, [esi+4*ebx+1]
        shl edx, 8
        mov dh, [esi+4*ebx+2]
        mov dl, [esi+4*ebx+3]

        ; F += A + K + M
        add eax, edx

        mov ebx, [esp+20]
        mov [esp], ebx

        mov ebx, [esp+16]
        mov [esp+20], ebx

        mov ebx, [esp+12]
        mov [esp+16], ebx

        ; Leftrotate
        mov ebx, [esp]
        mov edx, eax
        shl edx, ebx

        mov ebx, 32
        sub ebx, [esp]
        shl eax, ebx

        or eax, edx

        add [esp+12], eax

        ; ++i
        inc ecx

        ret


start:
        ; Read string from stdin in correct format
        ...

        call md5

        ; Print results
        push eax
        push ebx
        push ecx
        push edx
        push [strfmt]
        call [printf]
        pop eax

        ; Exit with success
        push 0
        call [ExitProcess]
