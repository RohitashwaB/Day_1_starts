

from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

x,y = iris.data, iris.target

print("features", iris.feature_names)



iris_df = pd.DataFrame(data=np.c_[iris['data'], iris['target']], columns=iris['feature_names'] + ['target'])

train_iris_df, valid_iris_df, test_iris_df = np.split(iris_df.sample(frac=1), [int(0.2*len(iris_df)), int(0.8*len(iris_df))])

knn = KNeighborsClassifier(n_neighbors=3)

x_train = train_iris_df.drop('target', axis=1)
y_train = train_iris_df['target']
x_test = test_iris_df.drop('target', axis=1)
y_test = test_iris_df['target']

knn.fit(x_train, y_train)
accuracy = knn.score(x_test, y_test)
print(accuracy)



import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

predictions = knn.predict(x_test)

cm = confusion_matrix(y_test, predictions, labels=knn.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=knn.classes_)
disp.plot()
plt.show()

