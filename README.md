# Sistema de Atendimento e Pedidos em Python

## 1. Nome do Estudante
Frederico Brasil Pereira Santana

## 2. Nome da Disciplina
Algoritmos e Programação - Análise e Desenvolvimento de Sistemas (Unilavras)

## 3. Título do Projeto
Desenvolvimento de um Sistema de Atendimento e Pedidos em Python

## 4. Breve Descrição do Programa
Este projeto é um sistema via terminal para atendimento em uma pequena lanchonete, desenvolvido inteiramente em Python. Ele tem o objetivo de substituir o registro manual, permitindo a identificação do cliente, a escolha de produtos a partir de um cardápio predefinido, o cálculo automático dos valores (incluindo regras de desconto progressivas) e o fechamento da compra com a forma de pagamento. A solução foi estruturada utilizando recursos fundamentais de programação, como funções, laços de repetição e estruturas de decisão, garantindo o funcionamento contínuo sem o uso de estruturas de dados avançadas, como listas ou dicionários.

## 5. Principais Funcionalidades Implementadas
* **Identificação do cliente:** Coleta do nome no início do atendimento.
* **Apresentação do cardápio e seleção:** Organização das opções de produtos e preços utilizando funções modulares e a estrutura `match-case`.
* **Controle de repetição de pedidos:** Implementação de um laço `while` que permite ao cliente inserir múltiplos itens e escolher o momento exato de finalizar o pedido.
* **Validação de entradas:** Tratamento de opções inválidas no cardápio, quantidades zeradas/negativas e preenchimento incorreto na forma de pagamento, evitando cálculos errados.
* **Cálculo automático e regras de desconto:** Acúmulo de subtotais por item e aplicação dinâmica de descontos no fechamento (5% para compras entre R$ 50,00 e R$ 99,99; e 10% para compras iguais ou superiores a R$ 100,00).
* **Resumo detalhado:** Exibição clara e formatada do recibo final contendo os dados do cliente, valor original, descontos aplicados, valor final e método de pagamento escolhido.

## 6. Instruções Necessárias para Executar o Programa
1. Certifique-se de ter o **Python 3** instalado no seu sistema (seja nativamente ou no seu ambiente Linux via WSL).
2. Faça o clone deste repositório ou baixe os arquivos diretamente para o seu computador.
3. Abra o terminal (ou o terminal integrado do VS Code) e navegue até o diretório onde o arquivo principal está localizado.
4. Execute o programa digitando o seguinte comando:
   ```bash
   python3 trabalho_final.py
