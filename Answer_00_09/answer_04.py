a = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

ds = {}
ls = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for i, _a in enumerate(a.split(' ')):
    _a = _a.replace(',', '')
    _a = _a.replace('.', '')

    if (i==1) in ls:
        char = _a[0]
    else:
        char = _a[:2]

    ds[char] = i+1

print(ds)
