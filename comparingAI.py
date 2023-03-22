from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import preprocessing
import file_importing


def main():
    X, y = file_importing.labelled_ICA(False)

    X = (preprocessing.StandardScaler()).fit_transform(X)  # Normalize data with 0 mean and std 1.

    # make an array of the analysis models
    models = []
    models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC(gamma='auto')))

    kfold = StratifiedKFold(n_splits=2, random_state=1, shuffle=True)
    for i, (train_index, test_index) in enumerate(kfold.split(X, y)):
        print(f"Fold {i}:")
        print(f"  Train: index={train_index}")
        print(f"  Test:  index={test_index}")

    results = []
    for name, model in models:
        cv_results = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
        results.append(cv_results)
        print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

if __name__ == "__main__":
    main()