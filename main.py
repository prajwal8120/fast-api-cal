# main.py
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development purposes)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>FastAPI Calculator</title>
        </head>
        <body>
            <h2>FastAPI Calculator</h2>
            <form action="/calculate" method="post">
                <label for="num1">Number 1:</label>
                <input type="number" step="any" id="num1" name="num1" required>

                <label for="num2">Number 2:</label>
                <input type="number" step="any" id="num2" name="num2" required>

                <label for="operation">Operation:</label>
                <select id="operation" name="operation" required>
                    <option value="add">Addition</option>
                    <option value="subtract">Subtraction</option>
                    <option value="multiply">Multiplication</option>
                    <option value="divide">Division</option>
                </select>

                <button type="submit">Calculate</button>
            </form>
        </body>
    </html>
    """

@app.post("/calculate")
def calculate(
    num1: float = Form(...),
    num2: float = Form(...),
    operation: str = Form(...),
):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            raise ValueError("Cannot divide by zero")
    else:
        raise ValueError("Invalid operation")

    return {"result": result}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

