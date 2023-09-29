from fastapi import FastAPI
import uvicorn
from sqlalchemy import create_engine  
from sqlalchemy import text

# engine = create_engine("postgresql://postgres:12345678*@database-2.cee2fckq20ga.us-east-1.rds.amazonaws.com:5432/postgres", echo=True)

engine = create_engine("sqlite:///db.sqlite")

conn = engine.connect() 
app = FastAPI()
from sqlalchemy import text

result = conn.execute(text("create table text (text varchar)"))
conn.close()
  


@app.get("/")
def hellow():
    return "oi esse é o back do betinho"
@app.post("/add")   
def add(text2:str):
    conn = engine.connect() 
    result = conn.execute(text(f"INSERT INTO text (text) VALUES ('{text2}')"))
    
    print(result.all())

@app.get("/read")
def read():
    conn = engine.connect() 
    result = conn.execute(text("Select * from text"))
    print(result.all())
    return result.all()

if __name__ == "__main__":
    uvicorn.run(app)