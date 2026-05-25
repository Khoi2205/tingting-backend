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
            "reply": "👋 Chào bạn!\nChọn chức năng bên dưới để chuyển sang bot chính:",
            "reply_markup": {
                "keyboard": [
                    [{"text": "🎲 Random tên"}],
                    [{"text": "✍️ Nhập tên"}],
                    [{"text": "🔍 Kiểm tra tài khoản"}],
                    [{"text": "💸 Rút tiền"}],
                    [{"text": "📦 VA đã tạo"}],
                    [{"text": "ℹ️ Thông tin"}]
                ],
                "resize_keyboard": True
            }
        }
    
    return {"reply": "✅ Đã nhận tin nhắn!\nGõ 'menu' để hiện menu."}

@app.get("/")
async def root():
    return {"status": "Backend OK"}
