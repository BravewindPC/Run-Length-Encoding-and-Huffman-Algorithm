# Smaller file size but doesnt accept number value
# Encode
def rle_encode(text):
    if not text:
        return ""

    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result += text[i-1] + str(count)
            count = 1

    result += text[-1] + str(count)

    return result

# Decode
def rle_decode(data):
    result = ""
    i = 0

    while i < len(data):
        char = data[i]
        i += 1

        count = ""
        while i < len(data) and data[i].isdigit():
            count += data[i]
            i += 1

        result += char * int(count)

    return result

# # Encode and Decode V2: Accept number value but higher compressed size
# def rle_encode(text):
#     if not text:
#         return ""

#     encoded = []
#     count = 1

#     for i in range(1, len(text)):
#         if text[i] == text[i-1]:
#             count += 1
#         else:
#             encoded.append(f"{count}:{text[i-1]}")
#             count = 1

#     encoded.append(f"{count}:{text[-1]}")

#     return "|".join(encoded)

# def rle_decode(encoded):
#     decoded = ""

#     for item in encoded.split("|"):
#         count, char = item.split(":", 1)
#         decoded += char * int(count)

#     return decoded


# Read CSV
filename = input("Insert File Name: ")
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

print("Original:")
print(text)

# Encode
encoded = rle_encode(text)

print("\nEncoded:")
print(encoded)

# Decode
decoded = rle_decode(encoded)

print("\nDecoded:")
print(decoded)

# Verify
print("\nVerification:")
print(text == decoded)

# Compression Ratio
original_size = len(text)
compressed_size = len(encoded)

print("\nOriginal characters:", original_size)
print("Compressed characters:", compressed_size)
print("Compression ratio:", round(original_size / compressed_size, 2))