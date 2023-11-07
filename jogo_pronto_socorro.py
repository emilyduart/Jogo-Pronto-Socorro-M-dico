import heapq
import random


fila_prioridades = []


def adicionar_paciente():
    nome = input("Nome do paciente: ")
    idade = int(input("Idade do paciente: "))
    prioridade = random.randint(1, 10)  
    paciente = (prioridade, nome, idade)
    heapq.heappush(fila_prioridades, paciente)


def atender_paciente():
    if fila_prioridades:
        paciente = heapq.heappop(fila_prioridades)
        print(f"Atendendo paciente: {paciente[1]}, Idade: {paciente[2]}, Prioridade: {paciente[0]}")
        return paciente
    else:
        print("Não há pacientes na fila.")

def visualizar_fila():
    print("Fila de pacientes:")
    for paciente in  fila_prioridades:
        print(f"Nome: {paciente[1]}, Idade: {paciente[2]}, Prioridade: {paciente[0]} ") 
        return paciente

ultimos_pacientes_chamados = []

def listar_ultimos_chamados():
    print("Últimos 5 pacientes chamados:")
    for i, paciente in enumerate(ultimos_pacientes_chamados[::-1]):
        print(f"{i + 1}. Nome: {paciente[1]}, Idade: {paciente[2]}, Prioridade: {paciente[0]}")

def gerar_simulacao(num_pacientes):
    for _ in range(num_pacientes):
        nome = f"Paciente_{random.randint(1, 100)}"
        idade = random.randint(1, 100)
        prioridade = random.randint(1, 10)
        paciente = (prioridade, nome, idade)
        heapq.heappush(fila_prioridades,paciente)
                       

while True:
    print("\nOpções:")
    print("1. Adicionar paciente")
    print("2. Atender próximo paciente")
    print("3. Visualizar fila de pacientes")
    print("4. Listar os 5 últimos pacientes chamados")
    print("5. Gerar simulação")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        adicionar_paciente()
    elif opcao == '2':
        paciente_atendido = atender_paciente()
        if paciente_atendido:
            ultimos_pacientes_chamados.append(paciente_atendido)
            if len(ultimos_pacientes_chamados) > 5:
                ultimos_pacientes_chamados.pop(0)
    elif opcao == '3':
        visualizar_fila()
    elif opcao == '4':
        listar_ultimos_chamados()
    elif opcao == '5':
        num_pacientes = int(input("Quantos pacientes deseja gerar na simulação? "))
        gerar_simulacao(num_pacientes)
    elif opcao == '6':
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")