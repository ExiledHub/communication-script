import paramiko
import os

def scp_transfer(source_path, destination_path, hostname, username, password=None, private_key=None):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password, key_filename=private_key)

        sftp = client.open_sftp()
        print("Llegamos hasta aca.")
        sftp.put(source_path, destination_path)

        sftp.close()
        client.close()

        # Eliminamos el archivo local.
        if os.path.isfile(source_path):
            os.remove(source_path)
    except:
        raise