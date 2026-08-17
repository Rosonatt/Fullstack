# Projeto Chamados

> Planejamento inicial de uma aplicação web para organização de solicitações de suporte técnico.

## Sobre este projeto

Este repositório foi desenvolvido como parte do meu processo de aprendizagem em Engenharia de Software e desenvolvimento web. A proposta é transformar um problema comum de atendimento — informações espalhadas em planilhas e mensagens — em uma solução simples, organizada e possível de evoluir.

Como venho estudando Python e desenvolvimento de aplicações web, escolhi tratar o projeto com uma separação clara entre interface, API, regras de negócio e armazenamento. Essa organização também se aproxima da forma como pretendo estruturar projetos futuros com tecnologias como Flask ou FastAPI, sem antecipar a implementação nesta atividade.

## Objetivo

Planejar um sistema de chamados que permita centralizar o registro, a consulta e o acompanhamento de solicitações de suporte técnico.

## Escopo da primeira versão

A primeira versão contempla:

- cadastro de chamados;
- consulta de chamados;
- acompanhamento e atualização de status;
- encerramento de chamados resolvidos.

Notificações, anexos, relatórios e integrações com outros canais ficam como possibilidades de evolução e não fazem parte desta etapa.

## Organização do projeto

- `docs/planejamento-semana-1.md`: problema, escopo, usuários, requisitos, recursos, fluxo, decisões e dúvida em aberto.
- `docs/diagrama-arquitetura.md`: diagrama arquitetural simplificado e explicação da comunicação entre componentes.
- `docs/contrato-api-chamados.md`: contrato inicial da API elaborado para a Atividade 2.
- `frontend/`: espaço reservado para a futura interface web.
- `backend/`: espaço reservado para a futura API e as regras de negócio.
- `database/`: espaço reservado para o futuro armazenamento dos dados.

## Andamento das atividades

### Atividade 1 — Planejamento inicial

Nesta primeira etapa, foram definidos o problema do sistema, o escopo inicial, as pessoas usuárias, os requisitos funcionais, os principais recursos, o fluxo prioritário e a arquitetura simplificada. Essa parte continua registrada nos documentos de planejamento e diagrama deste repositório.

### Atividade 2 — Contrato inicial da API

**Alteração feita para a Atividade 2:** foi acrescentado o contrato inicial da API de chamados, mantendo o planejamento original da Atividade 1. O novo documento descreve o recurso `chamados`, seus atributos, os endpoints de listagem, consulta, criação, atualização e remoção, os códigos HTTP previstos, exemplos em JSON, decisões técnicas, dúvidas pendentes e o ajuste realizado após a revisão por outra equipe.

A Atividade 2 representa um avanço do planejamento para a definição de como o futuro front-end e o back-end deverão se comunicar. Ainda não há implementação de código: o contrato serve como referência para uma etapa posterior de desenvolvimento.

## Relação com meu percurso

Este planejamento representa uma etapa anterior à programação: primeiro delimitar o problema, entender as pessoas usuárias e definir responsabilidades; depois escolher as tecnologias e implementar. Essa sequência é especialmente importante para mim porque conecta os estudos de Python e web aos fundamentos de arquitetura e organização de software.

## Observação

Esta entrega é exclusivamente de planejamento. Conforme o enunciado da atividade, não é necessário criar código de front-end, back-end ou banco de dados nesta etapa.
