from sys import argv, exit
from src.scp_script import scp_transfer

if __name__ == '__main__':
    # Revisamos que el numero de parametros recibidos sea el necesario.
    if len(argv) < 3:
        print("Please provide the source path as a command-line argument.")
        exit(1)
    
    sources = argv[1]
    if isinstance(sources, str):
        if sources[0] == '[' and sources[-1] == ']':
            sources = eval(sources) # We try to convert any string types into a list.
        else:
            sources = [sources]

    destination_path = argv[2]

    hostname  = argv[3]
    username  = argv[4]
    password  = argv[5]

    for source_path in sources:
        filename = ''
        try:
            filename = source_path.split('\\')[-1]
        except:
            filename = source_path.split('/')[-1]
        scp_transfer(source_path, f"{destination_path}/{filename}", hostname, username, password)
