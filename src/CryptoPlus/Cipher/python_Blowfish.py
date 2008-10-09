from blockcipher import *
from pyblowfish import Blowfish

def new(key,mode=MODE_ECB,IV=None,counter=None):
    """Create a new cipher object

    Wrapper for pure python implementation pyblowfish.py

        key = raw string containing the key
        mode = Blowfish.MODE_ECB/CBC/CFB/OFB/CTR/CMAC, default is ECB
        IV = IV as a raw string
            -> only needed for CBC mode
        counter = counter object (CryptoPlus.Util.util.Counter)
            -> only needed for CTR mode

    EXAMPLES:
    **********
    IMPORTING:
    -----------
    >>> from CryptoPlus.Cipher import python_Blowfish

    EXAMPLE: (http://www.schneier.com/code/vectors.txt)
    ----------

    >>> cipher = python_Blowfish.new(('0131D9619DC1376E').decode('hex'))
    >>> ( cipher.encrypt(('5CD54CA83DEF57DA').decode('hex')) ).encode('hex')
    'b1b8cc0b250f09a0'
    >>> ( cipher.decrypt((_).decode('hex')) ).encode('hex')
    '5cd54ca83def57da'

    CBC, CFB, OFB EXAMPLE: http://www.schneier.com/code/vectors.txt
    ----------------------
    >>> key = ('0123456789ABCDEFF0E1D2C3B4A59687').decode('hex')
    >>> IV = ('FEDCBA9876543210').decode('hex')
    >>> plaintext = ('37363534333231204E6F77206973207468652074696D6520').decode('hex')
    >>> cipher = python_Blowfish.new(key,python_Blowfish.MODE_CBC,IV)
    >>> ciphertext = cipher.encrypt(plaintext)
    >>> (ciphertext).encode('hex').upper()
    '6B77B4D63006DEE605B156E27403979358DEB9E7154616D9'


    >>> key = '0123456789ABCDEFF0E1D2C3B4A59687'.decode('hex')
    >>> iv = 'FEDCBA9876543210'.decode('hex')
    >>> plaintext = '37363534333231204E6F77206973207468652074696D6520666F722000'.decode('hex')

    >>> cipher = python_Blowfish.new(key,python_Blowfish.MODE_CBC,iv)
    >>> ciphertext = cipher.encrypt(plaintext)
    >>> (ciphertext).encode('hex').upper()
    '6B77B4D63006DEE605B156E27403979358DEB9E7154616D9'

    >>> cipher = python_Blowfish.new(key,python_Blowfish.MODE_CFB,iv)
    >>> ciphertext = cipher.encrypt(plaintext)
    >>> (ciphertext).encode('hex').upper()
    'E73214A2822139CAF26ECF6D2EB9E76E3DA3DE04D1517200519D57A6C3'

    >>> cipher = python_Blowfish.new(key,python_Blowfish.MODE_OFB,iv)
    >>> ciphertext = cipher.encrypt(plaintext)
    >>> (ciphertext).encode('hex').upper()
    'E73214A2822139CA62B343CC5B65587310DD908D0C241B2263C2CF80DA'"""
    return python_Blowfish(key,mode,IV,counter)

class python_Blowfish(BlockCipher):
    def __init__(self,key,mode,IV,counter):
        cipher_module = Blowfish
        self.blocksize = 8
        BlockCipher.__init__(self,key,mode,IV,counter,cipher_module)

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()