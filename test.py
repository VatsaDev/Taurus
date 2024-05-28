import google.generativeai as genai
import PIL.Image

genai.configure(api_key="AIzaSyARyT-7H4EBEgWUFixOtj8tjne-luUUPfI")
model = genai.GenerativeModel('gemini-1.5-flash-latest')

q = "whats in this image?"
img = PIL.Image.open('C:\\Users\\vatsa\\Desktop\\projects\\taurus\\testpic.png')

response = model.generate_content([q,img], stream=True)

for chunk in response:
  print(chunk.text)