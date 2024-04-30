# Demo Aplikasi

## (OPTIONAL) Setup Virtual Environment

```bash
python3 -m venv env
source ./env/bin/activate
```

## Install ASReview

```bash
python3 -m pip install asreview
```

Konfirmasi instalasi asreview.

```bash
which asreview
asreview --version
```


## Install Extension LSTM dan GRU

```bash
python3 -m pip install git+https://github.com/JahnsMichael/asreview-lstm-gru-classfier.git@main#egg=asreview-lstm-gru-classifier
```

Konfirmasi apakah extension sudah benar-benar terinstall dengan cara melihat apakah model LSTM dan GRU sudah terdapat dalam output command di bawah ini:

```bash
asreview algorithms
```

## Simulasi ASReview melalui CLI

```bash
asreview simulate $PATH_TO_DATASET -s $PATH_TO_DESIRED_OUTPUT --model $CLASSIFIER_MODEL_NAME --feature_extraction $FEATURE_EXTRACTION_MODEL --n_queries $NUMBER_OR_MODE_OF_QUERY --seed $SEED --n_prior_included $N_PRIOR_INCLUDED --n_prior_excluded $N_PRIOR_EXCLUDED --init_seed $INIT_SEED
```

Contoh:

```bash
asreview simulate data/Jeyaraman_2020_cleaned.csv -s simulation_output/gru64_doc2vec.asreview --model gru64 --feature_extraction doc2vec --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
```

Lebih lengkapnya:

```bash
asreview --help
```

## Mode Oracle melalui Web

```bash
asreview lab
```

Untuk menggunakan mode Oracle, diharapkan sudah mempersiapkan dataset untuk diseleksi dalam bentuk `.csv` (dengan terdapat kolom `title` dan `abstract`) atau dalam bentuk `.ris` dan `.bib`.