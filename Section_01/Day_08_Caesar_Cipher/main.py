# Day08_CaesarCipher.py

# Function to encode or decode text
def caesar(text, shift, direction):
    result = ""
    for char in text:
        if char.isalpha():  # Only encode letters
            shift_amount = shift % 26
            # Determine starting ASCII code
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            # Encode or decode
            if direction == "encode":
                result += chr((ord(char) - start + shift_amount) % 26 + start)
            else:
                result += chr((ord(char) - start - shift_amount) % 26 + start)
        else:
            result += char  # Keep non-letter characters the same
    return result

# User input
text = input("Enter text: ")
shift = int(input("Type shift number: "))
direction = input("Type 'encode' to encrypt, 'decode' to decrypt: ")

# Print result
print(f"Result: {caesar(text, shift, direction)}")
