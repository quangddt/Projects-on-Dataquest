from read import load_data
from dateutil.parser import parse

df = load_data()
times = df['submission_time']

def extract_hour(obj):
    datetime = parse(obj)
    return datetime.time().hour

df['submission_hour'] = df['submission_time'].apply(extract_hour)

if __name__ == "__main__":
    print(df['submission_hour'].value_counts())
    