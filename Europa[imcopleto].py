list = ['Belgium', 'UK', 'France', 'Greece', 'Italy', 'Poland', 'Portugal', 'Romania', 'Czecho-Slovakia', 'Spain']
L = str(input('Escolhe um pais da Sociedade das nações, se tivereves certo ganhas, se nao perdes: '))
i = 0
for i in range(len(list)-1):
    #print(list[i])
    if L == list[i]:
elif L != list[i]:
    print('Haha erraste')
else:
    print('Boa!!')