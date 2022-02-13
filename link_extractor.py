import bs4
import requests

url = "http://community.dur.ac.uk/hubert.shum/comp42315"
page_url = "http://community.dur.ac.uk/hubert.shum/comp42315/publicationfull_year_characteranimation.htm"


def get_page_info(url: str = page_url):
  response = requests.get(url)
  soup = bs4.BeautifulSoup(response.text, "html.parser")
  return soup


def get_publication_info(class_name: str = "w3-cell-row") -> list:
  soup = get_page_info()
  return soup.find_all(class_ = class_name)


def get_unique_url_links(class_name: str = "ImgIconPublicationDiv"):
  unique_url = []
  publications = get_publication_info()
  for link in range(len(publications)):
      unique_url.append(url + '/' + publications[link].find(class_= 'ImgIconPublicationDiv').find('a').get('href'))
  return unique_url


if __name__ == "__main__":  
  all_pub_links = get_unique_url_links()
