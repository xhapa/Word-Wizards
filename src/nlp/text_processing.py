# Spacy
from typing import Any
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
        self.pos = []
        self.lemmas = []
        self.entities = []
        self.summary = ''
    
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
            yield (ent.text.lower(),ent.label_)

    def get_keywords(self):
        for phrase in self.doc._.phrases[:10]:
            yield phrase.text.capitalize()

    def summarizer(self):
        for sent in self.doc._.textrank.summary(limit_phrases=3, limit_sentences=3):
            self.summary += str(sent)

    def __getattr__(self, name):
        if name == 'json_dict':
            return {'text': self.text, 'lang': self.lang_detection,'tokens':self.tokens,'word_count': self.word_count, 'pos': self.pos,
           'entities':self.entities, 'lemma':self.lemmas, 'keywords': self.keywords, 'summary':self.summary}

    async def get_preprocessing(self):
        await self.nlp_pipeline_selector()
        self.remove_double_spaces()
        self.tokens = list(self.tokenization())
        self.pos = list(self.tagging())
        self.lemmas = list(self.remove_stopwords_lemmatizer())

    async def get_processing(self):
        self.words_counter()
        self.entities = list(map(lambda x : (x[0].title(), x[1]),list(set(self.ner()))))
        self.keywords = list(self.get_keywords())
        self.summarizer()