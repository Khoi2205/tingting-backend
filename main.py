from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user_id: int
    username: str | None = None
    text: str

@app.post("/webhook")
async def webhook(msg: Message):
    text = msg.text.lower().strip()
    
    if text in ["/start", "menu", "/menu", "chào"]:
        return {
            "reply": "👋 Chào bạn!\nChọn chức năng bên dưới:",
            "reply_markup": {
                "inline_keyboard": [
                    [{"text": "🎲 Random tên", "url": "https://t.me/baokmnetbot?start=random"}],
                    [{"text": "✍️ Nhập tên", "url": "https://t.me/baokmnetbot?start=nhapten"}],
                    [{"text": "🔍 Kiểm tra tài khoản", "url": "https://t.me/baokmnetbot?start=check"}],
                    [{"text": "💸 Rút tiền", "url": "https://t.me/baokmnetbot?start=ruttien"}],
                    [{"text": "📦 VA đã tạo", "url": "https://t.me/baokmnetbot?start=va"}],
                    [{"text": "ℹ️ Thông tin", "url": "https://t.me/baokmnetbot?start=info"}]
                ]
            }
        }
    
    return {"reply": "✅ Đã nhận tin nhắn!"}

@app.get("/")
async def root():
    return {"status": "Backend OK"}
