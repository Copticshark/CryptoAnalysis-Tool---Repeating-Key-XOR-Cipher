# Cryptanalysis Tool - Repeating Key XOR Cipher

This project implements a tool to analyze and decrypt text that has been encrypted using a repeating-key XOR cipher. It uses frequency analysis and statistical methods to determine the key length and decrypt the ciphertext.

## Files

- `cse108_hw2_asharkaw.py`: Main implementation file containing the cryptanalysis algorithm
- `plaintext.py`: A helper script to decrypt the ciphertext when the key is known
- `cipher.txt`: The encrypted text file (not shown in the provided files)
- `key.txt`: Contains encrypted or key-related data

## How It Works

1. **Key Length Detection**:
   - Uses frequency analysis to determine the most likely key length
   - Analyzes character frequencies in different offsets of the ciphertext
   - Calculates Index of Coincidence (IoC) for different key lengths

2. **Letter Frequency Analysis**:
   - Uses English letter frequencies (stored in array `q`)
   - Analyzes each position in the key separately
   - Scores possible key bytes based on resulting plaintext character frequencies

3. **Decryption Process**:
   - Splits ciphertext into streams based on key length
   - Tests each possible byte value (0-255) for each position in the key
   - Verifies that decrypted text is printable ASCII
   - Scores results based on English letter frequencies

## Usage

```bash
# To run the cryptanalysis tool
python3 cse108_hw2_asharkaw.py

# To decrypt with a known key
python3 plaintext.py
```

## Implementation Details

### Main Components

1. **Frequency Analysis**:
```python
frequencies = [0] * 256
for ch in ptext[start::l]:
    frequencies[ch] += 1
```

2. **English Letter Frequencies**:
- Stored in array `q`
- Used for scoring potential decryptions

3. **Key Finding**:
```python
def bestByte(stream):
    # Tests all possible bytes (0-255)
    # Returns the byte that produces the most likely English text
```

### Helper Functions

- `read_hex_file()`: Reads hex-encoded ciphertext
- `decrypt()`: Performs XOR decryption
- `allPrintable()`: Verifies if decrypted text is valid ASCII
- `byteToString()`: Converts byte arrays to strings

## Known Key Version

The `plaintext.py` script contains a simpler version that decrypts the text using a known key:
```python
key = bytes([0xAE, 0x22, 0x00, 0xAF, 0x2F, 0xB8, 0x99, 0x11, 0xDD, 0x00])
```

## Technical Theory

This tool breaks a repeating-key XOR cipher using:
1. Kasiski examination principles to find key length
2. Frequency analysis to determine individual key bytes
3. Statistical analysis of English text patterns
4. Validation of printable ASCII characters

The algorithm is based on the fact that English text has predictable letter frequencies, and XOR encryption with a repeating key creates patterns that can be analyzed.

Would you like me to explain any particular aspect in more detail? For example, I could dive deeper into the frequency analysis or explain how the key length detection works.
