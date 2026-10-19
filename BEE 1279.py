end_of_file = True
try:
    n = int(input())
except EOFError:
    end_of_file = False

while end_of_file:
    
    leap = False
    huluculu = False
    bulukulu = False

    if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
        leap = True
        if (n % 55 == 0):
            bulukulu = True

    if(n % 15 == 0):
        huluculu = True

    if(leap):
        print('This is leap year.')
    if(huluculu):
        print('This is huluculu festival year.')
    if(bulukulu):
        print('This is bulukulu festival year.')
    if not (leap or huluculu or bulukulu):
        print('This is an ordinary year.')

    try:
        n = int(input())
    except EOFError:
        break

    print('')
    
        