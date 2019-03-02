from codecs import encode, decode

target_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
byte_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hex_to_base64(hex_message):
    """ Converts a message in bytes (hex) to a base64 string """
    bytes_message = hex_to_bytes(hex_message)
    base64_message = bytes_to_base64(bytes_message)
    return base64_message.decode()[:-1]

def hex_to_bytes(message):
    """ Converts a message in hex into bytes """
    byte_message = decode(message, 'hex')
    return byte_message

def bytes_to_hex(message):
    """ Converts a bytes messages into hex """
    return encode(message, 'hex')

def bytes_to_base64(message):
    """ Converts a byte string into a hex string """
    base64_message = encode(message, 'base64')
    return base64_message

