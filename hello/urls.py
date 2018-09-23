#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 23:11:59 2018

@author: yutaka
"""

from django.urls import path
from . import views

urlpatterns = [
        path('',views.index, name='index')
        ]