import os

import httpx

API_KEY = os.environ.get('API_KEY')


def check_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = kwargs.get('api_key', API_KEY) or API_KEY
        if not api_key:
            raise ValueError('API key is required')
        if not api_key.startswith('sk-'):
            raise ValueError('API key must start with "sk-"')
        kwargs['api_key'] = api_key
        return func(*args, **kwargs)

    return wrapper


@check_api_key
async def completions(message, api_key=None):
    """Get completions for the message."""
    url = "https://api.openai.com/v1/completions"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            json=message.dict(),
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=60,
        )
        return response.json()


@check_api_key
async def completions_turbo(message, api_key=None):
    """Get completions for the message."""
    url = "https://api.openai.com/v1/chat/completions"
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            json=message.dict(),
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=60,
        )
        return response.json()


@check_api_key
async def credit_summary(api_key=None):
    """Get the credit summary for the API key."""
    url = "https://api.openai.com/dashboard/billing/credit_grants"
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=60,
        )
        return response.json()
