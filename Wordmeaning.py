import requests

word = 'pneumonoultramicroscopicsilicovolcanoconiosis'
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(f"Definitions for '{word}':")
    for meaning in data[0]['meanings']:
        part_of_speech = meaning['partOfSpeech']
        for definition in meaning['definitions']:
            print(f"({part_of_speech}) - {definition['definition']}")
else:
    print(f"Error {response.status_code}: Word not found or other issue.")
