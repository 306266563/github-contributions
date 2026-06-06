import requests

def get_trending_repos(language='python'):
    """
    Fetch trending repositories from GitHub.
    This can be used as a source for Manus to perform deep analysis.
    """
    url = f"https://api.github.com/search/repositories?q=language:{language}&sort=stars&order=desc"
    try:
        response = requests.get(url)
        data = response.json()
        repos = data.get('items', [])[:5]
        print(f"Top 5 Trending {language.capitalize()} Repositories:")
        for repo in repos:
            print(f"- {repo['full_name']} ({repo['stargazers_count']} stars): {repo['description']}")
    except Exception as e:
        print(f"Error fetching trends: {e}")

if __name__ == "__main__":
    get_trending_repos('python')
    print("\nTrend Analyzer Ready. Use this data to feed into Manus for deeper insights.")

# Added timeout handling for API requests.