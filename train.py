import subprocess
import shutil
import multiprocessing 

from pathlib import Path

from asreview import ASReviewData, ASReviewProject
from asreview.review import ReviewSimulate
from asreview.project import ProjectExistsError
from asreview.models.classifiers import (
  LogisticClassifier,
  NaiveBayesClassifier,
  NN2LayerClassifier,
  RandomForestClassifier,
  SVMClassifier
)
from asreview.models.query import MaxQuery
from asreview.models.balance import DoubleBalance
from asreview.models.feature_extraction import (
  Tfidf,
  Doc2Vec
)

from models.power_cnn import POWER_CNN
from models.wide_doc2vec import wide_doc2vec

def init_folders():
  data_path = Path("data")
  data_path.mkdir(exist_ok=True)

  parent_project_path = Path("projects")
  parent_project_path.mkdir(exist_ok=True)

  parent_project_path = Path("states")
  parent_project_path.mkdir(exist_ok=True)

def download_dataset():
  subprocess.run(["wget", "-O", "data/brouwer_et_al.xlsx", "https://osf.io/download/2mwkd/"])

def simulate_project(
    name,
    data_filename,
    classifier_model,
    feature_extraction_model,
    query_model=MaxQuery,
    balance_model=DoubleBalance
  ):
  project_path = Path("projects", name)
  project_path.mkdir(exist_ok=True)

  try:
    project = ASReviewProject.create(
      project_path=project_path / "simulation",
      project_id=name,
      project_mode="simulate",
      project_name=name,
    )
  except ProjectExistsError:
    shutil.rmtree(project_path)
    project = ASReviewProject.create(
      project_path=project_path / "simulation",
      project_id=name,
      project_mode="simulate",
      project_name=name,
    )

  print(f"{name}: Project Created")

  data_obj = ASReviewData.from_file(
    Path("data", data_filename)
  )
  reviewer = ReviewSimulate(
    as_data=data_obj,
    model=classifier_model(),
    query_model=query_model(),
    balance_model=balance_model(),
    feature_model=feature_extraction_model(),
    n_instances=1,
    project=project,
    n_prior_included=10,
    n_prior_excluded=10,
    stop_if='min'
  )

  print(f"{name}: ReviewSimulate object Created")

  project.update_review(status="review")
  print(f"{name}: Review start")
  try:
      reviewer.review()
      project.mark_review_finished()
  except Exception as err:
      project.update_review(status="error")
      print(f"{name}: Review error: {err}")
  print(f"{name}: Review end")

  project.export(Path("states", f"{name}.asreview"))
  print(f"{name}: Review exported")


if __name__ == '__main__':
  simulations = [
    multiprocessing.Process(target=simulate_project, args=("B_NB_T", "brouwer_et_al.csv", NaiveBayesClassifier, Tfidf)),
    multiprocessing.Process(target=simulate_project, args=("B_L_T", "brouwer_et_al.csv", LogisticClassifier, Tfidf)),
    multiprocessing.Process(target=simulate_project, args=("B_RF_T", "brouwer_et_al.csv", RandomForestClassifier, Tfidf)),
    multiprocessing.Process(target=simulate_project, args=("B_SVM_T", "brouwer_et_al.csv", SVMClassifier, Tfidf)),
    multiprocessing.Process(target=simulate_project, args=("B_L_D", "brouwer_et_al.csv", LogisticClassifier, Doc2Vec)),
    multiprocessing.Process(target=simulate_project, args=("B_RF_D", "brouwer_et_al.csv", RandomForestClassifier, Doc2Vec)),
    multiprocessing.Process(target=simulate_project, args=("B_NN_D", "brouwer_et_al.csv", NN2LayerClassifier, Doc2Vec)),
    multiprocessing.Process(target=simulate_project, args=("B_CNN_D", "brouwer_et_al.csv", POWER_CNN, wide_doc2vec))
  ]
  for simulation in simulations:
    simulation.start()
  for simulation in simulations:
    simulation.join()