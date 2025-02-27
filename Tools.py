def int8(vec):
    return int(vec, 2)

def vec8(num):
    return bin(num)[2:].zfill(8)

def reverse_bytes(vec):
    res = []
    for i in range(0, len(vec), 8):
        block = vec[i: i + 8]
        res.append(block)

    return ''.join(res[::-1])
