Fastapi ->
    high performance web framework for building APIs with python
    Comparable to nodeJS and GO
    intutive and less code duplication
    Automatic request validation using Pydantic
    Auto generation of OpenAI and Swagger docs

Install Fastapi ->
    poetry add fastapi uvicorn

Basic FastAPI application->
    FastAPI(): Initializes the application.
    @app.get("/"): Decorator to define a GET endpoint at the root path.
    async def: Defines an asynchronous function for better performance (async vs sync)
    BaseModel: Pydantic's base class for data models
    FastAPI automatically validates data based on the defined models.
    Type Hints: Enhance code readability and enable validation.
    path parameter vs query parameter

Running FastAPI application using Uvicorn->
    Uvicorn - ASGI server (Asynchronous Server Gateway Interface and is suitable for asynchronous applications)
    uvicorn main:app --reload
    main:app: refer to app object in main.py file
    reload: auto reload server with codechanges (useful in development and debugging)
    http://127.0.0.1:8000/
    
FastAPI documentation->
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
    Interactive interface to test API endpoints.
    Automatically generated from the code and type annotations.

Dockerizing FastAPI-> 
    Docker file, installing poetry dependency via poetry.lock
    docker build -t disfiiguredsoul/fastapi-app .
    docker run -d --name fastapi-container -p 80:80 disfiiguredsoul/fastapi-app
    docker push disfiiguredsoul/fastapi-app
Recap->
