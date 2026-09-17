---
name: nutri-ai
description: Analisa cardápios escolares do projeto NUTRI-AI, incluindo frutas, repetição, diversidade, sazonalidade e perguntas relacionadas ao PNAE. Use quando o usuário pedir análise de cardápios escolares ou alimentos oferecidos.
---

# NUTRI-AI

Analise cardápios do projeto aberto no workspace. A skill precisa ser usada com
a pasta clonada do NUTRI-AI aberta; ela não contém os cardápios em si.

## Localização dos dados

No diretório do projeto, os cardápios ficam em `Cardápios/` e o SAFRA-AI fica
em `SAFRA-AI-v1.0/`. Se essas pastas não estiverem no workspace, peça ao usuário
para abrir a cópia local do repositório ou informar o caminho dela.

Antes de uma análise ampla, leia `SAFRA-AI-v1.0/AGENTS.md`. Para consultas sobre
frutas, repetição ou variedade, siga o fluxo de extração, normalização e
classificação descrito nele.

## Análise de cardápios

1. Localize os arquivos do período solicitado em `Cardápios/`.
2. Para PDFs, extraia o texto com `pypdf`. Para imagens ou planilhas, use uma
   forma apropriada de leitura antes de concluir a análise.
3. Para perguntas sobre frutas oferecidas, conte a fruta indicada na refeição
   ou linha `FRUTA`. Só inclua frutas usadas como ingrediente em sucos,
   vitaminas ou preparações se o usuário pedir isso explicitamente.
4. Informe as datas, alimentos e quantidades que fundamentam a resposta.
5. Se o documento não permitir confirmar uma informação, responda `NÃO FOI
   POSSÍVEL VERIFICAR` e explique brevemente o motivo.

## Preservação dos arquivos

Não modifique arquivos em `Cardápios/`. Se for necessário gerar algum arquivo
temporário durante a análise, use `Arquivos Temporários/` na raiz do projeto.
