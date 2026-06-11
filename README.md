# Como configurar/instalar o `Power Manager` no `Linux Ubuntu` pelo `Terminal Emulator`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar o `Power Manager` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands and configurations to configure/install the `Power Manager` on `Linux Ubuntu`._

## Descrição [2]

### `Power Manager`

O `Power Manager` é uma aplicação ou recurso de _software_ projetado para gerenciar o consumo de 
energia e as configurações de energia em sistemas computacionais, como _laptops_ e _desktops_. Ele 
oferece aos usuários a capacidade de personalizar o comportamento do sistema em relação ao 
gerenciamento de energia, permitindo que ajustem configurações como suspensão, desligamento 
automático do monitor e economia de energia da CPU. O `Power Manager` é valioso para otimizar o uso 
de energia, prolongar a vida útil da bateria em dispositivos móveis e reduzir o consumo de energia 
em sistemas de _desktop_, contribuindo para uma experiência de computação mais eficiente e amigável 
ao meio ambiente. Geralmente, ele oferece opções para criar perfis de energia personalizados, 
adaptando-se às necessidades dos usuários em diferentes cenários de uso.

## 1. Como configurar/instalar o `Power Manager`no `Linux Ubuntu` [1][3]

Para configurar/instalar o `Power Manager` no `Linux Ubuntu`, você pode seguir estes passos:

1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:

    ```bash
    Ctrl + Alt + T
    ```    

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando:
    ```bash
    sudo apt clean
    ```

    2.2 Remover pacotes `.deb` antigos ou duplicados do `cache` local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando:
    ```bash
    sudo apt autoclean
    ```

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando:
    ```bash
    sudo apt autoremove -y
    ```

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt update
    ```

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes:
    ```bash
    sudo apt --fix-broken install
    ```

    2.6 Limpar o `cache` do gerenciador de pacotes `apt` novamente:
    ```bash
    sudo apt clean
    ```

    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt list --upgradable
    ```

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`:
    ```bash
    sudo apt full-upgrade -y
    ```

Para alterar a ação do evento `HandleLidSwitch` para `suspend` no `systemd`, você precisará editar o arquivo de configuração do `systemd-logind`. Aqui está como você pode fazer isso:

1. Abrir o arquivo de configuração para edição: Você precisa editar o arquivo `/etc/systemd/logind.conf`. Geralmente, isso requer permissões de administrador, então você usará um editor de texto com `sudo`. Por exemplo, se você preferir usar o `nano` como editor de texto, o comando seria: 

    ```bash
    sudo nano /etc/systemd/logind.conf
    ```

2. **Modificar a configuração:** Dentro do arquivo `logind.conf`, procure pela linha que contém `HandleLidSwitch`. Se essa linha começar com um `#`, isso significa que ela está comentada (desativada). Você precisará descomentá-la (remover o `#`) e alterar seu valor para `suspend`. Deverá ficar assim:

    ```bash
    HandleLidSwitch=suspend
    ```

    Se a linha não existir, você pode simplesmente adicionar essa linha ao final do arquivo:

    ```bash
    #  This file is part of systemd.
    #
    #  systemd is free software; you can redistribute it and/or modify it under the
    #  terms of the GNU Lesser General Public License as published by the Free
    #  Software Foundation; either version 2.1 of the License, or (at your option)
    #  any later version.
    #
    # Entries in this file show the compile time defaults. Local configuration
    # should be created by either modifying this file, or by creating "drop-ins" in
    # the logind.conf.d/ subdirectory. The latter is generally recommended.
    # Defaults can be restored by simply deleting this file and all drop-ins.
    #
    # Use 'systemd-analyze cat-config systemd/logind.conf' to display the full config.
    #
    # See logind.conf(5) for details.

    [Login]
    #NAutoVTs=6
    #ReserveVT=6
    #KillUserProcesses=no
    #KillOnlyUsers=
    #KillExcludeUsers=root
    #InhibitDelayMaxSec=5
    #UserStopDelaySec=10
    #HandlePowerKey=poweroff
    #HandleSuspendKey=suspend
    #HandleHibernateKey=hibernate
    HandleLidSwitch=suspend
    #HandleLidSwitchExternalPower=suspend
    #HandleLidSwitchDocked=suspend
    #HandleRebootKey=reboot
    #PowerKeyIgnoreInhibited=no
    #SuspendKeyIgnoreInhibited=no
    #HibernateKeyIgnoreInhibited=no
    #LidSwitchIgnoreInhibited=yes
    #RebootKeyIgnoreInhibited=no
    #HoldoffTimeoutSec=30s
    #IdleAction=ignore
    #IdleActionSec=30min
    #RuntimeDirectorySize=10%
    #RuntimeDirectoryInodesMax=400k
    #RemoveIPC=yes
    #InhibitorsMax=8192
    #SessionsMax=8192
    ```

3. **Salvar e fechar o arquivo:** Após fazer a alteração, salve e feche o arquivo. No `nano`, você pode fazer isso pressionando `Ctrl+O` para salvar as mudanças e depois `Ctrl+X` para sair.

4. **Aplicar as mudanças:** Para que as alterações tenham efeito, você precisa reiniciar o `systemd-logind`. Isso pode ser feito com o seguinte comando:

    ```bash
    sudo systemctl restart systemd-logind
    ```

    Tenha em mente que reiniciar o systemd-logind pode encerrar a sua sessão atual e todas as aplicações abertas, então salve seu trabalho antes de executar este comando.

Por favor, note que alterar as configurações de gerenciamento de energia pode ter efeitos diferentes dependendo do hardware e do ambiente de _desktop_ que você está usando. Certifique-se de testar o comportamento após fazer essas alterações para garantir que ele atenda às suas expectativas.


### 2. Código completo para configurar/instalar/usar

Para configurar/instalar/usar para limpar o `Power Manager` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:

    ```bash
    Ctrl + Alt + T
    ```

2. Digite o seguinte comando e pressione `Enter`:

    ```bash
    NÂO há.
    ```


## Referências

[1] OPENAI. **Instalar o `power manager` no `linux ubuntu` pelo `terminal emulator`.** Disponível em: <https://chat.openai.com/c/a20133bf-1604-438b-ba06-09a5587540e1> (texto adaptado). ChatGPT. Acessado em: 02/02/2024 18:43.

[2] OPENAI. **Vs code: editor popular.** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 02/02/2024 18:43.

