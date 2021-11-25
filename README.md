# yhttp-rabbitmq

[![PyPI](http://img.shields.io/pypi/v/yhttp-rabbitmq.svg)](https://pypi.python.org/pypi/yhttp-rabbitmq)
[![Build](https://github.com/yhttp/yhttp-rabbitmq/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/yhttp/yhttp-rabbitmq/actions/workflows/build.yml)
[![Coverage Status](https://coveralls.io/repos/github/yhttp/yhttp-rabbitmq/badge.svg?branch=master)](https://coveralls.io/github/yhttp/yhttp-rabbitmq?branch=master)


RabbitMQ extension for [yhttp](https://github.com/yhttp/yhttp).


### Install

```bash
pip install yhttp-pony
```


### Usage

```python
from yhttp import Application
from yhttp.ext.rabbitmq import install as rabbitmq_install


app = Application()
rabbitmq_install(app)
app.settings.merge(f'''
rabbitmq:

''')

# TODO: example
app.ready()
```
