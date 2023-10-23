from aiokafka import AIOKafkaConsumer
import asyncio

async def consume():
    consumer = AIOKafkaConsumer('demo-topic', bootstrap_servers='localhost:9094', auto_offset_reset='earliest', group_id='default')
    
    # Get cluster layout and join group `my-group`
    await consumer.start()

    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset, msg.key, msg.value, msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()

asyncio.run(consume())