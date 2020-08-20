

with open("./reg_data.txt") as file:
	reg = file.read()

voters=[]

reg = reg.split("\n")

for elem in reg:
	try:
		if int(elem[-4:]) <= 2000:
			voters.append(elem[:-5])
	except:
		print(' ')

# counting
with open("./vote_data.txt") as file:
        vote = file.read()

res = [0,0,0,0,0,0]  # res[0] will be never used
vote=vote.split("\n")

def add_vote(t):
	global res
	res[t] = res[t]+1

for elem in vote:
    try:
        v = int(elem[0])
    except:
        print(' ')
    else:
        adh = elem[2:]
        if adh in voters:
            add_vote(v)

# counting completed

print(res)

par = {
	"TDP" : res[1],
	"YCP" : res[2],
	"BJP" : res[3],
	"INC" : res[4],
	"NOTA" : res[5]
}

m=max(res)
for party in par:
	if par[party] == m:
		winner = "Winner : " + party
	print(party + " : " + str(par[party]))

print(winner)
print("Done")


# plot pie chart for votes

explode=[0,0,0,0,0,0]  # explode 1 elem in pie
maxpos = res.index(max(res))
explode[maxpos] = 0.1
explode=explode[1:]
explode = tuple(explode)

import matplotlib.pyplot as plt

labels = "TDP", "YCP", "BJP", "INC", "NOTA"
sizes = res[1:]
colors = ['gold', 'skyblue', 'orange', 'yellowgreen', 'red']

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
#plt.show()
plt.savefig("./static/res.jpeg", bbox_inches='tight')

