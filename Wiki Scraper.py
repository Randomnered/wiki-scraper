import requests
from bs4 import BeautifulSoup

print("=== DYNAMIC WIKIPEDIA SEARCHER ===")
# 1. Ask the user what they want to search for
user_keyword = input("Enter a topic to search on Wikipedia: ")

# 2. Format the keyword to match Wikipedia's URL style (capitalize first letter, swap spaces for underscores)
formatted_keyword = user_keyword.strip().title().replace(" ", "_")
url = f"https://en.wikipedia.org/wiki/{formatted_keyword}"

# 3. Add our friendly User-Agent header
headers = {
    "User-Agent": "MyInteractiveScraperBot/1.0 (contact: youremail@example.com)"
}

print(f"\nSearching for '{user_keyword}' at: {url}...\n")
response = requests.get(url, headers=headers)

# 4. Check if the page actually exists
if response.status_code == 404:
    print(f"❌ Error: The page '{user_keyword}' does not exist on Wikipedia.")
    print("Check your spelling or try a more specific topic.")
elif response.status_code != 200:
    print(f"❌ Failed to fetch page. Server returned status code: {response.status_code}")
else:
    # 5. Parse the page if everything is good
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract and print the official page title
    article_title = soup.find("h1", id="firstHeading").text
    print(f"✨ FOUND ARTICLE: {article_title} \n")
    
    # Extract paragraphs from the main body content
    body_content = soup.find("div", id="bodyContent")
    paragraphs = body_content.find_all("p")
    
    print("--- ARTICLE SUMMARY ---")
    count = 0
    for p in paragraphs:
        text = p.text.strip()
        
        if text:
            print(text)
            print()  # Add space between paragraphs
            count += 1
            
        if count >= 3:
            break
