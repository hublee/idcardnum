

ratios = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
ratios2 = {
	0:'1',
	1:'0',
	2:'X',
	3:'9',
	4:'8',
	5:'7',
	6:'6',
	7:'5',
	8:'4',
	9:'3',
	10:'2'
	}

odd = [1,3,5,7,9]
even = [0,2,4,6,8]

def a(srcid):

	gender = int(srcid[16])
	tmpGender = even
	if gender in odd:
		tmpGender = odd

	print(srcid)

	idlist = []
	for g in range(len(tmpGender)):
		tg = tmpGender[g]
		if tg == gender:
			continue
		tmpSrcid = srcid[0:16] + str(tg)
		sumProduct = 0
		for i in range(len(tmpSrcid)):
			num = int(tmpSrcid[i])
			product = num * ratios[i]
			sumProduct += product
		mod = sumProduct%11
		lastNum = ratios2[mod]
		idlist.append(tmpSrcid + lastNum)
		# print(tmpSrcid + lastNum)

	return idlist


if __name__ == '__main__':
	idlist = a('371521199007077532')
	print(idlist)
	# print(ratios2.get(1))