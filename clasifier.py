from sklearn import tree

#height weight shoe size
X = [[12,23,7],[12,243,8],[123,23,6],[23,12,5]]
Y = ['male','male','female','female']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

pred= clf.predict([[12,23,3]])

print(pred)
