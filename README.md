# 🏛️ Desafio Técnico TI — Cartório Leandro Félix
## Vaga: Suporte Técnico em T.I
### Projeto: "CartórioLF Support & Backup Toolkit"

Seja bem-vindo(a) à etapa prática do processo seletivo da equipe de Tecnologia da Informação do **Cartório Leandro Félix** (Caldas Novas - GO).

---

## 🎯 Objetivo do Desafio
Nosso objetivo **não é pedir que você faça testes que dependam da nossa rede interna**, mas sim avaliar como você **cria uma ferramenta real, útil e autocontida** para a rotina de um departamento de TI.

Você irá aprimorar e completar o script `cartorio_toolkit.py`, que atua em três frentes essenciais do cartório:
1. **Diagnóstico de Estação & Chamados no GLPI** (Suporte ao usuário).
2. **Rotina de Backup Seguro & Auditoria SHA-256** (Segurança e conformidade).
3. **Uso de IA Generativa & Relatório Técnico** (Automação e documentação).

---

## 🗂️ Estrutura do Repositório

```text
desafio_template/
├── 📄 README.md                        # Instruções do desafio e regras de entrega
├── 📄 TRILHA_INVESTIGACAO_TEMPLATE.md  # Template OBRIGATÓRIO do seu relatório
├── 🐍 cartorio_toolkit.py              # Script principal com a estrutura e os TODOs
├── ⚙️ config.json                      # Configurações do ambiente do cartório
├── 📁 dados_cartorio/                  # Arquivos simulados para teste do backup
├── 📁 backup_local/                    # Onde o backup .zip gerado deve ser salvo
└── 📁 logs/                            # Onde os logs e o ticket GLPI serão gravados
```

---

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o **Python 3.8+** instalado.
2. Clone o repositório ou descompacte os arquivos na sua máquina.
3. No terminal, execute:
   ```bash
   python cartorio_toolkit.py
   ```
4. Observe os logs no terminal e o que foi gerado na pasta `logs/`.

---

## 📋 As 3 Tarefas que Você Deve Implementar

### 🔹 Tarefa 1: Diagnóstico da Estação para o GLPI (`diagnosticar_estacao`)
Quando um escrevente relata lentidão ou falha, o técnico roda essa função para capturar os dados reais da máquina.
* Capture o **IP local real**, o **hostname**, o **usuário logado** e o **Sistema Operacional**.
* Calcule o **espaço livre em disco da partição principal** (ex: `C:\` no Windows ou `/` no Linux). Se estiver abaixo de 20%, marque como `CRÍTICO`.
* Crie o arquivo `logs/ticket_glpi_gerado.txt` formatado de forma limpa, pronto para colar em um chamado do GLPI com data e hora.

### 🔹 Tarefa 2: Backup Local & Integridade Criptográfica (`executar_backup_e_auditoria`)
Segurança jurídica exige comprovação de que os atos notariais foram salvos sem corrupção de dados.
* Verifique se a pasta `dados_cartorio/` existe e possui arquivos.
* Calcule o hash **SHA-256** de cada arquivo antes de compactar.
* Compacte todos os arquivos em um único `.zip` salvo em `backup_local/` com o nome no padrão: `backup_cartorio_YYYYMMDD_HHMMSS.zip`.
* Grave no arquivo de log (`logs/auditoria_cartorio.log`) o status, a lista de arquivos e seus respectivos hashes SHA-256.

### 🔹 Tarefa 3: Resumo com IA & Trilha de Resolução (`TRILHA_INVESTIGACAO.md`)
* Edite o arquivo `TRILHA_INVESTIGACAO_TEMPLATE.md`, renomeie para `TRILHA_INVESTIGACAO.md` e preencha todas as seções:
  * Como você pensou e construiu a solução.
  * Quais prompts você usou em IAs generativas (ChatGPT, Claude, etc.) e como validou o código.
  * Suas respostas para os 4 estudos de caso reais do cartório (desligamento, pedido de senha por WhatsApp, pfSense VPN vs NAT e recuperação de desastres).

---

## 📤 Como Realizar a Entrega (Passo a Passo)

Para avaliar sua familiaridade com o fluxo profissional de Git e GitHub, siga este processo:

### 1. Preparação no seu GitHub (Repositório Privado OBRIGATÓRIO):
> ⚠️ **Importante (Sigilo do Processo):** Para garantir o sigilo das respostas e igualdade entre os concorrentes, **não faça Fork público**. Crie um **repositório privado** na sua conta:

1. **Baixe os arquivos** (via Git Clone ou Download ZIP) deste repositório para o seu computador.
2. No seu GitHub pessoal, crie um **novo repositório** com visibilidade **Privada (Private)** (ex: `desafio-ti-cartorio`).
3. Suba os arquivos base para o seu repositório privado.
4. Acesse **Settings > Collaborators** do seu repositório e adicione o usuário **`humbertofo`** como colaborador (necessário para que a equipe de TI consiga avaliar sua entrega).
5. Crie uma branch chamada `solucao-[seu-nome]` (ex: `solucao-rodrigo-fernandes`) e faça commits organizados à medida que resolver cada tarefa.

### 2. O que deve conter no seu repositório:
* O script `cartorio_toolkit.py` funcional e documentado.
* O arquivo `TRILHA_INVESTIGACAO.md` (renomeado a partir de `TRILHA_INVESTIGACAO_TEMPLATE.md`) com todas as seções preenchidas.
* O arquivo `config.json` e os arquivos de teste originais preservados.

### 3. Envio da Solução:
Envie um e-mail para **`humberto.oliveira@cartorioleandrofelix.com.br`** com o seguinte formato:

* **Para:** `humberto.oliveira@cartorioleandrofelix.com.br`
* **Assunto:** `[Desafio Técnico TI - Cartório Leandro Félix] Solução - [Seu Nome Completo]`
* **Corpo do e-mail:**
  > Olá, Humberto!  
  > Segue o link com a minha solução do desafio técnico para a vaga de Suporte Técnico em T.I:  
  > 🔗 **Link do meu repositório:** `https://github.com/[seu-usuario]/desafio-tecnico-ti-cartorio`  
  >  
  > *Breve resumo da minha abordagem:* [1 a 2 parágrafos contando como estruturou a solução]  
  > *Meu WhatsApp de contato:* [Seu Telefone]  
  >  
  > Fico à disposição para a defesa técnica e entrevista!

---

## ⏱️ Prazo de Entrega
* **Data Limite:** Até **Segunda-feira, 19/10/2026 às 12:00h** (horário de Brasília). Soluções enviadas após este horário não serão computadas.

Boa sorte! Queremos ver como você estrutura seu código, sua linha de raciocínio e seu compromisso técnico.

