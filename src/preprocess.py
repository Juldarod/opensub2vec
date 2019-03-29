import re

lines = 0

# input_path = '/home/julda/Documents/OpenSubtitles2018.en'
w_input_path = 'D:\OpenSubtitles2018.en\OpenSubtitles2018.en'
# output_path = '/home/julda/Documents/opensub2018.cor'
w_output_path = 'D:\OpenSubtitles2018.en\opensub2018.cor'
# output1 = open('/home/julda/Documents/example.cor', 'w+')

# input = open(input_path, 'r')
# output = open(output_path, 'w+')
input = open(w_input_path, 'r')
output = open(w_output_path, 'w+')
# input.readlines()

for line in input:
    lines += 1
    dash = re.sub(r'- ', '', line).lower()
    noise = re.sub(r'[^a-zA-Z\'áéíóúÁÉÍÓÚ]+', ' ', dash).lower()
    output.write(re.sub(r' \'', '\'', noise))
    output.write('\n')

# for i in range(50):
#     lines += 1
#     dash = re.sub(r'- ', '', input.readline()).lower()
#     noise = re.sub(r'[^a-zA-Z\'áéíóúÁÉÍÓÚ]+', ' ', dash).lower()
#     output1.write(re.sub(r' \'', '\'', noise))
#     output1.write('\n')

output.close()
print('%s lines processed' % lines)
# output1.close()
