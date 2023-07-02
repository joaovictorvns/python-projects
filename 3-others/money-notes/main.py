values = (100, 50, 20, 10, 5, 2)

print('Digite o valor: ', end='')
n = int(input())

for i in values:
    print(f'{n//i} nota(s) de R$ {i},00')
    n %= i
print(f'{n} nota(s) de R$ 1,00')