import pandas as pd
fruit = {'orange': [3,2,0,1], 'apple' : [0,3,7,2], 'grapes' : [7,14,6,15]}
df1 = pd.DataFrame(fruit)
print(df1)

fruit2 = {'grapes' : [13,12,10,2,55,98], 'mango' : [10,13,17,2,9,76], 'banana' : [20,23,27,4,0,9], 'pear' : [21,24,28,51,22,25], 'pineapple' : [30,33,38,30,36,31] }
df2 = pd.DataFrame(fruit2)
#df2 = df2.drop(df1.index[2])
print(df2)

df3 = pd.concat((df1, df2), axis=1)


print(df3)