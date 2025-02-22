# Docker compose com Django e banco de dados

## Informações gerais

- Assunto: Docker, conteinizar aplicativos
- Disciplina: *sistemas operacionais*

## Relatório

### Aluno

- nome: Ana Maria Ferreira de Abreu Guedes 
- matrícula: 20232014040001

### Relato
Para a realização da atividade foi criada uma branch chamada docker no repositório do PDS web Bizzu e nela foram criados dois arquivos: Dockerfile e docker-compose.yml. <br>
Inicialmente,no arquivo Dockerfile foi implementado um código que tinha como objetivo criar a imagem da aplicação com base na imagem python sendo instalada dentro desse conteiner /bizzu que foi criado nesse mesmo arquivo além da imagem foi instalada todas as dependências que estão especificadas no arquivo requirements.txt
Mas, com isso apenas criamos a imagem não fazendo a execução em nenhum momento e por isso criamos o arquivo docker-compose.yml para conseguirmos fazer a execução com a criação de um service. Dentro desse service, configuramos algumas coisas para que a aplicação podesse funcionar como:<br>
- Build: Palavra-chave que indica o path que ele precisa fazer para chegar até o dockerfile que é o que ele precisa construir, usa o . pois eles estão no mesmo diretório 
- Command: Comando que ele precisar executar para rodar a aplicação. Usamos o bash -c para concatenar os dois comando o de migrate e de runserver pois normalmente para rodar uma palicação django precisa fazer esses dois comandos 
- Ports: Em que porta a aplicação está e a porta do conteiner para conectar os dois<br><br>
Para a representação do banco de dados foi necessária a alteração do arquivo de settings para que em vez do SQLITE ele usasse POSTGRES mas para isso primeiro adicionamos um novo service no docker-compose e configuramos algumas coisas para tal:<br>
- container_name: Nomear o container que vai armazear o banco 
- ports: Conectar a porta do conteiner a porta do banco
- image: Para consumir a imagem do postgres 
- environment: Adicionar informações de conexão como user e senha que são variáveis de ambiente 
- Volumes: Local de armazenamento persistente de informações<br>
Com isso criamos um novo service chamado DB que coloca nosso banco postgres em um conteiner. <br>
Não foi necessário a criação de um novo arquivo dockerfile pois o postgres já tem sua própria imagem que será usada da forma que foi fornecida sem adição de novos recursos. <br>
### Arquivos docker e de configuração do django
Como os arquivos não são suportados em markdown colocarei no mesmo diretório que está o relatório. O nome já exemplifica o que contém em cada arquivo, como dockerfile é o dockerfile e o setting são as configurações do nosso projeto no django.
