car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()
print(x)
a = ('key1', 'key2', 'key3')
b = 56
thisdict = dict.fromkeys(a, b)
print(thisdict)
z = car.get("model")
print(z)
g = car.items()
print(g)
print(car.keys())
print(car.values())
f=x.popitem()
print(x)
h=car.pop("model")
print(car)
i = car.setdefault("color", "white")
print(car)
x.update({"color": "Red"})
print(x)

