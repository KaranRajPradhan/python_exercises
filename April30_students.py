# class Human(object):
#     def __init__(self, name):
#         self.name = name
    
#     def greeting(self):
#         print(f"Hello, my name is {self.name}.")

# karan = Human("Karan")
# print(karan.name)
# karan.greeting()

# alfrin = Human("Alfrin")
# alfrin.greeting()



# #######################################################################################



# class Series(object):
#     def __init__(self, title):
#         self.title = title
#         self.seasons = None
#         self.start_date = None

#     def get_show_date(self, current_date, episode_number):
#         show_date = self.start_date + (7 * (episode_number - 1))
#         print(show_date)
#         days_left = show_date - current_date
#         if days_left < 0:
#             print(f"Show already aired {days_left * -1} day(s) ago")
#         else:
#             print(f"You have {days_left} days left until the episode no. {episode_number} airs")
        
# got = Series("Game of Thrones")
# print(got.title)
# got.seasons = 8

# got.start_date = 14
# got.get_show_date(15, 4)



# #######################################################################################



# class Song(object):
#     def __init__(self,lyrics):
#         self.lyrics = lyrics
    
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)

# happy_bday = Song(["Happy Birthday to you",
#                     "I dont want to get sued",
#                     "So I'll stop right there"])
# bulls_on_parade = Song(["They rally around the family",
#                         "With pockets full of shells"])

# happy_bday.sing_me_a_song()
# bulls_on_parade.sing_me_a_song()

# #######################################################################################



class Book(object):
    def __init__(self, title, author, genre, pages, year, price):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.year = year
        self.price = price
        self.pages_left = None
        self.time_left = None
    
    def get_pages_left(self, pages_read):
        self.pages_left = self.pages - pages_read
        return self.pages_left
    
    def get_time_left(self, read_speed, pages_read):
        self.time_left = self.get_pages_left(pages_read) / read_speed
        return self.time_left

diaspora = Book("Diaspora", "Greg Egan", "Science Fiction", 345, 2008, 395)

print(f"Pages left is {diaspora.get_pages_left(255)}")
# diaspora.get_pages_left(255)
print(f"Time left is {diaspora.get_time_left(25, 255)}")
# diaspora.get_time_left(25, 255)