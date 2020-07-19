from langclass import Train, Test, Development, Hallucination, Language

# creating language dictionaries
dev = [{"word": "corgis", "lemma": "corgi", "tags": "N;PL;CUTE"}
       for i in range(10)]
trn = [{"word": "corgimus", "lemma": "corgi", "tags": "N;PL;ADORABLE"}
       for i in range(10)]
tst = [{"word": "potatoes", "lemma": "corgi", "tags": "N;PL;SASSY"}
       for i in range(10)]
hall = [{"word": "corgs", "lemma": "corgi", "tags": "N;PL;SPICY"}
        for i in range(10)]

# naming for the language
name = 'corg60'

# assigning the files
devclass = Development(dictionary=dev, langname=name)
trnclass = Train(trn, name)
tstclass = Test(tst, name)
hallclass = Hallucination(hall, name)

# assigning the language
corgi = Language(Train=trnclass, Test=tstclass,
                 Development=devclass, Hallucination=hallclass)

# printing information for language
print(corgi)

# saving the languages to the server
corgi.create()

# if you want to create a single file use this code below...
# devclass.create()
