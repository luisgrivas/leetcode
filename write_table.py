import argparse
import re


row = "| [{}]({}) | {} | {} | {} |\n"

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="File Name.", type=str)
parser.add_argument("-l", "--level", help="Problem Level.", type=str, default='')

args = parser.parse_args()

file_name = args.filename
dir_file = "problems/{}".format(file_name)
level = args.level

with open(dir_file, 'r') as file:
	lines = file.readlines()
	header = lines[0]
	number = re.search(r'\d+', header).group()
	title = header.replace('#', '').strip()
	py = '```python' in " ".join(lines)
	cpp = '```c++' in " ".join(lines)

with open('README.md', 'r+') as file:
	lines = file.readlines()
	write_index = -1

	for ind, line in enumerate(lines):
		if line[0] == '|':
			match = re.search(r'\d+', line)
			pnumber = match.group() if match else number
			if int(pnumber) < int(number):
				write_index = ind

	row = row.format(title, dir_file, level,
		":white_check_mark:" if py else ':x:', ":white_check_mark:" if cpp else ':x:')
	lines.insert(write_index + 1, row)

	file.seek(0)
	file.writelines(lines)