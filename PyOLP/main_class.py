#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2013, Cameron White
#                                                                              
# PyGithub is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.                                                           
#                                                                              
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS   
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#                                                                      
# You should have received a copy of the GNU Lesser General Public License
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.

import api_exceptions
from price import Price
from product import Product
from store import Store
from requester import Requester

DEFAULT_BASE_URL = "http://www.oregonliquorprices.com"

class PyOPl:

    def __init__(self, base_url=DEFAULT_BASE_URL):

        self.__requester = Requester(base_url)

    def get_product(self, id=None):
        """
        :calls: `GET /api/v1/product/`
        :param code: string
        :rtype: :class: `product.Product`
        """
        assert isinstance(id, str), id
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/api/v1/product/" + str(id) + "/"
        )
        return Product(self.__requester, headers, data)

    def get_store(self, id=None):
        """
        :calls: `GET /api/v1/store/`
        :param id: string
        :rtype: :class: `store.Store`
        """
        assert isinstance(id, str), id
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/api/v1/store/" + str(id) + "/"
        )
        return Store(self.__requester, headers, data)

    def get_price(self, id=None):
        """
        :calls: `GET /api/v1/price/`
        :param id: string
        :rtype: :class: `price.Price`
        """
        assert isinstance(id, str), id
        headers, data = self.__requester.requestJsonAndCheck(
            "GET",
            "/api/v1/price/" + str(id) + "/"
        )
        return Price(self.__requester, headers, data)

