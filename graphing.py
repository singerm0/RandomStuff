# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:36:52 2018

@author: Matthew
"""
import numpy as np
import pandas as pd

import random
from sklearn.manifold import TSNE
from sklearn import preprocessing
from matplotlib import pyplot as plt
from bokeh.plotting import figure, output_file, show, ColumnDataSource

#initializing dummy input
def main(fake,*data):
    if fake == True:
        vects = [0]*500
        questions = ['']*500
        answers = ['']*500
        
        nouns = ("puppy", "car", "rabbit", "girl", "monkey")
        verbs = ("runs", "hits", "jumps", "drives", "barfs") 
        adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
        adj = ("adorable", "clueless", "dirty", "odd", "stupid")
        
        
        for x in range(len(vects)):
            num = random.sample(range(1,5),4)
            vects[x] = random.sample(range(1,1000),300)
            questions[x] = nouns[num[0]] +' '+verbs[num[1]]+' '+adv[num[2]]+' '+adj[num[3]]
            num = random.sample(range(1,5),4)
            answers[x] = nouns[num[0]] +' '+verbs[num[1]]+' '+adv[num[2]]+' '+adj[num[3]]
        

        startquest =  dict(zip(questions,vects))
        startanswer = dict(zip(answers,vects))
    
        test = {'questions':startquest,
                'answers':startanswer}
    
    questData = test['questions']
    ansData = test['answers']
    
    questWord = list(questData.keys())
    questVects = list(questData.values())
    questionArr = npectY':tsne_results[:len(questVects),1]})
        
    .array(questVects)
    
    ansWord = list(ansData.keys())
    ansVects = list(ansData.values())
    answersArr = np.array(ansVects)
    combinedVects = np.concatenate([questionArr,answersArr],axis=0)
    tsne = TSNE(n_components =2,verbose=0,perplexity=15,n_iter=50000, early_exaggeration =5)
    tsne_results = tsne.fit_transform(combinedVects)
    
    plt.scatter(tsne_results[:,0],tsne_results[:,1])
    
    finalQuestions = pd.DataFrame({'words':questWord,
                                   'origVects':questVects,
                                   'vectX':tsne_results[:len(questVects),0],
                                   'v
    finalAnswers = pd.DataFrame({'words':ansWord,
                                 'origVects':ansVects,
                                 'vectX':tsne_results[len(questVects):,0],
                                 'vectY':tsne_results[len(questVects):,1]})
    return (finalQuestions,finalAnswers)

if __name__ == '__main__':
    (questions,answers) = main(1)

#%%

output_file("toolbar.html")
souce = ColumnDataSource(data=dict(
        x = list(questions.vectX),
        y = list(questions.vectY),
        words = list(questions.words)
        ))
TOOLTIPS = '''
    <div>
        <span style="font-size: 17px; font-weight: bold;">@desc</span>
    </div> '''
# create a new plot with the toolbar below
bplt = figure(plot_width=1000, plot_height=1000, tooltips=TOOLTIPS,
           title=None, toolbar_location='below')
bplt.circle('x','y', size=10,souce=souce)

show(bplt) 
#%%
from bokeh.plotting import figure, output_file, show

output_file("toolbar.html")

# create a new plot with the toolbar below
p = figure(plot_width=400, plot_height=400,
           title=None, toolbar_location="below")

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)  

#%%
from bokeh.plotting import figure, output_file, show, ColumnDataSource

output_file("toolbar.html")

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y=[2, 5, 8, 2, 7],
    desc=['A', 'b', 'C', 'd', 'E'],
    imgs=[
        'https://bokeh.pydata.org/static/snake.jpg',
        'https://bokeh.pydata.org/static/snake2.png',
        'https://bokeh.pydata.org/static/snake3D.png',
        'https://bokeh.pydata.org/static/snake4_TheRevenge.png',
        'https://bokeh.pydata.org/static/snakebite.jpg'
    ],
    fonts=[
        '<i>italics</i>',
        '<pre>pre</pre>',
        '<b>bold</b>',
        '<small>small</small>',
        '<del>del</del>'
    ]
))

TOOLTIPS = """
    <div>
        <div>
            <img
                src="@imgs" height="42" alt="@imgs" width="42"
                style="float: left; margin: 0px 15px 15px 0px;"
                border="2"
            ></img>
        </div>
        <div>
            <span style="font-size: 17px; font-weight: bold;">@desc</span>
            <span style="font-size: 15px; color: #966;">[$index]</span>
        </div>
        <div>
            <span>@fonts{safe}</span>
        </div>
        <div>
            <span style="font-size: 15px;">Location</span>
            <span style="font-size: 10px; color: #696;">($x, $y)</span>
        </div>
    </div>
"""
#%%
p = figure(plot_width=400, plot_height=400, tooltips=TOOLTIPS,
           title="Mouse over the dots")

p.circle('x', 'y', size=20, source=source)
