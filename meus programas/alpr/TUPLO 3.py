# K = [2,4,23,1,76,3,36]
#Informe qual o maior valor do vector acima
def maior(K):
    kay = 0
    for i in range(len(K)):
        if K[i] > kay:
            kay = K[i]
    print(kay)
K = [2,4,23,1,76,3,36]
maior(K)
