from sklearn.linear_model import LogisticRegression

hours=[[1],[2],[3],[4],[5]]
result=[0,0,0,1,1]
# 0=fail 1=pass
model=LogisticRegression()
model.fit(hours,result)
print("Prediction:",model.predict([[4]]))