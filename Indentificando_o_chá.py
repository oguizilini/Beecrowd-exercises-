resposta = []
t = int(input())
n = input()
i = 0
while i <= 8:
    resposta.append(int(n[i]))
    i += 2

if t in resposta:
    print(resposta.count(t))

else: 
    print('0')