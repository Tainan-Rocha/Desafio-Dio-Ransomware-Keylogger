# Desafio-Dio-Ransomware-Keylogger
Através desse repositorio, irei documentar processos realizados para criacao de Ransomware e Keylogger simulados, em um ambiente controlado e para afins de estudos.

## 🔍 Tecnologias
- Python

## [📌 Criacao Ransomware Simulado](Ransomware)

Este projeto foi desenvolvido com fins educacionais, demonstrando na prática o funcionamento de criptografia simétrica aplicada a arquivos locais.

Utiliza a biblioteca cryptography (Fernet) para:

- Criptografar arquivos
- Restaurar arquivos criptografados (descriptografia)


## [📌 Criacao Keylogger Simulado](Keylogger)

Este projeto foi desenvolvido com fins educacionais, com o objetivo de entender como funciona a captura de eventos de teclado em Python.

O projeto contém duas versões:

-  Keylogger local: registra teclas digitadas em um arquivo (log.txt)
-  Keylogger com envio: registra teclas e envia os dados periodicamente por e-mail


## 🛡️ Reflexão: Medidas de Prevenção e Defesa

Conforme os programas que criei acima, podemos ver que sao muitos perigosos, a partir disso, podemos pensar em como detectar, prevenir e mitigar esse tipo de ameaça.

### 1. 🦠 Antivírus (detecção de comportamento)

Antivírus modernos não analisam só arquivos — eles observam comportamentos suspeitos.

#### 🔍 Exemplos de comportamentos detectáveis:
- Monitoramento contínuo do teclado
- Escrita frequente em arquivos de log
- Modificação em massa de arquivos
- Execução de scripts em segundo plano

#### 🛡️ Medidas de defesa:
- tilizar antivírus com EDR (Endpoint Detection and Response)
- Monitorar processos desconhecidos
- Bloquear execuções suspeitas automaticamente


### 2. 🔥 Firewall e Controle de Rede

Firewalls controlam o tráfego de entrada e saída do sistema.

#### 🔍 Exemplos de comportamentos detectáveis:
-  Conexões com servidores externos (ex: SMTP)
-  Envio automático e periódico de dados
-  Tráfego incomum de aplicações locais
#### 🛡️ Medidas de defesa:
-  Restringir conexões de saída não autorizadas
-  Monitorar aplicações que acessam a rede
-  Implementar regras de bloqueio para serviços sensíveis

### 3. 🧪 Sandboxing

Sandboxing permite executar programas em ambientes isolados para análise.

#### 🔍 O que pode ser observado:
-  Captura de eventos do teclado
-  Alterações em arquivos do sistema
-  Tentativas de comunicação externa
-  Padrões de comportamento automatizado
#### 🛡️ Medidas de defesa:
-  Executar arquivos suspeitos em sandbox antes de liberar
-  Bloquear programas com comportamento malicioso
-  Utilizar soluções de análise automatizada

### 👤 4. Conscientização do Usuário

O fator humano é uma das principais vulnerabilidades em segurança.

#### 🔍 Riscos comuns:
-  Execução de arquivos desconhecidos
-  Download de fontes não confiáveis
-  Falta de atenção a permissões solicitadas
#### 🛡️ Medidas de defesa:
-  Educação em segurança digital
-  Verificação de origem de arquivos
-  Evitar execução de scripts desconhecidos


## 👨‍💻 Autor

Tainan Silva da Rocha