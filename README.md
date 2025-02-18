
# Scanner de Portas

Este é um simples script de **escaneamento de portas** desenvolvido em Python. Ele permite verificar quais portas estão abertas em um determinado IP ou domínio.

## Funcionalidades

- Escaneamento de portas TCP em um intervalo específico (por padrão, 1 a 1024).
- Exibe portas abertas no destino especificado.
- Utiliza múltiplas threads para escaneamento rápido.
- Mostra mensagens informativas durante o processo.

## Requisitos

Para rodar o projeto, é necessário ter o Python 3.x instalado na sua máquina.

Além disso, você precisa da biblioteca `socket`, que já vem pré-instalada no Python.

## Como Usar

1. Clone este repositório ou faça o download do arquivo `scanner.py`.
   
   Para clonar o repositório:

   ```bash
   git clone https://github.com/NascimentoLuis/ScannerDePorta.git
   ```

2. Acesse a pasta do projeto:

   ```bash
   cd ScannerDePorta
   ```

3. Execute o script Python:

   ```bash
   python scanner.py
   ```

4. Digite o **IP ou domínio** do alvo que deseja escanear, por exemplo:

   ```
   Digite o IP ou domínio do alvo: 172.100.1.10
   ```

5. O script começará a escanear as portas e mostrará as portas abertas.

## Como Funciona

O script realiza o seguinte:

- Cria uma conexão TCP com o alvo em cada porta do intervalo definido.
- Se a conexão for bem-sucedida, a porta é considerada aberta e é exibida no terminal.
- O script utiliza múltiplas threads para melhorar o desempenho e escanear várias portas simultaneamente.

## Exemplo de Saída

```bash
Digite o IP ou domínio do alvo: 0.1.1.10...
Escaneando 0.1.1.10...
[+] Porta 22 está aberta
[+] Porta 80 está aberta
[+] Porta 443 está aberta
Escaneamento concluído para 0.1.1.10...
```

## Contribuindo

Se você deseja melhorar ou corrigir o código, fique à vontade para abrir um **pull request**.

1. Fork este repositório.
2. Crie uma branch para a sua mudança (`git checkout -b minha-mudanca`).
3. Faça suas alterações e adicione (`git add .`).
4. Faça o commit das suas mudanças (`git commit -m "Descrição das mudanças"`).
5. Envie para o repositório (`git push origin minha-mudanca`).
6. Abra um pull request.

