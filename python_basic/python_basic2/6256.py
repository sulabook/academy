a = {'아메리카노': 1900, '카페모카': 3300, '에스프레소': 1900, '카페라떼': 2500, '카푸치노': 2500, '바닐라라떼': 2900}
b = {'헤이즐럿라떼': 2900, '카페모카': 3300, '밀크커피': 3300, '아메리카노': 1900, '샷크린티라떼': 3300}
new_menu = {k:v for k, v in a.items() if k not in b}
[new_menu.update({k:v}) for k, v in b.items() if k not in new_menu]
result = {item for item in new_menu.items() if item[1] >= 3000}
print(result)
