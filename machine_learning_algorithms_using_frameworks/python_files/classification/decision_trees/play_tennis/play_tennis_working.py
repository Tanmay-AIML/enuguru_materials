#import six
import sys
#sys.modules['sklearn.externals.six'] = six
#import mlrose
from id3 import Id3Estimator
from id3 import export_graphviz
from os import system
import numpy as np

feature_names = ['Outlook','Temperature','Humidity','Wind','PlayTennis']
inputda = np.array([['Sunny', 'Hot', 'High', 'Weak'],
                    ['Sunny', 'Hot', 'High', 'Strong'],
                    ['Overcast', 'Hot', 'High', 'Weak'],
                    ['Rain', 'Mild', 'High', 'Weak'],
                    ['Rain', 'Cool', 'Normal', 'Weak'],
                    ['Rain', 'Cool', 'Normal', 'Strong'],
                    ['Overcast', 'Cool', 'Normal', 'Strong'],
                    ['Sunny', 'Mild', 'High', 'Weak'],
                    ['Sunny', 'Cool', 'Normal', 'Weak'],
                    ['Rain', 'Mild', 'Normal', 'Weak'],
                    ['Sunny', 'Mild', 'Normal', 'Strong'],
                    ['Overcast', 'Mild', 'High', 'Strong'],
                    ['Overcast', 'Hot', 'Normal', 'Weak'],
                    ['Rain', 'Mild', 'High', 'Strong']] )

inputsa = np.array([['No'],
                    ['No'],
                    ['Yes'],
                    ['Yes'],
                    ['Yes'],
                    ['No'],
                    ['Yes'],
                    ['No'],
                    ['Yes'],
                    ['Yes'],
                    ['Yes'],
                    ['Yes'],
                    ['Yes'],
                    ['No']])

inputsa = inputsa.reshape(len(inputsa),)
estimator = Id3Estimator()
estimator.fit(inputda,inputsa,check_input=False)
export_graphviz(estimator.tree_, 'tree.dot', feature_names)
system("dot -Tpng tree.dot > ID3_Rafa_Play_Tennis.png")
