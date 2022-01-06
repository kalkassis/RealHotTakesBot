import tweepy
import random
import time
from datetime import datetime

ConsumerKey = INSERT HERE
ConsumerSecret = INSERT HERE

AccessKey = INSERT HERE
AccessSecret = INSERT HERE
BearerToken = INSERT HERE

# create an instance of the twitter client and passing it the keys required to authenticate.
client = tweepy.Client(consumer_key=ConsumerKey, consumer_secret=ConsumerSecret,
                       access_token=AccessKey, access_token_secret=AccessSecret, bearer_token=BearerToken)

authentication = tweepy.OAuthHandler(ConsumerKey, ConsumerSecret)
api = tweepy.API(authentication)
# the same tweet cannot be made twice!

# client.create_tweet(text="Bob!")

SentenceStarters = ["Man I swear, ", "Honestly, ", "Bro, ", "Tbh, ", "Don't hate but, ", "Man, ", "You know what, ",
                    "Real talk, "]
# NO SPACES IN THIS LIST
PlayerList = ["Norman Powell", "Danilo Gallinari", "Steven Adams", "Will Barton", "Jalen Green",
              "Kevin Huerter", "Jonas Valanciunas", "Mitchell Robinson", "Duncan Robinson", "Derrick Rose",
              "Jordan Clarkson", "Robert Covington", "Seth Curry", "Miles Bridges", "Devonte' Graham",
              "John Wall", "Darius Garland", "Dejounte Murray", "Lauri Markkanen", "Terry Rozier", "Caris LeVert",
              "Tim Hardaway Jr", "Dillon Brooks", "Andrew Wiggins", "Cade Cunningham", "Joe Harris", "Jusuf Nurkic",
              "Tyrese Haliburton", "OG Anunoby", "Jaren Jackson Jr", "Kemba Walker", "Aaron Gordon",
              "Spencer Dinwiddie",
              "Bojan Bogdanovic", "Mikal Bridges", "Malcolm Brogdon", "Bogdan Bogdanovic", "D'Angelo Russell",
              "Joe Ingles", "Jarrett Allen", "Christian Wood", "Collin Sexton", "Gordon Hayward", "Lonzo Ball",
              "Fred VanVleet", "Clint Capela", "John Collins", "Jerami Grant", "Anthony Edwards", "Buddy Hield",
              "Kristaps Porzingis", "Marcus Smart", "Mike Conley", "LaMelo Ball", "Tobias Harris", "DeMar DeRozan",
              "Myles Turner", "Kyle Lowry", "Julius Randle", "Michael Porter Jr.", "Domantas Sabonis", "Nikola Vucevic",
              "Pascal Siakam", "Draymond Green", "Shai Gilgeous-Alexander", "Deandre Ayton", "De'Aaron Fox",
              "Zach LaVine", "Klay Thompson", "Ja Morant", "CJ McCollum", "Russell Westbrook", "Ben Simmons",
              "Jaylen Brown", "Brandon Ingram", "Rudy Gobert", "Karl-Anthony Towns", "Zion Williamson",
              "Jrue Holiday", "Bam Adebayo", "Kyrie Irving", "Khris Middleton", "Donovan Mitchell",
              "Trae Young", "Jimmy Butler", "Devin Booker", "Jayson Tatum", "Chris Paul", "Paul George",
              "Bradley Beal", "James Harden", "Anthony Davis", "Damian Lillard",
              "Joel Embiid", "Nikola Jokic", "Stephen Curry", "Luka Dončić", "LeBron James",
              "Giannis Antetokounmpo", "Kevin Durant"]

TeamList = ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls", "Cleveland Cavaliers",
            "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors", "Houston Rockets", "Indiana Pacers",
            "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies", "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves",
            "New Orleans Pelicans", "New York Knicks", "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns",
            "Portland Trail Blazers", "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"]
# NO SPACES IN THIS LIST
PlayerPositions = ["Point Guard", "Shooting Guard", "Small Forward", "Power Forward", "Center"]

DescriptorsList = [" BEST ", " WORST ", " FUNNIEST ", " WEIRDEST ", " SMARTEST ", " LUCKIEST ", " CLUTCHEST ",
                   " LOYALIST "]

FinishersList = ["its over lol, skip to next season. ", "instant dub don't @ me ",
                 "its lit ", "I'll stop watching ball "]
HashtagList = ["#nba", "#basketball", "#hottake", "#baller", "#realtalk", "#facts", "#nolie",
               "#buckets", "#baller"]

ReplyList = ["BIG facts!", "Best believe", "this is wild", "idk what to think", "insane", "thats an L"]

random.seed(datetime.now())
for _ in iter(int, 1):
    TweetChooser = random.randint(1, 6)

    if TweetChooser == 1:  # in the case that Tweet Chooser is 1, we generate the following tweet
        SelectedIntro = random.choice(SentenceStarters)  # choose intro, choice allows for duplicates
        SelectedPlayer = random.choice(PlayerList)  # Choose one item from PlayerList
        SelectedPosition = random.choice(PlayerPositions)
        SelectedDescriptor = random.choice(DescriptorsList)
        SelectedTag = random.choice(HashtagList)
        FinalTweet = str(SelectedIntro) + str(SelectedPlayer) + " is the" + str(SelectedDescriptor) + str(SelectedPosition) + " in the league. " + str(SelectedTag)
        print(FinalTweet)
        client.create_tweet(text=FinalTweet)
        time.sleep(1800)  # sleep for the specified amount of seconds, so we don't spam Twitter
        continue  # break out of this iteration and continue to the next
    elif TweetChooser == 2:
        SelectedIntro = random.choice(SentenceStarters)  # choose intro, choice allows for duplicates
        SelectedPlayer = random.sample(PlayerList, 2)  # Choose one item from PlayerList, sample does not duplicate
        SelectedFinisher = random.choice(FinishersList)
        SelectedTag = random.choice(HashtagList)
        FinalTweet = str(SelectedIntro) + "if " + str(SelectedPlayer[0]) + " and " + str(SelectedPlayer[1]) + " team up, " + str(SelectedFinisher) + str(SelectedTag)
        print(FinalTweet)
        client.create_tweet(text=FinalTweet)
        time.sleep(1800)  # sleep for the specified amount of seconds, so we don't spam Twitter
        continue  # break out of this iteration and continue to the next
    elif TweetChooser == 3:
        SelectedPlayer = random.choice(PlayerList)
        SelectedTeam = random.choice(TeamList)
        SelectedTag = random.choice(HashtagList)
        FinalTweet = str(SelectedPlayer) + " needs to join the " + str(SelectedTeam) + ", free my boy " + str(SelectedTag)
        print(FinalTweet)
        client.create_tweet(text=FinalTweet)
        time.sleep(1800)  # sleep for the specified amount of seconds, so we don't spam Twitter
        continue  # break out of this iteration and continue to the next
    elif TweetChooser == 4:
        SelectedPlayer = random.choice(PlayerList)
        SelectedTeam = random.choice(TeamList)
        SelectedTag = random.choice(HashtagList)
        FinalTweet = str(SelectedTeam) + " needs to get rid of " + str(SelectedPlayer) + " , dudes a bum " + str(SelectedTag)
        print(FinalTweet)
        client.create_tweet(text=FinalTweet)
        time.sleep(1800)  # sleep for the specified amount of seconds, so we don't spam Twitter
        continue  # break out of this iteration and continue to the next
    elif TweetChooser == 5:
        SelectedPlayer = random.choice(PlayerList)
        SelectedTag = random.choice(HashtagList)
        FinalTweet = str(SelectedPlayer) + " I see you bro!! " + str(SelectedTag)
        print(FinalTweet)
        client.create_tweet(text=FinalTweet)
        time.sleep(1800)  # sleep for the specified amount of seconds, so we don't spam Twitter
        continue  # break out of this iteration and continue to the next
    elif TweetChooser == 6:
        toRetweet = tweepy.Cursor(api.search_tweets, q='#NBA').items(1)  # grab one tweet that includes #NBA
        for retweet in toRetweet:
            client.retweet(retweet.id)  # retweet the tweet
        time.sleep(1800)
        continue

