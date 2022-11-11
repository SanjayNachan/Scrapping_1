import advertools as adv
import pandas as pd

cx = 'coder'
key = '603815510de1545b6'
adv.__version__

wikipedia_urls = ['https://https://www.pararius.com/apartments/amsterdam',  # search for this domain as a keyword
                  'https:https://www.pararius.com/apartments/amsterdam/wrong_page',  # search for this domain as a keyword (does not exist)
                  'site:https://www.pararius.com/apartments/amsterdam', # search for this site/page (exists)
                  'site:https://www.pararius.com/apartments/amsterdam/wrong_again'] # search for this site/page (does not exist)
wikipedia = adv.serp_goog(cx=cx, key=key, q=wikipedia_urls)
wikipedia = pd.read_csv('housing.csv')
print(wikipedia)


