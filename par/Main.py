def main() :
    numero = int(input ("digite um numero: "))


    i = 2

    while numero != i and numero != 1:
        if numero % i == 0:
            break
        i += 1

    if numero == i:
        print("O numero", numero, "é primo")
    elif numero == 1:
        print("O numreo 1 não é primo")
    else: 
        print("O numero", numero, "não primo porque é divisivel por ", i)


    return 0 
main()