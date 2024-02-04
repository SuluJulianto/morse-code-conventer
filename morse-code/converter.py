class MorseCodeConverter:
    def __init__(self):
        self.morse_code_dict = {
            'A': '._',    # A
            'B': '_...',  # B
            'C': '_._.',  # C
            'D': '_..',   # D
            'E': '.',     # E
            'F': '.._.',  # F
            'G': '__.',   # G
            'H': '....',  # H
            'I': '..',    # I
            'J': '.___',  # J
            'K': '_._',   # K
            'L': '._..',  # L
            'M': '__',    # M
            'N': '_.',    # N
            'O': '___',   # O
            'P': '.__.',  # P
            'Q': '__._',  # Q
            'R': '._.',   # R
            'S': '...',   # S
            'T': '_',     # T
            'U': '.._',   # U
            'V': '..._',  # V
            'W': '.__',   # W
            'X': '_.._',  # X
            'Y': '_.__',  # Y
            'Z': '__..',  # Z
            ' ': '_______________'  # Space
        }

        self.reverse_morse_code_dict = {v: k for k, v in self.morse_code_dict.items()}

    def convert_to_morse(self, text):
        morse_result = '\n'.join([self.morse_code_dict.get(char.upper(), '______') for char in text])
        return morse_result

    def convert_to_text(self, morse_code):
        text_result = ''.join([self.reverse_morse_code_dict.get(code, ' ') for code in morse_code.split('\n')])
        return text_result


if __name__ == "__main__":
    # Create an instance of MorseCodeConverter
    converter = MorseCodeConverter()

    # User input
    name_input = input("Enter your name: ")

    # Perform Morse code conversion
    morse_code_result = converter.convert_to_morse(name_input)

    # Display the result
    print('Your name in Morse code is:')
    print(morse_code_result)

    # Perform reverse conversion
    text_result = converter.convert_to_text(morse_code_result)
    print('Back to text:')
    print(text_result)
