#aiter
import asyncio

class AsyncIterator:
	def __init__(self, start, stop):
		self.start = start
		self.stop = stop

	def __aiter__(self):
		self.cur = self.start
		return self

	async def __anext__(self):
		await asyncio.sleep(1)
		if self.cur >= self.stop:
			raise StopAsyncIteration

		self.cur += 1
		return self.cur - 1


async def exemple():
	custom_obj = AsyncIterator(1,10)
	obj_iter = aiter(custom_obj)
	print(obj_iter)
	async for num in obj_iter :
		print(num)
#asyncio.run(exemple())


a = [1,2,3,4,5]
#print(all(a))
#montre si c'est itérable

a = [1,2,0,3,4,5]
#print(any(a))
#montre si c'est itérable
#print(bin(76))
#print(bool(0))

print(complex(3,4))
#delattr() delete attribute from an object


import math
#print(dir(math))#nous dit tous les méthodes que nous pouvons utiliser
#fltr permet de filtrer et retourne un iterator, un peu comme une liste on peut iterer sur chaque élément de l'iterator
#frozenset fera rendra set immutable
#map permet de maper (comme en math) un peut comme une fonction de R -> R (a image dans R)

