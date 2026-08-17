# Planejamento inicial do sistema de chamados

## Apresentação da proposta

Este documento registra a primeira definição do sistema de chamados. A intenção foi começar pelo problema e pelo fluxo de atendimento, sem transformar a atividade em uma implementação antecipada.

A escolha por uma solução web conversa com meu interesse em desenvolvimento de aplicações e com os estudos de Python e desenvolvimento web apresentados no meu perfil. Neste momento, porém, o foco é a especificação: deixar claro o que o sistema deve resolver antes de decidir detalhes de código, banco ou infraestrutura.

## 1. Descrição do problema e do domínio

A empresa de suporte técnico registra solicitações de pessoas clientes em planilhas e mensagens dispersas. Essa forma de trabalho dificulta localizar os chamados, acompanhar o andamento dos atendimentos e manter um histórico confiável.

A aplicação proposta será um sistema web de gestão de chamados para o domínio de suporte técnico. Seu objetivo é centralizar o registro e o acompanhamento das solicitações, permitindo que a pessoa cliente acompanhe seu chamado e que a equipe de suporte organize o atendimento.

## 2. Escopo inicial

### Incluído na primeira versão

- Cadastro de chamados por uma pessoa cliente.
- Consulta de chamados.
- Acompanhamento do status do chamado pela pessoa cliente.
- Atualização de status pela pessoa atendente.
- Encerramento de chamados resolvidos pela pessoa atendente.

### Fora do escopo inicial

- Notificações automáticas.
- Anexos em chamados.
- Relatórios gerenciais.
- Integração com outros canais de atendimento.

### Evolução futura

Como evolução futura, poderá ser incluído um serviço de notificações para informar mudanças de status à pessoa cliente. Essa funcionalidade não faz parte da primeira versão. Outras evoluções possíveis são anexos e relatórios, mas elas só devem ser analisadas depois que o fluxo básico estiver bem definido.

## 3. Pessoas usuárias e objetivos

| Pessoa usuária | Objetivo principal |
|---|---|
| Pessoa cliente | Registrar uma solicitação e acompanhar o andamento do chamado. |
| Pessoa atendente | Consultar chamados, atualizar seus status e encerrá-los quando resolvidos. |

## 4. Requisitos funcionais

- **RF01 — Cadastro:** O sistema deve permitir que uma pessoa cliente registre um chamado com título e descrição.
- **RF02 — Consulta:** O sistema deve permitir que uma pessoa cliente consulte os chamados registrados por ela.
- **RF03 — Consulta de atendimento:** O sistema deve permitir que uma pessoa atendente consulte os chamados abertos.
- **RF04 — Atualização:** O sistema deve permitir que uma pessoa atendente altere o status de um chamado.
- **RF05 — Encerramento:** O sistema deve permitir que uma pessoa atendente encerre um chamado quando a solicitação for resolvida.

## 5. Recursos principais do sistema

| Recurso | Possíveis informações armazenadas |
|---|---|
| Chamado | Identificador, título, descrição, status e data de abertura. |
| Cliente | Identificador, nome e contato. |
| Atendente | Identificador e nome. |
| Categoria | Identificador e nome. |

Não são definidos tabelas ou tipos de dados nesta etapa de planejamento.

## 6. Fluxo prioritário: registrar chamado

1. A pessoa cliente acessa a tela de abertura de chamado.
2. A pessoa cliente informa o título e a descrição da solicitação.
3. A interface web valida o preenchimento básico e envia as informações para a API.
4. A API encaminha a solicitação ao back-end.
5. O back-end valida os dados e aplica as regras de negócio para criar o chamado com status inicial aberto.
6. O banco de dados armazena o registro do chamado.
7. A aplicação retorna uma confirmação para a interface web.
8. A interface informa à pessoa cliente que o chamado foi registrado e apresenta seu identificador e status.

## 7. Comunicação entre os componentes

- A interface web coleta os dados, apresenta as telas e exibe os resultados para a pessoa usuária.
- A API recebe as solicitações da interface e devolve respostas para ela.
- O back-end concentra as validações e as regras de negócio, como a criação e a alteração de status de chamados.
- O banco de dados armazena os chamados e os dados relacionados a clientes, atendentes e categorias.
- A comunicação principal segue o sentido: pessoa usuária → interface web → API → back-end → banco de dados. As respostas retornam pelo caminho inverso.

Essa separação foi escolhida porque facilita compreender o papel de cada parte do sistema. Ela também cria uma base coerente para uma futura implementação em Python, sem obrigar que a tecnologia seja definida agora.

## 8. Respostas às perguntas de revisão

- **O que a interface faz neste fluxo?** Coleta o título e a descrição, envia os dados e apresenta a confirmação do cadastro.
- **Qual regra precisa ficar no back-end?** Validar os dados recebidos, definir o status inicial como aberto e autorizar a criação do chamado.
- **Onde os chamados são armazenados?** No banco de dados.
- **Qual componente pode ser substituído com menor impacto se as responsabilidades estiverem separadas?** A interface web pode ser substituída por outra interface, desde que continue se comunicando com a API; o armazenamento também pode evoluir sem alterar diretamente a interface.

## 9. Decisões da equipe

- A primeira versão será limitada às operações essenciais de chamados: cadastrar, consultar, atualizar status e encerrar.
- O fluxo prioritário escolhido será o registro de chamado.
- As regras de negócio ficarão concentradas no back-end.
- A interface web se comunicará com o back-end por meio de uma API.
- A proposta será mantida simples nesta etapa, para que a futura implementação possa ser feita gradualmente durante os estudos de desenvolvimento web.
- Notificações, anexos e relatórios serão tratados como evoluções posteriores.

## 10. Dúvida em aberto

Ainda precisa ser definido quais valores de status serão utilizados além de “aberto” e “encerrado”, por exemplo, se haverá os estados “em atendimento” e “aguardando retorno”. Também será necessário decidir, em uma etapa futura, qual tecnologia de armazenamento atende melhor ao volume esperado de chamados.

## 11. Checklist da entrega

- [x] Problema e domínio descritos de forma objetiva.
- [x] Escopo inicial delimitado.
- [x] Evolução futura registrada fora do escopo.
- [x] Duas pessoas usuárias identificadas.
- [x] Cinco requisitos funcionais definidos.
- [x] Recursos principais listados.
- [x] Fluxo prioritário descrito passo a passo.
- [x] Comunicação entre interface, API, back-end e banco explicada.
- [x] Decisões e dúvida em aberto registradas.
