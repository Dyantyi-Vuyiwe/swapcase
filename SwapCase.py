#Creating a fundction that swaps case 
def swapcase(text):
    '''Give a string, swap the cases of the letters:'''
    new_text = ''
    
    for char in text:
        if char == char.lower():        #turns lowercase to uppercase
            new_char = char.upper()
            new_text += new_char
        elif char == char.upper():      #turns upper into lower
            new_char = char.lower()
            new_text += new_char
    print(new_text)
swapcase('Life Is GOOD ENJOY IT!')    