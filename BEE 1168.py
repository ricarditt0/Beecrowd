

n = int(input())

for _ in range(n):
    number = input()
    total_leds = 0
    for digit in number:
        match digit:
            case '0':
                total_leds += 6
            case '1':
                total_leds += 2
            case '2':
                total_leds += 5
            case '3':
                total_leds += 5
            case '4':
                total_leds += 4
            case '5':
                total_leds += 5
            case '6':
                total_leds += 6
            case '7':
                total_leds += 3
            case '8':
                total_leds += 7
            case '9':
                total_leds += 6
    print(f"{total_leds} leds")