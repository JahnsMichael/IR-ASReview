# Original runs

asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/nb_tf-idf.asreview --model nb --feature_extraction tfidf --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/lr_tf-idf.asreview --model logistic --feature_extraction tfidf --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/svm_tf-idf.asreview --model svm --feature_extraction tfidf --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/rf_tf-idf.asreview --model rf --feature_extraction tfidf --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/power-cnn_wide-doc2vec.asreview --model power_cnn --feature_extraction wide_doc2vec --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/rf_doc2vec.asreview --model rf --feature_extraction doc2vec --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/lr_doc2vec.asreview --model logistic --feature_extraction doc2vec --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/nn-2-layer_doc2vec.asreview --model nn-2-layer --feature_extraction doc2vec --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/nn-2-layer_wide-doc2vec.asreview --model nn-2-layer --feature_extraction wide_doc2vec --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/lr_sbert.asreview --model logistic --feature_extraction sbert --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
asreview simulate data/Jerayaman_2020_cleaned.csv -s simulation_output/nn-2-layer_sbert.asreview --model nn-2-layer --feature_extraction sbert --n_queries min --seed 200 --n_prior_included 10 --n_prior_excluded 10 --init_seed 200
