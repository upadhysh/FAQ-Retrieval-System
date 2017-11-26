# FAQ-Retrieval-System

In this task, we have a corpus of frequently asked questions and answers from various domains that have been provided. The corpora of questions in the database are represented by Q. The query is in SMS language which may or may not contain noise. The goal of the task is to find a question Q* from the corpora of FAQ’s Q, that is the best possible match for the SMS query S.

I have two parameters for calculating the score of a question, keyword score and similarity score.
The methods for calculating the keyword score, like disemvoweling, are based on the general observations made about the language and slangs used by people while typing SMS text.
On the other hand, the similarity score is calculated using dynamic programming techniques for string comparison and pattern matching algorithms, like Longest Common Subsequence and Gestalt Pattern Matching.

## System Implementation
Preprocessing Disemvoweling Removal of stop words Keyword matching
Calculation of weight of each word using:
*Similarity ratio
*Longest Common Subsequence ratio
*Levenshtein Distance *Inverse Document Frequency
Creation of variant lists for each SMS word Similarity score
Total Score

## Preprocessing
We create a hash table of words W that contains all the words occurring in all the questions in Q with the keys being characters a-z and numbers 0-9.

Example: ‘i’ contains all the words in the set Q that start with ‘i’, like
‘insurance’, ‘improve’, and so on
A list of stop words is also prepared and disemvoweled
Digits occurring in SMS token are replaced by a string based on a manually designed digit-to-string mapping (“8”->“eight”).
Single character words in the SMS query are removed.

## Disemvoweling
We describe the process of removing vowels from a string as disemvoweling and the string from which vowels are removed is said to be disemvoweled.
We apply this process of disemvoweling to the SMS query because in general, it has been observed that the user tries to compress the text by removing vowels.


## Calculation of weight of a word
For each token of the SMS query (not disemvoweled), we calculate its similarity with every word w in the corpus W. The weight of a word is given by the equation:
Weight(w,s)= LCSR(w,s)*SMRatio(w,s) *IDF(w) LevDistance(w,s) ...(2)
*LCSR(w, s) - Longest Common Subsequence Ratio of the SMS query token s and the word w in W.
*SMRatio(w, s) - Similarity ratio using Ratcliff/Obershelp algorithm. *LevDistance(w, s)-Levenshtein Distance between disemvoweled w and s
*LevDistance(w, s)-Levenshtein Distance between disemvoweled w and s

