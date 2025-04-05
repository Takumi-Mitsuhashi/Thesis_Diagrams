import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#書体をTimes New Romanに
plt.rcParams['font.family'] = 'Times New Roman'

#データフレームの作成
data=pd.DataFrame({
    'Year':[1858, 1861, 1862, 1863, 1864, 1867, 1871],
    'Otago':[6995, 30163, 45588, 67420, 49019, 48577, 60722],
    'Southland':[None, 1820, 3455, 9545, 8085, 7943, 8769],
    'Auckland':[18177, 24420, 27644, 35703, 42132, 48321, 62335],
    'Wellington':[11753, 12566, 13643, 15214, 14987, 21950, 24001]
})

# 図の作成
fig, ax = plt.subplots(2, 2, figsize=(8, 8))  # 縦横の比率

# 各サブプロットにlineplotを描画
sns.lineplot(x='Year', y='Otago', data=data, color='black', marker='o', ax=ax[0, 0], label='Otago')
sns.lineplot(x='Year', y='Southland', data=data, color='black', marker='o', ax=ax[0, 1], label='Southland')
sns.lineplot(x='Year', y='Auckland', data=data, color='black', marker='o', ax=ax[1, 0], label='Auckland')
sns.lineplot(x='Year', y='Wellington', data=data, color='black', marker='o', ax=ax[1, 1], label='Wellington')

# 凡例の位置の設定
ax[0, 0].legend(loc='upper left')
ax[0, 1].legend(loc='upper left')
ax[1, 0].legend(loc='upper left')
ax[1, 1].legend(loc='upper left')

#Y軸ラベルの設定
ax[0, 0].set_ylabel('Population')
ax[0, 1].set_ylabel('')
ax[1, 0].set_ylabel('Population')
ax[1, 1].set_ylabel('')

#X軸ラベルの設定
ax[0, 0].set_xlabel('')
ax[0, 1].set_xlabel('')
ax[1, 0].set_xlabel('Year')
ax[1, 1].set_xlabel('Year')

#Y軸の範囲の設定
ax[0,0].set_ylim(0, )
ax[0, 1].set_ylim(0, 12000)
ax[1,0].set_ylim(0,)


# 全体のタイトル
fig.suptitle('The Population of Each Region (1858-1871)', fontsize=16)

# レイアウト調整
plt.tight_layout(rect=[0, 0, 1, 0.96])  # suptitleのスペースを確保

# グラフ表示
plt.show()