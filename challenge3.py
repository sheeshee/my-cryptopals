from challenge1 import hex_to_bytes


def single_xor_decode_from_string(message):
    """ Applies xor between a single char and a series of chars """
    byte_array = hex_to_bytes(message)
    return single_xor_decode(byte_array)


def single_xor_decode(byte_array):
    collection = {}
    for ref in [i for i in range(255)]:
        decoded = ''.join([chr(ref ^ element) for element in byte_array])
        collection[ref] = {
            'text': decoded,
            'score': score(decoded)[0],
            'key': ref
        }
    rank = sorted(collection, key=lambda x: collection[x]['score'])[::-1]
    return collection[rank[0]]

def score(message):
    """ returns an array of counted letters according to "ETAOIN SHRDLU" """
    message = message.upper()
    common_chars = "ETAOIN SHRDLU"
    score = {}
    total_score = 0
    for weight, char in enumerate(common_chars[::-1]):
        score[char] = message.count(char) * (weight + 1)
        total_score += score[char]
    return total_score, score

