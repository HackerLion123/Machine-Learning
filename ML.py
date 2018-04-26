from sklearn import tree

#smooth = 0,Bumpy = 1
features = [[140,0],[150,0],[120,1],[110,1],[155,0],[120,0],[100,0]]
labels = ["apple","apple","orange","orange","apple","banna","banna"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

u = clf.predict([[input("Weight : "),input("Smooth 0 or Bumpy 1 : ")]])
print u

#print clf.predict([[130,0]])
#print clf.predict([[120,0]])
#print clf.predict([[120,1]])
