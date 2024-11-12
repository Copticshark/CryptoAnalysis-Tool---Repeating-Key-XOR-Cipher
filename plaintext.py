def main():
    cpath = 'cipher.txt'
    key = bytes([0xAE, 0x22, 0x00, 0xAF, 0x2F, 0xB8, 0x99, 0x11, 0xDD, 0x00])

    ctext = read_hex_file(cpath)
    ptext = decrypt(ctext, key)
    print("Decrypted plaintext:")
    print(ptext.decode('ascii'))

def read_hex_file(filepath):
    with open(filepath, 'r') as file:
        hex_data = file.read().replace('\n', '')
        byte_data = bytes.fromhex(hex_data)
    return byte_data

def decrypt(ctext, key):
    ptext = bytearray()
    for i in range(len(ctext)):
        ptext.append(ctext[i] ^ key[i % len(key)])
    return ptext

if __name__ == '__main__':
    main()