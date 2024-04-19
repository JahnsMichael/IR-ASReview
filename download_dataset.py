import subprocess
import pandas as pd
from pathlib import Path


def download_dataset():
  subprocess.run(["wget", "-O", "data/brouwer_et_al.xlsx", "https://osf.io/download/2mwkd/"])
  read_file = pd.read_excel(Path("data", "brouwer_et_al.xlsx"))
  read_file.to_csv(Path("data", "brouwer_et_al.csv"), index=False, header=True)

if __name__ == '__main__':
  download_dataset()