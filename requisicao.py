import automatizar
import settings
import requests


mensagem = automatizar.chamada("https://www.cnnbrasil.com.br/tecnologia/")
mensagem = [item for frase in mensagem for item in frase]
mensagem = "\n\n".join(mensagem)

headers = {
  "Content-Type": "application/json",
  "apikey": settings.EVOLUTION_API_TOKEN
}
url = f"{settings.EVOLUTION_API_URL}/message/sendText/{settings.EVOLUTION_INSTANCE}"
payload = {
  "number": "5551990136528",
  "text": mensagem,
}

try:

  response = requests.post(url, json=payload, headers=headers)
  response_data = response.json()

  if response.status_code == 200 or response.status_code == 201:
      print (response_data)
  else:
      print (response_data)

except Exception as e:
    print(e)