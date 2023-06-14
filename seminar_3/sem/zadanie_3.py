# Напишите программу для печати всех уникальных значений в словаре.
#
# Input:  [{"V": "S001"}, {"V": "S002"},
#          {"VI": "S001"}, {"VI": "S005"},
#          {"VII": " S005 "}, {" V ":" S009 "},
#          {" VIII ":" S007 "}]
#
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_dict = [{"V": "S001"}, {"V": "S002"},
             {"VI": "S001"}, {"VI": "S005"},
             {"VII": " S005 "}, {"V": " S009 "},
             {"VIII": " S007 "}]

# dictionary = {}
dictionary  = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": " S005 "}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
# list = set()
# for i in dictionary:
#     for j in i.keys():
#         list.add(i[j].strip())
# print(list)

print(set([list(i.values())[0].strip() for i in dictionary]))