import hashlib

def calcmd5(*kwargs):
    
    plaintext = ''
    for i in kwargs:
        plaintext += str(i)       
    m = hashlib.md5()
    m.update(plaintext)    
    return m.hexdigest()
if __name__=='__main__':
    print calcmd5('asd','a','sd')