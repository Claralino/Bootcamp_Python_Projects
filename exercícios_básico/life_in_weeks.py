
idade = input("digite sua idade: ")

meses_total = 12 * 90
semanas_total = 52 * 90
dias_total = 365 * 90

meses_restantes = meses_total - (int(idade) * 12)
semanas_restantes = semanas_total - (int(idade) * 52)
dias_restantes = dias_total - (int(idade) * 365)

print(f"você tem {dias_restantes} dias, {semanas_restantes} semanas, e {meses_restantes} meses restantes")

# ou transformas a idade em int antes: idade_int = int(idade)