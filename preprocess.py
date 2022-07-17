import spacy
from spacy.tokens import DocBin
import pickle as pkl

nlp = spacy.blank("en")
training_data = pkl.load( open('./files/train.pickle', 'rb') )
testing_data = pkl.load( open('./files/test.pickle', 'rb') )

# the DocBin will store the example documents
db = DocBin()
i=0
for text, annotations in training_data:
    i+=1
    print(i)
    doc = nlp(text)
    ents = []
    for start, end, tag in annotations['entities']:
        span = doc.char_span(start, end, label=tag)
        if span == None:
            print('Skipping Entity')
        else:
            ents.append(span)
        print(span)
        
    print('\n')
    print('************************')
    print(ents)
    
    doc.ents = ents
    db.add(doc)
db.to_disk("./files/train.spacy")


# the DocBin will store the example documents
db_test = DocBin()
for text, annotations in testing_data:
    doc = nlp(text)
    ents = []
    for start, end, label in annotations['entities']:
        span = doc.char_span(start, end, label=label)
        if span == None:
            print('Skipping Entity')
        else:
            ents.append(span)
    doc.ents = ents
    db_test.add(doc)
db_test.to_disk("./files/test.spacy")