import pwn

HOST = "localhost"
PORT = 8888

io = pwn.remote(HOST, PORT)
while True:
    try:
        io.recvuntil(b'Solve the problem: ')
        problem = io.recv().decode()
        ans = str(eval(problem))
        print(problem + "=" + ans)
        io.sendline(ans.encode())
    except:
        break

io.interactive()