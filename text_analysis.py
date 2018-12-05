#Text Analysis of StackOverflow question

with open("", "r") as infile:
	reader = csv.reader(infile)
	header = next(reader)
	for row in reader:
		#length of questions
		q_len = len(row[0].split(" "))

		#duplicate questions
		if "[duplicate]" in question:
			dup_count += 1




