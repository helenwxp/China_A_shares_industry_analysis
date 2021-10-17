# %%
import jieba
from os import path
from imageio import imread
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, ImageColorGenerator
# jieba.enable_paddle()
import pandas as pd
from zhon.hanzi import punctuation
from tqdm import tqdm

# %% designate working directory
d = os.getcwd()
font_path = d+'\\word_cloud-master\\examples\\fonts\\SourceHanSerif\\SourceHanSerifK-Light.otf'

stopwords_path = d+'\\stopwords-master\\cn_stopwords.txt'
with open(stopwords_path, encoding='utf-8') as f_stop:
    f_stop_text = f_stop.read()
    f_stop_seg_list = f_stop_text.splitlines()

# %%
inds = ['能源材料', '石油', '电力', '钢铁冶金', '机械设备', '化学工业', '交通运输', \
        '汽车工业', '房产建筑', '建材', '轻工纺织', '服装业', '农林牧渔', '公共服务', \
        'IT', '电信', '家电', '电子电器', '文化', '文体教育', '传媒行业', '医药', \
        '食品饮料', '烟酒', '零售业', '日用化品', '酒店餐饮', '家庭服务']

for ind_str in tqdm(inds):
    # load policy texts
    policydf = pd.read_excel('industry_policies_with_texts.xlsx', sheet_name=ind_str)
    contents = list(policydf.contents.dropna().values)
    txt = ''.join(contents)

    # word segmentation 
    wordlist = []
    for word in jieba.lcut(txt):
        if not (word in punctuation) and not(word in f_stop_seg_list):
            wordlist.append(word)

    # generate wordcloud
    back_coloring = imread(path.join(d, d + '\\imgs\\background\\'+ind_str+'.jpg'))
    wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=back_coloring,
                max_font_size=100, random_state=42, width=1000, height=860, margin=2,)


    wc.generate(' '.join(wordlist))

    # wordcloud visualization
    wcimgpath = d+'\\imgs\\wc\\'+ind_str+'.jpg'

    # create coloring from image
    image_colors_byImg = ImageColorGenerator(back_coloring)

    # show
    # we could also give color_func=image_colors directly in the constructor
    plt.imshow(wc.recolor(color_func=image_colors_byImg), interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.imshow(back_coloring, interpolation="bilinear")
    plt.axis("off")
    # plt.show()

    wc.to_file(path.join(d, wcimgpath))
