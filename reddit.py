import os
from dotenv import load_dotenv
import praw
import matplotlib.pyplot as plt

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT'),
)

words = []

commonWords = ['on', 'ja', 'et', 'ei', 'see', 'kui', 'ka', 'aga', 'siis', '', 'seda', 'oma', 'oli', 'mis', 'sa', 'saab', 'ta', 'või', 'palju', 'ole', 'ning', 'kas', 'need', 'selle', 'kes', 'ise', 'pole','mida', 'nagu', 'väga', 'ma', 'ikka', 'nüüd''ära', 'olla', 'kuidas', 'oleks',]

for submission in reddit.subreddit("Eesti").hot(limit=5):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        word = ""
        for letter in top_level_comment.body:
            if letter == " ":
                if word and not word[-1].isalnum():
                    word = word[:-1]
                word = word.strip().lower()
                if word not in commonWords:
                    words.append(word)
                word = ""
            else:
                word += letter

wordCount = {}

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1


sortedList = sorted(wordCount, key = wordCount.get, reverse = True)

keyWords = sortedList[:10]
keyCount = []

for w in keyWords:
    keyCount.append(wordCount[w])

print(keyWords, keyCount)

plt.title('Top comments for r/Eesti')
plt.pie(keyCount, labels=keyWords, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')

plt.savefig('eesti.png')
# plt.show()
