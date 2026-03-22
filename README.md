# FastAPI ML Insurance Premium Prediction

## Project Overview

This project is a Machine Learning API built using FastAPI that predicts the insurance premium category based on user input such as age, BMI, smoking status, city tier, and other personal details. The project also includes a frontend interface and Docker support for deployment.

---

## Features

* FastAPI backend for prediction API
* Machine Learning model integration
* Streamlit frontend UI
* Docker support for containerization
* REST API with Swagger documentation
* Insurance premium category prediction

---

## Tech Stack

* Python
* FastAPI
* Machine Learning (Scikit-learn)
* Streamlit
* Docker
* Uvicorn

---

## Project Structure

```
fastapi-ml-insurance-app/
│
├── app.py
├── frontend.py
├── requirements.txt
├── dockerfile
├── README.md
├── .gitignore
│
├── config/
│   └── city_tier.py
│
├── model/
│   └── predict.py
│
├── schema/
│   ├── user_input.py
│   └── predicted_response.py
```

---

## Installation

### Step 1: Clone Repository

```
git clone https://github.com/your-username/fastapi-ml-insurance-app.git
cd fastapi-ml-insurance-app
```

### Step 2: Install Requirements

```
pip install -r requirements.txt
```

---

## Run FastAPI Server

```
uvicorn app:app --reload
```

FastAPI will run on:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## Run Frontend (Streamlit)

```
streamlit run frontend.py
```

---

## Run Using Docker

```
docker build -t fastapi-insurance .
docker run -p 8000:8000 fastapi-insurance
```

---

## API Endpoints

| Method | Endpoint | Description                        |
| ------ | -------- | ---------------------------------- |
| GET    | /        | Home                               |
| POST   | /predict | Predict Insurance Premium Category |
| GET    | /docs    | Swagger UI                         |

---

## Example Input

```
{
  "age": 30,
  "bmi": 25.4,
  "children": 2,
  "smoker": "no",
  "city": "Chandigarh"
}
```

## Example Output

```
{
  "predicted_category": "Medium"
}
```

---

## Author

Gursewak Singh

---

## Future Improvements

* Deploy on AWS / Render
* Add database support
* Improve ML model accuracy
* Add authentication
