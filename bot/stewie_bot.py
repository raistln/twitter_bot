from config import create_api
import csv
from random import choice
from PIL import Image, ImageFont, ImageDraw 
import time
import tweepy
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()



def create_lst_quotes():
    logger.info("open this csv shit")
    with open('stewie_angry.csv', newline='') as quote:
        reader = csv.reader(quote)
        angry = list(reader)
        return angry

def stewies_angry(api):
    logger.info("Steview don´t like you")
    my_image = Image.open("stewie griffin.jpg")
    title_font = ImageFont.truetype('Roboto-Bold.ttf', 22)
    logger.info("Preparing to insult you")
    insults = create_lst_quotes()
    choosed = choice(insults)
    insults.remove(choosed)
    quote = re.split(r"\.|\,", choosed[0], 1)
    if len(quote) == 2:
        title_text1 = quote[0] + ","
        title_text2 = quote[1]
    else:
        splitted = quote[0].split(" ")
        title_text1 = " ".join(splitted[:len(splitted)//2])
        title_text2 = " ".join(splitted[len(splitted)//2:])
    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((25,20), text=title_text1, fill=(40, 46, 46), font=title_font)
    image_editable.text((65,60), text=title_text2, fill=(40, 46, 46), font=title_font)
    logger.info("Ready to insult you")
    my_image.save("result.jpg")
    api.update_with_media("result.jpg")
    

def main():
    api = create_api()
    while True:
        stewies_angry(api)
        logger.info("Waiting...")
        time.sleep(43200)
    create_lst_quotes()
    main()

if __name__ == "__main__":
    main()
