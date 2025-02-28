import numpy as np

def int8(vec):
    return int(vec, 2)

def vec8(num):
    return bin(num)[2:].zfill(8)

def vec128(num):
    return bin(num)[2:].zfill(128)

def reverse_bytes(vec):
    res = []
    for i in range(0, len(vec), 8):
        block = vec[i: i + 8]
        res.append(block)

    return ''.join(res[::-1])

_xormap = {('0', '1'): '1', ('1', '0'): '1', ('1', '1'): '0', ('0', '0'): '0'}
def xor(x, y):
    x, y = str(x), str(y)
    return ''.join([_xormap[a, b] for a, b in zip(x, y)]).zfill(len(x))

def generate_bin_sequence(len):
    return ''.join(str(x) for x in np.random.choice([0, 1], size=len))

def generate_key():
    return generate_bin_sequence(256)

def string_to_binary(text):
    return ''.join(bin(ord(i))[2:].zfill(8) for i in text)

def binary_to_string(binary):
    return ''.join(chr(int(binary[i:i + 8], 2)) for i in range(0, len(binary), 8))
