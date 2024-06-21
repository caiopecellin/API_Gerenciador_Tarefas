#imports from libraries
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.responses import RedirectResponse, JSONResponse

#imports from app
from database import engine, Base
from controllers import task_controller

#create app FastAPI
app = FastAPI(
    title="API de Tarefas",
    description="API para gerenciamento de tarefas diárias",
    version="1.0.99",
    openapi_url="/openapi.json",
    docs_url=None,
    redoc_url=None,
    contact={
        "name": "Caio Pecellin Costa",
        "email": "caiopecellin@gmail.com",
        "url": "https://www.linkedin.com/in/caio-costa-a9606b187/"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },
    servers=[
        {
            "url": "http://localhost:8000",
            "description": "Servidor de desenvolvimento"
        }
    ],
)

#Create model in db
Base.metadata.create_all(bind=engine)
#Create routes about this model
app.include_router(task_controller.router)

#Function for handler errors
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": str(exc.detail)}
    )

#Function for handler any error
@app.exception_handler(Exception)
async def general_exception_handler(request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Um erro inesperado aconteceu"}
    )

#Function for first entry in api
@app.get("/", tags=["Redirect"], include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

#Function for declare openapi docs
@app.get("/docs", tags=["Redirect"], include_in_schema=False)
async def get_swagger_ui():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Swagger UI"
    )

#Function for openapi.json
@app.get("/openapi.json", tags=["Redirect"], include_in_schema=False)
async def get_openapi():
    return get_swagger_ui(
        title="API de Tarefas",
        version="1.0.99",
        description="API para gerenciamento de tarefas diárias",
        routes=app.routes,
    )

#Initialize app
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
