beer = {'하이트': 2000, '카스': 2100, '칭따오': 2500, '하이네켄': 4000, '버드와이저': 500}
result = {k:v*1.05 for k, v in beer.items()}
print(beer, '           # 인상 전', sep='')
print(result, ' # 인상 후', sep='')
#}           # 인상 전
#} # 인상 후
