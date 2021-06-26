from selenium.webdriver import Chrome
from instascrape import Profile, scrape_posts
import requests 

scraped_post = []
data_scraped = []
# Creating our webdriver
webdriver = Chrome()
file_data = open("data.txt", "w")
# Scraping Joe Biden's profile
session: requests.Session = None
SESSIONID = '25329686837:wv6If3GCw4HPE0:16'
headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
           "cookie": f"sessionid={SESSIONID};"}
joe = Profile("dkksemarang")
joe.scrape(headers=headers)

# Scraping the posts
posts = joe.get_posts(webdriver=webdriver,login_pause=15, login_first=True)
# scraped, unscraped = scrape_posts(posts, silent=False, headers=headers, pause=10)
# print(type(scraped), scraped)
# for i, post in enumerate(scraped):
#     post.shortcode
    # scraped_post.append(post)
#     post.scrape(session=session, webdriver=webdriver, headers=headers)
#     scraped_post.append(post)
    # data_scraped.append(f"https://www.instagram.com/p/{post.shortcode}, {post.upload_date} \n")
    # file_data.write(f"https://www.instagram.com/p/{post.shortcode} \n")
    # file_data.close()
for i, post in enumerate(posts):
    data_scraped.append(f"https://www.instagram.com/p/{post.source} \n")
    print(post.source)

    # print(scraped_post)
# print(scraped_post[2].shortcode)
file_data.writelines(data_scraped)
file_data.close()
# print((scraped[0].scrape(session=session, webdriver=webdriver, headers=headers)))
# url = f"https://www.instagram.com/p/{posts[0].shortcode}"
# print(url)
# print(type(posts))
# print(posts[0].source)