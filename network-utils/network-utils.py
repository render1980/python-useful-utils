import re

def split_into_x_chunks(string,x=10):
    size = len(string)
    chunksize = size//x
    for pos in range(0, size, chunksize):
        yield string[pos:pos+chunksize]

# ip_view_to_binary('255.255.255.0') => 11111111111111111111111100000000
def ip_view_to_binary(ip_view):
    numbers = ip_view.split('.')
    binaries = []
    for n in numbers:
        binary = bin(int(n)).replace("0b", "")
        while len(binary) <= 8:
            binary = '0' + binary
        binaries.append(binary)
    return ''.join(binaries)

# binary_view_to_ip('11111111111111111111111100000000') => '255.255.255.0'
def binary_view_to_ip(binary_ip):
    chunks = list(split_into_x_chunks(binary_ip, 4))
    res = []
    for c in chunks:
        c_dec = int(c, 2)
        res.append(str(c_dec))
    return '.'.join(res)
    
## Host IP (Bitwise AND) Subnet Mask /28
## (10 & 255) = 10
## (1 & 255) = 1
## (15 & 255) = 15
## (101 & 240) = 96
## => 10.1.15.96 self net address
