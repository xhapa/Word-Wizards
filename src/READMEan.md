# Analyze Route

The `analyze_route` in your FastAPI application provides endpoints for NLP analysis. It includes routes for analyzing text, counting words, extracting entities, identifying keywords, and generating a summary.

## Endpoints

### Analyze Text

- **Endpoint**: `/analyze/`
- **Method**: GET
- **Description**: Analyzes the provided text using NLP. If no `nlp_data_id` is provided, a new NLP analysis entry is created. Returns the analysis menu template.

### Words Count

- **Endpoint**: `/analyze/words-count/{nlp_data_id}`
- **Method**: GET
- **Description**: Displays the word count for a specific NLP analysis identified by `nlp_data_id`.

### Entities

- **Endpoint**: `/analyze/entities/{nlp_data_id}`
- **Method**: GET
- **Description**: Displays the named entities extracted during NLP analysis for a specific `nlp_data_id`.

### Keywords

- **Endpoint**: `/analyze/keywords/{nlp_data_id}`
- **Method**: GET
- **Description**: Displays the keywords extracted during NLP analysis for a specific `nlp_data_id`.

### Summary

- **Endpoint**: `/analyze/summary/{nlp_data_id}`
- **Method**: GET
- **Description**: Displays the summary generated during NLP analysis for a specific `nlp_data_id`.

## Templates

- The analysis menu template is located at `'analyze_menu.html'`.
- Templates for words count, entities, keywords, and summary pages are located at `'./content/words_count_page.html'`, `'./content/entities_page.html'`, `'./content/keywords_page.html'`, and `'./content/summary_page.html'`, respectively.

## Dependencies

- The `NLPDataService` class from `services/nlp_data.py` is used to interact with NLP data in the database.

## Cookies

- The `analyze_it` endpoint reads the `text_data` and `id_data` cookies to determine whether to create a new NLP analysis entry or use an existing one.

Feel free to extend this documentation as needed. If you have specific details about the templates or additional functionalities, please provide them, and I can incorporate them into the documentation.