import argparse
import bs4 as bs
import urllib.request

def getLatestTweets():
	print("Enter profiles url :")
	url = str(input())
	source = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(source,"html.parser")
	tweetsNum = 1
	print(50 * "*")
	print("Profile name :",soup.title.text)
	print("Here are the 21 latest tweets")
	for tweets in soup.findAll("div", {"class" : "content"}):
		print("Tweet number :",tweetsNum)
		print(tweets.find("p").text)
		tweetsNum = tweetsNum + 1
	print(50 * "*")

def getTweetsbyword():
	print("Enter profiles url :")
	url = str(input())
	source = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(source,"html.parser")
	print("Enter the word you are looking for : ")
	word = str(input())
	for tweets in soup.findAll("div", {"class" : "content"}):
		if(word in tweets.text):
			print(tweets.find("p").text)


parser = argparse.ArgumentParser()
parser.add_argument("-all",action="store_true")
parser.add_argument("-sw",action="store_true")
args = parser.parse_args()


if args.all:
	getLatestTweets()
elif args.sw:
	getTweetsbyword()

