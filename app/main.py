from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.get('/logwire')
async def root():
    return {'messages': 'Hello from logwire'}