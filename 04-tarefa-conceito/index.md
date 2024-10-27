# Conceito de tarefas

## Informações gerais

- Capítulo: [Conceito de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-04.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Ana Maria Ferreira de Abreu Guedes 
- matrícula: 20232014040001

## Respostas dos exercícios

espostas exercícios:

1. Basicamente, com o propósito de evitar que o processador fique ocioso e problemas sejam ocasionados em cima disto, como o empate do funcionamento do SO,  o time sharing atribui a cada tarefa do processador receba uma fatia de tempo, ou seja, um prazo para processar.
2. A duração do quantum/fatia de tempo é variada de acordo com o sistema operacional. Por exemplo, o linux demora de 10 a 200 milissegundos enquanto o windows demora de 1 a 100 milissegundos a depender do tipo de tarefa.

3.

4. E → P - É possível quando ocorre o fim do quantum

E → S - É possível quando um recurso indisponível é solicitado  

S → E - Não é possível

P → N - Não é possível

S → T - Não é possível

S → P - É possível ao contrário do E → S ela é possível quando o recurso solicitado está disponível.

E → T - É possível quando a tarefa é encerrada, tanto por ser concluída quanto por ter ocorrido algum tipo de erro.

N → S - Não é possível

P → S - Não é possível

5. P → P → N → T → S → P → S → N → E → S