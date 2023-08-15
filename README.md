# Kalimmat Arabic Words Collection

## Introduction

This March, I observed that the website [kalimmat.com](https://kalimmat.com/) was experiencing internal server errors, making certain pages and specific regex inaccessible. After attempting to notify them without receiving any response, I devised a script to salvage the dataset available on their site to ensure this valuable resources were preserved. Currently, the website is operational, and I have validated its functionality using my script.

## Script Overview

- **words.py**: This script is utilized to scrape Arabic words from `kalimmat.com`. Depending on the specified URL, it can fetch words that either start or end with a particular Arabic letter. The words are then processed, cleaned, and saved as a JSON file.
  
- **readjson.py**: As the name suggests, this script reads the JSON files created by `words.py`. It specifically retrieves words that end with a defined sequence of letters, but this behavior can be easily customized.

## Dataset Files

1. **startWithWords.json**: Contains words from the common dictionary scraped under the "starts-with" URL.
2. **startsWithWordsSome.json**: Features words from the official dictionary scraped under the "starts-with" URL.
3. **startWithWordsOLD.json**: An older dataset, representing the initial attempt to salvage the words from the site.
4. **endsWithWords.json**: Contains words from the common dictionary scraped under the "ends-with" URL.
5. **endsWithWordsSome.json**: Contains words from the official dictionary scraped under the "ends-with" URL.
6. **endsWithWordsOLD.json**: An older version of the dataset scraped under the "ends-with" URL.

## Usage

1. **Scraping Words**:
   Run the `words.py` script after selecting the desired URL (starts-with or ends-with). The scraped words will be saved to the respective JSON file.

2. **Reading the JSON Files**:
   Use the `readjson.py` script to read and process data from the JSON files. For instance, to retrieve words that end with a specific sequence of letters.


## Acknowledgments

I would like to express my appreciation to the team behind [kalimmat.com](https://kalimmat.com/) for providing such a valuable resource for the Arabic language. This dataset was created purely for preservation purposes, and all credit for the content goes to them.
