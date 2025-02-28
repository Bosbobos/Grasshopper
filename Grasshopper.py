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

    def EncryptBinText(self, text, IV, decrypt = False): # Uses 4-th method - Режим простой замены с зацеплением
        res = ''
        n = 128
        text += '0' * (len(text) % 128)
        block_num = len(text) // 128
        register = IV
        for i in range(block_num):
            block = text[i * 128:(i + 1) * 128]

            if decrypt:
                decrypted = self.DecryptBlock(block)
                encrypted = Tools.xor(decrypted, register[:n])
                register = register[n:] + block
            else:
                xored = Tools.xor(block, register[:n])
                encrypted = self.EncryptBlock(xored)
                register = register[n:] + encrypted
            res += encrypted

        return res

    def DecryptBinText(self, text, IV):
        return self.EncryptBinText(text, IV, True)

    def EncryptText(self, text, IV, decrypt = False):
        if not decrypt: text += ' ' * 10
        binText = Tools.string_to_binary(text)
        if decrypt:
            encrypted = self.DecryptBinText(binText, IV)
        else:
            encrypted = self.EncryptBinText(binText, IV)

        result = Tools.binary_to_string(encrypted)
        if decrypt: result = result.split(' '*3)[0]
        return result

    def DecryptText(self, text, IV):
        return self.EncryptText(text, IV, True)
