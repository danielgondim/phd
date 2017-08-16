'''from nltk.tag import StanfordNERTagger

st = StanfordNERTagger('/home/danielgondim/workspace-new/phd/experiments/project-2017-2/stanford-ner-2014-06-16/classifiers/english.all.3class.distsim.crf.ser.gz',
  '/home/danielgondim/workspace-new/phd/experiments/project-2017-2/stanford-ner-2014-06-16/stanford-ner.jar') 

print st.tag("Rami Eid is studying at Stony Brook University in NY".split())'''

import ner
tagger = ner.HttpNER(host='localhost', port=1234)
print tagger.get_entities("University of California is located in California, United States")