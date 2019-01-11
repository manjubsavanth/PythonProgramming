# Multi class confusion matrix

from sklearn.metrics import confusion_matrix

y_actual = [2, 0, 3, 2, 0, 1, 3, 2, 0, 1, 2, 0, 3, 2, 0, 1, 3, 2, 0, 1]
y_pred = [2, 1, 2, 3, 0, 1, 3, 2, 0, 1, 2, 0, 3, 2, 0, 1, 3, 2, 0, 1]

cm = confusion_matrix(y_actual, y_pred)
print(cm)

rows,column = cm.shape

# Accuracy
""" Ratio of all the values predicted as true by sum of all of the predictions"""
def accuracy(confusion_matrix):
    diagonal_sum = confusion_matrix.trace()
    sum_of_all_elements = confusion_matrix.sum()
    return diagonal_sum / sum_of_all_elements 

# Precision by class 
"""Precision - precision is the fraction of cases where the algorithm correctly predicted 
class i out of all instances where the algorithm predicted i (correctly and incorrectly), 
It is the ratio of label by column sum"""

def precision(label,conf_matrix):
    col = conf_matrix[:, label]
    return conf_matrix[label,label]/col.sum()

# Recall by class
"""Recall - fraction of cases where the algorithm correctly predicted i out of all of the cases which are labelled as i, 
It is the ratio of label by row sum"""

def recall(label,conf_matrix):
    row = conf_matrix[label, :]
    return conf_matrix[label,label]/row.sum()


# Overall precision 
def precision_macro_average(conf_matrix):
    rows, columns = conf_matrix.shape
    sum_of_precisions = 0
    for label in range(rows):
        sum_of_precisions += precision(label, conf_matrix)
    return sum_of_precisions / rows


# Overall recall
def recall_macro_average(conf_matrix):
    rows, columns = conf_matrix.shape
    sum_of_recalls = 0
    for label in range(columns):
        sum_of_recalls += recall(label, conf_matrix)
    return sum_of_recalls / columns

print("\n Metrics by classes \n label precision recall")
for label in range(rows):
    print(f"{label:5d} {precision(label, cm):9.3f} {recall(label, cm):6.3f}")

print("\nOverall metrics")
print("Accuracy:", accuracy(cm))
print("Precision total:", precision_macro_average(cm))
print("Recall total:", recall_macro_average(cm))    

