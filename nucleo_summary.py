import sys

input_file = sys.argv[1]

data = open( input_file, 'r' )

def letter_position( input_file ):
	return [dict(enumerate(list(line.strip()), start=1)) for line in input_file]

def position_dict( ltr_pos_list ):
    keys = set().union(*(d for d in ltr_pos_list))
    return {k: "".join(d.get(k,'') for d in ltr_pos_list)  for k in keys}

def unique_letters( input_file ):
	unique = list( set( ''.join([line.strip() for line in input_file])))
	unique.sort()
	return unique

def position_breakdown( pos_dict, letters ):
	return {position: {letter: \
	float(pos_dict[position].count(letter)) / float(len(pos_dict[position])) \
	for letter in letters} for position in pos_dict.keys()}
 
def summary_print( pos_summ ):
	for pos in pos_summ.keys():
		print "Position:", pos
		for ltr in pos_summ[pos].keys():
			print "%s:" % ltr, "{0:.0%}".format(pos_summ[pos][ltr])
		print

uniques = unique_letters( data )

data.seek(0)

ltr_pos = letter_position( data )

pos_dict = position_dict( ltr_pos )

pos_summary = position_breakdown( pos_dict, uniques )

summary_print( pos_summary )

