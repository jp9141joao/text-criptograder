import os
import random

# Function to encrypt a message according to the chosen security level
def Encrypt(phrase, level):
    """
    Encrypts the given phrase by applying a character-substitution cipher
    multiple times based on the chosen level.
    - level 1: single round of substitution
    - level 2: two rounds of substitution
    - level 3: three rounds of substitution
    The “animation” part simulates the encryption process by displaying
    random characters until the correct one appears, for each character in the final cipher text.
    """
    # Level 1: Single round of substitution
    if level == 1:
        os.system('cls')                 # Clear console (Windows)
        phrase = phrase.upper()          # Convert input to uppercase for consistent mapping

        # Define the mapping strings:
        # - Alphabet: all possible characters we might encounter in the input
        # - Cipher1 and Cipher2: two ciphertext alphabets; each plaintext character maps to two ciphertext characters
        Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Cipher1  = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Cipher2  = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'

        result = ''      # Will hold the full ciphertext after substitution
        layout = ''      # Used during “animation” to show building cipher text character by character
        status = 'Encrypting'  # Status message that displays progress dots

        size = len(phrase)    # Number of characters in the original phrase

        # Build the ciphertext by substituting each character in the phrase
        for i in range(size):
            # Find the index of the current character in Alphabet
            j = Alphabet.find(phrase[i])
            # Append the corresponding two ciphertext characters from Cipher1 and Cipher2
            result += f'{Cipher1[j]}{Cipher2[j]}'

        size = len(result)   # Now size refers to the length of the final ciphertext

        # “Animation” loop: for each ciphertext character, display random chars until the correct one appears
        for i in range(size):
            while True:
                crt = random.choice(Cipher1)      # Pick a random character from Cipher1
                layout_x = layout + crt           # Append this random char to current layout
                status += '.'                     # Add a dot to the status message
                print(f'    {status}\n    {layout_x}')
                os.system('cls')                  # Clear console to simulate live progress

                # Reset the status string length back to “Encrypting” if it gets too long
                if len(status) == 19:
                    status = 'Encrypting'

                # If the randomly chosen char matches the actual ciphertext char, accept it
                if crt == result[i]:
                    layout += crt   # Append the correct character to layout permanently
                    break           # Move on to the next character in the ciphertext

    # Level 2: Two rounds of substitution (apply the same mapping twice)
    elif level == 2:
        os.system('cls')
        phrase = phrase.upper()

        Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Cipher1  = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Cipher2  = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'

        result = ''
        layout = ''
        status = 'Encrypting'

        size = len(phrase)

        # First round: build an intermediate ciphertext
        for i in range(size):
            j = Alphabet.find(phrase[i])
            result += f'{Cipher1[j]}{Cipher2[j]}'

        # Prepare for second round by treating the intermediate ciphertext as new input
        phrase = result
        result = ''
        size = len(phrase)

        # Second round: substitute each character of the intermediate ciphertext again
        for i in range(size):
            j = Alphabet.find(phrase[i])
            result += f'{Cipher1[j]}{Cipher2[j]}'

        size = len(result)

        # Same animation as before, but now building the twice-encrypted final text
        for i in range(size):
            while True:
                crt = random.choice(Cipher1)
                layout_x = layout + crt
                status += '.'
                print(f'    {status}\n    {layout_x}')
                os.system('cls')
                if len(status) == 19:
                    status = 'Encrypting'
                if crt == result[i]:
                    layout += crt
                    break

    # Level 3: Three rounds of substitution (apply the mapping three times)
    elif level == 3:
        os.system('cls')
        phrase = phrase.upper()

        Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Cipher1  = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Cipher2  = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'

        result = ''
        layout = ''
        status = 'Encrypting'

        size = len(phrase)

        # First substitution round
        for i in range(size):
            j = Alphabet.find(phrase[i])
            result += f'{Cipher1[j]}{Cipher2[j]}'

        # Prepare for second round
        phrase = result
        result = ''
        size = len(phrase)

        # Second substitution round
        for i in range(size):
            j = Alphabet.find(phrase[i])
            result += f'{Cipher1[j]}{Cipher2[j]}'

        # Prepare for third round
        phrase = result
        result = ''
        size = len(phrase)

        # Third substitution round
        for i in range(size):
            j = Alphabet.find(phrase[i])
            result += f'{Cipher1[j]}{Cipher2[j]}'

        size = len(result)

        # Animation to build the three-times-encrypted final text
        for i in range(size):
            while True:
                crt = random.choice(Cipher1)
                layout_x = layout + crt
                status += '.'
                print(f'    {status}\n    {layout_x}')
                os.system('cls')
                if len(status) == 19:
                    status = 'Encrypting'
                if crt == result[i]:
                    layout += crt
                    break

    else:
        # If the level is not 1, 2, or 3, it’s invalid
        print('Invalid Option!')
        return

    # After encryption is done, clear screen and display the final ciphertext
    os.system('cls')
    print(f'Encrypted message successfully!\nYour encrypted phrase is "{result}"')

    # Ask user whether to go back to the main menu or exit
    continue_ = int(input('Do you want to continue?\n1- Yes\n2- No\nR: '))
    return (continue_ == 1)


# Function to decrypt a message according to the chosen security level
def Decrypt(phrase, level):
    """
    Reverses the encryption process:
    - level 1: single round reverse (take every even-indexed character and map back)
    - level 2: reverse two rounds (apply reverse logic twice)
    - level 3: reverse three rounds (apply reverse logic three times)
    Uses the same “animation” to simulate decryption progress.
    """
    # Level 1: Reverse one round of substitution
    if level == 1:
        phrase = phrase.upper()
        Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Cipher1  = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Cipher2  = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'

        result = ''
        layout = ''
        status = 'Decrypting'

        size = len(phrase)

        # Each plaintext character in the original was mapped to 2 ciphertext chars
        # We extract every even-indexed character of the ciphertext (which came from Cipher1)
        for i in range(size):
            if i % 2 == 0:
                j = Cipher1.find(phrase[i])    # Find index in Cipher1
                result += f'{Alphabet[j]}'      # Map back to the alphabet

        size = len(result)

        # Animation: display random letters until the correct one appears for each character
        for i in range(size):
            while True:
                crt = random.choice(Alphabet)
                layout_x = layout + crt
                status += '.'
                print(f'    {status}\n    {layout_x}')
                os.system('cls')
                if len(status) == 19:
                    status = 'Decrypting'
                if crt == result[i]:
                    layout += crt
                    break

        # Finally, show the decrypted phrase
        os.system('cls')
        print(f'Encrypted message successfully!\nYour decrypted phrase is "{result}"')

    # Level 2: Reverse two rounds of substitution (apply the above logic twice)
    elif level == 2:
        phrase = phrase.upper()
        Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Cipher1  = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Cipher2  = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'

        result = ''
        layout = ''
        status = 'Decrypting'

        size = len(phrase)

        # First reverse pass: take every even-indexed char and map back
        for i in range(size):
            if i % 2 == 0:
                j = Cipher1.find(phrase[i])
                result += f'{Alphabet[j]}'

        # Prepare for second reverse pass
        phrase = result
        result = ''
        size = len(phrase)

        # Second reverse pass: again, take every even-indexed char from the intermediate result
        for i in range(size):
            if i % 2 == 0:
                j = Cipher1.find(phrase[i])
                result += f'{Alphabet[j]}'

        size = len(result)

        # Animation to show decryption progress
        for i in range(size):
            while True:
                crt = random.choice(Alphabet)
                layout_x = layout + crt
                status += '.'
                print(f'    {status}\n    {layout_x}')
                os.system('cls')
                if len(status) == 19:
                    status = 'Decrypting'
                if crt == result[i]:
                    layout += crt
                    break

        os.system('cls')
        print(f'Encrypted message successfully!\nYour decrypted phrase is "{result}"')

    # Level 3: Reverse three rounds (apply reverse logic three times)
    elif level == 3:
        phrase = phrase.upper()
        Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"}{[]_+-/,;?. 1234567890:<>ÇÂÃÁÀÒÓÔÍÌÙÚÈÉÊ'
        Cipher1  = 'Z$K8GDV7ÂY]HN5{PÈ?SÒQUÌ4"<ÍJ&Ê!6}_3RÁWBÓ )TÙ2OÇ>EC+À;[#-1F9XM%Ú0IÔ:Ã(,*ÉLA@^/.'
        Cipher2  = '&]R!J7F#_6.}@5 ÚHÇ<{PÊ(/%É1À+Ó^SÌYÂ,T8U>"Q2?ÃMZ9ÈXK*G0:ÙÔIC3OANVE[Á4ÒWB;D$-L)Í'

        result = ''
        layout = ''
        status = 'Decrypting'

        size = len(phrase)

        # First reverse pass
        for i in range(size):
            if i % 2 == 0:
                j = Cipher1.find(phrase[i])
                result += f'{Alphabet[j]}'

        # Prepare for second reverse pass
        phrase = result
        result = ''
        size = len(phrase)

        # Second reverse pass
        for i in range(size):
            if i % 2 == 0:
                j = Cipher1.find(phrase[i])
                result += f'{Alphabet[j]}'

        # Prepare for third reverse pass
        phrase = result
        result = ''
        size = len(phrase)

        # Third reverse pass
        for i in range(size):
            if i % 2 == 0:
                j = Cipher1.find(phrase[i])
                result += f'{Alphabet[j]}'

        size = len(result)

        # Animation for decryption
        for i in range(size):
            while True:
                crt = random.choice(Alphabet)
                layout_x = layout + crt
                status += '.'
                print(f'    {status}\n    {layout_x}')
                os.system('cls')
                if len(status) == 19:
                    status = 'Decrypting'
                if crt == result[i]:
                    layout += crt
                    break

        os.system('cls')
        print(f'Encrypted message successfully!\nYour decrypted phrase is "{result}"')

    else:
        print('Invalid Option!')
        return

    # Ask the user if they want to continue or exit
    continue_ = int(input('Do you want to continue?\n1- Yes\n2- No\nR: '))
    return (continue_ == 1)


# Main loop: display the menu and call the appropriate function
while True:
    os.system('cls')
    option = int(input('* Option Menu *\n1- Encrypt\n2- Decrypt\n3- Exit\nR: '))

    if option == 3:
        # Exit the program
        print('Program Terminated!')
        break

    elif option == 1:
        # Encrypt flow
        os.system('cls')
        level = int(input('Select Encryption Level:\n1- Amateur\n2- Medium\n3- Military\nR: '))
        phrase = str(input('Enter the phrase to encrypt: '))
        if Encrypt(phrase, level) == False:
            # If user chose not to continue, terminate
            print('Program Terminated!')
            break

    elif option == 2:
        # Decrypt flow
        os.system('cls')
        level = int(input('Select Encryption Level of the phrase:\n1- Amateur\n2- Medium\n3- Military\nR: '))
        phrase = str(input('Enter the phrase to decrypt: '))
        if Decrypt(phrase, level) == False:
            # If user chose not to continue, terminate
            print('Program Terminated!')
            break

    else:
        # Invalid menu choice
        print('Invalid Option')
