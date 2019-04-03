
def string_to_byte_array(string):
    return [i for i in bytes(string, 'utf-8')]

def byte_array_to_string(bytes):
    return ''.join([chr(b) for b in bytes])


def encrypter(bytified_msg, key):
    key_length = len(key)
    bytified_key = string_to_byte_array(key)
    secret = ''
    for i, msg_byte in enumerate(bytified_msg):
        new_byte = bytified_key[i % key_length] ^ msg_byte
        secret += '{0:0{1}x}'.format(new_byte, 2)
    return secret

def encrypter_from_string(message, key):
    """ Encrypts a single line using a key """
    bytified_msg = string_to_byte_array(message)
    secret = encrypter(bytified_msg, key)
    return secret


if __name__ == "__main__":
    message = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
    key = 'ICE'

    secret = encrypter(message, key)
    print(secret)
