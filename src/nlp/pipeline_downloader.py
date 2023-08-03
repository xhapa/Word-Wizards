# Spacy
import spacy

def pipeline_downloader():
    spacy.cli.download("en_core_web_md")
    spacy.cli.download("nl_core_news_md")
    spacy.cli.download("es_core_news_md")
