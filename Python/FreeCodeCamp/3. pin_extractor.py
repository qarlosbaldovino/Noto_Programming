def pin_extractor(poems):
    secret_codes = [] #Creamos una lista vacía
    for poem in poems: #Iteramos por poema (En este caso son tres) "Stars and the moon shine in the sky white and until the end of the night"
        secret_code = '' #Creamos una variable string vacía
        lines = poem.split('\n') #Creamos una lista separadas por el ENTER \n de los versos. ['Stars and the moon', 'shine in the sky', 'white and', 'until the end of the night']
        for line_index, line in enumerate(lines): #Hacemos una lista enumerada por cuantos versos tiene el poema [(0,'Stars and the moon'), (1,'shine in the sky'), (2,'white and'), (3,'until the end of the night')]
            words = line.split() #Acá separamos cada verso por palabras ['Stars', 'and', 'the', 'moon']['shine', 'in', 'the', 'sky']['white', 'and']['until', 'the', 'end', 'of', 'the', 'night']
            if len(words) > line_index: #Validamos si el tamaño de la palabra es mayor a la enumeración índice |Stars = 5 > 0|In = 2 > 1|"" = 0 < 2|End = 3 > 2|  
                secret_code += str(len(words[line_index])) # |5|2|0|2|
            else:
                secret_code += '0' #En la tercera iteración entra acá porque al no haber palabra su LENGTH es 0
        secret_codes.append(secret_code) #Va agregando a la lista los lenghts obtenidos
    return secret_codes
    
poem = 'Stars and the moon\nshine in the sky\nwhite and\nuntil the end of the night'
poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

poems = [poem,poem2,poem3]
print(pin_extractor(poems))