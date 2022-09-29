# Projeto PCS3643 - Laboratório de Engenharia de Software I (Grupo 10)

Este repositório armazena o projeto referente à disciplina PCS3643 - Laboratório de Engenahria de Software I. Este arquivo apesenta um breve tutorial
para instalação e execução do aplicativo na sua máquina local.

## Pré-Requisitos

Primeiramente, é necessário que se tenha Python 3.6+ instalado em sua máquina, bem como git e o Django. Para a isntalação das ferramentas necessárias, refira-se às referências específicas de cada uma, disponíveis na iternet.

Caso você deseje rodar a aplicação em um ambiente virtual, primeiramente selecione a pasta desejada para armazenar o projeto e, dentro dela, após a instalação do Pyhton, crie um ambiente virtual executanto os seguintes comandos:

```
python -m venv env
./env/bin/activate
```

Uma pasta `env` deve ser criada e o ambiente virtual executado do seu terminal. Dentro dessa mesma pasta, com o ambiente virtual ativo, instale o django e o git para seguir com a instalação e execução do aplicativo.

## Instalação

Após a instalação das ferramentas necessárias para executar a aplicação, para clonar esse repositório na sua máquina basta clicar no botão `code` e copiar o endereço mostrado por ele. Em sua máquina, dentro de uma pasta qualquer desejada, abra um terminal e execute o comando abaixo, subtituindo 'LinkCopiado' pelo endereço que você copiou:

```
git clone LinkCopiado
```

O repositório LabEngSoft-Grupo10 deve aparecer na pasta em que você executou o comando.

## Execução do Aplicativo em um Servidor Local

Após clonar o repositório do projeto, entre na pasta LabEngSoft-Grupo10 que foi criada e execute o aplicativo em um servidor local. Para fazer isso, basta rodar os comandos abaixo:

```
cd LabEngSoft-Grupo10 (caso não esteja na pasta raiz do repositório clonado)
python manage.py runserver
```

Dessa forma, seu terminal deve executar o aplicativo em um servidor local e retornar o caminho para que você possa acessá-lo. Ele deve se parecer com algo assim 
`http://127.0.0.1:8000/`, tendo em mente que o número do servidor pode mudar. Por fim, basta abrir seu navegador e colar este endereço e o aplicativo será executado na sua tela.
