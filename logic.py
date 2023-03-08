import random

board = ["Via!", "Vicolo Corto", "Probabilità_1", "Vicolo Stretto", "Tassa Patrimoniale", "Stazione SUD",
         "Bastioni Gran Sasso", "Imprevisti_1", "Viale Monterosa", "Viale Vesuvio", "Prigione/Transito", "Via Accademia",
         "Società Elettrica", "Corso Ateneo", "Piazza Università", "Stazione OVEST", "Via Verdi",
         "Probabilità_2", "Corso Raffaello", "Piazza Dante", "Parcheggio Gratuito", "Via Marco Polo", "Imprevisti_2",
         "Corso Magellano", "Largo Colombo", "Stazione NORD", "Viale Costantino", "Viale Traiano",
         "Società Acqua Potabile", "Piazza Giulio Cesare", "In Prigione!", "Via Roma", "Corso Impero",
         "Probabilità_3", "Largo Augusto", "Stazione EST", "Imprevisti_3", "Viale dei Giardini",
         "Tassa del Lusso", "Parco della Vittoria"]

num_rolls = 1000
go_to_jail = board.index("In Prigione!")
jail = board.index("Prigione/Transito")

def roll_dice():
    return random.randint(1, 6)

def update_position(current_position, dice_1, dice_2):
    if (current_position + dice_1 + dice_2) % len(board) == go_to_jail:
        return jail
    else:
        return (current_position + dice_1 + dice_2) % len(board)


# To store how many times positions in the board are visited
histogram = {idx: 0 for idx in range(len(board))}

# Initialize values for starting the game
current_position = 0
in_jail = False
jail_counter = 0

# Main loop that simulates the game of a single piece
for i in range(num_rolls):
    if in_jail and jail_counter < 3:
        dice_1 = roll_dice()
        dice_2 = roll_dice()
        if dice_1 == dice_2:  # Go out of jail rule
            in_jail = False
            jail_counter = 0
            current_position = update_position(current_position, dice_1, dice_2)
        else:
            jail_counter += 1
    else:
        dice_1 = roll_dice()
        dice_2 = roll_dice()
        current_position = update_position(current_position, dice_1, dice_2)

    if current_position == go_to_jail:
        in_jail = True
        current_position == jail

    histogram[current_position] += 1

