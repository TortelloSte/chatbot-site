from fastapi import FastAPI, APIRouter, HTTPException, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

router = APIRouter(
    prefix="/chatbot",
    tags=["VersionOne"],
    responses={404: {"description": "Not Found"}},
)

class ChoiceRequest(BaseModel):
    choice: str

@router.get("/chatbot/")
async def chatbot():
    return HTMLResponse("""
        <html>
        <head>
            <title>Chatbot</title>
        </head>
        <body>
            <h1>Scegli un'opzione:</h1>
            <form action="/chatbot/make_choice/" method="post">
                <select name="choice">
                    <option value="1">Voglio chiedere un preventivo</option>
                    <option value="2">Mi voglio iscrivere alla newsletter</option>
                    <option value="3">Ho già il preventivo, voglio contattare qualcuno</option>
                </select>
                <input type="submit" value="Invia">
            </form>
        </body>
        </html>
    """)

@router.post("/chatbot/make_choice/")
async def make_choice(choice: str = Form(...)):
    if choice == "1":
        return {"message": "Hai scelto di chiedere un preventivo."}
    elif choice == "2":
        return {"message": "Hai scelto di iscriverti alla newsletter."}
    elif choice == "3":
        return {"message": "Hai già un preventivo e vuoi contattare qualcuno."}
    else:
        raise HTTPException(status_code=400, detail="Scelta non valida")