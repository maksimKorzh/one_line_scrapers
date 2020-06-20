###########################################
#
# Syntatically one line of code to scrape
#        UK Real Estate properties
#           from rightmove.co.uk
#
#                    by
#
#             Code Monkey King
#
###########################################
###########################################
#
#           How to run this code
#
###########################################
#
# 1. Invoke SCRAPY Shell in the directory
#    containing THIS file
#
# 2. Then copy and paste the following:
#    exec(open('rightmove.py', 'r').read())
#
#    You should've obtain CSV file
#
###########################################
###########################################
#
#   How to wrap this code into one line
#
###########################################
#
# 1. Invoke either SCRAPY or PYTHON Shell
#
# 2. Then copy and paste the following:
#    print(' '.join([''.join(line.strip()) for line in open('rightmove.py', 'r').read().split('\n') if '#' not in line]))
#  
#    You should obtain this like line
#    import csv; [ [ fetch('https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E87490&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false&index=' + str(page * 24)),  [ csv.DictWriter( open('rightmove.csv', 'a'), ['title', 'url', 'address', 'price', 'description', 'date']).writerow( { 'title': card.css('h2[class="propertyCard-title"]::text') .get() .strip(),  'url': card.css('a[class="propertyCard-link"]::attr(href)') .get(),  'address': card.css('address[class="propertyCard-address"] *::text') .getall()[-2],  'price': card.css('div[class="propertyCard-priceValue"]::text') .get() .strip(),  'description': card.css('span[itemprop="description"] *::text') .get(),  'date': ' '.join(list(filter(None, [ text.strip() for text in card.css('div[class="propertyCard-branchSummary"] *::text') .getall()])))  }  )  for card in response.css('div[class="propertyCard-wrapper"]')] ][-1]  for page in range(0, 4) ]
#
###########################################

import csv; [
    [
        # loop over the range of pages and crawl pagination
        fetch('https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E87490&insId=1&radius=0.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false&index=' + str(page * 24)),

        # data extraction
        [
            # append item/row to table
            csv.DictWriter(
                open('rightmove.csv', 'a'),
                ['title', 'url', 'address', 'price', 'description', 'date']).writerow(
                    {
                        'title': card.css('h2[class="propertyCard-title"]::text')
                                     .get()
                                     .strip(),
                                     
                        'url': card.css('a[class="propertyCard-link"]::attr(href)')
                                   .get(),
                        
                        'address': card.css('address[class="propertyCard-address"] *::text')
                                       .getall()[-2],
                        
                        'price': card.css('div[class="propertyCard-priceValue"]::text')
                                     .get()
                                     .strip(),
                        
                        'description': card.css('span[itemprop="description"] *::text')
                                           .get(),
                        
                        'date': ' '.join(list(filter(None, [
                                    text.strip()
                                    for text in
                                    card.css('div[class="propertyCard-branchSummary"] *::text')
                                    .getall()])))
                
                    }

                )
                
                # loop over property cards
                for card in response.css('div[class="propertyCard-wrapper"]')]
        ][-1]
        
    # loop over the range of pages    
    for page in range(0, 4)
]















                    
