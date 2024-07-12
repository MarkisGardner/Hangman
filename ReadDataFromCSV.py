import pandas as pd

def load_data():
    columns = ['Common Name', 'Species Group','Federal Listing Status']
    df = pd.read_csv('ListedAnimals.csv', usecols=columns)
    animals = df.values.tolist()
    return animals

