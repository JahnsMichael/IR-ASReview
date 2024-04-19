from pathlib import Path

def init_folders():
  data_path = Path("data")
  data_path.mkdir(exist_ok=True)

  parent_project_path = Path("projects")
  parent_project_path.mkdir(exist_ok=True)

  parent_project_path = Path("states")
  parent_project_path.mkdir(exist_ok=True)

if __name__ == '__main__':
  init_folders()