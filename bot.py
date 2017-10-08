import aiml



# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("LOAD AIML B")

sessionId = 12345
sessionData= kernel.getSessionData(sessionId)

kernel.setPredicate("name", "Alex", sessionId)


# Press CTRL-C to break this loop
while True:
    print kernel.respond(raw_input("Enter your message >> "))