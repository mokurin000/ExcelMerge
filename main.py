import os
from polars import DataFrame

# 获取 data/*/*.txt
directory = "data"
l = [
    os.path.join(directory, subdir, file)
    for subdir in os.listdir(directory)
    for file in os.listdir(os.path.join(directory, subdir))
    if file.endswith(".txt")
]

data = []

for path in l:
    if not path:
        continue

    with open(path, "r", encoding="utf-8") as f:
        lines = f.read().split("\n")
        if len(lines) < 2:
            print(lines[0])
            continue
        columns = lines[0].split("\t")
        info = lines[1].split("\t")
        data.append({column: info for column, info in zip(columns, info)})

DataFrame(data).write_excel("total.xlsx")
