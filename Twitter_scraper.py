import bs4 as bs
import urllib.request

def getLatestTweets(profile):
	tweetsNum = 1
	print(50 * "*")
	print("Profile name :",soup.title.text)
	print("Here are the 21 latest tweets")
	for tweets in profile.findAll("div", {"class" : "content"}):
		print("Tweet number :",tweetsNum)
		print(tweets.find("p").text)
		tweetsNum = tweetsNum + 1
	print(50 * "*")

def getTweetsbyword(profile,word):
	for tweets in profile.findAll("div", {"class" : "content"}):
		if(word in tweets.text):
			print(tweets.find("p").text)

source = urllib.request.urlopen("https://twitter.com/lichessorg").read()

soup = bs.BeautifulSoup(source,"html.parser")
#getLatestTweets(soup)
#getTweetsbyword(soup,"analysis")

