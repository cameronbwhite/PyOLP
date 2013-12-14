PyOLP
=====

Python library implementing the Oregon Liquor Prices V1 API

## Examples

```python
>>> from PyOLP import PyOLP
>>> p = PyOLP()

# Get all the products that are 90 proof and are on sale
>>> for product in p.get_products(proof=90.0, on_sale=True):
...     print('{} ${}'.format(product.title, product.get_price().amount))
Bulleit 95 Rye $29.95
Bulleit Bourbon Frontier $29.95
C.m. Parrot Bay Coconut 90 $17.95
George Dickel #12 $19.95
Korbel Gold Reserve Vsop $16.95
Metaxa Ouzo $16.45

product = p.get_product('171')
>>> product.id
u'171'
>>> product.age
0.0
>>> product.bottles_per_case
24
>>> product.code
u'0314E'
>>> print(product.created_at)
2012-09-23 23:59:53.051544
>>> product.description
u'' 
>>> print(product.modified_at)
2013-12-01 05:33:37.371012
>>> product.on_sale
False
>>> product.proof
80.0
>>> product.size
u'375 ML'
>>> product.slug
u'0314e'
>>> product.title
u'Canadian Rich & Rare'
>>> product.status
u''

>>> price = product.get_price()
>>> price.amount
6.4
>>> print(price.created_at)
2012-09-23 23:59:53.057700
>>> print(price.effective_date)
2012-10-01 00:00:00
>>> price.id
u'171'
>>> print(price.modified_at)
2012-09-23 23:59:53.057717

>>> store = p.get_store('243')
>>> store.id
u'243'
>>> store.address
u'212 NE Main St, Willamina, OR 97396, USA'
>>> store.address_raw
u'212 NE Main St. 97396'
>>> store.county
u'Yamhill'
>>> store.hours_raw
u'9-6 M-S; Closed Sunday'
>>> store.key
1147
>>> store.latitude
45.079367
>>> store.longitude
-123.484112
>>> store.name
u'Willamina Liquor'
>>> store.phone
u'(503) 876-2112'
```
## Credit

Special thanks to all the fantastic developers who worked on 
https://github.com/jacquev6/PyGithub. This library used many
idea from that that project including the overall architecture 
and parts of the code.
