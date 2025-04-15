import requests

webhook_url = 'https://discord.com/api/webhooks/1361601007905149050/qqOS0Cd6Qi5C8fvYDzaVquL2q5H3qfUl-UlhLO3bPcdgHE4TsRy_wzEj6chC-kCRApO-'
data = {
    "content": "Ahoj! Právě jsem něco udělal ve VS Code 💻"
}

requests.post(webhook_url, json=data)
