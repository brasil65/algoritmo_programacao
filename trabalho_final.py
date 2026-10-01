def exibir_cardapio():
    """Apresenta as opções disponíveis para o cliente."""
    print("\n" + "-"*30)
    print("           CARDÁPIO")
    print("-"*30)
    print("1 - Hambúrguer Tradicional - R$ 25.00")
    print("2 - Batata Frita           - R$ 15.00")
    print("3 - Refrigerante           - R$ 8.00")
    print("4 - Suco Natural           - R$ 10.00")
    print("5 - Sobremesa              - R$ 12.00")
    print("0 - Finalizar Pedido")
    print("-"*30)

def processar_pedido(codigo):
    """
    Recebe o código do produto e retorna o seu nome e preço.
    Utiliza match-case para evitar o uso de listas ou dicionários.
    """
    match codigo:
        case "1":
            return "Hambúrguer Tradicional", 25.00
        case "2":
            return "Batata Frita", 15.00
        case "3":
            return "Refrigerante", 8.00
        case "4":
            return "Suco Natural", 10.00
        case "5":
            return "Sobremesa", 12.00
        case _:
            return "", 0.0  # Retorna valores zerados para opções inválidas

def calcular_desconto(valor_total):
    """
    Aplica as regras de desconto com base no valor total da compra.
    """
    if valor_total >= 100.00:
        percentual = 10
    elif valor_total >= 50.00:
        percentual = 5
    else:
        percentual = 0

    valor_desconto = valor_total * (percentual / 100)
    valor_final = valor_total - valor_desconto

    return percentual, valor_desconto, valor_final

def escolher_pagamento():
    """
    Solicita e valida a forma de pagamento utilizando um laço de repetição.
    """
    while True:
        print("\n--- FORMAS DE PAGAMENTO ---")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")
        opcao = input("Escolha a forma de pagamento (1/2/3): ")

        match opcao:
            case "1":
                return "Dinheiro"
            case "2":
                return "PIX"
            case "3":
                return "Cartão"
            case _:
                print("Opção inválida! Por favor, digite 1, 2 ou 3.")

def principal():
    """Função principal que gerencia o fluxo do sistema."""
    print("Bem-vindo ao Sistema de Atendimento!")
    nome_cliente = input("Por favor, informe seu nome: ")

    total_compra = 0.0

    # Laço de repetição para continuar recebendo pedidos até o usuário digitar "0"
    while True:
        exibir_cardapio()
        codigo = input("Digite o código do produto desejado (ou '0' para finalizar): ")

        if codigo == "0":
            break

        nome_produto, preco = processar_pedido(codigo)

        # Validação de opção incorreta
        if preco == 0.0:
            print("\n>>> Código inválido! Por favor, escolha uma opção válida do cardápio.")
            continue

        quantidade_str = input(f"Quantas unidades de '{nome_produto}' você deseja? ")
        quantidade = int(quantidade_str)

        if quantidade <= 0:
            print("\n>>> Quantidade inválida. Tente novamente.")
            continue

        # Cálculo do subtotal e acúmulo no total
        subtotal = preco * quantidade
        total_compra += subtotal
        print(f"\n✅ Adicionado: {quantidade}x {nome_produto} - Subtotal: R$ {subtotal:.2f}")

    # Ao finalizar o pedido, calcular descontos e exibir o resumo se houve alguma compra
    if total_compra > 0:
        percentual, valor_desconto, valor_final = calcular_desconto(total_compra)
        forma_pagamento = escolher_pagamento()

        # Apresentação do resultado final
        print("\n" + "="*40)
        print("          RESUMO DO PEDIDO")
        print("="*40)
        print(f"Cliente: {nome_cliente}")
        print(f"Valor original da compra: R$ {total_compra:.2f}")
        print(f"Desconto aplicado:        {percentual}%")
        print(f"Valor do desconto:        R$ {valor_desconto:.2f}")
        print(f"Valor final a pagar:      R$ {valor_final:.2f}")
        print(f"Forma de pagamento:       {forma_pagamento}")
        print("="*40)
        print("Obrigado pela preferência e volte sempre!\n")
    else:
        print("\nNenhum pedido foi realizado. Atendimento encerrado.")

# Ponto de entrada do programa
if __name__ == "__main__":
    principal()