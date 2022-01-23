from fastapi import FastAPI 
import os
from Finding_CS import chatbot
import uvicorn

app = FastAPI()

@app.get('/')
async def root():
    return { "Message" : "Finding Answers"}

@app.post('/questions')
async def get_answer(ques: str):
    obj = chatbot()
    Dictionary_Of_QA = obj.GettingAnswers(ques)
    return Dictionary_Of_QA

if __name__=="__main__":
    uvicorn.run(app)