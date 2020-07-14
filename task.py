import requests

response=requests.get('https://api.covid19api.com/summary')

data=response.json()
list_for_git=[]
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

def check_cases():
    string=input("Enter country name: ")
    string=string.lower()
    if string in saved_dic.keys():
     print("Total Confirmed cases for "+string+" : "+str(saved_dic[string]))
     check_cases()
    else:
        print("Not exxist")
        check_cases()
if __name__ == '__main__':
    check_cases()