#!/usr/bin/python
# -*- coding: utf-8 -*-

# [Import start]
from server import app
# [Import end]

@app.route('/')
def hello():
    return "Hello_world"

if __name__ == '__main__':
    app.run()
