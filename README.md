PyOLP
=====

Python library implementing the Oregon Liquor Prices V1 API

## Examples ## 

```python
>>> p = PyOPl()

product = p.get_product('171')

>>> product.id
u'171'
>>> product.title
u'Canadian Rich & Rare'
>>> product.on_sale
False
>>> product.bottles_per_case
24

>>> store = p.get_store('243')
>>> store.id
u'243'
>>> store.name
u'Willamina Liquor'
>>> store.address
u'212 NE Main St, Willamina, OR 97396, USA'
>>>store.hours_raw
Out[23]: u'9-6 M-S; Closed Sunday'
```
