
########################
# Automate nice netcat #
########################

from pwn import remote, context

context.log_level = 'debug'
context.log_level = 'error'

url = "mercury.picoctf.net"
port = 22342

r = remote(url, port)
output = r.recvall().decode()

output = output.replace(" ", "")
output = output.split("\n")
output.remove('')

# print(output)

ints = []
for i in output:
    ints.append(int(i))
# print(ints)

ascii_ = []
for i in ints:
    ascii_.append(chr(i))
# print(ascii_)

for i in ascii_:
    print(i, end='')
