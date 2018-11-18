import re
import sys

input_file = sys.argv[1]
output_text=[]

with open(input_file) as f:
	text = f.readlines()

for line in text:
	line = re.sub('sie','',line)
	line = re.sub(' i ','  ',line)
	line = re.sub('oraz','',line)
	line = re.sub('nigdy','',line)
	line = re.sub('dlaczego','',line)
	output_text.append(line)

for line in output_text:
	print(line)
