# https://forums.raspberrypi.com/viewtopic.php?t=160295
# https://stackoverflow.com/questions/9322796/keep-a-subprocess-alive-and-keep-giving-it-commands-python
# https://stackoverflow.com/questions/63782892/using-asyncio-to-wait-for-results-from-subprocess
# https://stackoverflow.com/questions/50473113/how-to-run-async-function-forever-python

import asyncio

proc = None

async def run(cmd: str):
    global proc

    proc = await asyncio.create_subprocess_shell(
        cmd,
        stderr=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE
    )

    msg = await proc.stdout.readline()
    
    print(msg)

    await proc.stdin.write('pairable on')

    # stdout, stderr = await proc.communicate()

    # print(f'[{cmd!r} exited with {proc.returncode}]')

    # if stdout:
    #     print(f'[stdout]\n{stdout.decode()}')
    # if stderr:
    #     print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('bluetoothctl'))