from nltk.translate.bleu_score import sentence_bleu
reference = [
    '這是一隻狗'.split(),
    '這是隻狗'.split(),
    '一隻狗'.split(),
    '是一隻狗'.split() 
]
candidate = '是一隻狗'.split()
print('BLEU score -> {}'.format(sentence_bleu(reference, candidate)))

print('Individual 1-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))
print('Individual 2-gram: %f' % sentence_bleu(reference, candidate, weights=(0, 1, 0, 0)))
print('Individual 3-gram: %f' % sentence_bleu(reference, candidate, weights=(0, 0, 1, 0)))
print('Individual 4-gram: %f' % sentence_bleu(reference, candidate, weights=(0, 0, 0, 1)))