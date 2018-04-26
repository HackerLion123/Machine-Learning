from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

iris_dataset = load_iris()

print iris_dataset.feature_names
print iris_dataset.target_names
print iris_dataset.data[0]
test_data = [0,60,110]

#traning data
train_label = np.delete(iris_dataset.target,test_data)
train_data = np.delete(iris_dataset.data,test_data,axis=0)

#testing data
test_label = iris_dataset.target[test_data]
test_data = iris_dataset.data[test_data]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_label)

print test_label

print clf.predict(test_data)

#To Display the descision tree
import graphviz
 
dot_data = tree.export_graphviz(clf, out_file=None) 
#graph = graphviz.Source(dot_data) 
graph.render("iris_dataset") 

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris_dataset.feature_names,  
                         class_names=iris_dataset.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
print graph 
