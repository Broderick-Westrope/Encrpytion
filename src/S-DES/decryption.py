from keyGenerator import *

# Decipher a bloc


def decryptBlock(block, key):
    k1, k2 = generate_k1_k2(key)
    ciphertext = np.array(bitarray(block).tolist())
    ip_Cypher = IP(ciphertext)
    fk1_Cypher = FK(ip_Cypher, k2)
    fk1_Cypher_Switch = switch(fk1_Cypher)
    fk2_Cypher = FK(fk1_Cypher_Switch, k1)
    return IP_inverse(fk2_Cypher)


# Decipher an encrypted S-DES message and returns the decrypted bit code and ascii code
def decryptString(message, key):
    result = ""
    for bloc in range(0, len(message), 8):
        a = decryptBlock(message[bloc:bloc+8], key)
        str1 = ''.join(str(e) for e in a*1)
        result += str1
    return result
