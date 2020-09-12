import os, json
from telegram.ext import Updater

updater = Updater(token=os.environ['TOKEN'], use_context=True)
COUNT = 2

class Ping():
  def __init__(self, count, hostname):
    self.count = count
    self.hostname = hostname
  
  def run(self, use_exit=False):
    cmd = "ping -c " + str(self.count) + " " + self.hostname
    respond = os.system(cmd)
    if use_exit is False:
      return respond
    else:
      respondm = os.system(cmd + "; kill -9 %d"%(os.getppid()))
      return respond

with open('host.json') as json_file:
    HOSTNAME = json.load(json_file)

for i in range(len(HOSTNAME['server_ip'])):
  execute = Ping(COUNT,HOSTNAME['server_ip'][i])
  result = execute.run()
  if result != 0:
    host_down = HOSTNAME['server_ip'][i]
    updater.bot.send_message(chat_id=int(os.environ['CHATT_ID']),text="Host : " + host_down + " is down!")