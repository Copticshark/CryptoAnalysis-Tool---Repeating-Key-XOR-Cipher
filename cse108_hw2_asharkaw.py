#!/usr/bin/env python3
import itertools

cpath = 'cipher.txt'


def main():
    frequencies = [0] * 256
    sum = 0
    highestSum = 0
    keyLength = 1
    key = bytes([0, 0]) # Change

    ctext = read_hex_file(cpath)
    ptext = decrypt(ctext, key)
    print(f"ptext {ptext}")
    print(f"ctext {ctext}")
    print(f"is ptext = ctext {ptext == ctext}")

    for l in range(1,15):
        for start in range(l):
            frequencies = [0] * 256
            sum = 0
            for ch in ptext[start::l]:
                frequencies[ch] += 1
            for frequency in frequencies:
                sum += (frequency/(len(ptext)/l))**2
            if sum > highestSum:
                highestSum = sum
                keyLength = l

    q = [0] * 256
    q[97] = 0.082
    q[98] = 0.015
    q[99] = 0.028
    q[100] = 0.043
    q[101] = 0.13
    q[102] = 0.022
    q[103] = 0.02
    q[104] = 0.061
    q[105] = 0.07
    q[106] = 0.0015
    q[107] = 0.0077
    q[108] = 0.04
    q[109] = 0.024
    q[110] = 0.067
    q[111] = 0.075
    q[112] = 0.019
    q[113] = 0.00095
    q[114] = 0.06
    q[115] = 0.063
    q[116] = 0.091
    q[117] = 0.028
    q[118] = 0.0098
    q[119] = 0.024
    q[120] = 0.0015
    q[121] = 0.02
    q[122] = 0.0074

    streams = []
    for _ in range(keyLength):
        streams.append([])
    
    for i, byte in enumerate(ptext):
        streams[i%keyLength].append(byte)

    print(f"streamlength {[len(s) for s in streams]}")

    def computeSumFrequency(decodedStream):
        frequencies = [0] * 256
        sum = 0
        for ch in decodedStream:
            frequencies[ch] += 1
        for i in range(97, 123):
            sum += (frequencies[i]/len(decodedStream))*q[i]

        return sum


    def bestByte(stream):
        decodedStreams = []
        for b in range(256):
            decodedStream = []
            for ch in stream:
                decodedStream.append(ch ^ b)
            decodedStreams.append([b, decodedStream])

        printableDecodedStreams = [s for s in decodedStreams if allPrintable(s[1])]  
        scores = [s+[computeSumFrequency(s[1])] for s in printableDecodedStreams]
        if len(scores) == 0:
            print(f"decoded stream {byteToString(decodedStream[0])}")
            print(f"all Printable {allPrintable(decodedStreams[0][1])}")
            return 0
        maxScores =  max(scores, key=lambda s: s[2])
        print(f"maxScores {maxScores}")
        print(f"string {byteToString(maxScores[1])}")
        return maxScores[0]
    
    secretKey = [bestByte(s) for s in streams]
    print(f"secretKey {secretKey}")
    print(secretKey)
    


def byteToString(a) :
    return bytes(a).decode('ascii')


def allPrintable(decodedStream):
    try: 
        s = byteToString(decodedStream)
        return True
    except:
        return False

def read_hex_file(fpath):
    with open(fpath, mode='rt', encoding='ascii') as f:
        return bytes.fromhex(f.read().strip())


def decrypt(data, key):
    return bytes([p ^ k for (p, k) in zip(data, itertools.cycle(key))])

if __name__ == '__main__':
    main()

