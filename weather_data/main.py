import pandas

data= pandas.read_csv("weather.csv")
print(data)

templist= data.temp.to_list
print(templist)
print(data.temp.max())
print(data.temp.mean())

print(data[data.day=="Monday"])
print(data[data.temp==16])
print(data[data.temp==data.temp.max()])
