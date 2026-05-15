import asyncio


async def couroutine_fun(name : str) -> str:
    print("Entered couroutine_fun")
    await asyncio.sleep(0.1);
    return f"Finished couroutine_fun for {name}"

async def main() :
    # couroutine_obj = couroutine_fun("tarun")
    # print(couroutine_obj)
    # result = await couroutine_obj
    # print(result)
    task1 = asyncio.create_task(couroutine_fun("tarun"))
    print("task1")
    task2 = asyncio.create_task(couroutine_fun("tarun2"))
    print("task2")
    task_result = await task1
    print(task_result)
    task_result = await task2
    print(task_result)

if __name__ == "__main__":
    asyncio.run(main())

