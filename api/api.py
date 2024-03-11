import requests


def check_api_key(func):
    def wrapper(*args, **kwargs):
        api_key = kwargs.get('api_key', None)
        base_url = kwargs.get('base_url', None)
        if not api_key:
            raise ValueError('请配置API_KEY')
        kwargs['api_key'] = api_key
        if not base_url:
            base_url = 'https://api.openai.com'
        kwargs['base_url'] = base_url
        print(kwargs)
        return func(*args, **kwargs)

    return wrapper


@check_api_key
def completions(message, api_key=None, base_url=None):
    """Get completions for the message."""
    url = f"{base_url}/v1/completions"
    response = requests.post(
        url,
        json=message.dict(),
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=60,
    )
    return response.json()


@check_api_key
def completions_turbo(message, api_key=None, base_url=None):
    """Get completions for the message."""
    url = f"{base_url}/v1/chat/completions"
    response = requests.post(
        url,
        json=message.dict(),
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=60,
    )
    return response.json()


@check_api_key
def credit_summary(api_key=None, base_url=None):
    """Get the credit summary for the API key."""
    url = f"{base_url}/dashboard/billing/credit_grants"
    response = requests.get(
        url,
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=60,
    )
    return response.json()
