import requests
import json
url = "http://localhost:11434/api/generate"

headers = {
    "Content-Type": "application/json"
}
data = {
  "model": "llama2", # You can change this value to a different model if you have a different one installed.
  "prompt": "Why is the sky blue?",
  "stream": False
}
#
if response.status_code == 200:
    response_text = response.text
    data = json.loads(response.text)
    actual_response = data["response"]
    print(actual_reponse)
else:
    print("Error:", response.status_code, response.text
