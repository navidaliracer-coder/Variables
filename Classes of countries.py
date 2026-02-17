class India():
    def capital(self):
        print("New delhi is the cpaital of india")
    
    def language(self):
        print("Hindi is the most spoken language in india")

    def type(self):
        print("india is a developing country")

class USA():
    def capital(self):
        print("Washington DC is the cpaital of America")
    
    def language(self):
        print("English is the most spoken language in America")

    def type(self):
        print("America is a developed country")

obj_ind = India()
obj_USA = USA()

for country in (obj_ind, obj_USA):
    country.capital()
    country.language()
    country.type()