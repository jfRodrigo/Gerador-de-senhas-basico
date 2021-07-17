chave = input("Digite a base da sua senha: ")


senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "10"
    elif letra in "Bb": senha = senha + "@"
    elif letra in "Cc": senha = senha + "2"
    elif letra in "Dd": senha = senha + "$"
    elif letra in "Ee": senha = senha + "#"
    elif letra in "Ff": senha = senha + "%"
    elif letra in "Gg": senha = senha + "&"
    elif letra in "Rr": senha = senha + "2"
    elif letra in "Vv": senha = senha + "3"
    elif letra in "Uu": senha = senha + "4"
    elif letra in "Zz": senha = senha + "7"
    elif letra in "Vv": senha = senha + "5"
    elif letra in "Ss": senha = senha + "8"
    elif letra in "Oo": senha = senha + "9"
    elif letra in "Xx": senha = senha + "0"


    else: senha = senha + letra 
print(senha)

    