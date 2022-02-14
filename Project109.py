import pandas as pd
import csv
import statistics
df=pd.read_csv("C:/Users/dell/Desktop/Python/folderA/datas/StudentsPerformance.csv")
heightList=df["reading score"].to_list()
heightMean=statistics.mean(heightList)
heightMedian=statistics.median(heightList)
heightMode=statistics.mode(heightList)
print("Mean,median,mode of score is {},{}and{}".format(heightMean,heightMedian,heightMode))
heightStdDev=statistics.stdev(heightList)
heightfsss,heightfsse=heightMean-heightStdDev,heightMean+heightStdDev
heightssss,heightssse=heightMean-(2*heightStdDev),heightMean+(2*heightStdDev)
heighttsss,heighttsse=heightMean-(3*heightStdDev),heightMean+(3*heightStdDev)

heightListOfsd=[result for result in heightList if result>heightfsss and result<heightfsse]
heightListOfssd=[result for result in heightList if result>heightssss and result<heightssse]
heightListOftsd=[result for result in heightList if result>heighttsss and result<heighttsse]

print("{}% data for line lying within first std. dev.".format(len(heightListOfsd)*100.0/len(heightList)))
print("{}% data for line lying within second std. dev.".format(len(heightListOfssd)*100.0/len(heightList)))
print("{}% data for line lying within third std. dev.".format(len(heightListOftsd)*100.0/len(heightList)))
