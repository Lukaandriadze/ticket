class Ticket:
    def __init__(self, film_name, ticket_price, count, language="Geo"):
        self.film_name = film_name
        self.ticket_price = ticket_price
        self.count = count
        self.language = language

    def __str__(self):
        return f"{self.film_name}, {self.ticket_price}, {self.count}, {self.language}"

class User(Ticket):
    def __init__(self, username, balance=0):
        super().__init__("Default Film", 0, 0, "Default Language")  # Default values for Ticket
        self.username = username
        self.balance = balance

    def __str__(self):
        return f"გამარჯობა {self.username}, თქვენ ანგარიშზე არის {self.balance}."

    def deposit(self, money):
        if (self.count * 10) <= money:
            print(f"თანხა საკმარისია ბილეთის საყიდლათ.")
        else:
            print(f"ეს თანხა არ არის საკმარისი ბილეთის საყიდლათ. თუ შეიტანთ {(self.count * 10)-money} ლარს, თქვენ შეძლებთ იყიდოთ ეს ბილეთები.")

name = input("გამარჯობა, შეიყვანეთ თქვენი სახელი: ")
film = input(f"{name}, შეიყვანე ფილმის სახელი, რომელიც გსურთ: ")
price = "10 ლარი"
count = int(input("შეიყვანეთ ბილეთების რაოდენობა: "))
money = int(input("რა თანხის შეტანა გსურთ ანგარიშზე: "))
user = User(name)
ticket = Ticket(film, price, count, "ენა:Geo")
print(f"ბილეთის დეტალები:ფილმი:{film},ერთიბილეთის ფასი {price},რაოდენობა {count},ენა:Geo")
user.deposit(money)


