import LinkedInScraper as ls

EMAIL=''
PASSWORD=''

scraper = ls.LinkedInScraper(EMAIL, PASSWORD)
scraper.login()
name, bio, address = scraper.scrape_profile('https://www.linkedin.com/in/syed-nabeel-sharafat-0b4738186/')
print('Name:',name)
print('Bio:',bio)
print('Address:',address)
scraper.close_browser()

 