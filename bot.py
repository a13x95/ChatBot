import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

#sessionId = 12345
#sessionData= kernel.getSessionData(sessionId)
#kernel.setPredicate("name", "Alex", sessionId)


# Press CTRL-C to break this loop
while True:
  message = raw_input("Your Message: ")
  if message == "quit" or message == "QUIT" or message == "EXIT" or message == "exit" or message == "close" or message == "CLOSE":
	exit()
  #elif message == "save":
	#kernel.saveBrain("bot_brain.brn")
  else:
	bot_response = kernel.respond(message)
	print bot_response