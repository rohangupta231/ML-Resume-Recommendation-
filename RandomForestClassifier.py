from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
# xtrain , xtest, ytrain, ytest = train_test_split(xx, df['label'], test_size = 0.2)
clf = RandomForestClassifier()
clf = clf.fit(xx, df['label'])
s = pickle.dump(clf, open("saved.sav", "wb"))
p = pickle.load(open("saved.sav", 'rb'))
p1 = p.predict(xx)