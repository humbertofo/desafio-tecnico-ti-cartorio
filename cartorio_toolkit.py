"""
================================================================================
CARTÓRIO LEANDRO FÉLIX - DEPARTAMENTO DE TI
Projeto: Support & Backup Toolkit (Desafio Técnico de Seleção)
================================================================================
Candidato: [Preencha seu Nome]
Data: [DD/MM/AAAA]

Este script é uma ferramenta modular que auxilia o suporte de TI do Cartório em:
  1. Diagnóstico rápido de estações de trabalho e geração de tickets para o GLPI.
  2. Rotina de backup local de dados notariais com verificação de integridade SHA-256.
  3. Resumo inteligente da saúde do ambiente.
"""

import os
import sys
import json
import socket
import getpass
import platform
import shutil
import hashlib
import zipfile
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

def registrar_log(mensagem, nivel="INFO", arquivo_log=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{timestamp}] [{nivel}] {mensagem}"
    print(linha)
    if arquivo_log:
        os.makedirs(os.path.dirname(os.path.abspath(arquivo_log)), exist_ok=True)
        with open(arquivo_log, "a", encoding="utf-8") as f:
            f.write(linha + "\n")

def carregar_config():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Arquivo config.json não encontrado em: {CONFIG_PATH}")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# ==============================================================================
# MÓDULO 1: DIAGNÓSTICO DE ESTAÇÃO & TICKET GLPI
# ==============================================================================
def diagnosticar_estacao(config):
    """
    [TAREFA 1 - DO CANDIDATO]:
    Coleta informações técnicas da máquina para gerar um chamado padronizado no GLPI.
    
    O que deve fazer:
      1. Coletar: Nome do computador (Hostname), usuário do Windows/Linux logado,
         Sistema Operacional e IP local da máquina.
      2. Checar espaço em disco da partição principal (ex: 'C:\\' ou '/'):
         - Calcular percentual de espaço livre.
         - Se o espaço livre for menor que o limite de 'limite_alerta_disco_percentual',
           marcar status como 'CRÍTICO', caso contrário 'NORMAL'.
      3. Gerar um arquivo de texto com o ticket formatado para o GLPI (caminho em config['arquivo_ticket_glpi']).
      4. Retornar um dicionário com os dados coletados.
    """
    print("\n--- [MÓDULO 1] Executando Diagnóstico da Estação ---")
    log_file = os.path.join(BASE_DIR, config.get("arquivo_log_auditoria", "auditoria.log"))
    
    # Exemplo de coleta básica (complete e aprimore):
    hostname = socket.gethostname()
    usuario = getpass.getuser()
    sistema_op = f"{platform.system()} {platform.release()}"
    
    # TODO: Implemente a captura do IP local da máquina:
    ip_local = "127.0.0.1" # Substitua pela captura real
    
    # TODO: Implemente o cálculo do espaço livre no disco (dica: shutil.disk_usage):
    espaco_total_gb = 0.0
    espaco_livre_gb = 0.0
    percentual_livre = 0.0
    status_disco = "NORMAL"
    
    # TODO: Gere o arquivo do ticket GLPI formatado e salve no caminho configurado:
    
    dados_diagnostico = {
        "hostname": hostname,
        "usuario": usuario,
        "sistema_operacional": sistema_op,
        "ip_local": ip_local,
        "espaco_total_gb": round(espaco_total_gb, 2),
        "espaco_livre_gb": round(espaco_livre_gb, 2),
        "percentual_livre": round(percentual_livre, 1),
        "status_disco": status_disco
    }
    
    registrar_log(f"Diagnóstico concluído para a estação: {hostname} (Usuário: {usuario})", arquivo_log=log_file)
    return dados_diagnostico

# ==============================================================================
# MÓDULO 2: ROTINA DE BACKUP & INTEGRIDADE SHA-256
# ==============================================================================
def calcular_sha256(caminho_arquivo):
    """
    Calcula o hash criptográfico SHA-256 de um arquivo para garantir integridade.
    """
    hasher = hashlib.sha256()
    with open(caminho_arquivo, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

def executar_backup_e_auditoria(config):
    """
    [TAREFA 2 - DO CANDIDATO]:
    Garante a regra de integridade do backup local dos documentos do cartório.
    
    O que deve fazer:
      1. Verificar se o diretório de dados ('diretorio_dados_cartorio') existe e tem arquivos.
      2. Calcular e mapear o hash SHA-256 de cada documento da pasta.
      3. Compactar todos os arquivos em um único arquivo .zip dentro de 'diretorio_backup_destino'
         com nome no padrão: 'backup_cartorio_YYYYMMDD_HHMMSS.zip'.
      4. Registrar no log de auditoria a lista de arquivos salvos e o hash de cada um.
      5. Retornar um dicionário com o resultado do backup (status, arquivo gerado, total de arquivos).
    """
    print("\n--- [MÓDULO 2] Executando Rotina de Backup & Integridade SHA-256 ---")
    log_file = os.path.join(BASE_DIR, config.get("arquivo_log_auditoria", "auditoria.log"))
    dados_dir = os.path.join(BASE_DIR, config.get("diretorio_dados_cartorio", "./dados_cartorio"))
    backup_dest_dir = os.path.join(BASE_DIR, config.get("diretorio_backup_destino", "./backup_local"))
    os.makedirs(backup_dest_dir, exist_ok=True)
    
    # TODO: Implemente a verificação defensiva de existência da pasta e arquivos:
    
    # TODO: Calcule o hash SHA-256 de cada arquivo antes de compactar:
    
    # TODO: Crie o arquivo .zip com data e hora:
    nome_zip = "backup_cartorio_pendente.zip"
    caminho_zip = os.path.join(backup_dest_dir, nome_zip)
    
    resultado_backup = {
        "status": "SUCESSO", # ou 'FALHA'
        "arquivo_gerado": caminho_zip,
        "total_arquivos": 0,
        "hashes": {}
    }
    
    registrar_log(f"Backup concluído: {resultado_backup['total_arquivos']} arquivos salvos em {caminho_zip}", arquivo_log=log_file)
    return resultado_backup

# ==============================================================================
# MÓDULO 3: ANÁLISE INTELIGENTE & DIÁRIO DE BORDO
# ==============================================================================
def gerar_resumo_executivo(diagnostico, backup_info):
    """
    [TAREFA 3 - DO CANDIDATO]:
    Consolida as informações do Módulo 1 e Módulo 2 em um resumo executivo claro
    para a liderança de TI.
    
    Além do código, você deve documentar no TRILHA_INVESTIGACAO.md como utilizou
    ferramentas de IA Generativa (ChatGPT, Claude, etc.) para desenhar ou refinar
    esse resumo e suas decisões técnicas.
    """
    print("\n--- [MÓDULO 3] Gerando Resumo Executivo da TI ---")
    
    # TODO: Estruture um resumo objetivo de 3 a 5 linhas combinando os resultados
    resumo = (
        f"=== RESUMO DIÁRIO DE TI - CARTÓRIO LEANDRO FÉLIX ===\n"
        f"Estação: {diagnostico.get('hostname')} | IP: {diagnostico.get('ip_local')}\n"
        f"Status do Disco: {diagnostico.get('status_disco')} ({diagnostico.get('percentual_livre')}% livre)\n"
        f"Status do Backup: {backup_info.get('status')} ({backup_info.get('total_arquivos')} arquivos protegidos)\n"
        f"====================================================="
    )
    print(resumo)
    return resumo

# ==============================================================================
# EXECUÇÃO PRINCIPAL
# ==============================================================================
def main():
    print("=" * 70)
    print(" INICIANDO TOOLKIT DE SUPORTE & BACKUP - CARTÓRIO LEANDRO FÉLIX")
    print("=" * 70)
    
    try:
        config = carregar_config()
        
        # 1. Executa Módulo 1
        diagnostico = diagnosticar_estacao(config)
        
        # 2. Executa Módulo 2
        backup_info = executar_backup_e_auditoria(config)
        
        # 3. Executa Módulo 3
        resumo = gerar_resumo_executivo(diagnostico, backup_info)
        
        print("\n[OK] Todas as etapas do Toolkit foram executadas.")
        print("Lembre-se de preencher o arquivo TRILHA_INVESTIGACAO.md antes de enviar!")
        
    except Exception as e:
        registrar_log(f"FALHA NA EXECUÇÃO: {str(e)}", nivel="ERRO")
        sys.exit(1)

if __name__ == "__main__":
    main()
