#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2013, Cameron White

class ApiException(Exception):

    def __init__(self, status, data):
        super(ApiException, self).__init__(self)
        self.__status = status
        self.__data = data

    @property
    def status(self):
        """
        The status returned by the API
        """
        return self.__status

    @property
    def data(self):
        """
        The (decoded) data returned by the API
        """
        return self.__data

    def __str__(self):
        return str(self.status) + " " + str(self.data)

class BadAttributeException(Exception):
    """
    Exception raised when the API returns an attribute with the wrong type.
    """
    def __init__(self, actualValue, expectedType):
        self.__actualValue = actualValue
        self.__expectedType = expectedType

    @property
    def actual_value(self):
        """
        The value returned by the API
        """
        return self.__actualValue

    @property
    def expected_type(self):
        """
        The type expected
        """
        return self.__expectedType
