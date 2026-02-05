import re

emojis = {
    'happy': '😊',
    'work': '💻',
    'love': '❤️',
    'tea': '☕'
}

message = input('Enter your message: ')
updated_message = []

for word in message.split():
    clean_word = word.lower().strip(".,!?")
    emoji = emojis.get(clean_word)
    if emoji:
        updated_message.append(f'{word} {emoji}')
    else:
        updated_message.append(word)

end_message = " ".join(updated_message)

print(end_message)

############

# new_message = message.split(' ')

# message_str = ''
# for word in new_message:
#     if word in emojis:
#         message_str += f'{word} {emojis[word] } '
#     else:
#         clean_word = re.split(r'[.,]', word)
#         if len(clean_word) > 0:
#             if clean_word[0] in emojis:
#                 message_str += f'{word} {emojis[clean_word[0]] } '
#             else : message_str += f'{word} '
#         else : message_str += f'{word} '
    
# print(message_str)


#################
# [new_message.insert((new_message.index(word)+1),emojis[word]) for word in new_message if word in emojis]

# def list_to_str(message_list):
#     message_str = ''
#     for word in message_list:
#         message_str += f'{word} '
#     return message_str

# print(list_to_str(new_message))

