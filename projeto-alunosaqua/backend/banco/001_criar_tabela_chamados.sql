-- Adaptado para o AlunoSaqua: chamados representam solicitacoes da comunidade escolar.
CREATE TABLE IF NOT EXISTS chamados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(120) NOT NULL,
    descricao TEXT NOT NULL,
    prioridade VARCHAR(20) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'aberto',
    criado_em TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT chamados_prioridade_valida
        CHECK (prioridade IN ('baixa', 'media', 'alta')),
    CONSTRAINT chamados_status_valido
        CHECK (status IN ('aberto', 'em_andamento', 'fechado'))
);
