from fastapi import FastAPI
app = FastAPI()

@app.get('/')
async def root():
    return {'amssage': 'Hello World'}

@app.get('/logwire')
async def root():
    return {'amssages': 'Hello from logwire'}