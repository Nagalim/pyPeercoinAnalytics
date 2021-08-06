import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
from datetime import datetime

x = []
y = []
txnconfirmed = []
txndate=[]
txntype=[]
txnlabel=[]
txnaddress=[]
txnamount=[]
txid=[]
SumTotal=0
walbalance=[]

with open('peercoin_txns.csv','r') as csvfile:
    csvtxndata = csv.reader(csvfile, delimiter = ',')
    txndata = list(csvtxndata)
    header = txndata[0]
    del txndata[0]
    txndata.reverse()
    for row in txndata:
        txnconfirmed.append(row[0])
        formdate=datetime.strptime(row[1], '%Y-%m-%dT%H:%M:%S')
        txndate.append(formdate)
        txntype.append(row[2])
        txnlabel.append(row[3])
        txnaddress.append(row[4])
        txnamount.append(row[5])
        txid.append(row[6])
        
        SumTotal+=float(row[5])
        walbalance.append(SumTotal)
        
x=txndate
y=walbalance
plt.bar(x, y, color = 'g', width = 0.72, label = "Amount")
plt.xlabel('Dates')
plt.ylabel('Sum Total (PPC)')
plt.title('Sum Total of Wallet')
plt.legend()
plt.show()
