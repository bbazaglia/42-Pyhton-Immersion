# References: 
# https://www.mediawiki.org/wiki/API:Search
# https://www.jcchouinard.com/wikipedia-api/

import sys
import json
import dewiki
import requests

def search_wiki(query, language='en'):
    url = f"https://{language}.wikipedia.org/w/api.php"
    
    # Perform a search request to find the most relevant Wikipedia page title
    # that closely matches the query, ignoring case sensitivity and minor misspellings
    search_params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': query,  # Search for the query term in Wikipedia
        'srlimit': 1        # Limit results to the most relevant match
    }
    
    search_response = requests.get(url, params=search_params)
    
    if search_response.status_code != 200:
        print(f"Error: HTTP {search_response.status_code}")
        return ''
    
    search_data = search_response.json()

    # Print the entire JSON response to understand its structure
    # print(json.dumps(search_data, indent=4))

    if not search_data.get('query', {}).get('search', []):
        print("No search results found.")
        return ''
    
    exact_title = search_data['query']['search'][0]['title']
    
    # Retrieve the content of the Wikipedia page using the exact title obtained from the search results
    extract_params = {
        'action': 'query',          
        'format': 'json',           
        'titles': exact_title,      # Use the exact page title obtained from the search
        'prop': 'extracts',         # Request the 'extracts' property to get the page content
        'exintro': True,            # Limit the extract to the introduction section only
        'explaintext': True         # Return the content in plain text format (without HTML markup)
    }
    
    extract_response = requests.get(url, params=extract_params)
    
    if extract_response.status_code != 200:
        print(f"Error: HTTP {extract_response.status_code}")
        return ''
    
    extract_data = extract_response.json()
    
    pages = extract_data.get('query', {}).get('pages', {})
    
    if not pages:
        print("No pages found.")
        return ''
    
    page = next(iter(pages.values()))
    
    if 'extract' not in page:
        print("No extract found for the page.")
        return ''
    
    return page.get('extract', '')

def remove_wiki_markup(text):
    return dewiki.from_string(text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <name_of_search>")
        sys.exit(1)
    
    query = sys.argv[1]

    print(f"Searching for: {query}")
    wiki_result = search_wiki(query, 'en')

    if not wiki_result:
        print("No content returned from Wikipedia.")
        sys.exit(1)

    wiki_result_formatted = remove_wiki_markup(wiki_result)

    filename = f"{query.replace(' ', '_')}.wiki"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(wiki_result_formatted)

    print(f"Result saved to: {filename}")

if __name__ == "__main__":
    main()