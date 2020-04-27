import asyncio
from wonderapipy import shards

async def main():
    shard = await shards.shards()
    print(shard)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())