from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="TingTing Backend")

class Message(BaseModel):
    user_id: int
    username: str | None = None
    text: str
    bot_type: str = "slave"

@app.post("/webhook")
async def webhook(msg: Message):
    text = msg.text.lower().strip()
    
    if text in ["/start", "hi", "hello", "chào"]:
        reply = "👋 Chào bạn! Đây là bot thử nghiệm thể tính tăng.\nBạn cần hỗ trợ gì?"
    elif any(word in text for word in ["tăng", "tang", "kích", "to", "lon"]):
        reply = "🔥 Tính năng tăng thể tính đang được kích hoạt...\n\nVui lòng chọn gói bạn quan tâm."
    else:
        reply = "✅ Đã nhận tin nhắn của bạn!"

    return {"reply": reply}

@app.get("/")
async def root():
    return {"status": "Backend đang chạy tốt!"}
