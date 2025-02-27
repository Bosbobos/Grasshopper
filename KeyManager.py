from OperationManager import OperationManager
from Tools import *

class KeyManager:
    opManager = OperationManager()
    key = ''
    round_const = ['0'*128]
    k = ['0' * 128] * 11 #round keys

    def __init__(self, key):
        if len(key) != 256:
            raise Exception('Key length must be 256')

        self.key = key
        self.calculate_round_consts()
        self.calculate_round_keys()

    def calculate_round_consts(self):
        for i in range(1, 32+1):
            vc = vec128(i)
            self.round_const.append(self.opManager.linear_transform(vc))

    def F(self, k, a1, a0):
        res = self.opManager.lsx(k, a1)
        res = xor(res, a0)

        return (res, a1)

    def calculate_round_keys(self):
        key = self.key[::-1]
        self.k[0], self.k[1] = key[:128], key[128:]

        for i in range(1, 4+1):
            k1, k2 = self.k[2 * i - 1], self.k[2 * i]
            for j in range(1, 8+1):
                 k1, k2 = (
                    self.F(self.round_const[8*(i-1)+j],
                    k1, k2))

            self.k[2 * i + 1], self.k[2 * i + 2] = k1, k2
