import csv

bom_rendimento = []
baixo_rendimento = []

with open('dados_alunos.csv', mode='r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        nome = linha['Nome']
        turma = linha['Turma']
        
        notas = [
            float(linha['Nota1']), 
            float(linha['Nota2']), 
            float(linha['Nota3']), 
            float(linha['Nota4'])
        ]
        frequencia = float(linha['Frequencia'])
        media = sum(notas) / len(notas)
        
       
        aluno_processado = {
            'Nome': nome,
            'Turma': turma,
            'Media': round(media, 2), 
            'Frequencia': frequencia,
            'Classificacao': ''
        }
        
       
        if media >= 7.0 and frequencia >= 75.0:
            aluno_processado['Classificacao'] = 'Bom Rendimento'
            bom_rendimento.append(aluno_processado)
        else:
            aluno_processado['Classificacao'] = 'Baixo Rendimento'
            baixo_rendimento.append(aluno_processado)


def salvar_csv(nome_arquivo, lista_dados):
    if not lista_dados:
        return 
        
   
    cabecalho = lista_dados[0].keys()
    
    with open(nome_arquivo, mode='w', encoding='utf-8', newline='') a
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
        escritor.writeheader()    
        escritor.writerows(lista_dados) 


salvar_csv('alunos_bom_rendimento.csv', bom_rendimento)
salvar_csv('alunos_baixo_rendimento.csv', baixo_rendimento)


print("Análise concluída com sucesso!")
print(f"Total de alunos com Bom Rendimento: {len(bom_rendimento)}")
print(f"Total de alunos com Baixo Rendimento: {len(baixo_rendimento)}")
