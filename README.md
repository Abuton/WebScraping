# WebScraping ETL

Arbitrary Publication Webscraping Project

## Link Extractor

### Design Explanation

I used Beautiful Soup Python library to scrape the url page given:

`http://community.dur.ac.uk/hubert.shum/comp42315/publicationfull_year_characteranimation.htm`.

I defined 3 python functions to achive this task.

- `get_page_info(url: str = page_url)`: to get the original page information. This function returns a beautifulSoup Object
- `get_publication_info(class_name: str = "w3-cell-row")`: This function get all publication in the current page. It accepts an argument class_name which depicts the div information to get. The function returns a list.
- `get_unique_url_links(class_name: str = "ImgIconPublicationDiv")`: This function get the url of each publication by extracting the text attached to the href attribute of the a tag in html. The text is prependded with the default url to make a complete link.

## Publication Details

### Design Explanation

The Process here was a simple for loop, I used a function defined earlier `get_page_info` to get information of each publication page.

Then I selected some text information as specified, this text are:
- title
- abstract
- publication
- bibtext
- endnotes
- plain
- citation

I implemented the for loop by defining lists to store each text information. The function I defined accepts one argument which is the result of the first task. Since this returns a list I looped that and select the field after inspecting the web page. I store all result into a dictionary which allows me to easily convert the that into a datafram using pandas Dataframe's `from_dict` method. I added a line `df.to_csv('file_name.csv', index=False)` to create a local file for the extracted information.
