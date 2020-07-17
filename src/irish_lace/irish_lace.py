# Irish lasce patterns scraper by Code Monkey King (Just paste & run below line into Srapy Shell)
(fetch('https://www.liveinternet.ru/users/koko_shik/post350158665'), [(fetch(('http:' if 'http' not in image_url else '') + image_url), open(image_url.split('/')[-1], 'wb').write(response.body)) for image_url in response.css('img[src*=".jpg"]::attr(src)').getall()])
