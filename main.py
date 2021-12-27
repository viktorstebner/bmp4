print("------------------------------------")
print("||--------------------------------||")
print("|| Super Cool Junk Repurpose Tool ||")
print("||--------------------------------||")
print("------------------------------------")
print("\nType \"start\" to start the assistant or type \"help\" to see all available commands\n")
isExitRequested = False
while isExitRequested == False:
    command = input(">")
    if command == "exit":
        isExitRequested = True
        continue
    if command == "help":
        print("---------------------------")
        print("List of available commands:\n")
        print("exit - close the program")
        print("help - display this list")
        continue
    print("Command not recognized, type \"help\" to see available commands")
print("end")

#do you want to submit building instructions, or do you want to get suggestions as to what to do with the items you might have?
#(scan all recipes for their ingredients)
#(for every ingredient: ask)
#do you have nails?
#(if yes) how many nails do you have?
