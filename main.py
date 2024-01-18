import os
import requests
from gtts import gTTS



# Transalate text to any language using RapidAPI
def translate(text,lang):
	url = "https://text-translator2.p.rapidapi.com/translate"
	payload = {
		"source_language": "en",
		"target_language": lang.lower(),
		"text": text
	}
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": "2664300b65mshaf894fcb83028f2p1123dajsnfbf8d3b59672",
		"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
	}
	# posting a request to the API
	response = requests.post(url, data=payload, headers=headers)
	response = response.json()
	return response['data']['translatedText']

# Get language code based on language name
def get_languages(lang):
	language_code = None
	url = "https://text-translator2.p.rapidapi.com/getLanguages"
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"X-RapidAPI-Key": "2664300b65mshaf894fcb83028f2p1123dajsnfbf8d3b59672",
		"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
	}
	# getting a request to the API
	response = requests.get(url, headers=headers)
	response = response.json()
	# Find the language code based on language name
	for language in response['data']['languages']:
		if lang.lower() == language['name'].lower():
			language_code = language['code']
			break
		else:
			language_code = "Not found"
			continue
	return language_code
# Testing
# Convert text to speech/ for macos
def text_to_speech(text):
	text = "The word you translate is: " + text
	tts = gTTS(text=text, lang='en', slow=False)
	tts.save("output.mp3")
	# for windows
	if os.name == 'nt':
		os.startfile("output.mp3")
	# for macos
	else:
		os.system("afplay output.mp3")


# Main function
print("If you are done choosing languages, enter 'q' to quit")
while True:
	find_lang = input("Enter nationality to find: ")
	if find_lang == 'q':
		print('\n' * 50)
		break
	print("Langauge code:",get_languages(find_lang))


langauge = input("Enter language code: ")
print("Enter 'q' to quit")
while True:
	text = input("Enter text to translate: ")
	result = translate(text, langauge)
	text_to_speech(result)
	if text == 'q':
		break

