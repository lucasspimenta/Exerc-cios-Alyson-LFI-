"""
Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final informar o nome do aluno e a sua média (aritmética)
"""
import math

aluno = input('Digite seu nome: ')
primeira_nota = float(input('Digite a nota da primeira prova: '))
segunda_nota = float(input('Digite a nota da segunda prova: '))
terceira_nota = float(input('Digite a nota da terceira prova: '))
media = (primeira_nota + segunda_nota + terceira_nota) / 3

print(f'O aluno {aluno} teve média final de {media} pontos.')
