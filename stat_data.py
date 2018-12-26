import pandas as pd
# import matplotlib.pyplot as plt


excel_file = "clever_excel.xls"
books = pd.read_excel(excel_file)

df1 = books.describe()


s = books.groupby('author')['index'].nunique()
df2 = s.to_frame()


books.hist(column="price")
# plt.show()

writer = pd.ExcelWriter('output.xlsx')
df1.to_excel(writer,'Central tendency')
df2.to_excel(writer,'Authors')

writer.save()
