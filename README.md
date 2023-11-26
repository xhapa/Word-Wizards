# Word Wizards

Word Wizards is a FastAPI-based web application for Natural Language Processing (NLP) analysis. It allows users to input text, analyze it using NLP, and view the analysis history.
## Getting Started

To run the Word Wizards application locally, follow these steps:

1. Clone the repository:
    
```bash
git clone https://github.com/xhapa/Word-Wizards.git
cd Word-Wizards
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
uvicorn main:app --reload
```
Open your web browser and go to http://localhost:8000 to access Word Wizards.

## Features
### Home Page

```/```: Displays the home page of Word Wizards.

### About Page

```/about```: Provides information about the Word Wizards application.

### Documentation

```/doc```: Redirects to the Word Wizards GitHub repository for documentation.

### History Page

```/history```: Displays the history of NLP analysis performed by Word Wizards users.

### Analyze Text

```/history/{nlp_data_id}```: Redirects to the NLP analysis page for a specific text based on the nlp_data_id.

### Update Text

```/history/update/{nlp_data_id}```: Updates the text associated with a specific NLP analysis identified by nlp_data_id.

## Project Structure

* ```main.py```: Entry point of the application.
* ```config/db.py```: Database configuration and setup.
* ```routers/from_text.py```: Router for handling text-related operations.
* ```routers/analyze.py```: Router for NLP analysis operations.
* ```nlp/pipeline_downloader.py```: Downloads NLP pipelines.
* ```services/nlp_data.py```: Handles NLP data-related services.

## Dependencies

* uvicorn: ASGI server for the FastAPI application.
* fastapi: Fast web framework for building APIs.
* jinja2: Template engine for HTML responses.
* sqlalchemy: SQL toolkit and Object-Relational Mapping (ORM) for database operations.

## Contributing

If you would like to contribute to Word Wizards, please follow the contribution guidelines.
