# Spacy
import spacy
import pytextrank

# Langdetect
from langdetect import detect

import re

class TextProcessing():
    def __init__(self, text) -> None:
        self.text = text
        self.__lang = detect(self.text)
        self.tokens = []
        self.tags = []
        self.lemmas = []
    
    @property
    def lang_detection(self):
        return self.__lang
    
    async def nlp_pipeline_selector(self):
        if self.__lang == 'en':
            self.nlp = spacy.load('en_core_web_md')
        elif self.__lang == 'es':
            self.nlp = spacy.load('es_core_news_md')
        elif self.__lang == 'de':
            self.nlp = spacy.load('nl_core_news_md')
        self.nlp.add_pipe("textrank")
        
        self.doc = self.nlp(self.text)

    def remove_double_spaces(self):
        self.text = re.sub('\s+', ' ', self.text)

    def tokenization(self):
        for token in self.doc:
            yield token.text

    def tagging(self):
        for token in self.doc:
            yield (token.text, token.pos_)
            
    def words_counter(self):
        self.word_count = len(self.tokens)

    def remove_stopwords_lemmatizer(self):
        threshold = 1
        for token in self.doc:
            if (not token.is_stop) and (len(token.text)> threshold):
                yield token.lemma_ 

    def ner(self):
        for ent in self.doc.ents:
            yield (ent.text,ent.label_)

    def get_keywords(self):
        for phrase in self.doc._.phrases[:10]:
            yield phrase.text

    def summarizer(self):
        for sent in self.doc._.textrank.summary(limit_phrases=3, limit_sentences=3):
            print(sent)

    async def get_preprocessing(self):
        await self.nlp_pipeline_selector()
        self.remove_double_spaces()
        self.tokens = list(self.tokenization())
        self.tags = list(self.tagging())
        self.lemmas = list(self.remove_stopwords_lemmatizer())
        self.keywords = list(self.get_keywords())
        self.words_counter()