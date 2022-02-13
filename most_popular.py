import nltk
import pandas as pd
nltk.download('english')


# a word is the combination of 5 or more character 
def get_100_most_common_words(df: pd.DataFrame) -> list:
  en_stops = set(stopwords.words('english'))
  title_abstract = list(df['title'] + " " + df['abstract'])
  w = [word for i in title_abstract for word in i.split() if len(word) >= 5 and word not in en_stops]
  title_abstract_count = Counter(w)
  return title_abstract_count.most_common(100)


if __name__ == "__main__":
  most_common_title_abstract_word = get_100_most_common_words(df)
