# TEDL
Relevant codes of the paper "TEDL: A Text Encryption Method Based on Deep Learning"

TEDL applies a two-stage structure.

At the first stage, both parties to the communication modify a public corpus under the instruction of the key, completing the construction of a confidential synthetic corpus, respectively. And the synthetic corpora mastered by both parties are expected to be consistent. Afterwards, the hyperparameters in the key direct the training on the synthetic corpus. Hence a word vector table is established, followed by a further process on it with the SHA-256 function to obtain a codebook. So far, the first stage called communication preparation ends.

At the second stage, when a word requires transmitting, the sender refers to the codebook and indexes the plaintext to obtain the corresponding ciphertext. And then the ciphertext is sent to the recipient. In turn, the receiver decrypts the ciphertext based on the mapping in the codebook, which is equally an inverse indexing operation. After completing the transmission of a word, both ends adjust the codebook in a certain way. Therefore, when the next word needs to be delivered, it is encrypted based on the new codebook. We illustrates the process as the following figure.
  
