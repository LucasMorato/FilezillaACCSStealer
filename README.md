# FilezillaACCSStealer

Este script Python captura o arquivo de contas FTP em máquinas comprometidas, com o FileZilla instalado, e envia o arquivo diretamente para um host remoto. O script foi criado para simplificar o roubo de credênciais do Red Team em máquinas infectadas.

Como o FileZilla armazena as informações de conta em um arquivo chamado 'sitemanager.xml', o script faz uso deste arquivo para capturar as informações de conta. O FileZilla armazena as senhas de conta em texto não criptografado, codificado com base64, facilitando a recuperação de senhas de contas. O script permite que essas informações sejam facilmente recuperadas ao serem enviadas diretamente para um host remoto.
