import pika
from bddrest import status
from yhttp.ext.rabbitmq import install


def test_rabbitmq_install(app, Given, redis):
    install(app)
    app.settings.merge('''
    ''')
    app.ready()

    @app.route()
    def get(req):
        with app.rabbitmq.acquire() as cxn:
            cxn.channel.basic_publish(
                body='banana',
                exchange='',
                routing_key='fruits',
                properties=pika.BasicProperties(
                    content_type='text/plain',
                    content_encoding='utf-8',
                    delivery_mode=2,
                )
            )

    with Given():
        assert status == 200
