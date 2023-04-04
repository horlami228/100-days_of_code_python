"""A dictionary inside a dictionary"""

travel_log = {"Lagos": {"Places_visited": ["Ikorodu", "Sango", "Ajegunle", "Mainland bridge"], "Total_visits": 4},
              "Germany": {"Places_visited": ["Berlin", "Hamburg", "Munich", "Dortmund"], "Total_visits": 4}}

"""A dictionary inside a list"""
travel_logs = [
    {"Country": "Lagos",
    "Places_visited": ["Ikorodu", "Sango", "Ajegunle", "Mainland bridge"], 
    "Total_visits": 5},

    {"Country": "Germany", 
    "Places_visited": ["Berlin", "Hamburg", "Munich", "Dortmund"], 
    "Total_visits": 2}
]

def add_new_country(Country, total_visit, places_visited):
    new_dic = {}
    new_dic["Country"] = Country
    new_dic["Places_visited"] = places_visited
    new_dic["Total_visits"] = total_visit
    travel_logs.append(new_dic)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_logs[2])