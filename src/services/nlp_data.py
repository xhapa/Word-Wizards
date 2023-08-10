# NLP
from nlp.text_processing import TextProcessing

# SQLModels
from sqlmodels.nlp_data import NLPData, select

class NLPDataService():
    def __init__(self, db) -> None:
        self.db = db

    async def create_nlp_data(self, text):
        try:
            nlp_prepro = TextProcessing(text)
            await nlp_prepro.get_preprocessing()
            await nlp_prepro.get_processing()
            new_prepro = NLPData(**nlp_prepro.json_dict)
            self.db.add(new_prepro)
            self.db.commit()
        except Exception as e:
            print(f"Error while creating NLP data: {e}")
            self.db.rollback() 
    
    def get_last_nlp_data(self):
        latest_item = self.db.exec(select(NLPData).order_by(-NLPData.nlp_data_id).limit(1)).first()
        return latest_item