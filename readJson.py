import json
import codecs

# Open the file in read mode with codecs module to handle Arabic characters
with codecs.open('endsWithWords.json', mode='r', encoding='utf-8') as f:
    # Load the JSON data from the file
    data = json.load(f)

# Print the data to verify it was loaded correctly
# words_with_m = [word for sublist in data["alf"].values() for word in sublist if word.endswith("اب")] # words that ends with alf-baa.
words = [word for sublist in data["alf"].values() for word in sublist if word.endswith("اب")]
print(data)

