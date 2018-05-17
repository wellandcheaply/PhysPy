'''
Messy scraper class which scrapes data on the elements from wikipedia
and uses it to write and format the ~3500 lines of code for use in PeriodicTable.py
'''

from bs4 import BeautifulSoup as bs
import requests as rq

req = rq.get('https://en.wikipedia.org/wiki/Chemical_element',)
soup = bs(req.text, 'lxml')

infotable = soup.find_all('table')[7].find_all('tr')

for datum in infotable:
	data = datum.find_all('td')
	if len(data) > 2:

		name = data[2].text
		symbol = data[1].text
		number = int(data[0].text)
		protons = number
		electrons = protons

		group_text = data[4].text
		group = 0
		if len(group_text) in [1, 2]:
			group = int(group_text)
		else:
			group = None

		period = int(data[5].text)

		# mass, density, melting point, boiling point, specific heat capacity, electronegativity
		where_to = {6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0}
		for index in [6,7,8,9,10,11]:
			text = data[index]
			if len(text.find_all('span')) == 0:
				text = text.text
			else:
				text = text.find_all('span')[1].text
			clean_text = ""
			for x in text:
				if x in["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
					clean_text += x
			try:
				where_to[index] = float(clean_text)
			except ValueError:
				where_to[index] = None


		neutrons = int(round(where_to[6], 0) - protons)
		print("# class defining an uncharged, isotopally typical {} atom".format(name))
		print("class {}(Atom):".format(symbol))
		print("    def __init__(self, position=None, velocity=None, momentum=None, nucleus=False):")
		print('        super().__init__(')
		print('                "{}",'.format(name))
		print('                "{}",'.format(symbol))
		print('                {},'.format(number))
		print('                {},'.format(protons))
		print('                {},'.format(neutrons))
		print('                {},'.format(electrons))
		print('                {},'.format(where_to[6]))
		print('                {},'.format(group))
		print('                {},'.format(period))
		print('                {},'.format(where_to[7]))
		print('                {},'.format(where_to[8]))
		print('                {},'.format(where_to[9]))
		print('                {},'.format(where_to[10]))
		print('                {},'.format(where_to[11]))
		print('                position=position,')
		print('                velocity=velocity,')
		print('                nucleus=nucleus')
		print('        )')

		print('$$$$')
		print('$$$$')

		print("# class defining an isotopally typical {} nucleus".format(name))
		print("class {}({}):".format(symbol+"_n", symbol))
		print("    def __init__(self, position=Vec([0, 0, 0]), velocity=Vec([0, 0, 0])):")
		print('        super().__init__(position, velocity, nucleus=True)')

		print('$$$$')
		print('$$$$')