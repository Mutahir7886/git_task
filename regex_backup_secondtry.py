import re
import re

# string='Maverick X3 (Base, X ds, X rc Turbo and X mr Turbo models), Maverick X3 MAX (Base and X ds models)'
# string = 'Defender and Defender MAX 2017 & prior'
# string='Defender, Defender MAX (2019 and prior)'
# string = 'G2 (except 6x6 models) et G2S, Commander, Commander MAX, Defender, Defender MAX, Maverick X3, Maverick X3 MAX, Maverick, Maverick MAX, Maverick Trail, Maverick Sport, Maverick Sport MAX'
# string='Commander, Commander MAX, Maverick, Maverick MAX, Maverick X3, Maverick X3 MAX, Defender, Defender MAX, Maverick Trail, Maverick Sport, Maverick Sport MAX'
# string='Maverick X3 & Maverick X3 MAX (64" models)'
string = 'Commander MAX, Maverick MAX, Maverick MAX X rs 2015 & prior'
string='Defender 2018 & prior'
string='Defender, Defender MAX (2019 & prior)'
string='Maverick X3 & Maverick X3 MAX (Base & X ds models)'
detail = []
checkkk = string.split(",")
if "&" in string and " and" in string:
 abc = string.split("and")
 detail = abc
elif "&" in string:
  if "," in string and "&" in string:
      abc = string.split(",")
      detail = abc
  else:
      abc = string.split("&",1)
      detail = abc
elif "," in string and "and" in string:
        if "(" in checkkk[0]:
            if '(' in string:
                first_split = string.split(")", 1)
                abc = first_split[1].strip(",").split(",")
                detail = abc
                detail.append(first_split[0] + ")")
                if "(" in detail[1]:
                    detail = detail
                else:
                    detail = detail[1:]
            else:
                abc = string.split(",")
                detail = abc

        else:
            abc = string.split(",")
            detail = abc

else:
        if "(" in checkkk[0]:
            if '(' in string:
                first_split = string.split(")", 1)
                abc = first_split[1].strip(",").split(",")
                detail = abc
                detail.append(first_split[0] + ")")

                if "(" in detail[1]:
                    detail = detail
                else:
                    detail = detail[1:]

            else:
                abc = string.split(",")
                detail = abc

        else:
            abc = string.split(",")
            detail = abc


print(detail)
print(len(detail))
