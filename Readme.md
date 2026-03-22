# FastAPI ML Insurance Premium Prediction

This project is a Machine Learning API built using FastAPI that predicts the insurance premium category based on user input.

## Features

* FastAPI Backend
* Machine Learning Model
* Insurance Premium Prediction
* Docker Support
* Frontend UI
* REST API

## Project Structure

```
app.py
frontend.py
dockerfile
requirements.txt
config/
model/
schema/
```

## Installation

```bash
pip install -r requirements.txt
```

## Run FastAPI

```bash
uvicorn app:app --reload
```

## Run Frontend

```bash
streamlit run frontend.py
```

## Docker Run

```bash
docker build -t fastapi-insurance .
docker run -p 8000:8000 fastapi-insurance
```

## Author

Gursewak Singh
