from covid import Covid

covid = Covid(source="worldometers")
data  = covid.get_data()

countries = covid.get_status_by_country_name("India") # extract by country
death     = countries["deaths"]                       # total deaths
confirmed = covid.get_total_confirmed_cases()         # total confirmed cases
