import uvicorn



if __name__ == "__main__":
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)# To run this FastAPI application, use the following commands to set up your environment:







# pip install uv
# python -m pip install uv                 (reliable)

# uv init .
# uv add fastapi
# uv add python-dotenv
# uv add fastapi-users[sqlalchemy]
# uv add imagekitio
# uv add uvicorn[standard]
# uv add aiosqlite



# http://localhost:8000/docs/redoc