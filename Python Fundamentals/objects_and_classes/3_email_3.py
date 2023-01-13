class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True
        return self.is_sent

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


email_objects_list = []

while True:
    command = input()

    if command == "Stop":
        break

    action_list = command.split()
    sender = action_list[0]
    receiver = action_list[1]
    content = action_list[2]
    email_obj = Email(sender, receiver, content)
    email_objects_list.append(email_obj)

index_list = list(map(int, input().split(", ")))
for element_eq_index in index_list:
    email_objects_list[element_eq_index].send()

for obj in email_objects_list:
    print(obj.get_info())
