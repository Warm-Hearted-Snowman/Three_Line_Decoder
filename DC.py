from sys import argv
if len(argv) > 1:
    text = argv[1]
else:
    text = input('Enter your String : \n')
lenght = len(text)
if lenght % 4 != 0:
    lenght = lenght//4+1
    lenght_2 = (lenght*2)-1
else:
    lenght = lenght//4
    lenght_2 = (lenght*2)
word = list(map(str, text))
line_1_final = []
line_2_final = []
line_3_final = []
for i in range(lenght):
    line_1_final.append(word.pop(0))
for i in range(lenght_2):
    line_2_final.append(word.pop(0))
line_3_final = word
final_word = []
for i in range(lenght):
    if len(line_1_final) != 0:
        final_word.append(line_1_final.pop(0))
    if len(line_2_final) != 0:
        final_word.append(line_2_final.pop(0))
    if len(line_3_final) != 0:
        final_word.append(line_3_final.pop(0))
    if len(line_2_final) != 0:
        final_word.append(line_2_final.pop(0))

print(''.join(final_word))
