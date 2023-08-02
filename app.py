from utils import postgres
from utils import eodh
import asyncio


async def main() -> None:
    connection = await postgres.connect_to_postgres()
    fundamentals = eodh.get_fundamentals("AAPL", "US", "General::Exchange")
    live_delayed = eodh.get_live_delayed("AAPL", "US")
    await eodh.get_live_socket("AMZN, TSLA", "US")
    await postgres.insert_json_data(connection, "fundamentals", fundamentals)
    print(fundamentals)
    print(live_delayed)


asyncio.run(main())
