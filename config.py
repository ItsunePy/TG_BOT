def token():
    with open('token.txt', 'r') as f: return f.read()

BOT_API_TOKEN = token

rzhunemogu_DICT = {
    'Анекдот': 1,
    'Афоризм': 4,
    'Тост': 6,
}