import random
import numpy as np
import matplotlib.pyplot as plt

board = ["Via!", "Vicolo Corto", "Probabilità_1", "Vicolo Stretto", "Tassa Patrimoniale", "Stazione SUD",
         "Bastioni Gran Sasso", "Imprevisti_1", "Viale Monterosa", "Viale Vesuvio", "Prigione/Transito", "Via Accademia",
         "Società Elettrica", "Corso Ateneo", "Piazza Università", "Stazione OVEST", "Via Verdi",
         "Probabilità_2", "Corso Raffaello", "Piazza Dante", "Parcheggio Gratuito", "Via Marco Polo", "Imprevisti_2",
         "Corso Magellano", "Largo Colombo", "Stazione NORD", "Viale Costantino", "Viale Traiano",
         "Società Acqua Potabile", "Piazza Giulio Cesare", "In Prigione!", "Via Roma", "Corso Impero",
         "Probabilità_3", "Largo Augusto", "Stazione EST", "Imprevisti_3", "Viale dei Giardini",
         "Tassa del Lusso", "Parco della Vittoria"]


num_pieces = 9000  # The number of pieces to simulate
num_rolls = 30
go_to_jail = board.index("In Prigione!")
jail = board.index("Prigione/Transito")


def roll_dice():
    return random.randint(1, 6)

def update_position(current_position, dice_1, dice_2):
    if (current_position + dice_1 + dice_2) % len(board) == go_to_jail:
        return jail
    else:
        return (current_position + dice_1 + dice_2) % len(board)


# To store how many times positions in the board are visited for each piece
local_histograms = [{idx: 0 for idx in range(len(board))} for i in range(num_pieces)]

# Initialize values to start the game
current_positions = [0] * num_pieces
in_jails = [False] * num_pieces
jail_counters = [0] * num_pieces

# Main loop that simulates the game
for i in range(num_rolls):
    for j in range(num_pieces):
        if in_jails[j] and jail_counters[j] < 3:
            dice_1 = roll_dice()
            dice_2 = roll_dice()
            if dice_1 == dice_2:  # Go out of jail rule
                in_jails[j] = False
                jail_counters[j] = 0
                current_positions[j] = update_position(current_positions[j], dice_1, dice_2)
            else:
                jail_counters[j] += 1
        else:
            dice_1 = roll_dice()
            dice_2 = roll_dice()
            current_positions[j] = update_position(current_positions[j], dice_1, dice_2)

        if current_positions[j] == go_to_jail:
            in_jails[j] = True
            current_positions[j] == jail

        local_histograms[j][current_positions[j]] += 1

# Combine the histograms of each piece to create a global one
global_histogram = {}
for histogram in local_histograms:
    for position, count in histogram.items():
        if position in global_histogram:
            global_histogram[position] += count
        else:
            global_histogram[position] = count

positions = list(global_histogram.keys())
counters = list(global_histogram.values())
frequencies = np.divide(counters, (num_rolls * num_pieces))

plt.bar(positions, frequencies)
plt.ylabel('Probability')
plt.xlabel('Position')
plt.xticks(positions)
plt.show()
