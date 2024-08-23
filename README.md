# Sistema Bancário Simples

Este é um sistema bancário simples em Python que permite ao usuário realizar operações básicas como depósito, saque, e consulta de extrato. O programa é interativo e funciona através de um menu que oferece diferentes opções ao usuário.

## Funcionalidades

- **Depósito**: Permite ao usuário adicionar um valor à sua conta.
- **Saque**: Permite ao usuário retirar um valor da sua conta, respeitando o saldo disponível, o limite de saque, e o número máximo de saques permitidos por dia.
- **Extrato**: Exibe todas as movimentações realizadas (depósitos e saques), além do saldo atual da conta.
- **Sair**: Encerra o programa.



**Interaja com o menu**:
 - `d`: Depositar um valor na conta.
 - `s`: Sacar um valor da conta (respeitando saldo, limite e número de saques).
 - `e`: Exibir o extrato e o saldo atual.
 - `q`: Sair do programa.

## Regras de Operação

- **Depósito**: 
  - O valor do depósito deve ser positivo.
- **Saque**:
  - O valor do saque não pode exceder o saldo disponível.
  - O valor do saque não pode exceder o limite de saque diário (R$ 500,00).
  - O número máximo de saques permitidos por dia é 3.
- **Extrato**:
  - Exibe todas as movimentações realizadas e o saldo atual.
  - Se não houver movimentações, informa que não foram realizadas operações.

## Exemplo de Uso

```python
# Exemplo de interação
"""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 1000

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e

================ EXTRATO ================
Depósito: R$ 1000.00

Saldo: R$ 1000.00
==========================================
"""
