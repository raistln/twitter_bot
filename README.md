# Murphy's bot
Sure you wake up early and what´s is what you need?? Correct you need an insult from the most evil genius from TV....Yes it´s Stewie Griffin: [Samu](https://twitter.com/stewieisangry)<br>
*People think I go out of my way to piss them off, Trust me, it´s not out of my way at all* :)
## What it is?
This is a twitter bot that tweets daily one insult with the image of Stewie Griffin, and he is very angry. It is automated with **Python** in **AWS**. 

I based this project, twitching and modifying it here and there, on [@_dylancastillo](https://twitter.com/_dylancastillo)'s bot, who wrote an excellent [template](https://github.com/dylanjcastillo/twitter-bot-python-aws-lambda) and a great [tutorial](https://dylancastillo.co/how-to-make-a-twitter-bot-for-free/) accompanying it. **All credit goes to him.**

## How it works?

+ First, there is a very basic web scrapping from a [import_quotes.py]("https://parade.com/1079501/stephanieosmanski/sarcastic-quotes/") containing the desired messages to post. Then, after a simple preprocessing using regex, I created a file containing all the potential tweets. 

+ The main functions that retrieve the tweets and post them using the Twitter API are in [stewie_bot.py]().





+ The [createlambdalayer.sh](https://github.com/DavidCarricondo/murphys_bot/blob/main/createlambdalayer.sh) creates a lambda layer with the libraries in requirements.txt and using a **Docker image**. This is the layer that will be uploaded to AWS.

+ The [buildpackage.sh](https://github.com/DavidCarricondo/murphys_bot/blob/main/buildpackage.sh) only wraps the function in a zip file to upload it as a lambda function. 

+ The lambda function is scheduled using **EventBridge**

