# NUTRI-AI / SAFRA-AI v1.0

## Estrutura oficial de distribuição

```text
NUTRI-AI/
├── Cardápios/
└── SAFRA-AI-v1.0/
```

A pasta `Cardápios` é propositalmente entregue vazia. O usuário cola nela os seus
cardápios antes ou durante o uso.

A pasta `SAFRA-AI-v1.0` contém toda a arquitetura: agentes, skills, specs, regras,
conhecimento, código, auditoria e saídas.

## Como usar

1. Descompacte `NUTRI-AI.zip`.
2. Abra a pasta mãe `NUTRI-AI` na IDE.
3. Cole os arquivos de cardápio em `NUTRI-AI/Cardápios/`.
4. Use o agente de IA da IDE e faça pedidos em linguagem natural, por exemplo:
   - "Analise os cardápios."
   - "Compare março e abril."
   - "Quais frutas mais se repetem?"
   - "Faça uma análise segundo as regras carregadas."
5. O agente deve ler `SAFRA-AI-v1.0/AGENTS.md` e `SAFRA-AI-v1.0/PROJECT.md`
   antes da análise e acionar somente os componentes necessários.

## Observação técnica importante

O comportamento automático depende de a IDE/agente suportar instruções de projeto,
leitura de arquivos e execução de comandos. O SAFRA fornece a arquitetura e as instruções,
mas uma IDE que não possua agente de IA não consegue "acionar agentes" por si só.

Para reduzir dependência de IDE, o SAFRA também pode ser executado por terminal.
