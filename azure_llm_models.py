# Databricks notebook source
# DBTITLE 1,Library Imports
# MAGIC %pip install openai

# COMMAND ----------

# DBTITLE 1,Example Using Azure Open AI
import os
import requests
import json
import openai

openai.api_key = "XXXXXXXX"
openai.api_base = "https://ra-openai-dev.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2022-12-01' # this may change in the future

deployment_name = 'textdavinci003' #This will correspond to the custom name you chose for your deployment when you deployed a model. 

# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'Who created the atomic bomb?'
response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=10)
text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print(start_phrase+text)

# COMMAND ----------

# DBTITLE 1,Example Using Azure Open AI with HTTP Requests
import requests
url = "https://ra-openai-dev.openai.azure.com/openai/deployments/textdavinci003/completions?api-version=2022-12-01"
headers = {"api-key": "XXXXXXX", "Content-Type": "application/json"}
body = '''{
  "prompt": "Once upon a time", 
  "max_tokens": 100, 
  "temperature": 1
}'''
response = requests.post(url, headers = headers, data = body)
print(response.text)

# COMMAND ----------

response.content

# COMMAND ----------


