# -*- coding: utf-8 -*-
from curses import has_il
import hashlib, binascii
# hashlib module is used to translate for hash by python.

def main():
    # hashlib has the constructor included md5(), sha1(), sha224(), sha256(), sha384(), sha512().
    md = hashlib.md5()
    message = "The quick brown for jumps over the lazy dog"
    md.update(message.encode("utf-8"))
    print(md.digest())
    print("Digest size:", md.digest_size, "\n", "BlockSize:", md.block_size)
    
    #compare the digest in sha224, sha256, sha384, sha512.
    print("DigestSHA224", hashlib.sha224(message.encode("utf-8")).hexdigest())
    print("DigestSHA256", hashlib.sha256(message.encode("utf-8")).hexdigest())
    print("DigestSHA384", hashlib.sha384(message.encode("utf-8")).hexdigest())
    print("DigestSHA512", hashlib.sha512(message.encode("utf-8")).hexdigest())
    #All output of hashes are unique

    # example of 160bishash for RIPEMD160
    h = hashlib.new('ripemd160')
    h.update(message.encode("utf-8"))
    h.hexdigest()
    
    # key derivation algorithm
    # If the hash algorithm has been used without treatment, it isn't resistant against brute force attacks.
    # A key derivation algorithm is used for hashing the password safety.
    #import hashlib, binascii
    algorithm = 'sha256'
    password = 'HomeWifi'.encode('utf-8')
    salt = 'salt'.encode('utf-8') # salt is the random data that can be used for additional input for one way function.
    nu_rounds = 1000
    key_length = 64 #length of key
    dk = hashlib.pbkdf2_hmac(algorithm, password, salt, nu_rounds, dklen=key_length)
    print("deriviated key", dk)
    print("Hexadecimal of deriviated key", binascii.hexlify(dk))
    
    #check the property of hash
    
    input = 'Sample Input Text'.encode('utf-8')
    for i in range(20):
        # add iterator to the tail of text
        input_text = input + str(i).encode('utf-8')
        # display the input and result of hash
        print(input_text, ':', hashlib.sha256(input_text).hexdigest())
    
if __name__ == "__main__":
    main()