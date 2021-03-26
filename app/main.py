from fastapi import FastAPI
import uvicorn
from connexion import DataAccess as da

app = FastAPI()

#
#brief30.cnclzdom1btx.eu-west-3.rds.amazonaws.com

@app.get("/")
async def root():
    return {"message": "Coucou!!!!!!!"}

#see all facilities
@app.get("/api/info")
async def facilities():
    result = da.get_facilities()
    return result

@app.get("/api/cost/{cost}")
async def facilities(cost = None):
    result = da.get_cost(cost)
    return result

@app.get("/api/facility/{facility}")
async def facilities(facility = None):
    result = da.one_facility(facility)
    return result