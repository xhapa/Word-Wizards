# NLP
from nlp.text_processing import TextProcessing

# SQLModels
from sqlmodels.nlp_data import NLPData

example = {'id':'112331','text': 'Hellooo how are you', 'lang': 'en','tokens':['Hello'],'word_count': '144', 'pos': ['(Hello, PRON)'],
           'entities':['Hello'], 'lemma':['Hell'], 'keywords': ['Hello'], 'summary':'Hello'}

class NLPDataService():
    def __init__(self, db) -> None:
        self.db = db

    async def create_nlp_data(self, text):
        try:
            nlp_prepro = TextProcessing(text)
            await nlp_prepro.get_preprocessing()
            new_prepro = NLPData(**nlp_prepro.json_dict)
            self.db.add(new_prepro)
            self.db.commit()  # Use an asynchronous commit if supported
        except Exception as e:
            # Handle the error appropriately (e.g., log the error, raise it, etc.)
            print(f"Error while creating NLP data: {e}")
            self.db.rollback() 
