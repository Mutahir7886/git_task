import requests

response=requests.get('https://api.covid19api.com/summary')

data=response.json()
my_data=data['Countries']
# print(my_data)
check=2
my_dic={}
saved_dic={}
for i in my_data:
    country_string=i['Country']
    country_string=country_string.lower()
    country_confirmed_cases=i['TotalConfirmed']
    my_dic[country_string]=country_confirmed_cases

saved_dic=my_dic
print(saved_dic)
def check():
    print("")
    check_input = input("Enter P for Prefix or S for Suffix or N for Normal Cases: ")
    if check_input == "S" or check_input=="s":
        suff()
        check()
    elif check_input == "P" or check_input=="p":
        preff()
        check()
    elif check_input=="N" or check_input=="n":
        normal_cases()
        check()
    else:
        print("no such functionality")

def suff():
    suffix_list = []
    string = input("Enter suffix keyword: ")
    string = string.lower()
    for item in saved_dic.keys():
        if item.endswith(string):
         suffix_list.append(item)
    print(suffix_list)
def preff():
    preff_list = []
    string = input("Enter prefix keyword: ")
    string = string.lower()
    for item in saved_dic.keys():
        if item.startswith(string):
         preff_list.append(item)
    print(preff_list)
def normal_cases():
    string=input("Enter country name: ")
    string=string.lower()
    if string in saved_dic.keys():
     print("Total Confirmed cases for "+string+" : "+str(saved_dic[string]))
     print("")
    else:
        print("Not exxist")
if __name__ == '__main__':
  check()