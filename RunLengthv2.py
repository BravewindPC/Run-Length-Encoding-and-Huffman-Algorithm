import csv

# Encode
def rle_encode(seq):
    if not seq:
        return []

    encoded = []
    current = seq[0]
    count = 1

    for item in seq[1:]:
        if item == current:
            count += 1
        else:
            encoded.append((current, count))
            current = item
            count = 1
    encoded.append((current, count))
    return encoded

# Decode
def rle_decode(encoded):
    decoded = []

    for value, count in encoded:
        decoded.extend([value] * count)

    return decoded

# Read CSV
filename = input("Masukan nama file: ")

with open(filename, "r") as f:
    text = f.read()

with open(filename, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    data = list(reader)

print("Columns:", header)

# Process each column

total_ratio = 0
total_original_size = 0
total_compressed_size = 0

for col in range(len(header)):

    original = [row[col] for row in data]

    encoded = rle_encode(original)

    decoded = rle_decode(encoded)

    print("\nColumn:", header[col])
    print("Original:")
    print(original[:10])

    print("Encoded:")
    print(encoded[:10])

    print("Decoded:")
    print(decoded[:10])

    print("\nVerification:")
    print(original == decoded)

    header_str = ",".join(header) + "\n"
    total_compressed_size += len(header_str.encode("utf-8"))
    for value, count in encoded:
        total_compressed_size += len(f"{value},{count}\n")

print("\nOriginal:", len(text))
print("Compressed:", total_compressed_size)

print("\nCompression Ratio:", round(len(text) / total_compressed_size, 2))