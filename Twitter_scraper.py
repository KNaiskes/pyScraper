import bs4 as bs
import urllib.request

source = urllib.request.urlopen("https://twitter.com/lichessorg").read()

soup = bs.BeautifulSoup(source,"html.parser")

print("Here are the 21 latest tweets from")
print(soup.title.text)
print(20 * "*")
tweetsNum = 1
for tweets in soup.findAll("div", {"class" : "content"}):
	print("Tweet number :",tweetsNum)
	print(tweets.find("p").text)
	tweetsNum = tweetsNum + 1

print(20 * "*")

