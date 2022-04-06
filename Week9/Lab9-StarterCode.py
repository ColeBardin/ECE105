import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm
from sklearn.ensemble import RandomForestClassifier

"""
Cole Bardin
14422557

ASSIGNMENT: COMPLETE err_test function below
"""

"""
ECE 105: Programming for Engineers 2
Created May 25, 2021
Steven Weber
SKLearn covertype dataset example solution

This code plots SVM and RF error rates vs. size of training set
"""

"""
def random_sample(N, n):
return a random sample of [0,...,N-1] of size n
"""
def random_sample(N, n):
    return np.random.choice(N, n, replace=False)

"""
def err(cls, X_tr, y_tr, X_te, y_te, cls):
train classifier cls and return error rate
"""
def err(cls, X_tr, y_tr, X_te, y_te):
    cls.fit(X_tr, y_tr)
    z_te = cls.predict(X_te)
    return len([1 for y, z in zip(y_te, z_te) if y != z])/len(y_te)

"""
COMPLETE:
err_test(M, f_all, X_tr, y_tr, X_te, y_te)
conducts M Monte Carlo trials for both the SVM and RF classifier for each f
f in f_all is the fraction of available training data to use on the classifier
X_tr, y_tr is the whole set of available training data: fraction f is used
X_te, y_te is the set of testing data available for measureing performance

The code should return two dictionaries: e_svm_ave, e_rf_ave
Both dictionaries have keys that are the training data fractions f_all
The values for key f is the average classifier error (over the M trials) for f
"""
def err_test(M, f_all, X_tr, y_tr, X_te, y_te):
    # initialize empty dictionaries for SVM and RF average error rates
    # named e_svm_ave and e_rf_ave
    # dictionary keys are the fractions in f_all
    # dictionary values are the average error for that fraction of training data
    e_svm_ave, e_rf_ave = {}, {}
    # iterate over each fraction f in f_all
    for f in f_all:
        # 1. n_tr is the number of training points to use with fraction f
        # note len(y_tr) is the total number of training points available
        n_tr = int(f*(len(y_tr)))
        # 2. initialize empty lists for SVM and RF errors
        # named e_svm and e_rf
        # these will hold the M sample error rates for the M Monte Carlo trials
        e_svm, e_rf = [], []
        # conduct M Monte Carlo trials
        for _ in range(M):
            # 3. generate random set of indices i_tr of size n_tr
            # make sure to use the random_sample function defined above
            # let i_tr be the random indices returned from random_sample
            i_tr = random_sample(len(y_tr), n_tr)
            # 4. use indices i_tr to specify the *actual* training set
            # let X_tra, y_tra be actual training set, sampled from X_tr, y_tr
            # using random indices i_tr
            X_tra, y_tra = X_tr[i_tr], y_tr[i_tr]
            # 5. append to e_svm the value returned by the err function above
            # where the classifier is the SVM classifer svm.SVC()
            # and using X_tra, y_tra, X_te, y_te
            e_svm.append(err(svm.SVC(), X_tra, y_tra, X_te, y_te))
            # 6. append to e_svm the value returned by the err function above
            # where the classifier is the RF classifer RandomForestClassifier()
            # and using X_tra, y_tra, X_te, y_te
            e_rf.append(err(RandomForestClassifier(), X_tra, y_tra, X_te, y_te))
        # 7. update dictionaries with average Monte Carlo trial error rates
        # use np.mean() on e_svm and e_rf to get Monte Carlo average
        # this is the value in the e_svm_ave and e_rf_ave dictionaries
        # for the key f
        e_svm_ave[f] = np.mean(e_svm)
        e_rf_ave[f] = np.mean(e_rf)
    # return SVM and RF average error rate dictionaries
    return e_svm_ave, e_rf_ave

"""
def plot_err(e_svm, e_rf, fn):
plot the SVM and RF error rates vs. fraction of used training data
"""
def plot_err(e_svm, e_rf, fn):
    plt.scatter(e_svm.keys(), e_svm.values(), label='SVM')
    plt.scatter(e_rf.keys(),  e_rf.values(),  label='RF')
    plt.xscale('log')
    plt.title('SVM and RF error rate vs. fraction of training data used')
    plt.xlabel('f: Fraction of available training data used')
    plt.ylabel('e: Testing error rate')
    plt.legend()
    plt.savefig(fn)

if __name__ == "__main__":
    # load the covertype dataset
    # https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_covtype.html
    # https://scikit-learn.org/stable/datasets/real_world.html#covtype-dataset
    dataset = datasets.fetch_covtype()
    # get feature and target data
    X, y = dataset.data, dataset.target

    # original and target sample size
    N, n = X.shape[0], 10000
    # random indices for sampling data to more manageable size
    i_sd = random_sample(N, n)
    # use the random indices to downsample X, y
    X_sd, y_sd = X[i_sd], y[i_sd]

    # target testing size
    n_te = 1000
    # random indices for testing data
    i_te = random_sample(n, n_te)
    # use the random indices to set testing data X_te, y_te
    X_te, y_te = X_sd[i_te], y_sd[i_te]

    # i_tr are indices in range(n) not in testing indices i_te
    i_tr = list(set(range(n)) - set(i_te))
    # use the indices to set the (max possible) training data X_tr, y_tr
    X_tr, y_tr = X_sd[i_tr], y_sd[i_tr]

    # fraction of available training data to use
    # recall: np.geomspace gives points evenly distributed on a log-axis
    f_all = np.geomspace(0.01, 1.00, 20)
    # number of Monte Carlo independent trials (for averaging out errors)
    M = 10
    # average error rates for SVM and RF for each fraction f
    e_svm, e_rf = err_test(M, f_all, X_tr, y_tr, X_te, y_te)

    # print error rates for both SVM and RF for each fraction f
    print("f\te_svm\te_rf")
    [print("{:.3f}\t{:.3f}\t{:.3f}".format(f, e_svm[f], e_rf[f])) for f in f_all]

    # plot error rates and save to file fn
    fn = "Lab9-SampleOutput.pdf"
    plot_err(e_svm, e_rf, fn)
