import challenge1

def test_hex_to_base64():
    """ Tests the byte to text conversion """
    byte_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    target_string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    converted_string = challenge1.hex_to_base64(byte_string)
    assert(target_string == converted_string)
