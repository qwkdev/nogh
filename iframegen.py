offset = 28

import os

with open('urls.txt') as f:
	urls = f.read()

urls = urls.split('\n')

for n, i in enumerate(urls):
	os.makedirs(f'{n+offset}')
	with open(f'{n+offset}/index.html', 'w') as f:
		f.write(f'<body style="margin: 0;"><iframe style="width: 100vw; height: 100vh; border: none; background: #000000" src="{i}"></iframe></body>')
	print(f'<a class="item"    style="background-image: url(\'https://github.com/qwkdev/nogh/blob/main/home/images/{n+offset}.png?raw=true\')" href="/nogh/{n+offset}"><p class="item-text">{"/".join(i.split("/")[3:])}</p></a>')