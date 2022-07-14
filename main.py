import asyncio
import os

from near_lake_framework import LakeConfig, streamer, near_primitives

async def main():    
    config = LakeConfig.mainnet()
    config.start_block_height = 69030747
    config.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    config.aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    stream_handle, streamer_messages_queue = streamer(config)
    while True:
        streamer_message = await streamer_messages_queue.get()
        print(f"Block #{streamer_message.block.header.height} Shards: {len(streamer_message.shards)}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())