from fastapi import FastAPI
import uvicorn
from sqlalchemy import create_engine  
from sqlalchemy import text

# engine = create_engine("postgresql://postgres:12345678*@database-2.cee2fckq20ga.us-east-1.rds.amazonaws.com:5432/postgres", echo=True)
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
app = FastAPI()
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("create table text (text varchar)"))
    # conn.commit()
    print(result)


@app.get("/")
def hellow():
    return "oi esse é o back do betinho"
@app.post("/add")   
def add(text:str):
    with engine.connect() as conn:
        result = conn.execute(text(f"INSERT INTO text (text)VALUES ({text})"))
        conn.commit()
    print(result.all())

@app.get("/read")
def read():
    with engine.connect() as conn:
        result = conn.execute(text("Select * from text"))
    print(result.all())
    return result.all()

if __name__ == "__main__":
    uvicorn.run(app)