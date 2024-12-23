

async def execute_callback(callback, callback_functions):
    data = callback.split('/')
    callback_text = data[0]
    args = data[1:] if len(data) > 1 else []

    callback_function = callback_functions.get(callback_text)
    if callback_function:
        return await callback_function(*args)
    else:
        print(f"No corresponding function found for the given key: {callback_text}")
