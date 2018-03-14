'''
NLP using spacy
python -m spacy download en_core_web_lg
'''

import spacy


nlp			= spacy.load('en_core_web_lg')

categories	= nlp(u'wood automobile metal')
sent 		= raw_input("Product description : ")
sent 		= nlp(unicode(sent, "utf-8"))

max 	= 0
ans		= ""

print ('-'*40)
print ('{:<20}'.format("Category"),"Match percentage")
print ('-'*40)

for category in categories:
    sum = 0
    len = 0
    for word in sent:
        sum += word.similarity(category)
        len += 1

    if(sum/len >max ):
        max = sum/len
        ans = str(category)

    print ('{:<20}'.format(str(category)),sum/len)

print ("\nCategory : ", ans)

