from challenge3 import single_xor_decode

def get_input_file():
    with open('4.txt', 'r') as f:
        raw = f.read()
    lines = raw.split('\n')
    return lines

def find_the_line(lines):
    decoded_lines = [single_xor_decode(line) for line in lines]
    max_score = 0
    loc_max = 0
    for i, entry in enumerate(decoded_lines):
        score = entry['score']
        if score > max_score:
            max_score = score
            loc_max = i
    return decoded_lines[loc_max]['text']


col = find_the_line(get_input_file())
print(col)