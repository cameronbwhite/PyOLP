#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Copyright (C) 2013, Cameron White

import api_exceptions
import urllib
import urlparse
import httplib

class Requester:
    
    def __init__(self, base_url):

        self.__base_url = base_url
        o = urlparse.urlparse(base_url)
        self.__hostname = o.hostname
        self.__port = o.port
    
    def requestJsonAndCheck(self, verb, url, parameters=None, requestHeaders=None, input=None):
        return self.__check(*self.requestJson(verb, url, parameters, requestHeaders, input))

    def requestJson(self, verb, url, parameters=None, requestHeaders=None, input=None):
        
        connection = httplib.HTTPConnection(self.__hostname, self.__port)

        connection.request(verb, url, input, requestHeaders)
        response = connection.getresponse()

        status = response.status
        responseHeaders = dict(response.getheaders())
        output = response.read()
        
        connection.close()

        return status, responseHeaders, output

    def __check(self, status, responseHeaders, output):
        if status >= 400:
            raise api_exceptions.ApiException(status, output)
        return responseHeaders, output
