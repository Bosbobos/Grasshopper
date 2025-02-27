from OperationManager import OperationManager
from KeyManager import KeyManager
import Tools

class Grasshopper:
    def __init__(self, key):
        self.key = key
        self.keyManager = KeyManager(key)
        self.opManager = OperationManager()

    def EncryptBlock(self, block):
        for i in range(1, 10):
            key = self.keyManager.k[i]
            block = self.opManager.lsx(key, block)

        block = Tools.xor(block, self.keyManager.k[10])

        return block

    def DecryptBlock(self, block):
        for i in range(10, 1, -1):
            key = self.keyManager.k[i]
            block = self.opManager.lsx_rev(key, block)

        block = Tools.xor(block, self.keyManager.k[1])

        return block