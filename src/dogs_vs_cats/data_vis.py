import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve

def plot_roc_curve(y_test: list, y_pred: list):
    '''Plots Receiver Operating Characteristic Curve.

        Parameters:
        y_test (list): list of true output values.
        y_pred (list): list of outputs predicted by model.
    '''
    fpr, tpr, tresholds = roc_curve(y_test, y_pred)
    roc_figure = plt.figure(figsize=(7, 7))
    plt.plot([0, 1], [0, 1], 'b--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    
    auc = roc_auc_score(y_test, y_pred)
    plt.title('Receiver Operating Characteristic Curve ROC, AUC={:.4}'.format(auc))
    plt.grid('on')
    plt.plot(fpr, tpr, 'r')
    plt.show()