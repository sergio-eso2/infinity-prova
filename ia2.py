numero_alunos = int(input("Digite o número de alunos: "))
    
    
total_notas = 0

    
for i in range(numero_alunos):
        
        nome = input("Digite o nome do aluno: ")
        
        
        notas = []
        for i in range(1, 4):
            nota = float(input(f"Digite a nota {i} do aluno {nome}: "))
            notas.append(nota)
        
        
        media = sum(notas) / len(notas)
        total_notas += media

        
        if media >= 7.0:
            status = "Aprovado"
            
        else:
            status = "Reprovado"
            
        
        
        print(f"\nNome: {nome}")
        print(f"Notas: {notas}")
        print(f"Média: {media}")
        print(f"Status: {status}\n")
    
    
if numero_alunos > 0:
        media_geral = total_notas / numero_alunos
else:
        media_geral = 0
    
print(f"Média geral da turma: {media_geral}")

