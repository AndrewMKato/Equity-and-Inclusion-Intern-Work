import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

with open('Inclusive_Classrooms_for_web.txt', 'r', encoding='utf-8') as file:
    classrooms_text: str = file.read()

stop_words = list(STOPWORDS)
stop_words.append('UCR')
stop_words.append('Riverside')
print(stop_words)

word_cloud = WordCloud(
    background_color='white',
    stopwords=stop_words,
    height=500, # In pixels.
    width=500 # In pixels.
)

word_cloud.generate(classrooms_text)

word_cloud.to_file('inclusive_classrooms_UCR.png')