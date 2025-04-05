import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

value1 = [18817, 17032, 10277, 5589, 4113, 4894]
value2 =[3312, 2782, 1104, 632, 690, 249]
label = ['New Zealand', 'Scotland', 'England', 'Ireland', 'Australia', 'Other']

fig = plt.figure(figsize=(20, 15))

color = ['0.2', '0.35', '0.5', '0.7', '0.8', '0.9']

# autopctのカスタム関数
def custom_autopct(pct):
    return f'{pct:.1f}%'  # テキストの形式を指定

ax1 = fig.add_subplot(121)
wedges1, texts1, autotexts1 = ax1.pie(x=value1, 
                                   labels=label, 
                                   autopct=custom_autopct, 
                                   startangle=90, 
                                   counterclock=False, 
                                   colors=color,
                                   textprops={'fontsize': 12, 'fontweight': 'bold', 'family': 'Times new roman'}
                                   )
ax1.set_title('Otago',
              fontsize=15,
              fontweight='bold',
              fontfamily='Times new roman' )

for i, autotext1 in enumerate(autotexts1):
    if label[i] in ['New Zealand', 'Scotland']:
        autotext1.set_color('white')
    else: autotext1.set_color('black')

for i, text1 in enumerate(texts1):
    if label[i] not in ['New Zealand', 'Scotland']:
        text1.set_color('gray')

ax2 = fig.add_subplot(122)
wedges2, texts2, autotexts2 = ax2.pie(x=value2, 
                                   labels=label, 
                                   autopct=custom_autopct, 
                                   startangle=90, 
                                   counterclock=False, 
                                   colors=color,
                                   textprops={'fontsize': 12, 'fontweight': 'bold', 'family': 'Times new roman'}
                                   )
ax2.set_title('Southland',
              fontsize=15,
              fontweight='bold',
              fontfamily='Times new roman')

#enumerate関数 リスト要素とそのインデックスを取得
for i, autotext2 in enumerate(autotexts2):
    if label[i] in ['New Zealand', 'Scotland']: #もしlabelのi番目の値が['New Zealand', 'Scotland']に含まれるなら
        autotext2.set_color('white')
    else: 
        autotext2.set_color('black')
        x, y = autotext2.get_position()  # 現在の位置を取得
        autotext2.set_position((x * 1.2, y * 1.2))  # 少し外側に移動

for i, text2 in enumerate(texts2):
    if label[i] not in ['New Zealand', 'Scotland']:
        text2.set_color('gray')

fig.suptitle('Demographic Distribution Based on Birthplace', 
             fontsize=18,
             fontweight='bold',
             fontfamily='Times new roman'
             )

plt.show()