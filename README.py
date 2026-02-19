#!/usr/bin/env python
# coding: utf-8

# # Como instalar o `drawing` no `Linux Ubuntu`

# ## Resumo
# 
# Este documento apresenta os passos necessários para instalar o utilitário `drawing` no `Linux Ubuntu`.

# ## _Abstract_
# 
# _This document shows the steps required to install the `drawing` utility on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `drawing`
# 
# O `drawing` é um editor de imagens simples para ambientes `Linux`, semelhante ao `Microsoft Paint`. Ele permite criar e editar imagens de forma intuitiva.

# ## 1. Instalar o `drawing` no `Linux Ubuntu`
# 
# Para instalar o `drawing`, siga os passos abaixo:
# 
# 1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:
# 
#     ```bash
#     Ctrl + Alt + T
#     ```
# 
# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
#     ```bash
#     sudo apt clean
#     ```
# 
#     2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
#     ```bash
#     sudo apt autoclean
#     ```
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
#     ```bash
#     sudo apt autoremove -y
#     ```
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt update
#     ```
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
#     ```bash
#     sudo apt --fix-broken install
#     ```
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
#     ```bash
#     sudo apt clean
#     ```
# 
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt list --upgradable
#     ```
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
#     ```bash
#     sudo apt full-upgrade -y
#     ```
# 
# 

# 3. Instale o `drawing` e verifique a instalação:
#     ```bash
#     sudo apt install drawing -y
#     drawing --version
#     ```
# 

# ## 2. Criar um desenho simples
# 
# Você pode executar o `drawing` sem parâmetros para abrir uma tela em branco:
# ```bash
# drawing
# ```
# Esse comando abre a interface do programa com um novo desenho.

# ## 3. Abrir uma imagem existente usando uma variável de terminal
# 
# Também é possível definir o arquivo a ser aberto em uma variável antes de chamar o `drawing`:
# ```bash
# img_file="~/Imagens/exemplo.png"
# drawing "$img_file"
# ```

# ## Referências
# 
# [1] OPENAI. ***Instalar o `drawing` no `linux ubuntu` pelo `terminal emulator`***. Disponível em: <https://chatgpt.com/g/g-p-6980caf949648191ad6acfcdbe590f9e/project>. ChatGPT. Acessado em: 07/08/2025 05:18.
