#
# Just paste one of the below lines into scrapy shell to run benchmark
#

# commercial sale benchmark (results: 1560)
total_results = []; [(fetch('https://www.immobilienscout24.de/gewerbe-flaechen/de/' + city + '/buero-kaufen/'), total_results.append(response.css('span[class="spec-result-list-number-of-hits-caption"]::text').get())) for city in open('german_cities.csv').read().split('\n')[0:-1]]; print(sum([(int(result.split()[0].replace('.', '')) if result.split()[0][0].isdigit() else 0) for result in total_results if result is not None]))

# residential houses rent (results: 3422)
total_results = []; [(fetch('https://www.immobilienscout24.de/Suche/de/' + city + '/haus-mieten/'), total_results.append(response.css('span[data-is24-qa="resultlist-resultCount"]::text').get())) for city in open('german_cities.csv').read().split('\n')[0:-1]]; print(sum([(int(result.split()[0].replace('.', '')) if result.split()[0][0].isdigit() else 0) for result in total_results if result is not None]))

# residential houses sale (results: 66286)
total_results = []; [(fetch('https://www.immobilienscout24.de/Suche/de/' + city + '/haus-kaufen/'), total_results.append(response.css('span[data-is24-qa="resultlist-resultCount"]::text').get())) for city in open('german_cities.csv').read().split('\n')[0:-1]]; print(sum([(int(result.split()[0].replace('.', '')) if result.split()[0][0].isdigit() else 0) for result in total_results if result is not None]))

# residential rent (results: 75592)
total_results = []; [(fetch('https://www.immobilienscout24.de/Suche/de/' + city + '/wohnung-mieten/'), total_results.append(response.css('span[data-is24-qa="resultlist-resultCount"]::text').get())) for city in open('german_cities.csv').read().split('\n')[0:-1]]; print(sum([(int(result.split()[0].replace('.', '')) if result.split()[0][0].isdigit() else 0) for result in total_results if result is not None]))

# residential sale (results: 34595)
total_results = []; [(fetch('https://www.immobilienscout24.de/Suche/de/' + city + '/wohnung-kaufen/'), total_results.append(response.css('span[data-is24-qa="resultlist-resultCount"]::text').get())) for city in open('german_cities.csv').read().split('\n')[0:-1]]; print(sum([(int(result.split()[0].replace('.', '')) if result.split()[0][0].isdigit() else 0) for result in total_results if result is not None]))

