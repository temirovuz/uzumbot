from dotenv import dotenv_values

envfile = dotenv_values(".env")
bot_token = envfile['TOKEN']