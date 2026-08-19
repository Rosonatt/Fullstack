# Planejamento do AlunoSaqua

## Integrantes

- Bruno Oliveira
- Natalia Cardoso
- Rosonatt Ferreira
- Ryan Guiwison

## 1. A ideia do projeto

O AlunoSaqua é um sistema web pensado para ajudar na organização de uma escola. A ideia é facilitar o acesso a informações e deixar mais simples o envio e o acompanhamento de pedidos feitos pela comunidade escolar.

Hoje uma dúvida ou um problema pode ser passado por mensagem, pessoalmente ou em uma anotação. Quando isso acontece em vários lugares, é fácil perder alguma informação. O AlunoSaqua reúne esses pedidos e ajuda a escola a saber o que ainda precisa ser atendido.

> **Comentário do grupo:** pensamos em colocar muitas funções logo de início, mas preferimos começar por uma parte menor. Assim, o projeto fica mais fácil de entender e de desenvolver.

## 2. Problema e público

O sistema será voltado para alunos, responsáveis, professores, funcionários, coordenação e direção. Cada pessoa terá uma necessidade diferente, mas todas poderão encontrar um espaço mais organizado para resolver assuntos da escola.

O foco inicial será o registro e o acompanhamento de solicitações. Elas podem ser dúvidas sobre frequência, problemas de acesso, pedidos de informação ou outras situações que precisem ser encaminhadas para alguém da escola.

## 3. Escopo inicial

### Nesta primeira parte

- registrar uma solicitação com título e descrição;
- informar o nível de prioridade;
- consultar solicitações cadastradas;
- filtrar pelo status;
- atualizar o andamento;
- encerrar uma solicitação resolvida;
- identificar quem fez o pedido.

### Para uma próxima etapa

- cadastro completo de alunos e funcionários;
- notas e médias;
- frequência;
- notificações automáticas;
- envio de arquivos;
- relatórios;
- integração com outros sistemas;
- organização por diferentes unidades escolares.

## 4. Pessoas usuárias

| Pessoa | O que pode fazer |
|---|---|
| Aluno ou aluna | Enviar uma dúvida ou pedido e acompanhar a resposta. |
| Responsável | Pedir ajuda sobre assuntos do aluno e ver o andamento. |
| Professor ou professora | Registrar uma situação da rotina escolar. |
| Funcionário | Enviar uma solicitação para o setor responsável. |
| Equipe da escola | Consultar os pedidos e atualizar o atendimento. |
| Direção ou coordenação | Acompanhar a organização geral em uma próxima versão. |

## 5. Requisitos funcionais

- **RF01 — Cadastro:** permitir que a pessoa registre uma solicitação com título, descrição e prioridade.
- **RF02 — Consulta:** permitir que a pessoa veja as solicitações feitas por ela.
- **RF03 — Consulta da equipe:** permitir que a equipe veja as solicitações que precisam de atendimento.
- **RF04 — Filtro:** permitir a busca por situação, como aberta, em atendimento ou resolvida.
- **RF05 — Atualização:** permitir que a equipe altere o status e acompanhe o andamento.
- **RF06 — Encerramento:** permitir que uma solicitação seja encerrada quando o problema for resolvido.

## 6. Informações principais

| Informação | Exemplos de dados |
|---|---|
| Solicitação | Número, título, descrição, prioridade, status e data. |
| Usuário | Nome, matrícula, tipo de usuário e contato. |
| Escola | Nome, endereço e unidade. |
| Categoria | Tipo do pedido e setor responsável. |

Essas informações mostram o que o sistema poderá precisar. A estrutura do banco pode ser detalhada quando a implementação começar.

## 7. Fluxo principal

1. A pessoa entra no AlunoSaqua.
2. Escolhe a opção para fazer uma solicitação.
3. Preenche o título, a descrição e a prioridade.
4. O sistema confere se os campos necessários foram preenchidos.
5. Os dados são enviados para a aplicação.
6. A solicitação é salva com o status `aberto`.
7. A pessoa recebe o número do registro e consegue acompanhar o andamento.
8. A equipe da escola consulta o pedido e atualiza o status quando trabalhar nele.

## 8. Como as partes se comunicam

- A **interface** mostra as telas e recebe as informações.
- A **API** faz a comunicação entre a tela e o restante do sistema.
- O **back-end** confere os dados e aplica as regras.
- O **banco de dados** guarda as solicitações e os dados dos usuários.

O caminho principal é: pessoa usuária → interface → API → back-end → banco de dados. Depois, a resposta volta até a tela.

## 9. Decisões do grupo

- O projeto terá o nome AlunoSaqua e será voltado para a realidade escolar.
- A primeira parte será o registro e acompanhamento de solicitações.
- O formato das mensagens da API será JSON.
- O status inicial de uma solicitação será `aberto`.
- As regras ficarão no back-end.
- Notas, frequência e notificações poderão ser incluídas mais tarde.
- O sistema será feito por partes, começando pelo fluxo mais importante.

## 10. Dúvidas para as próximas etapas

- Como a pessoa será identificada para fazer uma solicitação?
- Cada pedido será enviado automaticamente para um setor?
- Quais status serão usados até o atendimento terminar?
- O sistema será usado por uma escola ou por várias?
- Será possível anexar documentos e imagens?

> **Comentário do grupo:** essas partes ainda podem mudar quando começarmos a montar as telas e pensar melhor na implementação.

## 11. Checklist

- [x] Problema descrito.
- [x] Público definido.
- [x] Escopo inicial separado das próximas ideias.
- [x] Usuários identificados.
- [x] Requisitos funcionais definidos.
- [x] Informações principais listadas.
- [x] Fluxo principal explicado.
- [x] Interface, API, back-end e banco apresentados.
- [x] Decisões e dúvidas do grupo registradas.
