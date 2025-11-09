from api import get_rag_answer
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import ORJSONResponse
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(default_response_class=ORJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    question: str


@app.post("/query")
def ask(query: Query):
    print("Fetching")
    response = get_rag_answer(query.question)
    print("Fetching done")
    return {"answer": response}


# print(get_rag_answer("What is Hybrid recommeation system"))
# if __name__ =='__main__':

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
