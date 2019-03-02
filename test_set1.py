import challenge1
import challenge2

def test_challenge1():
    """ Tests the byte to text conversion """
    byte_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    target_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    converted_string = challenge1.hex_to_base64(byte_string)
    assert(target_string == converted_string)


def test_challenge2():
    """ Test the fix XOR metho for two equal-length buffers """
    target_string = "746865206b696420646f6e277420706c6179"
    input1 = "1c0111001f010100061a024b53535009181c"
    input2 = "686974207468652062756c6c277320657965"
    xord = challenge2.string_xor(input1, input2)
    assert(target_string == xord)
