from sklearn.linear_model import LinearRegression

x=[[1],[2],[3],[4],[5]]
y=[40,50,60,70,80]

model=LinearRegression()
model.fit(x,y)
print("Predicted Marks:",model.predict([[6]]))