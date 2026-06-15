import heapq
from collections import Counter

# Huffman Node
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# Build Huffman Tree
def build_tree(text):
    freq = Counter(text)
    heap = [Node(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]

# Generate Codes
def generate_codes(node, current="", codes=None):
    if codes is None:
        codes = {}

    if node is None:
        return codes

    if node.char is not None:
        codes[node.char] = current

    generate_codes(node.left, current + "0", codes)
    generate_codes(node.right, current + "1", codes)

    return codes

# Huffman Encoding
def huffman_encode(text):
    tree = build_tree(text)
    codes = generate_codes(tree)

    encoded = ''.join(codes[ch] for ch in text)

    return encoded, codes

# Read CSV
with open("data.csv", "r", encoding="utf-8") as f:
    text = f.read()

encoded, codes = huffman_encode(text)

print("Original Data:")
print(text)

print("\nHuffman Codes:")
for k, v in sorted(codes.items()):
    print(repr(k), ":", v)

print("\nEncoded Data:")
print(encoded)

# Compression Ratio
original_bits = len(text) * 8
compressed_bits = len(encoded)

print("\nOriginal bits:", original_bits)
print("Compressed bits:", compressed_bits)
print("Compression Ratio:", round(original_bits / compressed_bits, 2))