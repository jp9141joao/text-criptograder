# 🔒 **Sistema de Criptografia/Descriptografia de Textos** 🔓

Um programa interativo para criptografar e descriptografar mensagens utilizando múltiplos níveis de segurança. Baseado em substituições aleatórias de caracteres, é uma demonstração prática de criptografia simples.

---

## 🚀 **Visão Geral do Projeto**

Este projeto implementa um sistema interativo para criptografar e descriptografar mensagens usando uma substituição de caracteres aleatórios. Ele possui múltiplos níveis de dificuldade:

1. **Nível 1 (Amador)**: Substituições básicas de caracteres.
2. **Nível 2 (Médio)**: Substituições mais complexas com caracteres variados.
3. **Nível 3 (Militar)**: Maior complexidade, simulando padrões de criptografia avançados.

O código inclui uma interface interativa para permitir ao usuário escolher entre criptografar ou descriptografar mensagens e especificar o nível de segurança desejado.

---

## 🛠️ **Recursos Principais**

### Funcionalidades:
- **Criptografia com múltiplos níveis de dificuldade.**  
  Níveis de segurança com padrões próprios de substituição.
- **Descriptografia correspondente para cada nível.**  
  Possibilidade de descriptografar mensagens de acordo com o nível selecionado.
- **Interface Interativa com Menu Simples.**  
  Um menu claro para navegação:
  ```
  * Menu de Opção *
  1- Criptografar
  2- Descriptografar
  3- Sair
  ```
- **Base Aleatória para Segurança**: Uso de padrões aleatórios para dificultar a quebra de criptografia.

---

## ⚙️ **Configuração**

### Pré-requisitos
- Python 3.x deve estar instalado no sistema.

---

## ▶️ **Como Executar**

1. Clone o repositório no seu ambiente local:
```bash
git clone https://github.com/seu-usuario/sistema-criptografia.git
```

2. Instale qualquer dependência necessária (caso necessário, mas o código não depende de pacotes externos).

3. Execute o programa com:
```bash
python seu_arquivo.py
```

---

## 🎮 **Como Funciona**

O fluxo básico é o seguinte:

1. Ao iniciar o programa, o usuário verá um menu com as opções:  
   ```
   * Menu de Opção *
   1- Criptografar
   2- Descriptografar
   3- Sair
   ```

2. **Escolha de Operação:**  
   O usuário pode optar por criptografar ou descriptografar mensagens.

3. **Seleção do nível de dificuldade:**  
   O programa oferece níveis como:
   - **Nível 1**: Substituições simples e padrões básicos.
   - **Nível 2**: Substituições com base em variabilidade de caracteres.
   - **Nível 3**: Maior nível de aleatoriedade e complexidade.

4. O usuário digita a mensagem, e o programa realiza a operação com base no nível escolhido.

---

## 💬 **Tecnologias Utilizadas**

- **Python 3.x**: Lógica principal e tratamento de strings.
- Manipulação de sistema com `os.system('cls')` para atualização limpa do terminal.

---

## 💬 **Exemplo de Uso**

Após iniciar o programa, você verá o menu:

```
* Menu de Opção *
1- Criptografar
2- Descriptografar
3- Sair
R: 1
Selecione o Nivel de Criptografia:
1- Amadora
2- Media
3- Militar
R: 1
Digite a String que deseja criptografar: Teste
Mensagem Encriptografada com Sucesso!
Sua frase encriptografada é "Z$K8GDV7Â...etc"
```

---

## ⚙️ **Suporte para Níveis**

Os níveis alteram a complexidade da criptografia/descriptografia. O usuário seleciona o nível desejado no menu:

1. **Nível 1:** Substituições simples e regras básicas.
2. **Nível 2:** Substituições mais avançadas.
3. **Nível 3:** Substituições complexas, simulando níveis de criptografia avançados.

---

Agora você está pronto para usar e testar este incrível sistema de criptografia/descriptografia! Boa sorte! 🔒✨