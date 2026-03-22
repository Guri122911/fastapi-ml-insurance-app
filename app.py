from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.predicted_response import PredictionResponse
from schema.user_input import UserInput
from model.predict import predict_output, model, Model_version

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Insurance Premium Category Prediction API'}

@app.get('/health')
def health_check():
    return {
        'status': 'ok',
        "version": Model_version
    }

@app.post('/predict')
def predict_premium(data: UserInput):

    user_input = {
    'bmi': data.bmi,
    'age_group': data.age_group,
    'liftstyle_risk': data.lifestyle_risk,  # 👈 yahi rakho
    'city_tier': data.city_tier,
    'income_lpa': data.income_lpa,
    'occupation': data.occupation
}
    
    try:
        
        prediction = predict_output(user_input)

        return JSONResponse(
        status_code=200,
        content={'predicted_category': prediction}
        )
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))    