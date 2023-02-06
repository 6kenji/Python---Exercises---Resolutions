def pesquisa(sexo, resposta, entrevistados):
    percentagem = 0
    percentagem_masculina = percentagem - (entrevistados * 0.01)
    percentagem_femenina = percentagem - (entrevistados * 0.01)
    for k in range(entrevistados):
        print('Entrevistados: ',entrevistados)
        if sexo == 'MASCULINO' or sexo == 'masculino':
            print('A percentagem de homens que responderam sim é igual a:', percentagem_masculina)
        elif sexo == 'FEMENINO' or sexo == 'femenino':
            print('A percentagem de mulheres que responderam sim é igual a:', percentagem_femenina)
    for k in resposta:
        if k in resposta:
            resposta1 = resposta.count("SIM" or "sim" or "Sim")
            resposta2 = resposta.count("NAO" or "nao" or "Nao")
            print('O numero de pessoas que responderam sim é igual a: ', resposta1)
            print('O numero de pessoas que responderam não é igual a: ', resposta2)
#EXECUÇÃO
entrevistados = eval(input('Insiara o numero de pessoas que irão participar do inquerito: '))
sexo = input('Insira o seu sexo:  ')
resposta = input('Pretende voltar as aulas presenciais?: ')
pesquisa(sexo, resposta, entrevistados)