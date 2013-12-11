#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2013, Cameron White

import api_objects

class Price(api_objects.ApiObject):

    @property
    def amount(self):
        """
        :type: float
        """
        return self._amount 

    @property
    def created_at(self):
        """
        :type: datetime
        """
        return self._created_at

    @property
    def effective_date(self):
        """
        :type: datetime
        """
        return self._effective_date

    @property
    def id(self):
        """
        :type: string
        """
        return self._id
    
    @property
    def modified_at(self):
        """
        :type: datetime
        """
        return self._modified_at

    @property
    def product(self):
        """
        :type: related
        """
        return self._product

    def _initAttributes(self):
        self._amount = api_objects.NotSet
        self._created_at = api_objects.NotSet
        self._effective_date = api_objects.NotSet
        self._id = api_objects.NotSet
        self._modified_at = api_objects.NotSet

    def _useAttributes(self, attributes):
        if "amount" in attributes:
            self._amount = self._makeFloatAttribute(attributes["amount"])
        if "created_at" in attributes:
            self._created_at = self._makeDatetimeAttribute(attributes["created_at"])
        if "effective_date" in attributes:
            self._effective_date = self._makeDatetimeAttribute(attributes["effective_date"])
        if "id" in attributes:
            self._id = self._makeStringAttribute(attributes["id"])
        if "modified_at" in attributes:
            self._modified_at = self._makeDatetimeAttribute(attributes["modified_at"])
