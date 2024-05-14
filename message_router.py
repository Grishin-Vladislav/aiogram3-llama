from aiogram import Router
from aiogram.types import Message
import openai

router = Router()
history = [
    {
        "role": "system",
        "content": "You are an intelligent assistant."
    }
]


@router.message()
async def any_message(message: Message, client: openai.Client):
    history.append({"role": "user", "content": message.text})
    completion = client.chat.completions.create(
        model="local-model",
        messages=history,
        temperature=0.7,
    )
    content = completion.choices[0].message.content
    new_message = {"role": "assistant", "content": content}
    history.append(new_message)
    await message.answer(content)
