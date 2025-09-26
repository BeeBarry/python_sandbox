
alphabet = {
    'A': 'Alpha',     'B': 'Bravo',     'C': 'Charlie',   'D': 'Delta',
    'E': 'Echo',      'F': 'Foxtrot',   'G': 'Golf',      'H': 'Hotel',
    'I': 'Indigo',    'J': 'Juliet',    'K': 'Kilo',      'L': 'Lima',
    'M': 'Mobile',    'N': 'New York',  'O': 'Oscar',     'P': 'Papa',
    'Q': 'Queen',     'R': 'Romeo',     'S': 'Sierra',    'T': 'Tango',
    'U': 'Uniform',   'V': 'Victor',    'W': 'Whiskey',   'X': 'X-ray',
    'Y': 'Yankee',    'Z': 'Zulu'
}

while True:
    l = input('Write a letter in the alphabet (or "quit" to exit):  ')

    if l.lower() == 'quit':
        print('\nTerminal shutting down. See you again :) ')
        break

    result = alphabet.get(l.upper())

    if result:
        print(l.upper(),result, sep=' = ')
    else:
        print(f'"{l}" is not a valid letter, please try again.')
