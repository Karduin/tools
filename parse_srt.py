import srt

liste = ['123', 'yop', '56', 'bar', 'foo']

liste2 = [item for item in liste if item.isnumeric()]
print(liste2)