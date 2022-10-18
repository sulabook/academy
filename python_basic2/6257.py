fruit = ['   apple   ', 'banana', ' melon']
result = {e.strip():len(e.strip()) for e in fruit}
print(result)
