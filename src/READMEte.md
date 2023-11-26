# Text Router

The `text_router` in your FastAPI application provides endpoints for handling text input and submission for NLP analysis.

## Endpoints

### Text Input Form

- **Endpoint**: `/text/`
- **Method**: GET
- **Description**: Displays the form for entering text to be analyzed using NLP.

### Submit Text for Analysis

- **Endpoint**: `/text/submit`
- **Method**: POST
- **Description**: Submits the entered text for NLP analysis. Redirects to the analysis route (`/analyze/`) to view the results.

## Templates

- The form for entering text is located at `'from_text.html'`.

## Dependencies

- The `NLPDataService` class from `services/nlp_data.py` is used to interact with NLP data in the database.

## Analyze Route

- The `submit` endpoint sets cookies for `text_data` and `id_data` and redirects to the analysis route (`/analyze/analyze_it`).

Feel free to extend this documentation as needed. If you have specific details about the templates or additional functionalities, please provide them, and I can incorporate them into the documentation.