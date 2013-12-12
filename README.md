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
```
