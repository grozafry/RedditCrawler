import praw

reddit = praw.Reddit(user_agent='Comment Extraction (by /u/GrozaFry)',
                     client_id='9OpOMsOVNKyDDQ', client_secret="_vl27e93SNrQSGLJ0vb5-_HwZjg")

submission = reddit.submission(url='https://www.reddit.com/r/explainlikeimfive/comments/jgtxi/eli5_why_is_the_sky_blue_no_seriously_like_im/')

print("Question: ")
print(submission.title)
print(submission.selftext)
print("............................................................................")

count=0
for top_level_comment in submission.comments:
    count+=1
    print("Ans",count,": ")
    print(top_level_comment.body)
    print("............................................................................")
    if count>10:break

