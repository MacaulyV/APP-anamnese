from rich import print
import re

# Dicionários para armazenar informações sobre especialidades e médicos
especialidades = {
    "1": "Cardiologia",
    "2": "Dermatologia",
    "3": "Endocrinologia",
    "4": "Gastroenterologia",
    "5": "Neurologia",
    "6": "Ortopedia",
    "7": "Pediatria",
    "8": "Psiquiatria",
    "9": "Urologia"
}

medicos = {
    "Cardiologia": ["Dr. João Silva", "Dr. Pedro Costa", "Dr. Carlos Rocha"],
    "Dermatologia": ["Dra. Maria Santos", "Dra. Ana Pereira", "Dra. Beatriz Teixeira"],
    "Endocrinologia": ["Dr. Luís Almeida", "Dr. Antônio Soares", "Dr. José Ferreira"],
    "Gastroenterologia": ["Dra. Sofia Oliveira", "Dra. Mariana Castro", "Dra. Gabriela Cardoso"],
    "Neurologia": ["Dr. Ricardo Freitas", "Dr. Bruno Correia", "Dr. Francisco Dias"],
    "Ortopedia": ["Dra. Fernanda Monteiro", "Dra. Juliana Ribeiro", "Dra. Luciana Cunha"],
    "Pediatria": ["Dr. Rafael Sousa", "Dr. André Lopes", "Dr. Daniel Gomes"],
    "Psiquiatria": ["Dra. Patrícia Marques", "Dra. Renata Guimarães", "Dra. Aline Nunes"],
    "Urologia": ["Dr. Guilherme Mendes", "Dr. Eduardo Barros", "Dr. Leonardo Martins"]
}

dias = {
    "1": {"dia": "Segunda-feira", "horarios": ["09:00", "13:00", "17:00"]},
    "2": {"dia": "Terça-feira", "horarios": ["10:00", "14:00", "18:00"]},
    "3": {"dia": "Quarta-feira", "horarios": ["09:00", "13:00", "17:00"]},
    "4": {"dia": "Quinta-feira", "horarios": ["10:00", "14:00", "18:00"]},
    "5": {"dia": "Sexta-feira", "horarios": ["09:00", "13:00", "17:00"]},
    "6": {"dia": "Sábado", "horarios": ["10:00", "14:00"]},
    "7": {"dia": "Domingo", "horarios": []}
}

# Função para confirmar o nome do usuário
def confirmar_nome():
    while True:
        nome = input("Por favor, confirme o seu nome completo: ")
        if len(nome) <= 100 and re.match("^[A-Za-z ]*$", nome):
            print(f"Nome confirmado: {nome}.")
            break
        else:
            print("Nome inválido. Por favor, tente novamente.")

# Função para selecionar a especialidade médica
def selecionar_especialidade():
    while True:
        print("Escolha a especialidade médica:")
        for key, value in especialidades.items():
            print(f"{key}. {value}")

        opcao = input("Digite o número da opção escolhida: ")

        if opcao in especialidades:
            print(f"Você escolheu a especialidade de {especialidades[opcao]}.")
            if input("Gostaria de selecionar um médico de sua escolha? (S/N): ").lower() == 's':
                selecionar_medico(especialidades[opcao])
            else:
                selecionar_dia()
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Função para selecionar o médico
def selecionar_medico(especialidade):
    while True:
        print("Escolha o médico de sua preferência:")
        for i, medico in enumerate(medicos[especialidade], start=1):
            print(f"{i}. {medico}")

        opcao = input("Digite o número da opção escolhida: ")

        if 1 <= int(opcao) <= len(medicos[especialidade]):
            print(f"Você escolheu o médico {medicos[especialidade][int(opcao) - 1]}.")
            selecionar_dia()
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Função para selecionar o dia da consulta
def selecionar_dia():
    while True:
        print("Escolha o dia da sua consulta:")
        for key, value in dias.items():
            print(f"{key}. {value['dia']} - Horários disponíveis: {', '.join(value['horarios'])}")

        opcao = input("Digite o número da opção escolhida: ")

        if opcao in dias:
            print(f"Você escolheu o dia {dias[opcao]['dia']}.")
            selecionar_horario(dias[opcao]['horarios'])
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Função para selecionar o horário da consulta
def selecionar_horario(horarios):
    while True:
        print("Escolha o horário da sua consulta:")
        for i, horario in enumerate(horarios, start=1):
            print(f"{i}. {horario}")
        print(f"{len(horarios) + 1}. Voltar")

        opcao = input("Digite o número da opção escolhida: ")

        if 1 <= int(opcao) <= len(horarios):
            print(f"Você escolheu o horário {horarios[int(opcao) - 1]}.")
            adicionar_comentario()
            break
        elif int(opcao) == len(horarios) + 1:
            selecionar_dia()
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Função para adicionar um comentário
def adicionar_comentario():
    if input("Gostaria de adicionar um comentário com o motivo da consulta? (S/N): ").lower() == 's':
        comentario = input("Digite o seu comentário (máximo de 1000 caracteres): ")
        if len(comentario) > 1000:
            print("Seu comentário excede o limite de 1000 caracteres. Por favor, tente novamente.")
            adicionar_comentario()
        else:
            print("Seu comentário foi adicionado com sucesso.")
    inserir_codigo_convenio()

# Função para inserir o código do convênio
def inserir_codigo_convenio():
    while True:
        codigo = input("Digite o código do seu convênio: ")
        if len(codigo) == 10:
            print("Você acabou de marcar uma consulta. Você receberá um email de confirmação no email cadastrado no aplicativo.")
            break
        else:
            print("Código inválido. O código do convênio deve ter exatamente 10 caracteres. Por favor, tente novamente.")

def agendar_consulta_rotina():
    while True:
        opcao = input("Você gostaria de selecionar um médico de sua escolha? (S/N): ")

        if opcao.lower() == "s":
            selecionar_medico("Cardiologia")  # Aqui você pode substituir "Cardiologia" pela especialidade desejada
        elif opcao.lower() == "n":
            print("Você escolheu não selecionar um médico.")
            selecionar_dia()
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

def agendar_consulta():
    confirmar_nome()
    print("Escolha o tipo de consulta que deseja agendar:")
    print("1. Consulta de Rotina")
    print("2. Consulta de Acompanhamento")
    print("3. Consulta de Emergência")

    opcao = input("Digite o número da opção escolhida: ")

    if opcao == "1":
        agendar_consulta_rotina()
    elif opcao in ["2", "3"]:
        if opcao == "2":
            print("Você escolheu 'Consulta de Acompanhamento'.")
        else:
            print("Você escolheu 'Consulta de Emergência'.")
        selecionar_especialidade()
    else:
        print("Opção inválida. Por favor, tente novamente.")

def menu_inicial():
    while True:
        print("Bem-vindo ao nosso aplicativo de saúde! Escolha uma opção:")
        print("1. Agendar consulta")
        print("2. Cancelar consulta marcada")
        print("3. Teleconsulta")
        print("4. Sair")

        opcao = input("Digite o número da opção escolhida: ")

        if opcao == "1":
            agendar_consulta()
        elif opcao == "2":
            print("Você escolheu 'Cancelar consulta marcada'.")
            # Aqui você pode chamar a função para cancelar uma consulta
        elif opcao == "3":
            print("Você escolheu 'Teleconsulta'.")
            # Aqui você pode chamar a função para agendar uma teleconsulta
        elif opcao == "4":
            print("Obrigado por usar nosso aplicativo. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

menu_inicial()




