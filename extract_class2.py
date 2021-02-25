# by Kami Bigdely
# Extract class
class Hulu_Copy():
    def __init__(self,first_names, last_names, birth_year, movies, emails):
        self.first_names = ['elizabeth', 'Jim']
        self.last_names = ['debicki', 'Carrey']
        self.birth_year = [1990, 1962]
        self.movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
            ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
        self.emails = ['deb@makeschool.com', 'jim@makeschool.com']

    def send_hiring_email(self, email):
        print("email sent to: ", email)
            
    def send_email(self, emails, birth_year):
        for i, value in enumerate(emails):
            if birth_year[i] > 1985:
                print(first_names[i], last_names[i])
                print('Movies Played: ', end='')
                for m in movies[i]:
                    print(m, end=', ')
                print()
                send_hiring_email(value)

l=Hulu_Copy('liz')
l.send_hiring_email('liz')
emails = ['deb@makeschool.com', 'jim@makeschool.com']
l.send_email(emails)

