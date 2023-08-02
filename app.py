from utils import eod
from utils import postgres
from json import dumps as json_dumps
import asyncio


async def main() -> None:
    await postgres.insert_json_data("fundamentals", eod.get_live_delayed("AAPL.US"))
    await postgres.insert_json_data("live_delayed", eod.get_live_delayed("AAPL.US"))
    await eod.get_live_socket("AMZN,TSLA")

asyncio.run(main())
