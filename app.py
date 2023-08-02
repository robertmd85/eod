from utils import eod
from utils import postgres
import asyncio


async def main() -> None:
    postgres.insert_json_data("fundamentals", eod.get_live_delayed("AAPL.US"))
    postgres.insert_json_data("live_delayed", eod.get_live_delayed("AAPL.US"))
    await eod.get_live_socket("AMZN,TSLA")


asyncio.run(main())
