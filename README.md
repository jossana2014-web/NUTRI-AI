# NUTRI-AI

Repositório do projeto NUTRI-AI, voltado à leitura e análise de cardápios
escolares, com foco em frutas, diversidade alimentar, sazonalidade e
critérios do PNAE.

## Estrutura

- `Cardápios/`: cardápios de referência em PDF.
- `SAFRA-AI-v1.0/`: código, documentação e especificações do SAFRA-AI.
- `skills/nutri-ai/`: skill instalável para analisar os cardápios no Codex.
- `Perguntas que posso fazer.txt`: catálogo de consultas disponíveis.

## Usar a skill no Codex

Após clonar ou baixar este repositório, instale as dependências e copie a skill
para a pasta de skills do Codex.

No Windows PowerShell:

```powershell
cd NUTRI-AI
python -m pip install -r .\SAFRA-AI-v1.0\requirements.txt
Copy-Item -Recurse .\skills\nutri-ai "$env:USERPROFILE\.codex\skills\nutri-ai"
```

Abra uma nova conversa no Codex com a pasta `NUTRI-AI` como workspace. Depois,
use `$nutri-ai` ou faça perguntas normalmente, por exemplo:

```text
$nutri-ai Quais frutas se repetem nos cardápios de abril?
```

## Adicionar ou trocar cardápios

Os arquivos analisados ficam em `Cardápios/`. Para usar os seus próprios
cardápios:

1. Adicione arquivos PDF, PNG, JPG, JPEG, XLSX ou CSV à pasta `Cardápios/`.
2. Remova ou substitua os arquivos existentes se não quiser incluí-los nas
   análises.
3. Dê preferência a nomes que incluam o período ou mês, como
   `CARDÁPIO ABRIL 2026.pdf`; isso ajuda a identificar o período correto.
4. Não altere a estrutura de `SAFRA-AI-v1.0/`.

Os arquivos originais não são modificados durante a análise.

## SAFRA-AI

Consulte as instruções em [SAFRA-AI-v1.0/README.md](SAFRA-AI-v1.0/README.md).

## Licença

Este projeto está licenciado sob os termos descritos em
[SAFRA-AI-v1.0/LICENSE](SAFRA-AI-v1.0/LICENSE).
