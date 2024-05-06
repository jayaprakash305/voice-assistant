import pyttsx3
import wikipedia
from googlesearch import search

# Initialize the pyttsx3 engine for voice output
voice_engine = pyttsx3.init()

def search_wikipedia(query):
    try:
        # Search Wikipedia for the query and get a summary
        result_summary = wikipedia.summary(query, sentences=3)
        return result_summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation error (when the query is ambiguous)
        return "Ambiguous search query. Please be more specific."
    except wikipedia.exceptions.PageError as e:
        # Handle page error (when the query doesn't match any Wikipedia page)
        return "No page found for the given query."

def search_google(query):
    try:
        # Search Google and get the top search result
        search_results = search(query, lang='en')
        return next(search_results)
    except Exception as e:
        return "Error occurred while searching Google."

# Get user input for search query
search_query = input("Searching: ")

# Search Wikipedia
wikipedia_result = search_wikipedia(search_query)

# Search Google
google_result_url = search_google(search_query)

# Print and speak the results
print("Wikipedia Summary:")
print(wikipedia_result)
voice_engine.say("Wikipedia Summary:")
voice_engine.say(wikipedia_result)

print("\nTop Google Result:")
print(google_result_url)
voice_engine.say("Top Google Result:")
voice_engine.say(google_result_url)

# Run and wait for voice output
voice_engine.runAndWait()
