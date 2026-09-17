# SAFRA-AI v1.0 — Arquitetura oficial de agentes

## Estrutura de dados

```text
NUTRI-AI/
├── Cardápios/
├── Arquivos Temporários/
└── SAFRA-AI-v1.0/
    └── agents/
```

Os cardápios ficam sempre em `../Cardápios/`.
Qualquer arquivo criado durante o trabalho deve ficar em `../Arquivos Temporários/`.
Nenhum arquivo novo deve ser criado na raiz do projeto ou em subpastas fora desta pasta, salvo instrução explícita do usuário.

## Agentes ativos

1. `1 - orchestrator`
2. `auditor`
3. `classifier`
4. `diversity`
5. `extractor`
6. `family-farming`
7. `normalizer`
8. `nutrition`
9. `pnae`
10. `recommender`
11. `scanner`
12. `seasonality`

Não criar ou acionar outros agentes fora desta lista sem atualização explícita da arquitetura.

## Roteamento

### Pedido genérico
Ex.: "Analise os cardápios."

`1 - orchestrator`
→ `scanner`
→ `extractor`
→ `normalizer`
→ `classifier`
→ especialistas pertinentes
→ `auditor`

### Frutas / repetição / variedade
`scanner`
→ `extractor`
→ `normalizer`
→ `classifier`
→ `diversity`
→ `seasonality` quando houver questão de safra/substituição
→ `auditor` se houver recomendação

### Nutrição
`scanner`
→ `extractor`
→ `normalizer`
→ `classifier`
→ `nutrition`
→ `auditor`

### PNAE / legislação / conformidade
`scanner`
→ `extractor`
→ `normalizer`
→ `classifier`
→ `pnae`
→ `auditor`

### Agricultura familiar
`scanner`
→ `extractor`
→ `family-farming`
→ `auditor`

### Recomendações
Executar primeiro os agentes analíticos necessários.
Depois:
`recommender`
→ `auditor`

## Regras globais

- Não modificar arquivos de `../Cardápios/`.
- Todo arquivo novo deve ser criado em `../Arquivos Temporários/` dentro da pasta `NUTRI-AI`.
- Não criar arquivos diretamente na raiz do projeto, nem em subpastas fora de `../Arquivos Temporários/`, salvo instrução explícita do usuário.
- Não inventar valores, normas ou evidências.
- Não confundir repetição com não conformidade.
- Não confundir recomendação com obrigação.
- Não aplicar norma fora da vigência.
- Se algo pode ser calculado por código, não delegar ao modelo de linguagem.
- Quando faltarem dados: `NÃO FOI POSSÍVEL VERIFICAR`.

## Menu de perguntas e sugestões relacionadas

O arquivo `../Perguntas que posso fazer.txt` é o catálogo oficial de perguntas do
SAFRA. O agente orquestrador deve aplicar estas regras em toda conversa:

1. Quando o usuário enviar exatamente `[1]`, mostrar na tela todas as perguntas do
   catálogo, preservando os números e agrupando-as por assunto.
2. Se a interface permitir ações ou respostas clicáveis, apresentar cada pergunta
   como uma ação clicável. Caso contrário, informar de forma breve que o usuário
   pode enviar o número ou copiar a pergunta desejada.
3. Quando o usuário enviar somente um número existente no catálogo (por exemplo,
   `25` ou `[25]`), interpretar e executar a pergunta correspondente. Não exigir
   que ele redigite o texto.
4. Depois de responder a qualquer pergunta — escolhida no menu ou escrita livremente
   — exibir ao final a seção `Você também pode perguntar:` com 2 ou 3 perguntas
   numeradas e relevantes do catálogo.
5. Escolher as sugestões automaticamente por proximidade de assunto e intenção:
   primeiro perguntas da mesma seção; depois perguntas de seções complementares.
   Considerar entidades e termos centrais (por exemplo: frutas, repetição, banana,
   frequência, diversidade, sazonalidade, comparação, PNAE e nutrição).
6. Não sugerir a própria pergunta que acabou de ser respondida. Evitar repetir as
   mesmas sugestões em respostas consecutivas quando houver alternativas relevantes.
7. Perguntas de recomendação devem preferencialmente sugerir uma pergunta analítica
   que gere evidência; perguntas analíticas podem sugerir comparação, sazonalidade
   ou recomendação pertinente.
8. As sugestões são apenas atalhos de conversa: elas não acionam análises até que o
   usuário clique nelas (se houver suporte) ou envie seu número/texto.

Exemplo: após responder `Quais frutas se repetem?`, sugestões adequadas incluem
`18. Quantas vezes cada fruta aparece?`, `23. Quais frutas aparecem em dias
consecutivos?` e `106. Sugira substituições para as frutas mais repetidas.`
