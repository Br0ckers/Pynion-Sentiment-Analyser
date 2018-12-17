import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def sentiWordCloud(tweetarray,subject):

    text = ' '.join(tweetarray)
    print("array to plot {}".format(text))
    # Create and generate a word cloud image:
    #wordcloud = WordCloud().generate("happy happy sad sugar flowers angels good trump")
    #wordcloud = WordCloud().generate(text)

    # Display the generated image:
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
    print("got the word cloud")
    #wordcloud.to_file("app/img/word_cloud_{}.png".format(subject))
    wordcloud.to_file("app/static/word_cloud.png")
    print("saving the file")
