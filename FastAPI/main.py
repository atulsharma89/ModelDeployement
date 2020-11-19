#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 20:00:16 2020

@author: atul595525
"""

import uvicorn #for ASGI
from fastapi import FastAPI


#Create an object for teh appplication
app = FastAPI()


@app.get('/')

def index():
    return{'message': 'Hello World'}

#AS soon AS WE HIT THE HOME PAGE IT WILL SHOW THE WELOCME MESSAGE

#iN BELOW Step we will create a welcome page

@app.get('/Welcome')

def get_name(name: str):
    return{'Welcome to the world my dear friend': f'{name}'}

#whenever we are calling welcome API, its expecting a string input
#same string will be stored in local variable name and that will be returned


#Running the API with uvicorn
# This will be run at port 8000


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn main:app --reload
