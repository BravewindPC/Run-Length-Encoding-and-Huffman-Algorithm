import heapq
from collections import Counter

# Huffman Tree Node
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
    frequency = Counter(text)

    heap = [Node(ch, freq) for ch, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


# Generate Huffman Codes
def generate_codes(node, current="", codes=None):
    if codes is None:
        codes = {}

    if node is None:
        return codes

    if node.char is not None:
        # Handle single-character file
        codes[node.char] = current if current else "0"

    generate_codes(node.left, current + "0", codes)
    generate_codes(node.right, current + "1", codes)

    return codes


# Encode
def huffman_encode(text):
    tree = build_tree(text)
    codes = generate_codes(tree)

    encoded = "".join(codes[ch] for ch in text)

    return encoded, tree, codes


# Decode
def huffman_decode(encoded_data, tree):
    decoded = ""

    # Single-character case
    if tree.left is None and tree.right is None:
        return tree.char * len(encoded_data)

    current = tree

    for bit in encoded_data:
        if bit == "0":
            current = current.left
        else:
            current = current.right

        if current.char is not None:
            decoded += current.char
            current = tree

    return decoded


# MAIN PROGRAM

filename = input("Insert File Name: ")

with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

print("Original:")
print(text)

# Encode
encoded, tree, codes = huffman_encode(text)

print("\nHuffman Codes")
for ch in sorted(codes.keys()):
    print(repr(ch), ":", codes[ch])

print("\nEncoded:")
print(encoded)

# Decode
decoded = huffman_decode(encoded, tree)
print("\nDecoded:")
print(decoded)

# Verify
print("\nVerification:")
print(text == decoded)

# Compression Ratio
original_bits = len(text) * 8
compressed_bits = len(encoded)

print("\nCompression Analysis")
print("Original size:", original_bits, "bits")
print("Compressed size:", compressed_bits, "bits")
print("Compression ratio:", round(original_bits / compressed_bits, 2))