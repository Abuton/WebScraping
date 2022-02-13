import pandas as pd


def publication_details(links: list = all_pub_links):
  pub_details = {}
  title, abstract, publications, bibtext, endnotes, plain, citation = [],[],[],[],[],[],[]
  
  for link in links:
      soup = get_page_info(link)
      title.append(soup.find('h1').text)
      abstract.append(soup.find('p').text)
      citation.append(soup.find('span', class_='TextHighlightDefault').text)
      publications.append(soup.find_all('p')[1].text)
      bibtext.append(soup.find_all('p', class_='TextSmallDefault')[0].text)
      endnotes.append(soup.find_all('p', class_='TextSmallDefault')[1].text)
      plain.append(soup.find_all('p', class_='TextSmallDefault')[2].text)

  pub_details['title'] = title
  pub_details['abstract'] = abstract
  pub_details['publication'] = publications
  pub_details['bibtext'] = bibtext
  pub_details['endnotes'] = endnotes
  pub_details['plain'] = plain
  pub_details['citation'] = citation
#     pub_details['citation'] = [x.split('Citation:')[1] for x in pub_details['citation']]
  df = pd.DataFrame.from_dict(pub_details)
  df.to_csv('file_name.csv', index=False)
  return df

if __name__ == "__main__":
  df = publication_details()
