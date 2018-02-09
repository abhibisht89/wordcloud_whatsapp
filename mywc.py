import sys
from os import path
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS
from helper import preprocess

# get path to script's directory
currdir = path.dirname(__file__)

def create_wordcloud(name,text):
	# create numpy araay for wordcloud mask image
	mask = np.array(Image.open(path.join(currdir, "twi.png")))

	# create set of stopwords	
	stopwords = set(STOPWORDS)

	# create wordcloud object
	wc = WordCloud(background_color="white",
					max_words=1000, 
					mask=mask,
	               	stopwords=stopwords)
	
	# generate wordcloud
	wc.generate(text)

	# save wordcloud
	wc.to_file(path.join(currdir, name+".png"))

if __name__ == "__main__":
	filename="hcl.txt"
	data=preprocess(filename)
	# generate wordcloud
	create_wordcloud(path.splitext(filename)[0],data)
	print("Its done")