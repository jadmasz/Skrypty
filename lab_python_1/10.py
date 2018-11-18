import re
import sys

input_file = sys.argv[1]
output_text=[]

with open(input_file) as f:
	text = f.readlines()

for line in text:
	line = re.sub(' i ',' oraz ',line)
	line = re.sub(' oraz ',' i ',line)
	line = re.sub('nigdy','prawie nigdy',line)
	line = re.sub('dlaczego','czemu',line)
	output_text.append(line)

for line in output_text:
	print(line)
