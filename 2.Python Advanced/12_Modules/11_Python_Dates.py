'''
Function -> strftime
%b -> Month Name, Short Version
%B -> Month Name, Full Version
%m -> Month as number 01-12
%y -> Year, short version, without century
%Y -> Year Full Version
%H -> Hour 00-23
%I -> Hour 00-12
%p -> AM(Morning)/PM(Night)
%M -> Minute 00-59
'''

import datetime

now = datetime.datetime.now()
minute = now.strftime('%M')
hour = now.strftime('%H')
month = now.strftime('%B')
year = now.strftime('%Y')
print('Minute:', minute)
print('Hour:', hour)
print('Month:', month)
print('year:', year)