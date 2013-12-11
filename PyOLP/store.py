#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2013, Cameron White

import api_objects

class Store(api_objects.ApiObject):

    @property
    def address(self):
        """
        :type: string
        """
        return self._address

    @property
    def address_raw(self):
        """
        :type: string
        """
        return self._address_raw

    @property
    def county(self):
        """
        :type: string
        """
        return self._county

    @property
    def hours_raw(self):
        """
        :type: string
        """
        return self._hours_raw

    @property
    def id(self):
        """
        :type: string
        """
        return self._id
    
    @property
    def key(self):
        """
        :type: int
        """
        return self._key
    
    @property
    def latitude(self):
        """
        :type: float
        """
        return self._latitude
    
    @property
    def longitude(self):
        """
        :type: float
        """
        return self._longitude

    @property
    def name(self):
        """
        :type: string
        """
        return self._name

    @property
    def phone(self):
        """
        :type: string
        """
        return self._phone

    def _initAttributes(self):
        self._address = api_objects.NotSet
        self._address_raw = api_objects.NotSet
        self._county = api_objects.NotSet
        self._hours_raw = api_objects.NotSet
        self._id = api_objects.NotSet
        self._key = api_objects.NotSet
        self._latitude = api_objects.NotSet
        self._longitude = api_objects.NotSet
        self._name = api_objects.NotSet
        self._phone = api_objects.NotSet

    def _useAttributes(self, attributes):
        if "address" in attributes:
            self._address = self._makeStringAttribute(attributes["address"])
        if "address_raw" in attributes:
            self._address_raw = self._makeStringAttribute(attributes["address_raw"])
        if "county" in attributes:
            self._county = self._makeStringAttribute(attributes["county"])
        if "hours_raw" in attributes:
            self._hours_raw = self._makeStringAttribute(attributes["hours_raw"])
        if "id" in attributes:
            self._id = self._makeStringAttribute(attributes["id"])
        if "key" in attributes:
            self._key = self._makeIntAttribute(attributes["key"])
        if "latitude" in attributes:
            self._latitude = self._makeFloatAttribute(attributes["latitude"])
        if "longitude" in attributes:
            self._longitude = self._makeFloatAttribute(attributes["longitude"])
        if "name" in attributes:
            self._name = self._makeStringAttribute(attributes["name"])
        if "phone" in attributes:
            self._phone = self._makeStringAttribute(attributes["phone"])

