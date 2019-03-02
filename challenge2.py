from challenge1 import hex_to_bytes, bytes_to_hex
from codecs import decode, encode

def string_xor(hex_1, hex_2):
    """ Takes two equal-length buffers and produces their XOR combination """
    if len(hex_1) != len(hex_2):
        raise "The hex strings are different lengths!"
    byte_1 = hex_to_bytes(hex_1)
    byte_2 = hex_to_bytes(hex_2)
    xord = [0 for i in range(len(byte_1))]
    for i, _ in enumerate(byte_1):
        xord[i] = byte_1[i] ^ byte_2[i]
    new_bytes = ''.join(['{0:x}'.format(b) for b in xord])
    return new_bytes