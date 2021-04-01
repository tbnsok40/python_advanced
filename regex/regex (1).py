import re

search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

regex = '\d{2~3}[- ]?\d{3~4}[- ]?\d{4}[- ]'
result = re.findall(regex, search_target)
print(result)
