print("Programa 01")

print("Olá Mundo")

print("--------------------------------------------------------")
print("Programa 02")
idade = int(input("Digite sua idade: "))
print(idade)
print(type(idade))

print("--------------------------------------------------------")
print("Programa 03")

email = input("Digite o email: ")

if not '@' in email or not '.com' in email:
    print("Email invalido")
else:
    print("Email valido")

