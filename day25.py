# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
# #
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# # # print(data["temp"])
# # data_dict = data.to_dict()
# # print(data_dict)
# # tempt_list = data["temp"].to_list()
# # noob = data.condition
# # print(noob)
# # print(data[data.day == "Monday"])
#
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # convert = monday.temp * 1.8 + 32
# #
# # print(convert)
# # data_dict = {
# #     "students": ["amy", "james", "angela"],
# #     "scores": [76, 56, 65]
# # }
# # dataz = pandas.DataFrame(data_dict)
# # print(data)
#
#
# with open("squirrel_count.csv", mode="r") as file:
#     dataz = pandas.DataFrame(file)
#     print(dataz)

import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])


print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinammon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")