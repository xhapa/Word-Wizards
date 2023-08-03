from sqlmodels.nlp_data import NLPData

class NLPDataService():
    def __init__(self, db) -> None:
        self.db = db