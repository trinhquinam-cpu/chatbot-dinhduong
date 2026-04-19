from google import genai

client = genai.Client(api_key="AIzaSyDM0bzTDCCHcJrvKQ9FDXpPG9B2IDPH3rY")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Xin chào"
)

print(response.text)