import pandas as pd
import os

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
sns.set_theme(style="darkgrid")


def draw_plot(url=None, limit=15):
    paths = []
    if url == None:
        print('Please, pass the URL.')
    else:
        df = pd.read_json(url)
        columns = ['mean', 'max', 'min', 'floor_mean', 'floor_max', 'floor_min', 'ceiling_mean', 'ceiling_max', 'ceiling_min']
        for col in columns:
            if col in ['min', 'floor_min', 'ceiling_min']:
                ascending = True
            else:
                ascending = False
            title = f'Name_to_{col}_plot'
            data = {'name': df['name'], col: df[col]}
            data = pd.DataFrame(data=data).sort_values(by=col, ascending=ascending)[:limit]
            a = sns.barplot(x=col, y='name', data=data)
            a.set(xlabel=col, ylabel='Name', title=title)
            os.makedirs('plots', exist_ok=True)
            path = f'plots/{title}.png'
            plt.savefig(path)
            paths.append(path)
            plt.clf()
    return paths