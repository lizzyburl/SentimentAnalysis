from svmutil import *

y, x = svm_read_problem('trainingOutput');
m = svm_train(y, x, '-t 2 -s 2');

yTest, xTest = svm_read_problem('testingOutput');
p_label, p_acc, p_val = svm_predict(yTest, xTest, m);

print p_acc;
