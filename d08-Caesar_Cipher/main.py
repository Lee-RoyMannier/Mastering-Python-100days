alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Demander a l'utilsateur le mode
# Si encrypter -> decale le mot de x vers la droite
# Si décripter -> décale le mot de x vers al gauche


def caesar_cipher(word, shift, mode="encode"):
    new_word = ""
    for c in word:
        index_char = "".join(alphabet).find(c)
        if index_char == -1:
            new_word += c
        else:
            if mode == "encode":
                shift_alphabet = (index_char+shift) % len(alphabet)
            elif mode == "decode":
                shift_alphabet = (index_char-shift) % len(alphabet)
            new_word += alphabet[shift_alphabet]

    return new_word


word = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))
mode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
resultat = caesar_cipher(word, shift, mode=mode)
print(resultat)
