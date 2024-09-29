import pandas as pd

data = {
    'Студенты' : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Оценки' : [5, 4, 5, 4, 3, 4, 5, 5, 5, 3,]

}

df = pd.DataFrame(data)

print(df.describe())
