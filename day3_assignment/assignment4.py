'''A small ticket-booking system needs to treck of how many seats have been booked so far, using a global variable.

Create a global variable total_seats_books initialized to 0.
Write a function book_seats(n) that:
    adds n to total_seats_booked using the global keyword
    prints a message like: "booked 3 seat(s). total booked so far: 3"
Write a second function reset_bookings() that resets total_seats_booked back to 0 (this also needs the globle keyword).

sample calls and expected behaviour:

book_seats(3)
book_seats(5)
reset_bookings()
book_seats(2)

'''


# Write your code here

total_seats_booked = 0

def book_seats(n):
    global total_seats_booked
    total_seats_booked += n
    print(f"Bokked {n} seat(s). Total booked so far: {total_seats_booked}")


def reset_bookings():
    global total_seats_booked
    total_seats_booked = 0
    print(f"Booking have been reset.")


# --- test your functions below ---
book_seats(3)
book_seats(5)
reset_bookings()
book_seats(2)