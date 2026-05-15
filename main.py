import asyncio


async def couroutine_fun(name : str) -> str:
    print("Entered couroutine_fun")
    await asyncio.sleep(0.1);
    print(f"Finished couroutine_fun for {name}")

async def main() :
    couroutine_obj = couroutine_fun("tarun")
    print(couroutine_obj)
    result = await couroutine_obj
    print(result)

if __name__ == "__main__":
    asyncio.run(main())

