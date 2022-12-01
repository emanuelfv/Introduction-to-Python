#Faça um programa que peça 2 notas e calcule a média delas

#quantos alunos tem na sala?
numerodeAlunos = int(input('Numero de alunos na sala'))
print(f'Numero de alunos {numerodeAlunos}')

#para um indice em um intervalo de zero alunos ate numero de alunos na sala
for indice in range(0, numerodeAlunos):
    #ENTRADA DE DADOS
    nota1 = int(input('Nota Aluno 1'))
    nota2 = int(input('Nota Aluno2'))
    Notas = (nota1 + nota2)/2
    print(Notas)
    media = print(f'Nota Aluno1: {nota1}, ++ Nota Aluno2: {nota2} = {(nota1 + nota2 )/ 2}')

    #Se o aluno media maior que 7, ele passou
    #Se o aluno media menor que 7, ele reprovou
    #Se o aluno media igual 7, ele está de recuperação
    if (Notas > 7):
        print("aprovado")
    elif (Notas == 7):
        print('Recuperaçao')
    else:
        print('Reprovado')
