import numpy as np

f = open('hygdata_v3.csv')
star_lines = f.readlines()
print(f'Parsed {len(star_lines)} lines')
num_stars = len(star_lines) - 1

headers = star_lines[0].split(',')
print(f'Headers: {headers}')
dist_index = headers.index('dist')
print(f'Distance Index: {dist_index}')

#delete header line
star_lines.__delitem__(0)

star_dists = np.zeros(num_stars)
for line_index in range(len(star_lines)):
    line = star_lines[line_index].split(',')
    star_dists[line_index] = float(line[dist_index])

print(f'Mean star dist: {np.mean(star_dists)} parsecs.')

dist_cutoff = 5
print(f'Number of stars closer than {dist_cutoff} parsecs:')
count = sum(star_dist < dist_cutoff for star_dist in star_dists)
print(f'Count: {count}')

for line_index in range(len(star_lines)):
    line = star_lines[line_index].split(',')
    star_dist = float(line[headers.index('dist')])
    # if star_dist < dist_cutoff:
    #     star_name = line[headers.index('proper')].strip()
    #     print(f'* {star_name}')

# Why is Proxima Centauri in here, but not Alpha or Beta Centauri ? It seems that maybe a lot of proper names are missing ... ?
# Answer: Alpha is called Rigil Kentaurus
# Beta is called, 

#Proper Name Count:
print(f'Stars with proper names:')
_proper_count = 0 
for line_index in range(len(star_lines)):
    line = star_lines[line_index].split(',')
    star_name = line[headers.index('proper')].strip()
    if len(star_name) > 0:
        print(f'* {star_name}')
        _proper_count += 1
print(f'Total with names: {_proper_count}')

