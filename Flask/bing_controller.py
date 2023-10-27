import requests
import openai
import __main__

def requires_web_search(user_question: str) -> bool:
    prompt = (f"Given the user's question of an other conversation with ChatGPT: \"{user_question}\", "
              f"does it suggest an explicit need for real-time or up-to-date information from a web search? If you have doubt, say No. "
              f"If the question should be answered by a previous message, say No."
              f"Please answer with \"Yes\" or \"No\".")

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",  
        prompt=prompt,
        max_tokens=10
    )

    answer = response.choices[0].text.strip().lower()

    if "yes" in answer or "y" in answer:
        return True

    if "no" in answer or "n" in answer:
        return False
    raise ValueError(f"Unexpected response from model: {answer}")



def get_bing_search_results(query, mkt="fr-FR", count=3):
    bing_subscription_key = __main__.bing_subscription_key
    params = {"q": query, "mkt": mkt, "count": count}
    headers = {"Ocp-Apim-Subscription-Key": bing_subscription_key}
    try:
        response = requests.get(
            "https://api.bing.microsoft.com/v7.0/search", headers=headers, params=params
        )
        response.raise_for_status()
        results = response.json()

        names, URLs, snippets = [], [], []

        if "webPages" in results and "value" in results["webPages"]:
            for item in results["webPages"]["value"]:
                names.append(item["name"])
                URLs.append(item["url"])
                snippets.append(item["snippet"])

        return names, URLs, snippets

    except Exception as ex:
        print(f"An error occurred: {str(ex)}")
        return None, None, None
    

