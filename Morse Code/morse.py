string = "hello"

def toMorse(text):
    morseRef = {
        'A':'.-',   'B':'-...',  'C':'-.-.', 'D':'-..',
        'E':'.',    'F':'..-.',  'G':'--.',  'H':'....',
        'I':'..',   'J':'.---',  'K':'-.-',  'L':'.-..',
        'M':'--',   'N':'-.',    'O':'---',  'P':'.--.',
        'Q':'--.-', 'R':'.-.',   'S':'...',  'T':'-',
        'U':'..-',  'V':'...-',  'W':'.--',  'X':'-..-',
        'Y':'-.--', 'Z':'--..', ' ':'.....'
    }

    decrypt = {value: key for key,value in morseRef.items()}

    if '-' in text:
        return ''.join(decrypt[i] for i in text.split())
    return ' '.join(morseRef[i] for i in text.upper())


print(toMorse('Kd and Kyrie gonna dish out the league'))
print(toMorse('-... .- ... -.- . - -... .- .-.. .-..'))
