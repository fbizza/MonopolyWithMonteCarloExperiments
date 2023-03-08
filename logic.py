import random

board = ["Via!", "Vicolo Corto", "Probabilità_1", "Vicolo Stretto", "Tassa Patrimoniale", "Stazione SUD",
         "Bastioni Gran Sasso", "Imprevisti_1", "Viale Monterosa", "Viale Vesuvio", "Prigione/Transito", "Via Accademia",
         "Società Elettrica", "Corso Ateneo", "Piazza Università", "Stazione OVEST", "Via Verdi",
         "Probabilità_2", "Corso Raffaello", "Piazza Dante", "Parcheggio Gratuito", "Via Marco Polo", "Imprevisti_2",
         "Corso Magellano", "Largo Colombo", "Stazione NORD", "Viale Costantino", "Viale Traiano",
         "Società Acqua Potabile", "Piazza Giulio Cesare", "In Prigione!", "Via Roma", "Corso Impero",
         "Probabilità_3", "Largo Augusto", "Stazione EST", "Imprevisti_3", "Viale dei Giardini",
         "Tassa del Lusso", "Parco della Vittoria"]

num_rolls = 100000
go_to_jail = board.index("In Prigione!")
jail = board.index("Prigione/Transito")

def roll_dice():
    return random.randint(1, 6)

def update_position(current_position, dice_1, dice_2):
    if (current_position + dice_1 + dice_2) % len(board) == go_to_jail:
        return jail
    else:
        return (current_position + dice_1 + dice_2) % len(board)
