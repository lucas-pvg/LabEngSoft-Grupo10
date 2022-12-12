# Projeto PCS3643 - Laboratório de Engenharia de Software I (Grupo 10)

Este repositório armazena o projeto referente à disciplina PCS3643 - Laboratório de Engenahria de Software I. Este arquivo apesenta um breve tutorial
para instalação e execução do aplicativo na sua máquina local.

## Pré-Requisitos

Primeiramente, é necessário que se tenha Python 3.6+ instalado em sua máquina, bem como git, o Django e algumas outras bibliotecas python utilizadas no projeto. Para a instalação das ferramentas necessárias, refira-se às referências específicas de cada uma, disponíveis na iternet.

Caso você deseje rodar a aplicação em um ambiente virtual, primeiramente selecione a pasta desejada para armazenar o projeto e, dentro dela, após a instalação do Pyhton, crie um ambiente virtual executanto os seguintes comandos:

```
python -m venv env
./env/bin/activate
```

Uma pasta `env` deve ser criada e o ambiente virtual executado do seu terminal. Dentro dessa mesma pasta, com o ambiente virtual ativo, instale o git para seguir com a instalação e execução do aplicativo.


## Clonagem do Repositório

Após a instalação do git, para clonar esse repositório na sua máquina basta clicar no botão `code` e copiar o endereço mostrado por ele. Em sua máquina, dentro de uma pasta qualquer desejada, abra um terminal e execute o comando abaixo, subtituindo 'LinkCopiado' pelo endereço que você copiou:

```
git clone LinkCopiado
```

O repositório LabEngSoft-Grupo10 deve aparecer na pasta em que você executou o comando.


## Instalação do Django e das Outras Dependências

Após clonar o repositório para sua máquina, um arquivo `requirements.txt` deve ser encontrado dentro da pasta raiz do projeto, ou seja `LabEngSoft-Grupo10`. Para instalar o django e as outras dependências do projeto basta abrir um terminal, ativar seu ambiente virtual previamente criado e entrar na pasta raiz do projeto. Dentro dela, execute o comando:

```
pip install -r requirements.txt
```

O pip deve iniciar a instalação dos pacotes necessários para rodar o projeto localmente. Após instalar as dependências, apenas para a primeira vez que você for executar o projeto, execute o comando abaixo para ter certeza de que as migrations necessárias estão aplicadas:

```
python manage.py migrate
```


## Execução do Aplicativo em um Servidor Local

Após clonar o repositório do projeto, entre na pasta LabEngSoft-Grupo10 que foi criada e execute o aplicativo em um servidor local. Para fazer isso, basta rodar os comandos abaixo:

```
cd LabEngSoft-Grupo10 (caso não esteja na pasta raiz do repositório clonado)
python manage.py runserver
```

Dessa forma, seu terminal deve executar o aplicativo em um servidor local e retornar o caminho para que você possa acessá-lo. Ele deve se parecer com algo assim 
`http://127.0.0.1:8000/`, tendo em mente que o número do servidor pode mudar, apresentando a tela de monitoramento dos voos de partida e chegada. Para acessar a página de login do sistema, basta clicar em `logout` ou acessar `http://127.0.0.1:8000/members/login/`. Para criar usuários e atribuir diferentes grupos e permissões a eles, basta acessas o admin do django e manualmente criar os usuários desejados.

Com o projeto aberto em sua máquina, é possível acessar as demais telas tanto realizando o login e navegando na própria aplicação quanto acessando diretamente cada página substituindo o final do caminho `http://127.0.0.1:8000/` pelas outras telas disponíveis neste projeto, sendo elas:

* `/members/login` - tela de login
* `/crud` - tela de CRUD para operações de voo
* `/monitoramento/` - tela de monitoramento de voo
* `/relatorio` - tela de relatórios


## Acessando a Aplicação pelo Servidor 

A aplicação também está disponível em [labsoftg10.pythonanywhere.com](labsoftg10.pythonanywhere.com)
