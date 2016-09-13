import pandas

df1 = pandas.DataFrame(
	[
	[2,4,6],
	[10,20,30]
	],
	columns=["Price","Age","Value"],
	index=["First","Second"]
	)

# print(df1)

df2 = pandas.DataFrame([
	{"Name":"John", "Age":20},
	{"Name":"Mike", "Age":23}
	])
# print(df2)

# print(dir(df1))

# print(df1.mean())

# print(df1.Price.max())