# imports
# TODO: inclua aqui os imports (se necessário)


# funções
def listar_disciplinas(professores, nome_professor):
    # TODO: implemente o corpo da função
    pass


# programa principal
professores = [
    {
        "matricula": 1001,
        "nome": "João Silva",
        "cargo": "Professor Adjunto",
        "email": "joao.silva@faculdadeimpacta.com.br",
        "disciplinas": [
            {
                "codigo": "APA301",
                "nome_disciplina": "Análise e Projeto de Algoritmos",
                "turma": "CC3AM",
                "quantidade_alunos": 30,
            },
            {
                "codigo": "AED302",
                "nome_disciplina": "Algoritmos e Estruturas de Dados",
                "turma": "CC3AM",
                "quantidade_alunos": 25,
            },
        ],
    },
    {
        "matricula": 1002,
        "nome": "Maria Oliveira",
        "cargo": "Professora Associada",
        "email": "maria.oliveira@faculdadeimpacta.com.br",
        "disciplinas": [
            {
                "codigo": "LOO401",
                "nome_disciplina": "Linguagem Orientada a Objetos",
                "turma": "CC4AN",
                "quantidade_alunos": 40,
            },
            {
                "codigo": "TC402",
                "nome_disciplina": "Teoria da Computação",
                "turma": "CC4AM",
                "quantidade_alunos": 35,
            },
        ],
    },
    {
        "matricula": 1003,
        "nome": "Carlos Pereira",
        "cargo": "Professor Titular",
        "email": "carlos.pereira@faculdadeimpacta.com.br",
        "disciplinas": [
            {
                "codigo": "DBD701",
                "nome_disciplina": "Desenvolvimento para Big Data",
                "turma": "CC7AN",
                "quantidade_alunos": 28,
            },
            {
                "codigo": "COMP601",
                "nome_disciplina": "Compiladores",
                "turma": "CC6AM",
                "quantidade_alunos": 22,
            },
        ],
    },
    {
        "matricula": 1004,
        "nome": "Ana Costa",
        "cargo": "Professora Adjunta",
        "email": "ana.costa@faculdadeimpacta.com.br",
        "disciplinas": [
            {
                "codigo": "TG503",
                "nome_disciplina": "Teoria de Grafos",
                "turma": "CC5AM",
                "quantidade_alunos": 33,
            },
            {
                "codigo": "PIVC801",
                "nome_disciplina": "Processo de Imagens e Visão Computacional",
                "turma": "CC8AM",
                "quantidade_alunos": 27,
            },
        ],
    },
]

print(
    listar_disciplinas(professores, "João Silva")
)  # ['Análise e Projeto de Algoritmos', 'Algoritmos e Estruturas de Dados']
print(
    listar_disciplinas(professores, "Vitor Furlan")
)  # professor(a) não encontrado(a)
