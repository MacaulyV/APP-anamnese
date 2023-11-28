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

# Dicionário para armazenar as consultas agendadas
consultas_agendadas = {}

# Função para confirmar o nome do usuário
def confirmar_nome():
    while True:
        nome = input("Por favor, confirme o seu nome completo: ")
        if len(nome) <= 100 and re.match("^[A-Za-z ]*$", nome):
            print(f"Nome confirmado: {nome}.")
            return nome
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
            return especialidades[opcao]
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
            return medicos[especialidade][int(opcao) - 1]
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
            return dias[opcao]
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
            return horarios[int(opcao) - 1]
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
            return comentario
    else:
        return None

# Função para inserir o código do convênio
def inserir_codigo_convenio():
    while True:
        codigo = input("Digite o código do seu convênio: ")
        if len(codigo) == 10:
            print("Você acabou de marcar uma consulta. Você receberá um email de confirmação no email cadastrado no aplicativo.")
            return codigo
        else:
            print("Código inválido. O código do convênio deve ter exatamente 10 caracteres. Por favor, tente novamente.")

def agendar_consulta_rotina():
    while True:
        opcao = input("Você gostaria de selecionar um médico de sua escolha? (S/N): ")

        if opcao.lower() == "s":
            especialidade = "Cardiologia"  # Aqui você pode substituir "Cardiologia" pela especialidade desejada
            medico = selecionar_medico(especialidade)
        elif opcao.lower() == "n":
            print("Você escolheu não selecionar um médico.")
            especialidade = None
            medico = None
        else:
            print("Opção inválida. Por favor, tente novamente.")
            continue

        dia = selecionar_dia()
        horario = selecionar_horario(dia['horarios'])
        comentario = adicionar_comentario()
        codigo_convenio = inserir_codigo_convenio()

        # Armazenar os dados da consulta no dicionário de consultas agendadas
        nome = confirmar_nome()
        consultas_agendadas[nome] = {
            "especialidade": especialidade,
            "medico": medico,
            "dia": dia['dia'],
            "horario": horario,
            "comentario": comentario,
            "codigo_convenio": codigo_convenio
        }

        break

def agendar_consulta():
    nome = confirmar_nome()
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
        especialidade = selecionar_especialidade()
        medico = selecionar_medico(especialidade)
        dia = selecionar_dia()
        horario = selecionar_horario(dia['horarios'])
        comentario = adicionar_comentario()
        codigo_convenio = inserir_codigo_convenio()

        # Armazenar os dados da consulta no dicionário de consultas agendadas
        consultas_agendadas[nome] = {
            "especialidade": especialidade,
            "medico": medico,
            "dia": dia['dia'],
            "horario": horario,
            "comentario": comentario,
            "codigo_convenio": codigo_convenio
        }
    else:
        print("Opção inválida. Por favor, tente novamente.")

def cancelar_consulta():
    nome = input("Por favor, insira o seu nome completo: ")

    if nome in consultas_agendadas:
        print("Aqui estão os detalhes da sua consulta:")
        print(f"Tipo de Consulta: {consultas_agendadas[nome]['tipo_consulta']}")
        print(f"Nível de Prioridade: {consultas_agendadas[nome]['nivel_prioridade']}")

        if input("Você realmente deseja cancelar esta consulta? (S/N): ").lower() == 's':
            while True:
                codigo = input("Por favor, confirme o código do seu convênio: ")
                if codigo == consultas_agendadas[nome]['codigo_convenio']:
                    del consultas_agendadas[nome]
                    print("Sua consulta foi cancelada com sucesso.")
                    break
                elif codigo.lower() == 'sair':
                    print("Cancelamento de consulta cancelado.")
                    menu_inicial()
                    break
                else:
                    print("Código do convênio inválido. Por favor, tente novamente.")
        else:
            print("Cancelamento de consulta cancelado.")
    else:
        print("Não há consultas agendadas para este nome.")
        menu_inicial()

def questionario_emergencia():
    perguntas = [
        "Você tem alguma alergia?",
        "Você toma algum medicamento?",
        "Você tem alguma doença crônica?",
        "Você já foi hospitalizado?"
    ]

    respostas = {}

    for pergunta in perguntas:
        while True:
            resposta = input(pergunta + " (S/N): ")
            if resposta.lower() in ['s', 'n']:
                respostas[pergunta] = resposta
                break
            else:
                print("Resposta inválida. Por favor, responda com 'S' para sim ou 'N' para não.")

    print("Responda as próximas perguntas com sinceridade, elas decidirão seu tempo até ser atendido.")
    if input("Você está pronto para prosseguir? (Digite 'OK' para continuar): ").lower() == 'ok':
        return respostas
    else:
        menu_inicial()        

def questionario_sintomas():
    sintoma = input("Qual é o seu principal sintoma? (máximo de 30 caracteres): ")
    if len(sintoma) > 30:
        print("Seu sintoma excede o limite de 30 caracteres. Por favor, tente novamente.")
        questionario_sintomas()
    else:
        print("Seu sintoma foi registrado com sucesso.")

    print("Quando começou o seu sintoma?")
    print("1. Menos de 24 horas atrás")
    print("2. 1-3 dias atrás")
    print("3. 4-7 dias atrás")
    print("4. Mais de uma semana atrás")

    opcao = input("Digite o número da opção escolhida: ")

    if opcao == "1":
        pontos = 1
    elif opcao == "2":
        pontos = 2
    elif opcao == "3":
        pontos = 3
    elif opcao == "4":
        pontos = 4
    else:
        print("Opção inválida. Por favor, tente novamente.")
        questionario_sintomas()

    print("Qual é a intensidade do seu sintoma?")
    print("1. Leve: O sintoma é perceptível, mas não afeta significativamente as atividades diárias.")
    print("2. Moderado: O sintoma é incômodo e pode afetar algumas atividades diárias.")
    print("3. Grave: O sintoma é muito incômodo e afeta significativamente as atividades diárias.")
    print("4. Muito grave: O sintoma é extremamente incômodo e impede a realização de atividades diárias.")

    opcao = input("Digite o número da opção escolhida: ")

    if opcao == "1":
        pontos += 1
    elif opcao == "2":
        pontos += 2
    elif opcao == "3":
        pontos += 3
    elif opcao == "4":
        pontos += 4
    else:
        print("Opção inválida. Por favor, tente novamente.")
        questionario_sintomas()

    print("O seu sintoma está piorando ou melhorando?")
    print("1. Melhorando: O sintoma está diminuindo em intensidade ou frequência.")
    print("2. Inalterado: O sintoma não mudou em intensidade ou frequência.")
    print("3. Piorando: O sintoma está aumentando em intensidade ou frequência.")

    opcao = input("Digite o número da opção escolhida: ")

    if opcao == "1":
        pontos -= 2
    elif opcao == "2":
        pass
    elif opcao == "3":
        pontos += 2
    else:
        print("Opção inválida. Por favor, tente novamente.")
        questionario_sintomas()

    mensagem = avaliar_pontuacao(pontos)
    print(mensagem)

    nome, codigo_convenio = confirmar_detalhes()

    consultas_agendadas[nome] = {
        "tipo_consulta": "Consulta Remota",
        "nivel_prioridade": mensagem,
        "sintoma": sintoma,
        "pontos": pontos,
        "codigo_convenio": codigo_convenio
    }

    return sintoma, pontos


def confirmar_detalhes():
    while True:
        nome = input("Por favor, confirme o seu nome completo: ")
        if len(nome) <= 30 and nome.replace(' ', '').isalpha():
            print(f"Nome confirmado: {nome}.")
        else:
            print("Nome inválido. Por favor, tente novamente.")
            continue

        codigo_convenio = input("Por favor, confirme o código do seu convênio: ")
        if len(codigo_convenio) == 10:
            print(f"Código do convênio confirmado: {codigo_convenio}.")
            print("Por favor, fique de olho no seu e-mail. Você receberá um link para uma videochamada com um médico especialista.")
            break
        else:
            print("Código do convênio inválido. Por favor, tente novamente.")

    return nome, codigo_convenio

def avaliar_pontuacao(pontos):
    if 0 <= pontos <= 2:
        return "Seus sintomas parecem ser leves e não urgentes. No entanto, é importante monitorá-los. Seus sintomas serão avaliados dentro de 72 horas."
    elif 3 <= pontos <= 5:
        return "Seus sintomas podem exigir atenção médica em breve. Por favor, esteja preparado para uma teleconsulta nas próximas 48 horas."
    elif 6 <= pontos <= 8:
        return "Seus sintomas são preocupantes e você deve ser avaliado por um médico o mais rápido possível. Por favor, esteja preparado para uma teleconsulta nas próximas 24 horas."
    elif 9 <= pontos <= 10:
        return "Seus sintomas são muito graves e exigem atenção médica imediata. Por favor, esteja preparado para uma teleconsulta imediatamente. Se os sintomas piorarem, procure atendimento de emergência."
    else:
        return "Pontuação inválida."

# Agora, vamos chamar a função questionario_sintomas() dentro da função teleconsulta()

def teleconsulta():
    print("Escolha o tipo de consulta que deseja:")
    print("1. Consulta de Emergência")

    opcao = input("Digite o número da opção escolhida: ")

    if opcao == "1":
        print("Você escolheu 'Consulta de Emergência'.")
        print("Este tipo de consulta é destinado para quem precisa ser atendido rapidamente no mesmo dia.")
        if input("Você deseja prosseguir? (S/N): ").lower() == 's':
            print("Você escolheu prosseguir com a 'Consulta de Emergência'.")
            respostas = questionario_emergencia()
            sintoma, pontos = questionario_sintomas()
            # Aqui você pode adicionar o fluxo para a 'Consulta de Emergência'
        else:
            print("Você escolheu não prosseguir com a 'Consulta de Emergência'.")
            menu_inicial()
    else:
        print("Opção inválida. Por favor, tente novamente.")
        teleconsulta()

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
            cancelar_consulta()
        elif opcao == "3":
            teleconsulta()
        elif opcao == "4":
            print("Obrigado por usar nosso aplicativo. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

menu_inicial()

