from aiokafka import AIOKafkaProducer
import asyncio
import ujson

async def send_one():
    producer = AIOKafkaProducer(bootstrap_servers='localhost:9094', value_serializer=lambda v: ujson.dumps(v).encode('utf-8'))
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        for i in range(10):
            await producer.send("demo-topic", {"a": 123, "hello": "world"}, b"world")
        await producer.flush()
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()

asyncio.run(send_one())