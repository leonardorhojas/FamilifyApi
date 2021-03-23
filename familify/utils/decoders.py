morse = {
    " ": " ",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".\n": ".-.-.-",
}
morse_inv = dict((v, k) for (k, v) in morse.items())


def translate2Human(morse_cod):
    text_decoded = []
    list_morse = morse_cod.split(' ')
    for char_morse in list_morse:
        try:
            if char_morse != '':
                text_decoded.append(morse_inv[char_morse])
            else:
                text_decoded.append(' ')
        except:
            return Exception('error decoding unrecognized code') # TODO: properly manage exceptions
    return {'data': "".join(text_decoded)}


def translate2Morse(morse_cod):
    morse_cod = morse_cod.upper()
    text_decoded = []
    print(morse_cod)
    for char_morse in morse_cod:
        try:
            if char_morse != " ":
                text_decoded.append(morse[char_morse] + " ")
            else:
                text_decoded.append(" ")
        except:
            return Exception('error decoding unrecognized code', ) # TODO: properly manage exceptions
    return {'data': "".join(text_decoded)}


def binary_to_morse():
    pass
