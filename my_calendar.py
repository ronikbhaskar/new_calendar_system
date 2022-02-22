
from typing import Tuple
import prime
import datetime
from math import floor

NUM_SECONDS = 31556952

"""
it's redundant to recalculate, so I'll write it out here:
	
	365.2425 days per year (avg)
	24 hours per day
	3600 seconds per hour
	=> 36524.25 * 24 * 36 seconds per year
	=> 146097 * 6 * 36 seconds per year
	=> 31556952 seconds per year (natural number)

"""

def seconds_to_standard(seconds : int) -> str:
	"""
	this is just for sanity checks
	very simple
	"""
	
	if seconds < 0:
		return None
		
	days = seconds // 86400 if seconds >= 86400 else 0
	seconds %= 86400
	hours = seconds // 3600 if seconds >= 3600 else 0
	seconds %= 3600
	minutes = seconds // 60 if seconds >= 60 else 0
	seconds %= 60
	
	return f'{days} days, {hours} hours, {minutes} minutes, {seconds} seconds'

def get_ridiculous_splits() -> Tuple[int]:
	"""
	my exploratory code to find what I preferred
	"""
	
	pf = prime.prime_factorize(NUM_SECONDS)
	all_factors = prime.find_factors(pf)
	
	# 6-18 hours = 21600-64800 seconds
	true_ennai_len = None
	true_ennaike_per_arro = None
	true_arro_per_sol = None
	
	for ennai_len, num_arro in all_factors:
		if 21600 <= ennai_len <= 64800\
		and num_arro < 1000:
			
			ennai_factors = prime.prime_factorize(ennai_len)
			if 7 in ennai_factors \
			or 773 not in ennai_factors:
				continue
			
			arro_splits = prime.find_factors(prime.prime_factorize(num_arro))
			
			for ennaike_per_arro, arro_per_sol in arro_splits:
				# why make groups divisible by 7 again?
				if 5 <= ennaike_per_arro <= 10 \
				and ennaike_per_arro % 7 \
				and not ennaike_per_arro % 2 \
				and arro_per_sol < 70 \
				and ennaike_per_arro * ennai_len < 86400 * 6:
					true_ennai_len = ennai_len
					true_ennaike_per_arro = ennaike_per_arro
					true_arro_per_sol = arro_per_sol
					
	"""
	ennai len 62613
	ennaike per arro 8
	arro per sol/orbit 63
	"""
					
	# at this point I'm just hardcoding values
	
	moment = 773
	moments_per_ninth = 9
	ninths_per_ennai = 9
	
	return (moment,moments_per_ninth,ninths_per_ennai,true_ennaike_per_arro,true_arro_per_sol)
	
def get_seconds_since_new_year() -> int:
	# datetime(year, month, day, hour, minute, second[, microsecond])
	new_year = datetime.datetime(2022, 1, 1, 0, 0, 0)
	now = datetime.datetime.now()
	return floor(now.timestamp()) - floor(new_year.timestamp())
	
def get_ronik_time(time_splits : Tuple[int], seconds : int) -> Tuple[int]:
	"""
	generates time in new system
	starts at 0 for all counts
	last append is for orbits
	"""
	
	time = []
	for time_split in time_splits:
		time.append(seconds % time_split)
		seconds //= time_split
		
	time.append(seconds)
		
	return tuple(time)
	
def format_time(time : Tuple[int]) -> str:
	"""
	simple formatting function to make the time readable
	"""
	sing_plural = [
		('second', 'seconds'),
		('moment', 'moments'),
		('ninth', 'ninths'),
		('ennai', 'ennaike'),
		('arro', 'arro'),
		('orbit', 'orbits')
	]
	
	formatted_time = ''
	for t, (singular, plural) in zip(time, sing_plural):
		units = singular if t == 1 else plural
		formatted_time += f'{t} {units}\n'
		
	return formatted_time
	
def main():
	# time_splits = get_ridiculous_splits()
	time_splits = (773, 9, 9, 8, 63)
	seconds = get_seconds_since_new_year()
	current_time = get_ronik_time(time_splits, seconds)
	print(format_time(current_time))

if __name__ == "__main__":
	main()
