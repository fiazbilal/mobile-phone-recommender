# Mobile Phone Recommendation System

## Project Overview
A machine learning-powered system for mobile phone recommendations with web scraping capabilities.

## Database
```bash
cd be
```
To create database run:
```bash
python app/db/create_db.py
```

To apply migrations:
```bash
python app/db/run_migrations.py
```

## Setup
1. Create virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python run.py`

## Features
- Web scraping for mobile phone data
- Machine learning recommendations
- Health check endpoint