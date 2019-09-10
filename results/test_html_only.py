import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.ensemble import RandomForestClassifier as RF
from sklearn.feature_selection import f_classif as ANOVA
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression as LR

np.random.seed(42)

features = ['ageOfDomain', 'hasHttps', 'urlLength', 'prefixSuffix', 'hasIP', 'hasAt', 'redirects', 'shortenUrl', 'domainRegLength', 'DNSrecord', 'webTraffixAlexa', 'multSubDomains']
df1 = pd.read_csv('phish-0_w.csv', index_col=0)
df2 = pd.read_csv('alexa-0_w.csv', index_col=0)
df3 = pd.read_csv('phish0_5000.csv', index_col=0)
df4 = pd.read_csv('alexa0_5000.csv', index_col=0)
df5 = pd.read_csv('phish-0_k.csv')
df6 = pd.read_csv('alexa-0_k.csv')
feat1 = list(df1.columns)
feat2 = list(df3.columns)
feat = feat1[1:] + feat2[2:]
feat = feat + ['input_count']
# print (feat)
df1 = df1[features]
df2 = df2[features]
# print('df2 columns', df2.columns)
df3 = df3.drop('url', 1)
df4 = df4.drop('url', 1)
df3 = df3.drop('distance', 1)
df4 = df4.drop('distance', 1)

# print(df5.columns)
df5 = np.array(df5['input_count']).reshape(-1,1)
df6 = np.array(df6['input_count']).reshape(-1,1)

df1 = df1.values
df2 = df2.values
df3 = df3.values
df4 = df4.values
# print('df1 and df2:',df1.shape, df2.shape)
# print('df3 and df4:',df3.shape, df4.shape)
# print('df6 and df5:',df6.shape, df5.shape)

df1 = np.concatenate((df1, df3, df5), axis = 1)
df2 = np.concatenate((df2, df4, df6), axis = 1)

df1 = df1[:,-3:]
df2 = df2[:,-3:]
# print('df1 and df2:', df1.shape, df2.shape)

num_files = 5000
num_urls = num_files
indices = np.random.permutation(min(df1.shape[0], df2.shape[0]))
df1 = df1[indices,:]
indices = np.random.permutation(df1.shape[0])
df2 = df2[indices,:]
df3 = df1

frac = int(0.5 * num_files)
# print(num_files, frac)

x_train = df2[:frac, :]
x_train = np.concatenate((x_train, df3[:frac, :]), axis = 0)
y_train = np.zeros(frac)
y_train = np.concatenate((y_train, np.ones(frac)), axis = 0)

x_test = df2[frac:, :]
x_test = np.concatenate((x_test, df3[frac:, :]), axis = 0)
y_test = np.zeros(num_urls-frac)
y_test = np.concatenate((y_test, np.ones(num_urls-frac)), axis = 0)

# print(x_train.shape, x_test.shape)
# print(x_train.shape, x_test.shape)

test_all = {}
train_all = {}
# -------------
# RANDOM FOREST
# -------------
print('\nRandom Forest')
clf2 = RF()
clf2.fit(x_train, y_train)

print('test')
preds = clf2.predict(x_test)
print(sum(preds==y_test)/len(preds))
test_all['Random Forest'] = sum(preds==y_test)/len(preds)
print('train')
preds = clf2.predict(x_train)
print(sum(preds==y_train)/len(preds))   
train_all['Random Forest'] = sum(preds==y_train)/len(preds)

# -------------
# DECISION TREE
# -------------
print('\nDecision Tree')
dpth = []
acc = []
acc_train = []
criterion = 'entropy'
for max_depth in range(2,20):
    clf = DT(max_depth = max_depth, criterion  = criterion)
    clf.fit(x_train, y_train)
    preds = clf.predict(x_test)
    dpth.append(max_depth)
    acc.append(sum(preds==y_test)/len(preds))
    preds = clf.predict(x_train)
    acc_train.append(sum(preds==y_train)/len(preds))

arg = np.argmax(acc)
max_depth = dpth[arg]
clf = DT(max_depth = max_depth, criterion  = criterion)
clf.fit(x_train, y_train)

print('test')
preds = clf.predict(x_test)
print(sum(preds==y_test)/len(preds))
test_all['Decision Tree'] = sum(preds==y_test)/len(preds)   
print('train')
preds = clf.predict(x_train)
print(sum(preds==y_train)/len(preds))
train_all['Decision Tree'] = sum(preds==y_train)/len(preds)  


print(test_all)
results = pd.DataFrame(test_all, index=[0])
print(results)
results.to_csv('accuracy_html_only.csv', index=False)