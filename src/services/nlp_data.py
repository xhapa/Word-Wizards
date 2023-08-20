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
    
    def get_all_nlp_data(self):
        return self.db.query(NLPData).all()
    
    def get_by_id_nlp_data(self, text_id):
        return self.db.query(NLPData).filter(NLPData.nlp_data_id == text_id).first()

    async def update_nlp_data(self, text_id, text):
        nlp_data = self.db.query(NLPData).filter(NLPData.nlp_data_id == text_id).first()
        nlp_prepro = TextProcessing(text)
        await nlp_prepro.get_preprocessing()
        await nlp_prepro.get_processing()
        parse_data = nlp_prepro.json_dict

        if nlp_data is None:
            return None

        for key, value in parse_data.items():
            setattr(nlp_data, key, value)

        self.db.commit()
        self.db.refresh(nlp_data)
        return nlp_data