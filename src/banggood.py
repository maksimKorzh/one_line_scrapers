# reverse engineer AJAX call to scrape recommended products from banggood.com
import json; [(fetch('https://www.banggood.com/load/index/loadRecommendProduct.html?page=' + str(page)), [open('banggood.jsonl', 'a').write(json.dumps(item, indent=2) + '\n') for item in json.loads(response.text)['data']['list']])[-1] for page in range(0, 4)]
