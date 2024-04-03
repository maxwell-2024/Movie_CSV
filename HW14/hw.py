import json
import csv
import os
from ganres_data import ganres
from film_data_file import film_data

                                        #Step_1

ganres_to_dict = json.loads(ganres)
#print(type(ganres_to_dict),ganres_to_dict)
                                        #Step_2-5

for target_list in ganres_to_dict["results"]:
    #print(target_list)
    for name in target_list:
        genre_name = target_list["genre"]
        dict_name = str(genre_name)       
        #print(dict_name)
        os.makedirs(dict_name, exist_ok = True)
        file_name = os.path.join(dict_name, f"{dict_name}.csv")
        file_obj = open(file_name, "w")
        csv_obj = csv.writer(file_obj)
        csv_obj.writerow(["Title", "Year","Rating","Type","Ganres"])

        for g in film_data:
            for genre in g["gen"]:
                genre_list = [na["genre"] for na in g["gen"]]
                genre_str = ", ".join(genre_list)
                #print(genre_list, genre_str)
                
                if genre_name in genre_list:
                        title = g["title"].replace("Ô","O")
                        elem_list = [title, g["year"], g["rating"], g["type"], genre_str]
                        csv_obj.writerow(elem_list)
                        #print(elem_list)
                        break
                

    
