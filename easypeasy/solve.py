from pwn import *

r = remote('mercury.picoctf.net', 20266)

r.recvuntil("This is the encrypted flag!\n")

flag = r.recvlineS(keepends = False)

bin_flag = unhex(flag)

r.sendlineafter("What data would you like to encrypt? ", 'a' * (50000 - len(bin_flag)))

r.sendlineafter("What data would you like to encrypt? ", bin_flag)
r.recvline()

ans = unhex(r.recvlineS())
print(ans)