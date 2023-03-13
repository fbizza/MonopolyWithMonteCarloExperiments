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

go_to_jail = board.index("In Prigione!")
jail = board.index("Prigione/Transito")
special_positions = [board.index("Imprevisti_1"), board.index("Imprevisti_2"), board.index("Imprevisti_3"),
                     board.index("Probabilità_1"), board.index("Probabilità_2"), board.index("Probabilità_3")]
special_cards = {"Via": 1/32, "Prigione": 2/32, "Accademia": 1/32, "Colombo": 1/32, "Vicolo Corto": 1/32,
                 "Stazione": 1/32, "Parco della Vittoria": 1/32, "Other": 8/32}

def roll_dice():
    return random.randint(1, 6)

def draw_a_special_card():
    cards = list(special_cards.keys())
    weights = list(special_cards.values())
    carta = random.choices(cards, weights=weights)[0]
    return carta

def update_position(current_position, dice_1, dice_2):
    if (current_position + dice_1 + dice_2) % len(board) == go_to_jail:
        return jail
    elif (current_position + dice_1 + dice_2) % len(board) in special_positions:
        card = draw_a_special_card()
        if card == "Via":
            return board.index("Via!")
        elif card == "Prigione":
            return jail
        elif card == "Accademia":
            return board.index("Via Accademia")
        elif card == "Colombo":
            return board.index("Largo Colombo")
        elif card == "Vicolo Corto":
            return board.index("Vicolo Corto")
        elif card == "Stazione":
            return board.index("Stazione NORD")
        elif card == "Parco della Vittoria":
            return board.index("Parco della Vittoria")
        elif card == "Other":
            return (current_position + dice_1 + dice_2) % len(board)
    else:
        return (current_position + dice_1 + dice_2) % len(board)

def color_plot(plot):
    plot[1].set_color('sienna')
    plot[3].set_color('sienna')
    plot[6].set_color('lightblue')
    plot[8].set_color('lightblue')
    plot[9].set_color('lightblue')
    plot[11].set_color('fuchsia')
    plot[13].set_color('fuchsia')
    plot[14].set_color('fuchsia')
    plot[16].set_color('orangered')
    plot[18].set_color('orangered')
    plot[19].set_color('orangered')
    plot[21].set_color('red')
    plot[23].set_color('red')
    plot[24].set_color('red')
    plot[26].set_color('yellow')
    plot[27].set_color('yellow')
    plot[29].set_color('yellow')
    plot[31].set_color('green')
    plot[32].set_color('green')
    plot[34].set_color('green')
    plot[37].set_color('blue')
    plot[39].set_color('blue')
    return plot

def simulate_game(num_rolls, num_pieces):
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
    frequencies = np.divide(counters, (num_rolls * num_pieces)/100)

    ytick_values = [frequencies[0], frequencies[10], frequencies[25]]

    plot = color_plot(plt.bar(positions, frequencies))
    plt.ylabel('Probability (%)')
    plt.xlabel('Position')
    plt.xticks(positions)
    plt.yticks(ytick_values)
    plt.show()

# Useful to explain why certain positions are more frequent
def plot_sum_of_2_dice(n):
    rolls = []
    num_iterations = n
    for i in range(num_iterations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        rolls.append(total)

    # Plot a histogram of the rolls
    plt.hist(rolls, bins=range(2, 14), align='left', rwidth=0.8)
    plt.xlabel('Sum')
    plt.ylabel('Frequency')
    plt.title(f'Rolling Two Dice {num_iterations} Times')
    plt.xticks(range(2, 13))
    plt.show()