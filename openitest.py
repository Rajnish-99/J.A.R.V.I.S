from openai import OpenAI
from config import apikey
client = OpenAI(api_key= apikey)

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="what is your namewhat is your name\n\nI am an AI and do not have a name. You can call me OpenAI. What can I assist you with?",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

# Completion(id='cmpl-8kDIVrL8PLLHVUXjPSMCvYaaFYBf6', choices=[CompletionChoice(finish_reason='stop', index=0, logprobs=None, text='')], created=1706024895, model='gpt-3.5-turbo-instruct', object='text_completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=None, prompt_tokens=34, total_tokens=34))
