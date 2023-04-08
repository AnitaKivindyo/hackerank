def is_leap(year):
    '''This function checks if the year is a leap year or not accoring to the Gregorian calendar'''
    leap = False
    if year %4 == 0:
        leap = True
        if year %100 == 0:
            leap = False
            if year %400 == 0:
                leap = True     
    return leap

year = int(input())
print(is_leap(year))

    
    
