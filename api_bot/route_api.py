from fastapi import APIRouter
from API import chatbot

router = APIRouter()
router.include_router(chatbot.router)