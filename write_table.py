import argparse
import requests
import re


row = "| [{}]({}) | {} | {} | {} |\n"
url = "https://leetcode-stats-api.herokuapp.com/luisgrivas"
ranking_str = "Ranking: **{}**"

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="File Name.", type=str)
parser.add_argument("-l", "--level", help="Problem Level.", type=str, default='')

args = parser.parse_args()

file_name = args.filename
dir_file = "problems/{}".format(file_name)
level = args.level

user_data = requests.get(url).json()
ranking = user_data.get('ranking')


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
		
		if 'Ranking' == line[:7]:
			ranking_index = ind
	
	lines[ranking_index] = ranking_str.format(ranking)

	row = row.format(title, dir_file, level,
		":white_check_mark:" if py else ':x:', ":white_check_mark:" if cpp else ':x:')
	lines.insert(write_index + 1, row)

	file.seek(0)
	file.writelines(lines)