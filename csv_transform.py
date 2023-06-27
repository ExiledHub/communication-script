import pandas as pd
from sys import argv

if __name__ == '__main__':
    sources = argv[1]
    if isinstance(sources, str):
        if sources[0] == '[' and sources[-1] == ']':
            sources = eval(sources) # We try to convert any string types into a list.
        else:
            sources = [sources]

    destination_path = argv[2]

    for source in sources:
        df = pd.read_excel(source, skiprows=5).drop(['COMPANY TYPE', 'DOMICILE'], axis=1)
        df["AMB#"] = df["AMB#"].astype(str)
        df["AMB#"] = df["AMB#"].str.rjust(6, "0")
        df = df[['COMPANY NAME', 'AMB#']]
        df.to_csv(f"{destination_path}\\companias.csv", sep=";", index=False, header=False)