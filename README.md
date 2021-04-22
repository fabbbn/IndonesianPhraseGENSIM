# IndonesianPhraseGENSIM
Indonesian Phrase Detection using SGNS (GENSIM)

## How to use this program?
1. Clone this repo
2. Download wikidump and use extract_wiki.py to extract the text into .txt (clean and uncleaned) OR Download ready to use training datasets from link at training_datasets/README.md
3. Run training.py to train model. The result will be 6 models you can use (more detail read models/README.md) OR Download models from author's GDrive (link read models/README.md)
4. Run main.py to test the model

## The Datasets
1. Training dataset from wikidump (2021). Splitted by sentences ('\n')
2. Testing dataset is a .csv format list of queries and its label (expected phrase) with name of label: 'pertanyaan' and 'label' (so you can make your wn dataset for testing if you want to).
