def all_variants(text):
    for a in range(len(text)):
        for r in range(len(text) - a):
            yield text[a:r + a + 1]


b = all_variants("abc")
for i in b:
    print(i)
