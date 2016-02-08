#Swap Case https://www.codeeval.com/open_challenges/96/submit/

my_file = open("text.txt", "r")

def swap_case(String_o):
	end_str = []
	for a in String_o:
		if a == str.lower(a):
			k = str.upper(a)
			end_str.append(k)
		elif a == str.upper(a):
			l = str.lower(a)
			end_str.append(l)
	return "".join(end_str)

print swap_case(my_file.read())
my_file.close()