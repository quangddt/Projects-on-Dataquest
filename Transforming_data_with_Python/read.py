import pandas as pd
df = pd.read_csv("hn_stories.csv")
df.columns = ['submission_time', 'upvotes', 'url', 'headline']

def load_data():
    return df

if __name__ == "__main__":
    data = load_data()
    print(data.head(1))