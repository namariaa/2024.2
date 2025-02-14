Para a realização dos testes foi copiado o código dado na atividade no arquivo cliente.py e feita algumas alterações nesse processo como a adição de uma função que recebe quantos clientes simultâneos queremos e mostra além do retorno que já tinha na função dada "fazer_requisicao_get()" o tempo que demorou para fazer cada requisição simultânea para que dessa forma fossem testados com diferentes quantidades de clientes o comportamento do servidor. E foram observados os seguintes resultados:<br>
### Servidor HTTP sem thread <br>
1. **Com 1 cliente** <br>
Ao inserir pelo console o valor que preencherá a variável numero_de_clientes ele teve o seguinte retorno:<br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: 
(Foi o código html mas dado na atividade que retorna "Olá, mundo! Este é um servidor HTTP multithread em Python." mas não será colocado aqui pois esse arquivo é um markdown e ele interpreta o HTML como sendo algo para ser colocado na tela)<br>
Com 1 demorou: 0.0040 aproximadamente <br><br>
2. **Com 2 clientes simultâneos** <br>
A respota foi:
Status: 200 <br>
Motivo: OK <br>
Conteúdo: 
Novamente ele retornou o mesmo HTMl que permanecerá o mesmo em todos os testes já que a análise da performace com diferentes quantidades de clientes deve ser feita. <br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: 
HTML fornecido, enfatizando que a repetição do status e do conteúdo está correta pois essas foram as repostas para dois clientes diferentes e ao aumentar o número de clientes o número de resposta aumenta proporcionalmente<br>

Com 2 demorou: 0.0062 <br><br>
3. **Com 5 clientes simultâneos** <br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: 
(HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: 
(HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: 
(HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: 
(HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: 
(HTML fornecido no código da atividade)<br>

Com 5 demorou: 0.011299610137939453<br><br>

4. **Com 10 clientes simultâneos** <br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200<br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>

Com 10 demorou: 0.023837804794311523<br><br>

Com isso observamos então que quanto mais clientes acessando simultaneamente mais demorado o envio pelo servidor vai ser, pois o mesmo precisará fazer diversos processos um atrás do outro. <br><br>

### Servidor HTTP com thread <br>
1. **Com 1 cliente** <br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo:
(Como o propósito é o teste do mesmo retorno do servidor com ou sem thread o retorno é o mesmo do anterior, um HTML escrito "Olá, mundo!") <br>
Com 1 demorou: 0.0038259029388427734 <br><br>

2. **Com 2 clientes simultâneos** <br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>

Com 2 demorou: 0.005403995513916016<br><br>

3. **Com 5 clientes simultâneos** <br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>

Com 5 demorou: 0.008816003799438477 <br><br>

4. **Com 10 clientes simultâneos** <br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>
Status: 200 <br>
Motivo: OK <br>
Conteúdo: (HTML fornecido no código da atividade)<br>

Com 10 demorou: 0.015780210494995117<br><br>

Assim como o sem thread observamos que quanto mais clientes simultâneos mais tempo o servidor demora. Pórem, existe uma uma diferença notável vamos ver essa análise comparativa de valores: 

| Clientes Simultâneos | Sem Thread | Com Thread |
|----------------------|------------|------------|
| 1                    | 0.0040     | 0.0038     |
| 2                    | 0.0062     | 0.0054     |
| 5                    | 0.0112     | 0.0088     |
| 10                   | 0.02383    | 0.0157     |
<br>
Assim, podemos afirmar que com o uso de thread o processo é bem mais rápido e notamos essa diferença considerável principalmente com valores maiores de clientes simultâneos. Isso é em decorrência do uso de threads ser em suma a divisão desses processos que serão intercalados exinguindo a necessidade de aguardar um processo finalizar para iniciar outro com ocorre sem threads. Sem threads ele trata a requisção como uma só e a faz em sequência enquanto com threads as requisições são atendidadas várias ao mesmo tempo.
