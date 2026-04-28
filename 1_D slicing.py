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