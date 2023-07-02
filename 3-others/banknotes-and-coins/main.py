print('Digite o valor: ', end='')
n = int(float(input())*100)

def calc_display(form, values):
    global n
    print(f'{form.upper()}S:')
    for i in values:
        print(f'{n//i} {form}(s) de R$ {i/100:.2f}')
        n %= i

calc_display('nota', (10000, 5000, 2000, 1000, 500, 200))
calc_display('moeda', (100, 50, 25, 10, 5, 1))