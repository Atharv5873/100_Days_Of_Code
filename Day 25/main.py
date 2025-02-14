import csv,pandas

# # with open("Day 25\weather_data.csv") as data_file:
# #     data=csv.reader(data_file)
# #     temp=[]
# #     for  row in data: 
# #         if row[1]!='temp':
# #             temp.append(int(row[1]))
        
# # print(temp)

# data=pandas.read_csv("Day 25\weather_data.csv")

# data_dict=data.to_dict()
# temp_list=data["temp"].to_list()

# avg_temp=sum(temp_list)/len(temp_list)

# avg_temp=data["temp"].mean()
# print(avg_temp)
# print(f"The max temperate recorded was {data["temp"].max()}")

# print(data[data.day=="Monday"])
# print(data[data.temp==data.temp.max()])

data=pandas.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squ_count=len(data[data["Primary Fur Color"] == "Gray"])
cinn_squ_count=len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squ_count=len(data[data["Primary Fur Color"] == "Black"])

data_dict ={
    "Fur Color":["Grey","Cinnamon","Black"],
    "Count":[grey_squ_count,cinn_squ_count,black_squ_count]
}

df=pandas.DataFrame(data_dict)
df.to_csv("Day 25/squirrel count.csv")
