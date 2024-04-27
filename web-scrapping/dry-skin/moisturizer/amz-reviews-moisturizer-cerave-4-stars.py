import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

reviewlist = []

def get_soup(url):
    r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 2})
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup


def get_reviews(soup):
    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            try:
                # Convert date str to dd/mm/yyy format
                datetime_str = item.select_one('[data-hook="review-date"]').text.strip().split(' on ')[-1]
                date = datetime.strptime(datetime_str, '%B %d, %Y').strftime("%d/%m/%Y")
            except Exception as e:
                date = 'N/A'

            # Extract the helpful vote count
            try:
                helpful_count = int(item.find('span', {'data-hook': 'helpful-vote-statement'}).text.strip().split()[0])
            except (AttributeError, ValueError, IndexError):
                helpful_count = 0

            review = {
            'product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip(),
            'date': date,
            'title': item.find('a', {'data-hook': 'review-title'}).text.strip(),
            'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()),
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            'helpful_count': helpful_count, 
            }
            reviewlist.append(review)
    except:
        pass

for x in range(1,11):
    soup = get_soup(f'https://www.amazon.com/CeraVe-Moisturizing-Lotion-Hyaluronic-Fragrance/product-reviews/B07RK4HST7/ref=cm_cr_getr_d_paging_btm_next_{x}?ie=UTF8&reviewerType=all_reviews&filterByStar=four_star&pageNumber={x}')
    print(f'Getting page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df.to_csv('moisturizer-dry-skin-cerave-4-stars.csv', index=False)
print('Finish.')