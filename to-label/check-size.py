import pandas as pd

users = ['christina', 'flo', 'jules', 'lucien']

for user in users:
    data = pd.read_csv(f"./to-label-{user}.csv", header=None, names=["asin", "title", "description", "healthy", "vegetarian/vegan", "sport/productivity", "country"])
    print(f"{user}: {len(data.index)}")
