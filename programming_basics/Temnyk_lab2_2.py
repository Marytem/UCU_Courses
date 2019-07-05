def divided_by_thirteen(number):
    number = str(number) 
    if len(number) >= 3: 
        number = int(int(number[-1]) * 4 + int(number[0 : len(number)-1]))
        return (divided_by_thirteen(number))
    else:
        if int(number) % 13 == 0:
            return True
        else:
            return False