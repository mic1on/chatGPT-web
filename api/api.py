import os

import httpx

API_KEY = os.environ.get('API_KEY')
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
}


async def completions(message):
    """Get completions for the message."""
    url = "https://api.openai.com/v1/completions"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            json=message.dict(),
            headers=HEADERS,
            timeout=60,
        )
        return response.json()


async def credit_summary():
    """Get the credit summary for the API key."""
    url = "https://api.openai.com/dashboard/billing/credit_grants"
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers=HEADERS,
            timeout=60,
        )
        return response.json()
