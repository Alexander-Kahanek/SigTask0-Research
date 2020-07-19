from os import mkdir, remove


class Development:
    '''
    class for creating the development data

    Parameters
    ----------

    dictionary : a list of dictionary objects structured as [{"word", "lemma", "tags"}]

    langname : a string for only the langname structured as "deu_gml", do not use "."!

    filepath : automatically set to "task0-data/DEVELOPMENT-LANGUAGES/custom/"
    '''

    def __init__(self, dictionary, langname='corgi40', filepath='task0-data/DEVELOPMENT-LANGUAGES/custom/'):
        self.dictionary = dictionary
        self.langname = langname
        self.filepath = filepath
        self.nwords = len(dictionary)

    def __str__(self):
        return f'filepath is: {self.filepath}{self.langname}.dev\nnumber of words: {self.nwords}'

    def create(self):
        '''saves formatted development data'''

        fp = f'{self.filepath}{self.langname}.dev'

        try:
            mkdir(self.filepath)
        except:
            pass

        try:
            remove(fp)
        except:
            pass

        with open(fp, 'a') as fout:
            for line in self.dictionary:
                fout.write(f'{line["word"]}\t{line["lemma"]}\t{line["tags"]}')
                fout.write('\n')


class Train:
    '''
    class for creating the training data

    Parameters
    ----------

    dictionary : a list of dictionary objects structured as [{"word", "lemma", "tags"}]

    langname : a string for only the langname structured as "deu_gml", do not use "."!

    filepath : automatically set to "task0-data/DEVELOPMENT-LANGUAGES/custom/"
    '''

    def __init__(self, dictionary, langname='corgi40', filepath='task0-data/DEVELOPMENT-LANGUAGES/custom/'):
        self.dictionary = dictionary
        self.langname = langname
        self.filepath = filepath
        self.nwords = len(dictionary)

    def __str__(self):
        return f'filepath is: {self.filepath}{self.langname}.trn\nnumber of words: {self.nwords}'

    def create(self):
        '''saves formatted training data'''

        fp = f'{self.filepath}{self.langname}.trn'

        try:
            mkdir(self.filepath)
        except:
            pass

        try:
            remove(fp)
        except:
            pass

        with open(fp, 'a') as fout:
            for line in self.dictionary:
                fout.write(f'{line["word"]}\t{line["lemma"]}\t{line["tags"]}')
                fout.write('\n')


class Test:
    '''
    class for creating the testing data

    Parameters
    ----------

    dictionary : a list of dictionary objects structured as [{"word", "lemma", "tags"}]

    langname : a string for only the langname structured as "deu_gml", do not use "."!

    filepath : automatically set to "task0-data/DEVELOPMENT-LANGUAGES/custom/"
    '''

    def __init__(self, dictionary, langname='corgi40', filepath='task0-data/DEVELOPMENT-LANGUAGES/custom/'):
        self.dictionary = dictionary
        self.langname = langname
        self.filepath = filepath
        self.nwords = len(dictionary)

    def __str__(self):
        return f'filepath is: {self.filepath}{self.langname}.tst\nnumber of words: {self.nwords}'

    def create(self):
        '''saves formatted testing data'''

        fp = f'{self.filepath}{self.langname}.tst'

        try:
            mkdir(self.filepath)
        except:
            pass

        try:
            remove(fp)
        except:
            pass

        with open(fp, 'a') as fout:
            for line in self.dictionary:
                fout.write(f'{line["word"]}\t{line["lemma"]}\t{line["tags"]}')
                fout.write('\n')


class Hallucination:
    '''
    class for creating the hallucination data

    Parameters
    ----------

    dictionary : a list of dictionary objects structured as [{"word", "lemma", "tags"}]

    langname : a string for only the langname structured as "deu_gml", do not use "."!

    filepath : automatically set to "task0-data/DEVELOPMENT-LANGUAGES/custom/"
    '''

    def __init__(self, dictionary, langname='corgi40', filepath='task0-data/DEVELOPMENT-LANGUAGES/custom/'):
        self.dictionary = dictionary
        self.langname = langname
        self.filepath = filepath
        self.nwords = len(dictionary)

    def __str__(self):
        return f'filepath is: {self.filepath}{self.langname}.hall\nnumber of words: {self.nwords}'

    def create(self):
        '''saves formatted hallucination data'''

        fp = f'{self.filepath}{self.langname}.hall'

        try:
            mkdir(self.filepath)
        except:
            pass

        try:
            remove(fp)
        except:
            pass

        with open(fp, 'a') as fout:
            for line in self.dictionary:
                fout.write(f'{line["word"]}\t{line["lemma"]}\t{line["tags"]}')
                fout.write('\n')


class Language:
    '''
    class creates a language from the Train, Test, Development classes, which must be used.

    Hallucination : default None, can pass in this class if created
    '''

    def __init__(self, Train, Test, Development, Hallucination=None):
        self.trn = Train
        self.tst = Test
        self.dev = Development
        self.hall = Hallucination

    def __str__(self):

        sep = '\n--------------\n'

        string = f'{sep}{self.trn}{sep}{self.tst}{sep}{self.dev}{sep}'

        if self.hall is not None:
            string = f'{string}{self.hall}{sep}'

        return string

    def create(self):

        self.trn.create()
        self.tst.create()
        self.dev.create()

        if self.hall is not None:
            self.hall.create()

        print(f'files were saved to {self.trn.filepath}')
