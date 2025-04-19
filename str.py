import asyncio

from pyrogram import Client

print("Enter your app information from my.telegram.org/apps below.")


async def main():
    async with Client(
        ":memory:", api_id=int(input("28962746:")), api_hash=input("727457f88d661b08e636188a949cd9f3:")
    ) as app:
        print(await app.export_session_string(BQG577oAilvG1uSvyOXMaelV0o-CvAEmnP-5fY-oAdpJZRT620a0jAM7fbT0_By5qrxv7pLgOqCL-BFJlpN0P1qPCt9gvfGBO1po1qTIp4w-MuHTu2PIfG76DEOorT9YE5XYDzbJ8j6EjXLWrdpJ0wdKX-YcQypt4n9Sf_zLfrzN2D6LCP50wINvGVMLOGwUjos3tOPSY4nPeZWbLnc6UAlByHv-i5_xJTIyyb56keQD2wGPa2DgyME6MvPs6PSoFs7jyOW6mXuA1Ou5yL4FaFhDRvwr80XbTkDtwHSmWVys1Trk8Y4agToQ-hIbyP8lB2OAJ-Vu_eQb7vxVV_Q70Jo9zGgb8wAAAAGu00bKAA))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
