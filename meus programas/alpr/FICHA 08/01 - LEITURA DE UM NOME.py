def nome_pessoa(nome, sobrenome):
    con = nome + " " + sobrenome
    print(con)
#Exexcução
nome = str(input('Insira o seu nome: ')).strip()
sobrenome = str(input('Insira o seu sobrenome: ')).strip()
nome_pessoa(nome, sobrenome)