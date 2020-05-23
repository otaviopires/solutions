MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}

def decodeMorse(morse_code):
    word_decoded = ''
    letters_decoded = []
    words_decoded = []
    words = morse_code.split('   ')
    for word in words:
        if word == '':
            continue
        letters = word.split(' ')
        for letter in letters:
            if letter == '':
                continue
            letters_decoded.append(MORSE_CODE[letter])
        words_decoded.append(''.join(letters_decoded))
        letters_decoded = []
    return ' '.join(words_decoded)

def cleverDecodeMorse(morse_code):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morse_code.strip().split('   '))

print(decodeMorse('.... . -.--   .--- ..- -.. .'))
print(decodeMorse('.-'))
print(decodeMorse('.'))
print(decodeMorse('..'))
print(decodeMorse('. .'))
print(decodeMorse('.   .'))
print(decodeMorse('...---...'))
print(decodeMorse('... --- ...'))
print(decodeMorse('...   ---   ...'))
print(decodeMorse(' . '))
print(decodeMorse('   .   . '))
print(decodeMorse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '))

print('\nClever way:')
print(cleverDecodeMorse('.... . -.--   .--- ..- -.. .'))
print(cleverDecodeMorse('.-'))
print(cleverDecodeMorse('.'))
print(cleverDecodeMorse('..'))
print(cleverDecodeMorse('. .'))
print(cleverDecodeMorse('.   .'))
print(cleverDecodeMorse('...---...'))
print(cleverDecodeMorse('... --- ...'))
print(cleverDecodeMorse('...   ---   ...'))
print(cleverDecodeMorse(' . '))
print(cleverDecodeMorse('   .   . '))
print(cleverDecodeMorse('      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '))