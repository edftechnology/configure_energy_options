# Como instalar/configurar o `Xfce Power Manager` no `Linux Ubuntu` pelo `Terminal Emulator`

## Resumo

Neste documento estão contidos os principais comandos para instalar, verificar e configurar o `Xfce Power Manager` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands to install, verify, and configure `Xfce Power Manager` on `Linux Ubuntu`._

## Descrição [2][3]

### `Xfce Power Manager`

O `Xfce Power Manager`, fornecido pelo pacote `xfce4-power-manager`, gerencia fontes de energia,
nível de brilho, suspensão, hibernação, eventos da tampa e economia de energia do monitor. Ele é
destinado principalmente ao ambiente gráfico Xfce e utiliza componentes como `UPower`, `D-Bus` e
`systemd-logind` para executar as ações de energia suportadas pelo sistema.

No Xubuntu e em instalações do Ubuntu que usam o ambiente Xfce, o `Xfce Power Manager` geralmente
já vem instalado como parte de `xubuntu-core` ou `xubuntu-desktop`. O Ubuntu padrão com GNOME já
possui gerenciamento de energia integrado às Configurações do sistema, mas não necessariamente
inclui o pacote `xfce4-power-manager`. As instruções abaixo mostram a instalação completa mesmo
quando outro gerenciador de energia já está disponível. Evite executar simultaneamente dois
gerenciadores gráficos de energia, pois eles podem disputar eventos de suspensão, tampa e brilho.

## 1. Como instalar/configurar o `Xfce Power Manager` no `Linux Ubuntu` [1][2][3][4]

Para instalar/configurar o `Xfce Power Manager` no `Linux Ubuntu`, você pode seguir estes passos:

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

3. Verificar se o pacote já está instalado. Esse caso é comum no Xubuntu e em sessões Xfce:

    ```bash
    dpkg-query -W -f='${Status}\n' xfce4-power-manager 2>/dev/null | grep -q 'install ok installed' && echo 'O Xfce Power Manager já está instalado.' || echo 'O Xfce Power Manager não está instalado.'
    ```

4. Instalar o utilitário de gerenciamento de repositórios e habilitar o repositório `universe`, no qual o pacote é distribuído pelo Ubuntu:

    ```bash
    sudo apt install -y software-properties-common
    sudo add-apt-repository -y universe
    sudo apt update
    ```

5. Instalar o `Xfce Power Manager` e suas dependências:

    ```bash
    sudo apt install -y xfce4-power-manager
    ```

6. Confirmar a instalação e consultar a versão instalada:

    ```bash
    xfce4-power-manager --version
    ```

7. Iniciar ou reiniciar o gerenciador na sessão gráfica atual:

    ```bash
    xfce4-power-manager --restart
    ```

    Em uma sessão Xfce, ele também será iniciado automaticamente no próximo login. No GNOME, encerre primeiro o outro gerenciador gráfico de energia ou prefira as configurações nativas do ambiente.

8. Abrir a janela de configurações do `Xfce Power Manager`:

    ```bash
    xfce4-power-manager -c
    ```

9. Opcionalmente, configurar o `systemd-logind` para suspender ao fechar a tampa quando nenhum ambiente gráfico estiver controlando esse evento. Use um arquivo de sobreposição em vez de editar `/etc/systemd/logind.conf` diretamente:

    ```bash
    sudo install -d -m 0755 /etc/systemd/logind.conf.d
    printf '[Login]\nHandleLidSwitch=suspend\n' | sudo tee /etc/systemd/logind.conf.d/10-lid-switch.conf > /dev/null
    systemd-analyze cat-config systemd/logind.conf
    ```

    Reinicie o computador para aplicar essa configuração. Ambientes gráficos podem assumir o controle do evento da tampa por meio de um bloqueio de inibição; nesse caso, configure a ação diretamente no gerenciador de energia do ambiente.


### 2. Código completo para configurar/instalar/usar

Para instalar e verificar o `Xfce Power Manager` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abrir o `Terminal Emulator`. Você pode fazer isso pressionando:

    ```bash
    Ctrl + Alt + T
    ```

2. Digite o seguinte comando e pressione `Enter`:

    ```bash
    sudo apt install -y software-properties-common
    sudo add-apt-repository -y universe
    sudo apt update
    sudo apt install -y xfce4-power-manager
    xfce4-power-manager --version
    xfce4-power-manager --restart
    ```


## Referências

[1] OPENAI. **Instalar o `power manager` no `linux ubuntu` pelo `terminal emulator`**. Disponível em: <https://chatgpt.com/g/g-p-6980caf949648191ad6acfcdbe590f9e-instalar/c/a20133bf-1604-438b-ba06-09a5587540e1>. ChatGPT. Acessado em: 11/06/2026.

[2] XFCE. **Xfce4 power manager**. Disponível em: <https://docs.xfce.org/xfce/xfce4-power-manager/start>. Acessado em: 11/06/2026.

[3] XFCE. **Xfce4 power manager: primeiros passos**. Disponível em: <https://docs.xfce.org/xfce/xfce4-power-manager/getting-started>. Acessado em: 11/06/2026.

[4] UBUNTU. **Logind.conf e logind.conf.d: arquivos de configuração do gerenciador de login**. Disponível em: <https://manpages.ubuntu.com/manpages/noble/man5/logind.conf.5.html>. Acessado em: 11/06/2026.

