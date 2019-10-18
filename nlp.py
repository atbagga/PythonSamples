from textblob import TextBlob


text = '''
Conditions
This can be caused by excessive load. Too few AT/web roles in rotation. Bad code causing some loop. During deployments (which is expected) and other unknown circumstances. Could also be caused by a DOS Attack. This should be looked at ASAP.
'''

blob = TextBlob(text)
print(blob.tags)    # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

print(blob.noun_phrases)

import pdb
pdb.set_trace()
# WordList(['titular threat', 'blob',
#            'ultimate movie monster',
#            'amoeba-like mass', ...])
