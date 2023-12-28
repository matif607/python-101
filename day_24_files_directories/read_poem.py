# with open('jabberwocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines = jabber.readlines()



# print(lines)

with open('jabberwocky.txt', 'r') as jabber:
    text = jabber.read()
print(text)
# in this method file will be automatically closed
# just open will not close the file and if we forget to close then it will run into problems later