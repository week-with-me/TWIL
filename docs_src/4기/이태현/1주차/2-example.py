def is_normal_def():
    pass

async def is_coroutine():
    pass


print('Type')
print('def: ', type(is_normal_def))
print('async def: ', type(is_coroutine))

print('\n')

print('Call Function')
print('def: ', is_normal_def())
print('async def: ', is_coroutine())