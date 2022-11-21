from itertools import cycle


class Alphabet:
    alphabets = {
        "EN": "abcdefghijklmnopqrstuvwxyz",
        "RU": "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
        }
    alphabet = alphabets["EN"]

    @classmethod
    def set_alphabet(cls, language):
        cls.alphabet = cls.alphabets[language]
        return cls.alphabet

    @classmethod
    def add_alphabet(cls, language, alphabet_string):
        cls.alphabets[language] = alphabet_string


def encode(cipher_algorithm, *args):
    return cipher_algorithm(*args, encrypt=True)


def decode(cipher_algorithm, *args):
    return cipher_algorithm(*args, encrypt=False)


def viginere(text: str,
             key: str,
             alphabet: str = "EN",
             encrypt: bool = True,
             ROT: int = 0,
             ) -> str:
    """
    --- Return encrypted or decrtypted text ---

    text
        text to encrypte / decrypte

    key
        keyword used for encryption / decryption

    alphabet
        alphabet that is used for origin message, in any language You want

    encrypt
        True (default) - to encrypt
        False - to decrypt

    ROT
        default ROT equals to zero, means no ROT.
        ROT (from rotate) it's a shift for Caesar cipher has range from 0
        to alphabet_length, defines how will letter be rotated by (shifted).
        For Viginere cipher it's matter when key's letter equals the first
        letter in given alphabet.
        For example if we used English alphabet and our keyword='ace'
        and ROT=0 for text='annalist', we would get 'AprAnmSv', which null,
        third and sixth letters ['A', 'A', 'S'] are the same as original,
        because we defines no ROT and our key_letter equals 'a'
        for every three iteration of given keyword.
    """
    alphabet = Alphabet.set_alphabet(alphabet)
    len_alphabet = len(alphabet)
    multiplier = 1 if encrypt else -1
    text = text.lower()
    key_letter = cycle(key)
    result = []

    for letter in text:

        if letter in alphabet:
            key_index = alphabet.index(next(key_letter)) + ROT % len_alphabet
            letter_index = alphabet.index(letter)
            decrypted_index = ((letter_index + multiplier * key_index)
                               % len_alphabet)

            result.append(alphabet[decrypted_index])
        else:
            result.append(letter)

    encrypted_or_decrypted_text = "".join(result)
    return encrypted_or_decrypted_text
