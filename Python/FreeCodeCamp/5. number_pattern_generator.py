def number_pattern(n):
    string_numbers = ''
    if isinstance(n,int): #Se puede usar .isdigit()
        if n > 0:
            for number in range(1,n+1):
                if number == 1:
                    string_numbers = str(number)
                else:
                    string_numbers += f" {number}"
            
            return string_numbers
        else:
            return "Argument must be an integer greater than 0"
    else:
        return "Argument must be an integer value"
    
