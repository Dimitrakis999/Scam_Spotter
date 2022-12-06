from fastapi import FastAPI
from api.scrape import get_photo_text
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/predict")
def predict(url):
    text , image =get_photo_text(url)
    x=pd.DataFrame({'text':text,
                    'image':image})
