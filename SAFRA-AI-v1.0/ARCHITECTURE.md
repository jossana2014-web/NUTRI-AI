# Arquitetura SAFRA-AI v1.0

## Estrutura física

```text
NUTRI-AI/
├── Cardápios/
└── SAFRA-AI-v1.0/
    ├── agents/
    │   ├── 1 - orchestrator/
    │   ├── auditor/
    │   ├── classifier/
    │   ├── diversity/
    │   ├── extractor/
    │   ├── family-farming/
    │   ├── normalizer/
    │   ├── nutrition/
    │   ├── pnae/
    │   ├── recommender/
    │   ├── scanner/
    │   └── seasonality/
    ├── skills/
    ├── specs/
    ├── rules/
    ├── knowledge/
    ├── data/
    ├── src/
    ├── runtime/
    └── output/
```

## Princípio de projeto

Manter poucos agentes, cada um com função técnica clara. Evitar fragmentação em agentes
redundantes. O Orchestrator faz roteamento; os especialistas executam análises; o Auditor
faz a revisão final.

## Núcleo necessário

- Orchestrator: roteamento.
- Scanner: descoberta de documentos.
- Extractor: leitura/extração.
- Normalizer: padronização.
- Classifier: classificação alimentar.
- Diversity: variedade e repetição.
- Nutrition: análise nutricional.
- PNAE: conformidade normativa.
- Seasonality: sazonalidade/regionalidade.
- Family Farming: agricultura familiar.
- Recommender: recomendações.
- Auditor: controle de consistência.
