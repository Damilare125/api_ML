from fastapi import FastAPI
import uvicorn
import pickle


app = FastAPI(debug=True)

@app.get('/')
def home():
    return {'text': 'Planting and Harvesting of Crops Prediction'}


@app.get('/predict')
def predict(label_En: str, Country_En: str):
    model = pickle.load(open('C:/Users/new/OneDrive/Desktop/Data science/Model_pickle1', 'rb'))
    make_prediction = model.predict([[label_En, Country_En]])
    output = make_prediction
    
    return {'You can plant your crop during the {} season'.format(output)}

if __name__ == '__main__':
    uvicorn.run(app)
