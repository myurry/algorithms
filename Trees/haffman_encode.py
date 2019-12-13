### Read contraindicated ###
class Node:
    '''A node'''
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
        self.next = None

    def __add__(self, other):
        value = self.value + other.value
        letters = (other.letter, self.letter)
        return Node(letters, value)

    @classmethod
    def min(self, nodes):
        min_index = 0
        for i in range(1, len(nodes)):
            if nodes[i].value < nodes[min_index].value :
                min_index = i
        return min_index

### some variables I need ###
string = "A little example of how it works" # string to encode
chipher = {}     # dict {letter: count, ...}
lcd = {}         # dict {letter: binary, ...}

### building chipher, nodes
for letter in string:
    chipher.setdefault(letter, 0)
    chipher[letter] += 1
nodes = [Node(*x) for x in sorted(chipher.items(), key=lambda kv: (kv[1], kv[0]))]  # [Node(*(letter, count)), ...]

### Here I assembled the peaks
while len(nodes) > 2:
    nodes.append(nodes.pop(Node.min(nodes)) + nodes.pop(Node.min(nodes)))

### Func to encode the result, uses LetterCodeDictionary
def encode(node, key = ''):
    if type(node) != str:
        for i in range(len(node)):
            encode(node[i], key+str(i))
    else:
        lcd[node] = key

### ENCODING ###
for i in range(len(nodes)):
    encode(nodes[i].letter, key=str(i))

# a pair of tests
# print([wage.letter for wage in wages])
# print(sorted(lcd.items(), key=lambda x:len(x[1])))

### end phase ###
phrase = ''.join([lcd[letter] for letter in string])
print(f'{len(lcd)} letters, {len(phrase)} symbols')
for letter, value in lcd.items():
    print(f'{letter}: {value}')
print(f'Encoded string: {phrase}')

### Thanks ###
