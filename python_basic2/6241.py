url=input()
result = {'protocol':'', 'host':'', 'others':''}
result['protocol']=url[:url.find(':')]
result['host'] = url[url.find('//') + 2 : url.find('/', url.find('//') + 2)]
result['others'] = url[url.rfind('/') + 1:]
for k, v in result.items():
    print(f'{k}: {v}')
