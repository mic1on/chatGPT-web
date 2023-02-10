import os

import httpx


async def completions(message):
    url = "https://api.openai.com/v1/completions"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            json=message.dict(),
            headers={
                "Authorization": f"Bearer {os.environ.get('API_KEY')}",
            },
            timeout=60,
        )
        return response.json()
