ALPHABET = {'A': '.-',     'B': '-...',   'C': '-.-.',
            'D': '-..',    'E': '.',      'F': '..-.',
            'G': '--.',    'H': '....',   'I': '..',
            'J': '.---',   'K': '-.-',    'L': '.-..',
            'M': '--',     'N': '-.',     'O': '---',
            'P': '.--.',   'Q': '--.-',   'R': '.-.',
            'S': '...',    'T': '-',      'U': '..-',
            'V': '...-',   'W': '.--',    'X': '-..-',
            'Y': '-.--',   'Z': '--..',   'Å': '.--.-',
            'Ä': '.-.-',   'Ö': '---.',

            '0': '-----',  '1': '.----',  '2': '..---',
            '3': '...--',  '4': '....-',  '5': '.....',
            '6': '-....',  '7': '--...',  '8': '---..',
            '9': '----.',

            ' ': '/'}

REVERSE_ALPHABET = dict([(value, key) for key, value in ALPHABET.items()])


def to_morse(text):
    """Convert text to morse code."""
    return ' '.join([ALPHABET[c.upper()] for c in text if c.upper() in ALPHABET])


def from_morse(morse):
    """Convert morse code to text."""
    return ''.join([REVERSE_ALPHABET[c] for c in morse.split(' ') if c in REVERSE_ALPHABET])
