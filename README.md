# XOR Cipher Implementation

This repository contains an implementation of a repeating-key XOR cipher with both encryption and cryptanalysis capabilities. The system includes functionality for decrypting ciphertext using frequency analysis.

## Files Overview

- `plaintext.py`: Simple decryption script using a known key
- `cse108_hw2_asharkaw.py`: Advanced cryptanalysis script using frequency analysis
- `cipher.txt`: Input ciphertext file (hex-encoded)
- `key.txt`: Sample encryption key file
- `decrypted.txt`: Output of decryption attempt

## How It Works

### Basic Decryption (`plaintext.py`)
If you have the correct key, you can use the simple decryption script which:
1. Reads hex-encoded ciphertext from `cipher.txt`
2. XORs each byte with the corresponding byte from the repeating key
3. Outputs the decrypted ASCII text

### Cryptanalysis (`cse108_hw2_asharkaw.py`)
The cryptanalysis script attempts to break the cipher without knowing the key by:
1. Determining the likely key length using frequency analysis
2. Breaking the ciphertext into streams based on the key length
3. Analyzing each stream using English letter frequencies
4. Reconstructing the key by finding the most likely byte for each position

## Setup and Usage

1. Clone the repository and ensure you have Python 3.x installed.

2. To use the basic decryption (with known key):
```bash
python plaintext.py
```

3. To attempt cryptanalysis (without knowing the key):
```bash
python cse108_hw2_asharkaw.py
```

## Input Format

- The ciphertext should be stored in `cipher.txt` as hex-encoded text
- One line per input, no spaces
- Example format: `F94720DC5BD9F775FD74C14661D60FD7...`

## Implementation Details

### Key Features
- XOR-based encryption/decryption
- Key length detection using index of coincidence
- English letter frequency analysis
- Printable ASCII validation
- Stream separation for cryptanalysis

### Frequency Analysis
The script uses standard English letter frequencies:
```python
'a': 0.082, 'b': 0.015, 'c': 0.028, ...
```

These frequencies are used to score potential decryptions and identify the most likely key bytes.

## Security Considerations

This implementation is for educational purposes. Some important notes:
- XOR ciphers with repeating keys are vulnerable to frequency analysis
- The implementation assumes ASCII encoding and English plaintext
- No padding or additional security measures are implemented

## Error Handling

The scripts include basic error handling for:
- File I/O operations
- Hex decoding
- Character encoding issues

## Dependencies
- Python 3.x
- No external libraries required

## Contributing
When adding features or fixes:
1. Maintain the existing error handling patterns
2. Document any new frequency analysis approaches
3. Update the test files if modifying the core logic
