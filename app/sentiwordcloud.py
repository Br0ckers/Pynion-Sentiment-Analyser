import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def sentiWordCloud(tweetarray,subject):
    text = ' '.join(tweetarray)
    text = text.strip()
    if (text == None or text == ""):
        text = "NOTHING NIENTE NICHTS NIETS REIN NADA NIC NIMIC {}".format(subject)
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
    if (subject == "apphistory"):
        wordcloud.to_file("app/static/historical_word_cloud.png")
    else:
        wordcloud.to_file("app/static/word_cloud.png")
