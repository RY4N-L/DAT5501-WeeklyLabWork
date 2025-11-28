from ucimlrepo import fetch_ucirepo 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# fetch dataset 
car_evaluation = fetch_ucirepo(id=19) 
  
# data (as pandas dataframes) 
x = car_evaluation.data.features 
y = car_evaluation.data.targets 

# Change values to numerical
x.replace({'vhigh':4, 'high':3, 'med':2, 'low':1, 
           '5more': 5, 'more': 5, 
           'small': 1, 'medium': 2, 'big': 3}, inplace=True)

print (x.head())
# metadata 
print(car_evaluation.metadata) 
  
# variable information 
print(car_evaluation.variables) 

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
plot_tree(clf, feature_names=x.columns, class_names=y['class'].values, filled=True)
plt.tight_layout()
plt.show()





