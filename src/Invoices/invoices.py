# Invoices' images downloader (https://invoicehome.com/templates/invoice)
(fetch('https://invoicehome.com/templates/invoice'), [(fetch(url), open(url.split('/')[-1], 'wb').write(response.body)) for url in response.css('img[class="shadow-all-around responsive"]::attr(src)').getall()])
