from ucimlrepo import fetch_ucirepo 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
mushroom = fetch_ucirepo(id=73) 
  
# data (as pandas dataframes) 
x = mushroom.data.features 
y = mushroom.data.targets 
  
# Change values to numerical
x.replace({'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
           'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19,
           't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26,
           '?':0}, inplace=True)

# metadata 
print(mushroom.metadata) 
  
# variable information 
print(mushroom.variables) 

# show x data
print(y.head())

# format settings to show more rows and columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)

# Train/test split and decision tree classifier
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0, stratify=y)

clf = DecisionTreeClassifier(random_state=0)
clf.fit(x_train, y_train)

preds = clf.predict(x_test)
print ("test accuracy:", accuracy_score(y_test, preds))

'''
# Show feature importances
feature_importances = pd.Series(clf.feature_importances_, index=x.columns)
print("Feature importances:")
print(feature_importances.sort_values(ascending=False))
# Visualize the decision tree (optional)
from sklearn.tree import export_text
tree_rules = export_text(clf, feature_names=list(x.columns))
print("Decision Tree Rules:")
print(tree_rules)
'''

# show tree graphically
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
plt.savefig('decision_tree.png', dpi=100)
plot_tree(clf, feature_names=x.columns, class_names=y['poisonous'].values, filled=True)
plt.show()





