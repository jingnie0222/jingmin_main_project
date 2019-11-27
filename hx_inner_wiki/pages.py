# -*- coding: utf-8 -*-
import logging



def Page()
    try:
        page = int(request.GET['page'])
    except:
        page = int(1)
    item_on_page = int(15)
