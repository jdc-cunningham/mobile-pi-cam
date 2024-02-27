# https://forums.raspberrypi.com/viewtopic.php?t=160295
# https://stackoverflow.com/questions/9322796/keep-a-subprocess-alive-and-keep-giving-it-commands-python

import time
import asyncio

from threading import Thread
from subprocess import Popen, PIPE

process = None
bluetooth_active = False

class Bluetooth_API():
  def __init__(self):
    self.proc = None
    self.active = True
    self.clbk_var = None

  def start(self):
    self.proc = Popen(['bluetoothctl'], stdin=PIPE, stdout=PIPE)

  def callback(self, ctl_out):
    print(ctl_out)
    self.clbk_var = ctl_out

  def listen(self):
    while (self.active):
      ctl_out = repr(self.proc.stdout.readline())

      if (ctl_out):
        self.callback(ctl_out)

      time.sleep(0.05)

  def send(self, cmd):
    cmd_buf = "{0}\n".format(cmd).encode()

    print(cmd_buf)

    self.proc.stdin.write(cmd_buf)
    self.proc.stdin.flush()



bl = Bluetooth_API()

bl.start()

Thread(target=bl.listen).start()

cmds = [
  'power on',
  'discoverable on',
  'pairable on',
  'agent NoInputNoOutput',
  'default-agent'  
]

cur_cmd = cmds[0]
cur_cmd_processing = False

while (len(cmds) > 0):
  if (not cur_cmd_processing):
    cur_cmd = cmds[0]
    cur_cmd_processing = True
    bl.send(cur_cmd)

  if (bl.clbk_var):
    cur_cmd_processing = False
    bl.clbk_var = None
    cmds.pop(0)

  time.sleep(0.01)

print('all cmds sent')