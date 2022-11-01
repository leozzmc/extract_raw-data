from nltk.translate.bleu_score import *



hypothesis1 = ['It', 'is', 'a', 'guide', 'to', 'action', 'which',
                'ensures', 'that', 'the', 'military', 'always',
                'obeys', 'the', 'commands', 'of', 'the', 'party']


hypothesis2 = ['It', 'is', 'to', 'insure', 'the', 'troops',
               'forever', 'hearing', 'the', 'activity', 'guidebook',
               'that', 'party', 'direct']

reference1 = ['It', 'is', 'a', 'guide', 'to', 'action', 'that',
              'ensures', 'that', 'the', 'military', 'will', 'forever',
              'heed', 'Party', 'commands']
reference2 = ['It', 'is', 'the', 'guiding', 'principle', 'which',
              'guarantees', 'the', 'military', 'forces', 'always',
              'being', 'under', 'the', 'command', 'of', 'the',
              'Party']

reference3 = ['It', 'is', 'the', 'practical', 'guide', 'for', 'the',
              'army', 'always', 'to', 'heed', 'the', 'directions',
              'of', 'the', 'party']


## 0.50456...
print(sentence_bleu([reference1, reference2, reference3], hypothesis1))
## It will return 0 ,because there is no ngrams overlap for any order of n-grams
## This is because the precision for the order of n-grams without overlap is 0, 
## and the geometric mean in the final BLEU score computation multiplies the 0 with the precision of other n-grams.
print(round(sentence_bleu([reference1, reference2, reference3], hypothesis2),4))

## To avoid this harsh behaviour when no ngram overlaps are found a smoothing function can be used.
chencherry = SmoothingFunction()
print(sentence_bleu([reference1, reference2, reference3], hypothesis2,smoothing_function=chencherry.method1))


## The default BLEU calculates a score for up to 4-grams using uniform weights (this is called BLEU-4). 
## To evaluate your translations with higher/lower order ngrams, use customized weights. 
## E.g. when accounting for up to 5-grams with uniform weights (this is called BLEU-5) use:

weights = (1./5., 1./5., 1./5., 1./5., 1./5.)
print(sentence_bleu([reference1, reference2, reference3], hypothesis1, weights))