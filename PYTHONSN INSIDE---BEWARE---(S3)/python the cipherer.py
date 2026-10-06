# Python the cipherer


def shift_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using a shift cipher.

    :param text: The input string to encrypt or decrypt.
    :param shift: The number of positions to shift (can be negative).
    :param mode: 'encrypt' or 'decrypt'.
    :return: The transformed string.
    """
    if not isinstance(text, str):
        raise ValueError("Text must be a string.")
    if not isinstance(shift, int):
        raise ValueError("Shift must be an integer.")
    if mode not in ('encrypt', 'decrypt'):
        raise ValueError("Mode must be 'encrypt' or 'decrypt'.")

    # Normalize shift to range 0–25
    shift = shift % 26
    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around alphabet
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
        else:
            # Keep non-alphabetic characters unchanged
            result.append(char)

    return ''.join(result)


# Example usage
if __name__ == "__main__":
    try:
        message = input("Enter your message: ")
        shift_value = int(input("Enter shift value (integer): "))
        mode_choice = input("Enter mode (encrypt/decrypt): ").strip().lower()

        output = shift_cipher(message, shift_value, mode_choice)
        print(f"Result: {output}")

    except ValueError as e:
        print(f"Error: {e}")
