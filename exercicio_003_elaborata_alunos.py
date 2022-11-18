"""faça um programa que calcule o numero médio de alunos por turma.
para isto, peça a quantidade de turmas e a quantidade de alunos por turma.
as turmas não podem ter mais de 40 alunos por turma."""

turmas = int(input("Digite a quantidade de turmas! " ))
alunos = int(input("Digite a qunatidade de alunos! "))

media = int(alunos / turmas)
excesso = (media -40)

if media > 40:
    print("você excedeu a qunatidade de alunos por turma em:", excesso)
if media <= 40:
    print("\n A quantidade media de alunos por turma é:", media)
    print("\n A quantidade MÁXIMA de alunos por turma é:", media - excesso) 
    
    # COMO EU POSSO INSERIR O RESTO NA DIVISÃO DE ALUNOS?