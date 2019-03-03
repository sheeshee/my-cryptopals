import challenge1
import challenge2
import challenge3

import challenge5

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

def test_challenge3():
    """ Test to decode a message xord against a single character """
    coded_text = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    decoded_text = "Cooking MC's like a pound of bacon"
    mydecode = challenge3.single_xor_decode(coded_text)['text']
    assert(mydecode == decoded_text)

def test_challenge4():
    print('NO TEST FOR CHALLENGE 4')


def test_challenge5():
    """ Test for xor encryption """
    key = 'ICE'
    message = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    target = """0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"""
    my_encryption = challenge5.encrypter(message, key)
    assert(target == my_encryption)