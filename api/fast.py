from fastapi import FastAPI
from api.scrape import scrape_text
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
from keras.models import load_model
from api.text_processing import preprocess_pad


NLP_MODEL_PATH = 'saved_models/nlp/nlp_model.h5'
app = FastAPI()
app.state.model =load_model(NLP_MODEL_PATH)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


#GET http://localhost:8000/predict?url='https://www.airgom-bruxelles.be/'

@app.get("/predict")
def predict(url:str):
    X_text = scrape_text(url)

    # Process text for model ingestion
    X_text_padded = preprocess_pad([X_text])

    # Do prediction with model
    prediction = app.state.model.predict(X_text_padded)


    return {'probability':float(prediction)}

@app.get("/")
def root():
    return {
    'greeting': 'Hello'
}
