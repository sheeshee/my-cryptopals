from codecs import encode, decode

target_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
byte_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hex_to_base64(message):
    """ Converts a message in bytes (hex) to a base64 string """
    base64 = encode(decode(message, 'hex'), 'base64').decode()
    return base64

