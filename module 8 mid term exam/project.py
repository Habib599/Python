class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        Star_Cinema._hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.seats = {}
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        s1 = (id, movie_name, time)
        self.__show_list.append(s1)
        self.seats[id] = []
        for row in range(self.rows):
            row_seats = []
            for col in range(self.cols):
                row_seats.append(0)
            self.seats[id].append(row_seats)

    def book_seats(self, id, sit_r_c):
        if id in self.seats:
            for row, col in sit_r_c:
                if 0 <= row < self.rows and 0 <= col < self.cols:
                    if self.seats[id][row][col] == 0:
                        self.seats[id][row][col] = 1
                        print(f"Seat ({row}, {col}) booked for show {id} ")
                    else:
                        print(f"Seat ({row}, {col}) booked for show {id} ")
                else:
                    print(f"Invalid seat")
        else:
            print(f"Show ID {id} not found.")

    def view_show_list(self):
        print()
        for show in self.__show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")
        print()
    def view_available_seats(self, id):
        if id in self.seats:
            print(f"Available seats for show {id}:")
            for row in range(self.rows):
                for col in range(self.cols):
                    if self.seats[id][row][col] == 0:
                        print("0,", end=" ")  
                    else:
                        print("1,", end=" ")  
                print()  
            print()  
        else:
            print(f"Show with ID {id} not found.")




hal = Hall(7,7,1)

hal.entry_show(1, "Jawan ", "09:00 AM")
hal.entry_show(2, "Pushpa 2", "12:00 PM")
hal.entry_show(3, "Mission Imposible 7", "03:00 PM")

while True:
    print('1: View All Show Today')
    print('2: View Available Seats')
    print('3: Book Ticket')
    print('4: Exit.')

    op=int(input("Enter Option: "))

    if op == 1:
        hal.view_show_list()

    elif op == 2:
        show_id = int(input("Enter show ID: "))
        hal.view_available_seats(show_id)
        
    elif op == 3:
        show_id = int(input("show ID: "))
        num_seats = int(input("Number of seats to book: "))
        sit_r_c = []
        for i in range(num_seats):
            row = int(input(f"Enter seat row : "))
            col = int(input(f"Enter seat col : "))
            sit_r_c.append((row, col))
        hal.book_seats(show_id, sit_r_c)

    elif op == 4:
        break
    else:
        print("Invalid choice.")
