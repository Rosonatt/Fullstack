# AlunoSaqua

## Integrantes

- Bruno Oliveira
- Natalia Cardoso
- Raissa Queiroz
- Rosonatt Ferreira
- Ryan Guiwison

## Sobre o projeto

O AlunoSaqua é uma ideia de sistema para ajudar a escola a organizar melhor sua rotina. A proposta é reunir em um só lugar informações e pedidos de alunos, responsáveis, professores e funcionários.

A escola costuma receber dúvidas e solicitações por vários lugares. Às vezes isso acaba dificultando o acompanhamento. Com o AlunoSaqua, a pessoa poderia registrar o que precisa e acompanhar o andamento até receber uma resposta.

O projeto também pode crescer com o tempo e receber outras áreas, como notas, frequência, comunicados, cadastro de usuários e comunicação com a equipe pedagógica.

> **Comentário do grupo:** escolhemos esse tema porque ele faz sentido para o dia a dia de uma escola e dá espaço para criar várias funções úteis sem deixar a ideia confusa.

## Objetivo

Criar uma aplicação web simples para organizar solicitações da comunidade escolar e facilitar o contato com a equipe responsável.

## O que a primeira versão faz

- registra uma solicitação feita por aluno, responsável ou funcionário;
- permite consultar as solicitações registradas;
- mostra o andamento de cada solicitação;
- permite que a equipe responsável atualize o status;
- permite encerrar uma solicitação resolvida;
- guarda título, descrição, prioridade e situação do atendimento.

## O que pode entrar depois

- notas e médias;
- controle de frequência;
- envio de arquivos e imagens;
- notificações;
- relatórios para a direção;
- comunicação com outras plataformas da escola;
- organização por unidade, turma ou setor.

## Organização

- `docs/planejamento-semana-1.md`: planejamento, problema, usuários, requisitos e fluxo principal.
- `docs/diagrama-arquitetura.md`: visão de como as partes do sistema se comunicam.
- `docs/contrato-api-chamados.md`: regras e exemplos das solicitações da aplicação.
- `frontend/`: parte visual do sistema.
- `backend/`: regras e funcionamento da aplicação.
- `database/`: dados que serão armazenados.

## Como pensamos o sistema

A pessoa acessa o AlunoSaqua pelo site, preenche uma solicitação e envia. A aplicação confere os dados, registra a informação e mostra o status para quem fez o pedido. A equipe da escola consegue consultar as solicitações e atualizar o atendimento.

A parte visual conversa com a API, o back-end cuida das regras e o banco guarda os dados.

## Projeto de referência

O AlunoSaqua foi pensado a partir do projeto disponível em [github.com/Rosonatt/PEI5](https://github.com/Rosonatt/PEI5), que apresenta diferentes áreas para a administração escolar, direção, professores, alunos, responsáveis e equipe pedagógica.

Nesta etapa, o grupo focou em uma parte menor para deixar a proposta mais clara e possível de desenvolver. As outras funções podem ser adicionadas aos poucos.

> **Comentário do grupo:** a ideia é começar com algo simples, mas que realmente ajude a escola. Depois, outras funções podem ser encaixadas sem precisar refazer tudo.
