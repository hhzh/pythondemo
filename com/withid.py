res = '('
with open('d:/id.txt', 'r+') as fp:
    for line in fp.readlines():
        res = res +",'"+ line.strip()+"'"
print(res)
