#! bin/python3

from outcomeUtils import DeriveColumnLabels
from outcomeUtils import DeriveNewValues as der

import urllib, json
import numpy as np
import pandas as pd


def main():

	"""
	import data

	things to do: 
	- add check for metadata to ensure no unexpected columns
	"""

	# request_url = "https://data.austintexas.gov/views/9t4d-g238/rows.json"
	# response = urllib.request.urlopen(request_url)
	# str_response = response.readall().decode('utf-8')

	infile = 'test_data.json'
	obj = json.loads(open(infile).read())

	"""
	prepare pandas dataframe
	"""

	data = pd.DataFrame(obj['data'])
	data.columns = DeriveColumnLabels.get_labels(obj['meta']['view']['columns'])
	

	"""
	append columns
	"""

	data['d_is_live_outcome'] = data.apply (lambda data: der.identify_live_outcomes(data.outcome_type),axis=1)
	data['d_is_cat_or_dog'] = data.apply (lambda data: der.identify_cats_and_dogs(data.animal_type),axis=1)
	data['d_age_in_weeks'] = data.apply (lambda data: der.calc_animal_age_in_weeks(data.datetime, data.date_of_birth),axis=1)
	data['d_age_group'] = data.apply (lambda data: der.determine_age_group(data.d_age_in_weeks, data.d_is_cat_or_dog),axis=1)
	data['d_month_year_sort'] = data.apply (lambda data: der.get_month_year_sort(data.datetime),axis=1)
	data['d_month_year_label'] = data.apply (lambda data: der.get_month_year_label(data.datetime),axis=1)


	"""
	group dataframe by month-years
	"""

	monthly_data = data.groupby(['d_month_year_sort', 'd_month_year_label']).count()
	print(monthly_data)



if __name__ == '__main__':
	main()