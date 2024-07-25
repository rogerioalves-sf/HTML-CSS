
print("Bem-vindos à Empresa de Gerenciamento de Funcionários do Rogério Alves da Silva Filho")

lista_funcionarios = []
id_global = 123456  

def cadastrar_funcionario(id):
    global id_global
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))

    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    
    lista_funcionarios.append(funcionario.copy())
    
    id_global += 1


def consultar_funcionarios():
    while True:
        print("\nMenu de Consulta de Funcionários:")
        print("1) Consultar Todos")
        print("2) Consultar por Id")
        print("3) Consultar por Setor")
        print("4) Retornar ao menu")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
          
            print("\nLista de todos os funcionários:")
            for funcionario in lista_funcionarios:
                print(funcionario)
        
        elif opcao == '2':
        
            id_consulta = int(input("Digite o ID do funcionário: "))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print("\nFuncionário encontrado:")
                    print(funcionario)
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
        
        elif opcao == '3':
           
            setor_consulta = input("Digite o setor desejado: ")
            encontrados = []
            for funcionario in lista_funcionarios:
                if funcionario['setor'].lower() == setor_consulta.lower():
                    encontrados.append(funcionario)
            
            if encontrados:
                print(f"\nFuncionários do setor '{setor_consulta}':")
                for funcionario in encontrados:
                    print(funcionario)
            else:
                print(f"Nenhum funcionário encontrado no setor '{setor_consulta}'.")
        
        elif opcao == '4':
         
            return
        
        else:
            print("Opção inválida. Tente novamente.")


def remover_funcionario():
    id_remover = int(input("Digite o ID do funcionário a ser removido: "))
    global lista_funcionarios
    funcionarios_atualizados = []
    removido = False
    for funcionario in lista_funcionarios:
        if funcionario['id'] == id_remover:
            removido = True
            continue
        funcionarios_atualizados.append(funcionario)
    
    if removido:
        lista_funcionarios = funcionarios_atualizados
        print(f"Funcionário com ID {id_remover} removido com sucesso.")
    else:
        print("ID inválido. Funcionário não encontrado.")


while True:
    print("\nMenu Principal:")
    print("1) Cadastrar Funcionário")
    print("2) Consultar Funcionário")
    print("3) Remover Funcionário")
    print("4) Encerrar Programa")
    
    opcao_principal = input("Escolha uma opção: ")
    
    if opcao_principal == '1':
       
        cadastrar_funcionario(id_global)
    
    elif opcao_principal == '2':
        
        consultar_funcionarios()
    
    elif opcao_principal == '3':
       
        remover_funcionario()
    
    elif opcao_principal == '4':
       
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
