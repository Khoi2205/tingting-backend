from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    user_id: int
    username: str | None = None
    text: str
    bot_type: str = "slave"

@app.post("/webhook")
async def webhook(msg: Message):
    text = msg.text.lower().strip()
    
    if text in ["/start", "hi", "hello", "chào", "menu"]:
        reply = "👋 Chào bạn!\nChọn chức năng bên dưới:"
        buttons = {
            "inline_keyboard": [
                [{"text": "🎲 Random tên", "url": "https://t.me/baokmnetbot?start=random"}],
                [{"text": "✍️ Nhập tên", "url": "https://t.me/baokmnetbot?start=nhapten"}],
                [{"text": "🔍 Kiểm tra tài khoản", "url": "https://t.me/baokmnetbot?start=check"}],
                [{"text": "💸 Rút tiền", "url": "https://t.me/baokmnetbot?start=ruttien"}],
                [{"text": "ℹ️ Thông tin", "url": "https://t.me/baokmnetbot?start=info"}]
            ]
        }
        return {"reply": reply, "reply_markup": buttons}
    
    else:
        return {"reply": "✅ Đã nhận! Vui lòng chọn menu bên dưới."}

@app.get("/")
async def root():
    return {"status": "ok"}
