from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# mount static directory for serving up static files like index.html or favicon.ico
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Define the root route, do not allow it to display on the /docs schema, navigating to this endpoint will return html
@app.get("/", include_in_schema=False, response_class=HTMLResponse)
def root():
    with open("app/static/index.html") as f:
        return HTMLResponse(content=f.read())
