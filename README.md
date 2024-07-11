# Python Poo Exercises
Este repositório contém exercícios de Programação Orientada a Objetos (POO) em Python, todos solucionados com códigos originais e comentários explicativos. O objetivo é auxiliar na prática e no aprendizado da POO

## Exercícios

### 01 - Conta Bancária

Crie uma classe ContaBancaria que modele uma conta bancária simples. A classe deve ter atributos para o nome do titular, endereço,agência e número, saldo da conta Implemente métodos para:

- **Depositar**: Receber um valor como parâmetro e atualizar o saldo da conta
- **Sacar**: Receber um valor como parâmetro, verificar se há saldo suficiente e limite disponível, e atualizar o saldo caso seja possível.
- **Consultar Saldo**: Retornar o valor do saldo da conta.

### 02 - Veiculo

- Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
- No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
- Crie uma nova classe chamada Carro que herda da classe Veiculo.
- No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
- Em um arquivo chamado main.py, importe a classe Carro.
- No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
