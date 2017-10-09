import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

'''
sessionId = 12345
sessionData= kernel.getSessionData(sessionId)
kernel.setPredicate("dog", "Alex", sessionId)
client_dog=kernel.getPredicate("dog", sessionId)
kernel.setBotPredicate("nameOfBot","ChatBot")
bot_name=kernel.getBotPredicate("nameOfBot")

  elif message == "save":
	kernel.saveBrain("bot_brain.txt")
'''
def detect_nr (str):
    nr=0
    p=1
    for char in str:
        if char.isdigit()==True:
            nr=nr*p+int(char)
            p*=10
    return nr
# Press CTRL-C to break this loop
while True:
  message = raw_input("Your Message: ")
  if message == "quit" or message == "QUIT" or message == "EXIT" or message == "exit" or message == "close" or message == "CLOSE":
	exit()
  elif message.find("years")!=-1 or message.find("Years")!=-1 or  message.find("YEARS")!=-1:
      bot_response = kernel.respond(message)
      varsta = detect_nr(bot_response)
      if varsta>0 and varsta <= 4 :
                  print kernel.respond("small")
      elif varsta >= 5 and varsta <= 14:
                  print kernel.respond("prescolar")
      elif varsta >= 15 and varsta <= 18:
                  print kernel.respond("elev")
      elif varsta >= 19 and varsta <= 26:
                  print kernel.respond("student")
      elif varsta >= 27 and varsta <= 50:
                  print kernel.respond("adult")
      elif varsta >= 51 and varsta <= 90:
                  print kernel.respond("batran")
      elif varsta >= 91:
                  print kernel.respond("big")
      else :
                  print bot_response
  else:
      bot_response = kernel.respond(message)
      print bot_response