# MindsDB_Endpoint
Integrating the ChatGPT (endpoint) model with SQL MindsDB.


Setup:

1. Register at https://mindsdb.com
2. Enter password and login into .env
3. Create a model on mindsdb, these docs will help you: https://docs.mindsdb.com/integrations/ai-engines/openai
Example:
CREATE MODEL model_name
PREDICT answer
USING
engine = 'openai',
model_name = 'openai_model_name',
question_column = 'question',
context_column = 'context',
api_key = 'YOUR_OPENAI_API_KEY';
4. Done! You can also use my work for other purposes, the project was created as an endpoint for the Better GPT website, at the moment its further development will be frozen.

