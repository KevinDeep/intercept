from googlesearch import search
from bs4 import BeautifulSoup
import requests
from termcolor import colored
from urllib.parse import urlparse
print()
print("_____ __   _ _______ _______  ______ _______ _______  _____  _______")
print("   |   | \  |    |    |______ |_____/ |       |______ |_____]    |")
print(" __|__ |  \_|    |    |______ |    \_ |_____  |______ |          | ")
print("               𝐓𝐨𝐨𝐥𝐬 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐁𝐲 𝐊𝐞𝐯𝐢𝐧 𝐃𝐞𝐞𝐩 (𝐀𝐫𝐜𝐡𝐚𝐧𝐠𝐞𝐥 𝐖𝐡𝐢𝐭𝐞)")
                                                                     
print()
def get_social_media_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()
    if "facebook" in domain:
        return "Facebook"
    elif "twitter" in domain:
        return "Twitter"
    elif "instagram" in domain:
        return "Instagram"
    elif "linkedin" in domain:
        return "LinkedIn"
    elif "pinterest" in domain:
        return "Pinterest"
    elif "tiktok" in domain:
        return "TikTok"
    elif "youtube" in domain:
        return "YouTube"
    elif "snapchat" in domain:
        return "Snapchat"
    elif "reddit" in domain:
        return "Reddit"
    else:
        return domain

def decorate_result(title, url, color):
    print("_" * 50)
    print(colored("Title:", color), colored(title, color))
    print()
    print(colored("URL:", color), colored(url, color))
    print()
    print(colored("Found By:", color), colored(get_social_media_name(url), color))
    print("_" * 50)
    print()

def search_google(query):
    try:
        print("Search result on Google:")
        results = search(query, num_results=5)
        for i, url in enumerate(results, 1):
            print(f"Result Found {i}:")
            decorate_result("Google Search", url, "blue")
        print("=" * 50)
        print()
    except Exception as e:
        print("Error searching Google:", str(e))
        print("Continue to the next search.")
        print()

def search_bing(query):
    try:
        print("Search result on Bing:")
        url = f"https://www.bing.com/search?q={query}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = soup.select("li.b_algo h2 a")
        for i, result in enumerate(search_results, 1):
            print(f"Result Found {i}:")
            title = result.text
            url = result["href"]
            decorate_result(title, url, "white")
        print("=" * 50)
        print()
    except Exception as e:
        print("Error searching Bing:", str(e))
        print("Continue to the next search.")
        print()

def search_web(query):
    try:
        print("Search result on Web:")
        results = search(query, num_results=5)
        for i, url in enumerate(results, 1):
            print(f"Result Found {i}:")
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string if soup.title else "Titolo non disponibile"
            decorate_result(title, url, "green")
        print("=" * 50)
        print()
    except Exception as e:
        print("Error searching Web:", str(e))
        print("Continue to the next search.")
        print()

def search_news(query):
    try:
        print("Search result on News:")
        results = search(query, num_results=5)
        for i, url in enumerate(results, 1):
            print(f"Result Found {i}:")
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.title.string if soup.title else "Titolo non disponibile"
            decorate_result(title, url, "magenta")
        print("=" * 50)
        print()
    except Exception as e:
        print("Error searching News:", str(e))
        print("Continue to the next search.")
        print()

def search_images(query):
    try:
        print("Search result on Images:")
        results = search(query, num_results=5)
        for i, url in enumerate(results, 1):
            print(f"Result Found {i}:")
            decorate_result("Image Search", url, "cyan")
        print("=" * 50)
        print()
    except Exception as e:
        print("Error searching Images:", str(e))
        print("Continue to the next search.")
        print()

def main():
    query = input("What do you want to search: ")
    print()

    search_google(query)
    search_bing(query)
    search_web(query)
    search_news(query)
    search_images(query)

if __name__ == "__main__":
    main()
