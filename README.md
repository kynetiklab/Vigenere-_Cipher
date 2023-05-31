# Vigenere-_Cipher
 The Vigenère Cipher is a polyalphabetic substitution cipher that provides a stronger encryption than the simple Caesar cipher. It uses a keyword or phrase to encrypt and decrypt messages.

In the Vigenère cipher, each letter of the plaintext is shifted based on the corresponding letter of the keyword. The keyword is repeated cyclically until it matches the length of the plaintext. This creates a series of Caesar ciphers with different shift values.

To decrypt a Vigenère cipher, the same keyword is used to shift each letter of the ciphertext in the reverse direction.

This repository contains a Python implementation of the Vigenère cipher algorithm. It includes functions to both encrypt and decrypt messages using the Vigenère cipher. The user can provide a message and a keyword, and the implementation will return the encrypted or decrypted message accordingly.
