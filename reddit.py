import praw
import matplotlib.pyplot as plt

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent="",
)

words = []

for submission in reddit.subreddit("Eesti").hot(limit=10):
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
        word = ""
        for letter in top_level_comment.body:
            if letter == " ":
                if word and not word[-1].isalnum():
                    word = word[:-1]
                words.append(word.strip().lower())
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

for w in sortedList:
    keyCount.append(wordCount[w])

plt.title('Top comments for r/Eesti')
plt.pie(keyCount, labels=keyWords, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')

plt.save()

print(sortedList)