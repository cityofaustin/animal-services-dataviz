#! bin/python3

from datetime import datetime, date
import numpy as np
import pandas as pd

class DeriveColumnLabels(object):
	"""
	tbd
	"""
	def get_labels(columns):
		labels = []
		for i in columns:
			fieldName = i['fieldName']
			labels.append(fieldName)
		return labels

class DeriveNewValues(object):
	"""
	This class contains functions that use the original source data to derive new 
	data values. Later, the AppendNewColumns class will place these values 
	into new columns. 
	"""
	def identify_live_outcomes(outcome_type):
		live_outcome_value_list = ['Adoption', 'Transfer', 'Return to Owner', 'Relocate']
		if outcome_type in live_outcome_value_list:
			is_live_outcome = 1
		else:
			is_live_outcome = 0
		return is_live_outcome

	def calc_animal_age_in_weeks(date_of_outcome, date_of_birth):
		birth_date = date(int(date_of_birth[0:4]),int(date_of_birth[5:7]),int(date_of_birth[8:10]))
		outcome_date = date(int(date_of_outcome[0:4]),int(date_of_outcome[5:7]),int(date_of_outcome[8:10]))
		age = outcome_date - birth_date
		age_in_days = age.days
		age_in_weeks = age_in_days/7
		return age_in_weeks

	def identify_cats_and_dogs(type_of_animal):
		dog_and_cat_value_list = ['Dog', 'Cat']
		if type_of_animal in dog_and_cat_value_list:
			is_cat_or_dog = 1
		else:
			is_cat_or_dog = 0
		return is_cat_or_dog
        
	def determine_age_group(age_in_weeks, animal_type_test):
		if animal_type_test ==0:
			age_group = 'not cat or dog'
		else:
			if 0 < age_in_weeks < 6:
				age_group = 'neonate'
			elif 6 <= age_in_weeks < 52:
				age_group = 'kitten/puppy'
			elif 52 <= age_in_weeks:
				age_group = 'adult'
			else:
				age_group = 'unable_to_determine'
		return age_group

	def get_month_year_label(date_of_outcome):
		d = date(int(date_of_outcome[0:4]),int(date_of_outcome[5:7]),int(date_of_outcome[8:10]))
		month_year_label = d.strftime("%Y-%b")
		return month_year_label

	def get_month_year_sort(date_of_outcome):
		d = date(int(date_of_outcome[0:4]),int(date_of_outcome[5:7]),int(date_of_outcome[8:10]))
		month_year_sort = d.strftime("%Y-%m")
		return month_year_sort
