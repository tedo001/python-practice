import pandas as pd 
import matplotlib.pyplot as plt 
tata_motors=pd.read_csv(r"/content/drive/MyDrive/DataSet/TATAMOTORS.csv") 
tata_steel=pd.read_csv(r"/content/drive/MyDrive/DataSet/TATASTEEL.csv") 
tcs=pd.read_csv(r"/content/drive/MyDrive/DataSet/TCS.csv") 
print(tata_motors.head()) 
print(tata_motors.shape) 
print(tata_motors.info()) 
print(tata_motors.isna().sum()) 
print(tata_motors.duplicated().sum()) 
print(tata_steel.duplicated().sum()) 
print(tcs.duplicated().sum()) 
print(tata_motors.describe().round(2)) 
columns_to_drop = ['Trades','Deliverable Volume','%Deliverble'] 
tata_motors=tata_motors.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1) 
tata_steel=tata_steel.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1) 
tcs=tcs.drop(['Trades','Deliverable Volume','%Deliverble'], axis=1) 
tata_motors['Date'] = pd.to_datetime(tata_motors['Date']) 
tata_steel['Date'] = pd.to_datetime(tata_steel['Date']) 
tcs['Date'] = pd.to_datetime(tcs['Date']) 
plt.figure(figsize=(20,7)) 
plt.plot(tata_motors['Date'],tata_motors['Open'],color='blue',label='Tata Motors') 
plt.plot(tata_steel['Date'],tata_steel['Open'],color='grey',label='Tata Steel') 
plt.plot(tcs['Date'],tcs['Open'],color='orange',label='TCS') 
plt.title("Relation between Tata Motors, Tata Steel and TCS Price") 
plt.xlabel("Year") 
plt.ylabel("Price") 
plt.legend() 
plt.show() 
plt.figure(figsize=(20,7)) 
plt.plot(tata_motors['Date'],tata_motors['Volume'],color='blue',label='Tata Motors')
plt.plot(tata_steel['Date'],tata_steel['Volume'],color='grey',label='Tata Steel') 
plt.plot(tcs['Date'],tcs['Volume'],color='orange',label='TCS') 
plt.title("Relation between Tata Motors, Tata Steel and TCS Volume") 
plt.xlabel("Year") 
plt.ylabel("Volume") 
plt.legend() 
plt.show() 
sumTM=0 
s1=0 
for i in range(len(tata_motors)): 
if tata_motors.loc[i,'Date'].day==30: 
sumTM+=tata_motors.loc[i,'Open'] 
s1 +=1 
print("Total Invested in Tata Motors = Rs",round(sumTM,2)) 
print("Shares Owned of Tata Motors =",s1) 
print("Average Investmentment of 1 share = Rs",round((sumTM/s1),2)) 
tm_end=298.2 
result1=round((tm_end*s1)-sumTM,2) 
roiTM=round((result1/sumTM)*100,2) 
print("nInvestment Result:") 
if result1<0: 
print("Net Unrealised Loss = Rs",result1) 
else: 
print("Net Unrealised Profit = Rs",result1) 
print("Tata Motors ROI from 2000-1-3 to 2021-04-30 =",roiTM,"%")


#output:
Output:
Date Symbol Series Prev Close Open High Low Last Close \
0 2000-01-03 TELCO EQ 201.60 207.4 217.25 207.4 217.0 216.75 
1 2000-01-04 TELCO EQ 216.75 217.0 219.00 206.0 211.9 208.20 
2 2000-01-05 TELCO EQ 208.20 194.0 217.80 194.0 213.1 213.25 
3 2000-01-06 TELCO EQ 213.25 215.0 229.90 215.0 222.0 222.10 
4 2000-01-07 TELCO EQ 222.10 224.0 239.90 223.1 239.9 239.90 
 VWAP Volume Turnover Trades Deliverable Volume %Deliverble 
0 214.28 676126 1.448775e+13 NaN NaN NaN 
1 209.50 679215 1.422962e+13 NaN NaN NaN 
2 210.33 1120951 2.357684e+13 NaN NaN NaN 
3 225.29 1968998 4.435932e+13 NaN NaN NaN 
4 236.32 2199431 5.197636e+13 NaN NaN NaN 
(5306, 15)
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5306 entries, 0 to 5305
Data columns (total 15 columns):
# Column Non-Null Count Dtype 
--- ------ -------------- ----- 
0 Date 5306 non-null object 
1 Symbol 5306 non-null object 
2 Series 5306 non-null object 
3 Prev Close 5306 non-null float64
4 Open 5306 non-null float64
5 High 5306 non-null float64
6 Low 5306 non-null float64
7 Last 5306 non-null float64
8 Close 5306 non-null float64
9 VWAP 5306 non-null float64
10 Volume 5306 non-null int64 
11 Turnover 5306 non-null float64
12 Trades 2456 non-null float64
13 Deliverable Volume 4792 non-null float64
14 %Deliverble 4792 non-null float64
dtypes: float64(11), int64(1), object(3)
memory usage: 621.9+ KB
None
Date 0
Symbol 0
Series 0
Prev Close 0
Open 0
High 0
Low 0
Last 0
Close 0
VWAP 0
Volume 0
Turnover 0
Trades 2850
Deliverable Volume 514
%Deliverble 514
dtype: int64
0
0
0
 Prev Close Open High Low Last Close VWAP \
count 5306.00 5306.00 5306.00 5306.00 5306.00 5306.00 5306.00 
mean 409.43 410.15 417.12 402.18 409.45 409.45 409.76 
std 272.48 272.97 277.02 268.03 272.52 272.47 272.49 
min 58.80 58.00 60.70 57.55 58.75 58.80 59.24 
25% 174.60 174.76 178.82 171.01 174.72 174.60 175.18 
50% 377.25 378.90 384.75 372.60 377.52 377.25 378.46 
75% 523.15 523.48 530.80 515.91 523.49 523.15 523.72 
max 1365.15 1361.00 1382.00 1347.00 1362.00 1365.15 1362.15 
 Volume Turnover Trades Deliverable Volume %Deliverble 
count 5.306000e+03 5.306000e+03 2456.00 4792.00 4792.00 
mean 1.046560e+07 2.790772e+14 128439.98 2805962.22 0.36 
std 2.185034e+07 4.674351e+14 104954.58 3579713.03 0.16 
min 1.235100e+04 1.069384e+11 3434.00 12351.00 0.04 
25% 1.668994e+06 7.049025e+13 75478.25 646920.00 0.23 
50% 4.141648e+06 1.967418e+14 100034.00 1636751.50 0.36 
75% 8.706037e+06 3.175959e+14 142064.75 3761212.25 0.48 
max 3.905778e+08 9.365671e+15 1318669.00 73338482.00 1.00
Total Invested in Tata Motors = Rs 65977.3
Shares Owned of Tata Motors = 162
Average Investmentment of 1 share = Rs 407.27
nInvestment Result:
Net Unrealised Loss = Rs -17668.9



claude 
import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Import datasets
tata_motors = pd.read_csv("TATAMOTORS.csv")
tata_steel = pd.read_csv("TATASTEEL.csv")
tcs = pd.read_csv("TCS.csv")

# STEP 2: View data & check size
print(tata_motors.head())
print(tata_motors.shape)

# STEP 3: Datatypes & null values
print(tata_motors.info())
print(tata_motors.isna().sum())

# STEP 4: Check duplicates
print(tata_motors.duplicated().sum())
print(tata_steel.duplicated().sum())
print(tcs.duplicated().sum())

# STEP 5: Description
print(tata_motors.describe().round(2))

# STEP 6: Drop unwanted columns
columns_to_drop = ['Trades', 'Deliverable Volume', '%Deliverble']
tata_motors = tata_motors.drop(['Trades', 'Deliverable Volume', '%Deliverble'], axis=1)
tata_steel = tata_steel.drop(['Trades', 'Deliverable Volume', '%Deliverble'], axis=1)
tcs = tcs.drop(['Trades', 'Deliverable Volume', '%Deliverble'], axis=1)

# Convert Date columns
tata_motors['Date'] = pd.to_datetime(tata_motors['Date'])
tata_steel['Date'] = pd.to_datetime(tata_steel['Date'])
tcs['Date'] = pd.to_datetime(tcs['Date'])

# STEP 7: Price Comparison
plt.figure(figsize=(20, 7))
plt.plot(tata_motors['Date'], tata_motors['Open'], color='blue', label='Tata Motors')
plt.plot(tata_steel['Date'], tata_steel['Open'], color='grey', label='Tata Steel')
plt.plot(tcs['Date'], tcs['Open'], color='orange', label='TCS')
plt.title("Relation between Tata Motors, Tata Steel and TCS Price")
plt.xlabel("Year")
plt.ylabel("Price")
plt.legend()
plt.show()

# STEP 8: Volume Comparison
plt.figure(figsize=(20, 7))
plt.plot(tata_motors['Date'], tata_motors['Volume'], color='blue', label='Tata Motors')
plt.plot(tata_steel['Date'], tata_steel['Volume'], color='grey', label='Tata Steel')
plt.plot(tcs['Date'], tcs['Volume'], color='orange', label='TCS')
plt.title("Relation between Tata Motors, Tata Steel and TCS Volume")
plt.xlabel("Year")
plt.ylabel("Volume")
plt.legend()
plt.show()

# STEP 9: Return on Investment (ROI)
sumTM = 0
s1 = 0
for i in range(len(tata_motors)):
    if tata_motors.loc[i, 'Date'].day == 30:
        sumTM += tata_motors.loc[i, 'Close'] - tata_motors.loc[i, 'Open']
        s1 += 1

sumTS = 0
s2 = 0
for i in range(len(tata_steel)):
    if tata_steel.loc[i, 'Date'].day == 30:
        sumTS += tata_steel.loc[i, 'Close'] - tata_steel.loc[i, 'Open']
        s2 += 1

sumTCS = 0
s3 = 0
for i in range(len(tcs)):
    if tcs.loc[i, 'Date'].day == 30:
        sumTCS += tcs.loc[i, 'Close'] - tcs.loc[i, 'Open']
        s3 += 1

print(f"Tata Motors ROI: {sumTM}")
print(f"Tata Steel ROI: {sumTS}")
print(f"TCS ROI: {sumTCS}")

# Best investment
roi_dict = {'Tata Motors': sumTM, 'Tata Steel': sumTS, 'TCS': sumTCS}
best = max(roi_dict, key=roi_dict.get)
print(f"\nBest Investment: {best} with ROI = {roi_dict[best]}")