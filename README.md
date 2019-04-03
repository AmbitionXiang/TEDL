# TEDL
Relevant codes of the paper "TEDL: A Text Encryption Method Based on Deep Learning"

TEDL applies a two-stage structure.

At the first stage, both parties to the communication modify a public corpus under the instruction of the key, completing the construction of a confidential synthetic corpus, respectively. And the synthetic corpora mastered by both parties are expected to be consistent. Afterwards, the hyperparameters in the key direct the training on the synthetic corpus. Hence a word vector table is established, followed by a further process on it with the SHA-256 function to obtain a codebook. So far, the first stage called communication preparation ends.

At the second stage, when a word requires transmitting, the sender refers to the codebook and indexes the plaintext to obtain the corresponding ciphertext. And then the ciphertext is sent to the recipient. In turn, the receiver decrypts the ciphertext based on the mapping in the codebook, which is equally an inverse indexing operation. After completing the transmission of a word, both ends adjust the codebook in a certain way. Therefore, when the next word needs to be delivered, it is encrypted based on the new codebook. We illustrates the process as the following figure.

![](https://github.com/AmbitionXiang/TEDL/blob/master/images/overview.png)

And the process of using the codebook is shown as the following figure.
![](https://github.com/AmbitionXiang/TEDL/blob/master/images/process2.png)


A：Construction of Synthetic Corpus
    Step 1: Get Wikipedia corpus resources
    Step 2: Process the wiki's xml file into a normal txt file--process_xml.py
    Step 3: Convert traditional txt to simplified txt using opencc(Chinese)
    Step 4: Participle--segmentation_Chinese.py or segmentation_English.py
    Step 5: Process incremental corpus--incremental_corpus_preprocess.py
    Step 6: Add incremental corpus to original corpus
B: Training
    Run word2vec_model.py for word2vec model
    Run fasttext.py for fasttext model
    As for other models, please refer to the corresponding source codes in github.
C: Process the word vector table
    Run table_process.py
D: Some experiments
    recovery.py
    frequency_analysis.py
    correlation_analysis_1.py
    correlation_analysis_2.py
    plaintext_sensitivity_analysis.py
    ciphertext_sensitivity_analysis.py
    efficiency_analysis.py
  
  

