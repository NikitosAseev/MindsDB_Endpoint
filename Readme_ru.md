# MindsDB_Endpoint
Интеграция модели ChatGPT (Эндпоинт) с SQL MindsDB.

Настройка:

1. Зарегистрируйтесь на https://mindsdb.com
2. Введите пароль и логин в .env
3. Создайте модель на Mindsdb, эти документы помогут вам: https://docs.mindsdb.com/integrations/ai-engines/openai 
Пример: 
CREATE MODEL model_name 
PREDICT answer 
USING engine = 'openai', 
model_name = 'openai_model_name', 
question_column = 'question', 
context_column = 'context', 
api_key = 'YOUR_OPENAI_API_KEY';
4. Готово! Вы также можете использовать мою работу для других целей, проект был создан как Эндпоинт для сайта Better GPT, на данный момент его дальнейшее развитие будет заморожено.
