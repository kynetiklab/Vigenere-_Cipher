#Vigenere Cipher

def vigenere_encode(message, keyword):
    """
    This function encodes a message using the Vigenère Cipher.
    Parameters:
        message (str): The message to be encoded.
        keyword (str): The keyword used for encoding.
    Returns:
        coded_message (str): The encoded message.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    coded_message = ""
    keyword_length = len(keyword)
    for i, char in enumerate(message):
        if char.isalpha():
            char_index = alphabet.index(char.lower())
            keyword_char = keyword[i % keyword_length]
            keyword_char_index = alphabet.index(keyword_char)
            shift = (char_index + keyword_char_index) % 26
            coded_char = alphabet[shift]
            coded_message += coded_char.upper() if char.isupper() else coded_char
        else:
            coded_message += char
    return coded_message

message = "we'll have dinner at your place tonight!?"
keyword = "python"
coded_message = vigenere_encode(message, keyword)
print(coded_message)


#Vigenere Decipher

def vigenere_decode(coded_message, keyword):
    """
    This function decodes a message that has been encoded with the Vigenère Cipher.
    Parameters:
        coded_message (str): The message to be decoded.
        keyword (str): The keyword used to encode the message.
    Returns:
        decoded_message (str): The decoded message.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ""
    keyword_length = len(keyword)
    for i, char in enumerate(coded_message):
        if char.isalpha():
            char_index = alphabet.index(char.lower())
            keyword_char = keyword[i % keyword_length]
            keyword_char_index = alphabet.index(keyword_char)
            shift = (char_index - keyword_char_index) % 26
            decoded_char = alphabet[shift]
            decoded_message += decoded_char.upper() if char.isupper() else decoded_char
        else:
            decoded_message += char
    return decoded_message

coded_message = "lc'sz wyol qxlglf pr fchg isopt mvbvvfm!?"
keyword = "python"
decoded_message = vigenere_decode(coded_message, keyword)
print(decoded_message)
