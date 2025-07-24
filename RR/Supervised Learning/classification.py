from sklearn.linear_model import SGDClassifier


X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
clf.fit(X, y)

clf.predict([[2., 2.]])
clf.coef_
clf.intercept_

clf.decision_function([[2., 2.]])
clf = SGDClassifier(loss="log_loss", max_iter=5).fit(X, y)
clf.predict_proba([[1., 1.]]) 

