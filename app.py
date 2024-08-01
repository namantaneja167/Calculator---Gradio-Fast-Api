from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"This is a simple api to do mathematical operations"}

@app.get("/addition/{number1}/{number2}")
def addition(number1,number2):
    return {int(number1)+int(number2)}

@app.get("/subtraction/{number1}/{number2}")
def subtract(number1,number2):
    return {int(number1)-int(number2)}

@app.get("/multiplication/{number1}/{number2}")
def multiply(number1,number2):
    return {int(number1)*int(number2)}

@app.get("/division/{number1}/{number2}")
def divide(number1,number2):
    return {int(number1)/int(number2)}