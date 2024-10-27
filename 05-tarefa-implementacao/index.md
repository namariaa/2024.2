# Implementação de tarefas

## Informações gerais

- Capítulo: [Implementação de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-05.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Ana Maria Ferreira de Abreu Guedes 
- matrícula: 20232014040001

## Respostas dos exercícios

1. O TCB ou PCB é uma estrutura de dados que fica no núcleo que é associado a tarefas presentes no sistema e armazenam informações de contexto e gerência. Em suas estruturas geralmente organizadas em vetores contém informações como o identificador, estado, áreas de memória usadas, lista de recursos utilizados de tarefas, além de informações de contexto do processador e informações de gerência e contabilização.
2. 
3. XXXXX
4. Thread são fluxos de execução independentes de uma tarefa, que possuem seu próprio código, e que podem fazer o compartilhamento de recursos entre si ocorrendo simultaneamente. Todo esse processo objetiva o melhor desempenho da aplicação.
5. Dentre as vantagens temos uma melhor eficiência/rapidez já que o processo ocorre de formas independentes e simultâneas além de um menor consumo de recursos. Quanto as desvantagens temos como principal a maior probabilidade de erro e risco.
6. Em casos em que um erro em uma thread não pode afetam os demais processos e  não pode haver problemas de escalabilidade que esse modelo causa como em navegadores como chrome.
7. A → B → B → A → C → B → A → C → B → C
8.