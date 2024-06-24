import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDv06v0SjUCCwNaSoeTK-XwgbfgvDLVz9k")

model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("Как дела?")
print(response.text)