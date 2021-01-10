A simple application to learn deployment of ML model using FastAPI

## Key Learnings
1.  FastAPI application consist of main file which is responsible for:
    1.  launching the application
    2.  defining the endpoints
    3.  Add defining additional modules used by the endpoints
2.  main.py
    1.  fastapi which provides API functionality
    2.  BaseModel from pydantic acts as a model for HTTP Requests and Response
        1.  pydantic module also adds validations for user inputs
3.  Use dependency injection while building Model class for better unit testing
4.  The application can be packaged using Docker commands inside Dockerfile
5.  docker-compose.yaml file is used to combine containers
6.  ci.yaml file under .github/workflows allows to automate GitHub actions upon predefined triggers

## Commands used
### Launch the Service
```
uvicorn api.main:app
```
### Post the request when the server is running
```
127.0.0.1:8000/docs
```
or
```
curl -X POST "http://127.0.0.1:8000/predict" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"data\":[[0,0,0,0,0,0,0,0,0,0,0,0,0]]}"
```
### Docker compose
1.  Launching the service
```
docker-compose up
```
2.  Testing
```
docker-compose -f docker-compose.test.yaml up --abort-on-container-exit --exit-code-from fastapi-ml-learning
```

Referenced from - <a href="https://github.com/cosmic-cortex/fastAPI-ML-quickstart">GitRepo</a>
