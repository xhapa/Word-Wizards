# Spacy Text Processing

The `TextProcessing` class provides text processing capabilities using the SpaCy library for Natural Language Processing (NLP), along with additional libraries for language detection and keyword extraction.

## Initialization

- **Attributes**:
  - `text`: The input text for processing.
  - `__lang`: Detected language of the text using Langdetect.
  - `tokens`: List of tokenized words in the text.
  - `pos`: List of tuples containing token and its part-of-speech tag.
  - `lemmas`: List of lemmatized words.
  - `entities`: List of tuples containing named entities and their labels.
  - `summary`: A summary generated using the TextRank algorithm.

## Methods

- `lang_detection`: Property method that returns the detected language of the text.
- `nlp_pipeline_selector()`: Selects the SpaCy NLP pipeline based on the detected language and adds the TextRank algorithm.
- `remove_double_spaces()`: Removes double spaces from the text.
- `tokenization()`: Generator function for tokenizing the text.
- `tagging()`: Generator function for part-of-speech tagging.
- `words_counter()`: Counts the number of words in the text.
- `remove_stopwords_lemmatizer()`: Generator function for lemmatization after removing stopwords.
- `ner()`: Generator function for named entity recognition.
- `get_keywords()`: Generator function for extracting keywords using TextRank.
- `summarizer()`: Generates a summary using the TextRank algorithm.
- `json_dict`: Property method that returns a dictionary with processed text data.

## Preprocessing and Processing

- `get_preprocessing()`: Performs preprocessing steps, including language detection, NLP pipeline selection, and tokenization.
- `get_processing()`: Performs processing steps, including word counting, named entity recognition, keyword extraction, and summarization.

## Example Usage

```python
# Example usage of the TextProcessing class
text = "This is an example text for NLP analysis."
processor = TextProcessing(text)
await processor.get_preprocessing()
await processor.get_processing()
result = processor.json_dict
print(result)
```

Feel free to integrate this documentation into your project's README and extend it as needed. If you have specific details about the functionalities or additional use cases, please provide them, and I can incorporate them into the documentation.