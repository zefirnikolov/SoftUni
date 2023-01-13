class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send_eq_change_bool(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


big_list = []
while True:
    command = input()
    if command == "Stop":
        break

    action_list = command.split()
    message_eq_object = Email(action_list[0], action_list[1], action_list[2])
    big_list.append(message_eq_object)

new_list = list(map(int, input().split(", ")))
for element_eq_index in new_list:
    big_list[element_eq_index].send_eq_change_bool()

for index in range(len(big_list)):
    element_eq_object = big_list[index]
    print(element_eq_object.get_info())
