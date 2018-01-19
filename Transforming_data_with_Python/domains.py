from read import load_data
import re

df = load_data()

domains = df['url'].dropna()

def remove_subdomain(domain):
    match = re.search(r"\w+\.\w+$", domain)
    if match is not None:
        if match.group() == 'co.uk':
            match = re.search(r"\w+\.\w+\.\w+$", domain)
            return match.group()
        else:
            return match.group()

domains = domains.apply(remove_subdomain)

if __name__ == "__main__":
    print(domains.value_counts().head(100))  