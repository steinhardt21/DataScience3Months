
# coding: utf-8

# In[4]:


from sklearn import tree
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier

clf = tree.DecisionTreeClassifier()
clf_QDA = QuadraticDiscriminantAnalysis()
clf_LDA = LinearDiscriminantAnalysis()
clf_RFC = RandomForestClassifier()

# CHALLENGE - create 3 more classifiers...
# 1 QuadraticDiscriminantAnalysis
# 2 LinearDiscriminantAnalysis
# 3 RandomForestClassifier

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


# CHALLENGE - ...and train them on our data
# 	Fit the model according to the given training data and parameters.
clf = clf.fit(X, Y)
clf_QDA = clf_QDA.fit(X, Y)
clf_LDA = clf_LDA.fit(X, Y)
clf_RFC = clf_RFC.fit(X, Y)

#Perform classification on an array of test vectors X.
prediction = clf.predict([[190, 70, 43]])
predictionQDA = clf_QDA.predict([[190, 70, 43]])
predictionLDA = clf_LDA.predict([[190, 70, 43]])
predictionRFC = clf_RFC.predict([[190, 70, 43]])

# CHALLENGE compare their reusults and print the best one!

print(prediction)
print(predictionQDA)
print(predictionLDA)
print(predictionRFC)

