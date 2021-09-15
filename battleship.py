import pygame
from random import randint, choice

# Dimensione di ogni campo di battaglia
BATTLEFIELD_WIDTH = 10      # max 26 x 26, altimenti dopo finisco le lettere dell'alfabeto per identificare le celle orizzontali, e il sistema passa ai successivi caratteri ASCII
BATTLEFIELD_HEIGHT = 10     # max 26 x 26, come sopra

# Array contenente quante barche e di che dimensione per ogni tipo per ogni campo di battaglia:
#   [q.tà , lunghezza]
#   Elemento di esempio: [4, 1] signifca 4 navi da 1 cella
#                        [2, 3] signifca 2 navi da 3 celle
BATTLEFIELD_BOATS_NUM_AND_SIZE = [[4, 1], [3, 2], [2, 3], [1, 4]]

# Dimensioni dell'area grafica di pygame per disegnare i campi di battaglia
GRAPHIC_CELL_SIZE = 40                      # dimensione della cella nella rappresentazione grafica con pygame
GRAPHIC_DISTANCE_BETWEEN_FIELDS = 100       # distanza tra i due campi di battaglia (computer a sx e user a dx)
GRAPHIC_MARGIN_TOP = 50                     # distanza dei campi di battagla dal bordo superiore
GRAPHIC_MARGIN_BOTTOM = 50                  # distanza dei campi di battagla dal bordo inferiore
GRAPHIC_MARGIN_LEFT = 50                    # distanza dei campi di battagla dal bordo sinistro
GRAPHIC_MARGIN_RIGHT = 50                   # distanza dei campi di battagla dal bordo destro

# Colori degli elementi dei campi di battaglia
# Scelta colore RGB: https://www.w3schools.com/colors/colors_picker.asp
BATTLEFIELD_BACKGROUND_COLOR = (255, 255, 255)              # Sfondo

GRAPHIC_BATTLEFIELD_COMPUTER_GRID_COLOR = (47, 47, 40)      # Colore della griglia del campo di battaglia del computer
GRAPHIC_BATTLEFIELD_USER_GRID_COLOR = (0, 0, 102)           # Colore della griglia del campo di battaglia dello user

BOAT_INNER_COLOR = (47, 198, 64)                            # Colore dell'interno delle navi
BOAT_BORDER_COLOR = (6, 71, 13)                             # Colore del bordo delle navi
BOAT_BORDER_RADIUS = 5                                      # Raggio degli spigoli delle navi (0: spigolo)
BOAT_BORDER_WIDTH = 2                                       # Spessore dei bordi delle navi
SHOT_COLOR = (0, 102, 255)                                  # Colore di un colpo che NON ha colpito una barca
SHOT_HIT_COLOR = (204, 51, 0)                               # Colore di un colpo che ha colpito una barca
BOAT_HIT_COLOR = (255, 0, 0)                                # Colore della croce su una casella di una barca colpita
BOAT_SUNK_INNER_COLOR = (204, 51, 0)                        # Colore dell'interno di una nave affondata
BOAT_SUNK_BORDER_COLOR = (128, 0, 0)                        # Colore del bordo di una nave affondata

TEXT_FONT = "comicsansms"   # font per scritte

DEBUG = False       # Usata per il debug del programma, mettere a False quando definitiva. Se True scrive sulla console messaggi di debug

# Classe campo di battaglia (che contiene navi e colpi sparati)
class Battlefield:
    def __init__(self, title, width, height, screen, graph_origin_x, graph_origin_y, graph_cell_size):
        self.title = title                      # Titolo (nome) del campo di battaglia
        self.width = width                      # Larghezza del campo di battaglia
        self.height = height                    # Altezza del campo di battaglia
        self.screen = screen                    # Variabile pygame contenente il display (area grafica)
        self.graph_origin_x = graph_origin_x    # Posizione x dell'origine del campo di battaglia nell'area grafica
        self.graph_origin_y = graph_origin_y    # Posizione y dell'origine del campo di battaglia nell'area grafica
        self.graph_cell_size = graph_cell_size  # Dimensione del lato di ogni singola cella nell'area grafica
        self.boats = []                         # Lista di navi nel campo di battaglia
        self.shots = []                         # Lista di spari subiti dal campo di battaglia

    # Popola il campo di battaglia con le navi
    # list_num_and_size è un array contenente tanti elementi quanti sono i tipi e quantità di barche da creare
    # Elemento di esempio: [3, 2] signifca 3 navi di lunghezza 2
    def populate_field(self, list_num_and_size):
        for e in list_num_and_size:
            for i in range(e[0]):
                # creo una barca casuale di lunghezza e[1] e la aggiungo alla lista di barche nel campo di battaglia
                self.boats.append(self.create_random_boat(e[1]))
        if DEBUG:
            # Stampo la lsita di barche create
            print("#### Battlefield: " + self.title + " ####")
            for boat in self.boats:
                print("Boat: p1:(" + str(boat.p1.x) + "; " +str(boat.p1.y) + ") - p2:(" + str(boat.p2.x) + "; " +str(boat.p2.y) + ") - length:" + str(boat.length) + " - " + ("horizontal" if boat.is_horizontal else "vertical"))
            print()

    # Crea una barca in posizione ed orientamento casuale, di lunghezza length
    # Evita la sovrapposizione con altre barche già esistenti
    # length:   lunghezza della barca da creare
    def create_random_boat(self, length):
        length = length-1   # sottraggo 1 perchè gli indici partono da 0
        # scelgo l'orientamento casualmente
        orientation_choices = True, False
        orientation_horiz = choice(orientation_choices)
        # in base all'orientamento casuale scelto imposto la coordinata massima in x e y per non avere la barca che fuoriesca dal campo di battaglia
        if orientation_horiz:
            max_pos_x = self.width-1 - length
            max_pos_y = self.height-1
        else:
            max_pos_x = self.width-1 
            max_pos_y = self.height-1 - length
        
        # verifico che la barca non sia sovrapposta ad altre
        is_collision = True
        while is_collision:
            # genero la barca della lunghezza length richiesta in posizione e orientamento casuale finchè non evita di essere sovrapposta ad altre già presenti
            boat = Boat(Coord(randint(0, max_pos_x), randint(0, max_pos_y)), orientation_horiz, length)
            is_collision = self.check_collision(boat)
        return boat

    # Verifica se la barca passata è sovrapposta ad altre esistenti
    def check_collision(self, boat):
        for b in self.boats:
            # per ogni barca esistente nel campo di battaglia verifico se si sovrappone a quella passata
            collision = self.intersect(boat.p1, boat.p2, b.p1, b.p2)
            if collision:
                return True
        return False

    ############################# Algoritmo per verifica intersezione tra segmenti #############################
    # Usato algoritmo in: https://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
    def ccw(self, A,B,C):
        return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

    def intersect(self, A,B,C,D):
        return self.ccw(A,C,D) != self.ccw(B,C,D) and self.ccw(A,B,C) != self.ccw(A,B,D)
    ############################################################################################################

    # Funzione che verifica se shot è già contenuto in self.shots (significa che si è già sparato in questa posizione)
    def already_shooted(self, shot):
        for s in self.shots:
            if s.x == shot.x and s.y == shot.y:
                return True
        return False

    # Funzione che riceve un colpo sparato dall'avversario nel campo di battaglia
    def get_shot(self, shot):
        if not self.already_shooted(shot):
            # se il colpo non era già stato sparato allora lo aggiungo alla lista dei colpi ricevuti dal campo di battaglia
            self.shots.append(shot)
            for boat in self.boats:
                # per ogni barca nel campo di battaglia...
                boat.get_shot(shot)

    # Funzione che verifica se tutte le barche del campo di battaglia sono state affondate. Restituisce:
    # True:     se tutte le barche sono state affondate
    # False:    se ci sono nel campo di battaglia ancora barche non affondate
    # Serve per capire se la partita è terminata
    def are_all_boats_sunk(self):
        all_sunk = True
        for boat in self.boats:
            if boat.sunk != True:
                all_sunk = False
        return all_sunk

    ########################## Funzioni per la gestione dell'area grafica del campo di battaglia ##########################

    # Funzione che, date le coordinate grafiche passate di un punto determina le coordinate nel campo di battaglia
    # Se le coordinate grafiche sono fuori dal campo di battaglia la funzione restituisce None
    # Serve per convertire le coordinate grafiche (in cui si è cliccato col mouse) nelle coordinate del campo di battaglia
    def coord_from_graph_coord(self, graph_coord):
        # ricavo le coordinate grafiche del campo di battaglia
        graph_battlefield = pygame.Rect(self.graph_origin_x, 
            self.graph_origin_y, 
            self.width * self.graph_cell_size, 
            self.height * self.graph_cell_size)
        # Verifico se il punto graph_coord passato è all'interno del campo di battaglia...
        if graph_battlefield.collidepoint(graph_coord):
            # ... il punto graph_coord è interno al campo di battaglia
            graph_x, graph_y = graph_coord      # ricavo le coord grafiche x e y del punto graph_coord
            # resistuisco il punto nelle coordinate del campo di battaglia come classe Coord
            return Coord(
                (graph_x-self.graph_origin_x)//self.graph_cell_size , 
                (graph_y-self.graph_origin_y)//self.graph_cell_size
            )
        else:
            # ... il punto graph_coord è esterno
            return None


    # Funzione per scrivere sullo schermo un dato testo nella posizione, dimensione e colore passati:
    # text:         testo da scrivere
    # pos:          coordinate del punto centrale in cui scrivere i testo
    # text_height:  altezza del testo
    # text_color:   colore RGB del testo
    def print_to_screen(self, text, pos, text_height, text_color):
        font = pygame.font.SysFont(TEXT_FONT, text_height)
        img = font.render(text, True, text_color)
        text_rect = img.get_rect()
        text_rect.center = pos
        self.screen.blit(img, text_rect)

    # Funzione per ricavare la coordinata x (ascissa) da scrivere a monitor
    # in debug per le ascisse scrivo il numero della cella partendo da 0
    # NON in debug per le ascisse scrivo la lettera della cella partendo da "A"
    def get_ascissa_to_print(self, x):
        if DEBUG:
            return str(x)
        else:
            # se non si è in debug trasformo in lettera la x dal codice ASCII sapendo che la A è chr(65)
            return chr(65 + x)

    # Funzione per ricavare la coordinata y (ordinata) da scrivere a monitor
    # in debug per le ordinate scrivo il numero della cella partendo da 0
    # NON in debug per le ordinate scrivo il numero della cella partendo da 1
    def get_ordinata_to_print(self, x):
        if DEBUG:
            return str(x)
        else:
            # se non si è in debug trasformo in lettera la x dal codice ASCII sapendo che la A è chr(65)
            return str(x+1)

    # Funzione per disegnare il campo di battaglia sullo schermo passando alla funzione:
    # grid_color:                   colore dei bordi di ogni cella
    # hide_unsunk_boat:             True per nascondere le navi non affondate (serve per visualizzare il campo di battaglia del computer)
    #                               False per mostrarle tutte (serve per visualizzare il campo di battaglia dello user)
    def draw_field(self, grid_color, hide_unsunk_boat):
        # scrivo le lettere identificative delle coordinate delle celle e ne disegno i bordi
        for i in range(self.width):
            # Per ogni cella in ascissa...
            # ricavo la coordinata x in coordinate grafiche
            x = self.graph_origin_x + self.graph_cell_size * i
            self.print_to_screen(self.get_ascissa_to_print(i), (x+self.graph_cell_size/2, self.graph_origin_y-10), 10, grid_color)
            for j in range(self.height):
                # Per ogni cella in ordinata...
                # ricavo la coordinata y in coordinate grafiche
                y = self.graph_origin_y + self.graph_cell_size * j
                # scrivo la coordinata y della cella, solo quando sono alla prima colonna
                if i==0:
                    self.print_to_screen(self.get_ordinata_to_print(j), (self.graph_origin_x-10, y+self.graph_cell_size/2), 10, grid_color)

                # disegno il bordo della cella i,j
                pygame.draw.rect(self.screen, 
                    grid_color, 
                    pygame.Rect(x, y, self.graph_cell_size, self.graph_cell_size), 
                    1,      # Spessore dei bordi della griglia
                    0)      # Nessun raccordo degli spigoli

        # scrivo sopra alla griglia il titolo del campo di battaglia
        self.print_to_screen(self.title, 
            (self.graph_origin_x + (self.width * self.graph_cell_size)/2, self.graph_origin_y/2 - 10), 
            24, grid_color)

        # disegno ogni colpo ricevuto dal campo di battaglia
        # se il colpo avesse colpito una barca sarà poi sovrascritto dalla barca col simbolo del colpo andato a segno
        for shot in self.shots:
            graph_shot_x = self.graph_origin_x + shot.x * self.graph_cell_size + self.graph_cell_size/2
            graph_shot_y = self.graph_origin_y + shot.y * self.graph_cell_size + self.graph_cell_size/2
            pygame.draw.circle(self.screen, SHOT_COLOR, (graph_shot_x, graph_shot_y), self.graph_cell_size/3)

        # disegno ogni nave presente nel campo di battaglia
        for boat in self.boats:
            # Ricavo le coordinate grafiche della barca e la sua larghezza e altezza in coordinate grafiche
            graph_boat_p1_x = self.graph_origin_x + boat.p1.x * self.graph_cell_size
            graph_boat_p1_y = self.graph_origin_y + boat.p1.y * self.graph_cell_size
            graph_boat_width = (boat.p2.x - boat.p1.x) * self.graph_cell_size + self.graph_cell_size
            graph_boat_heigth = (boat.p2.y - boat.p1.y) * self.graph_cell_size + self.graph_cell_size
            # colore riempimento e bordo della barca...
            if boat.sunk:
                # ... se la barca è affondata
                inner_color = BOAT_SUNK_INNER_COLOR
                border_color = BOAT_SUNK_BORDER_COLOR
            else:
                # ... se la barca NON è affondata 
                inner_color = BOAT_INNER_COLOR
                border_color = BOAT_BORDER_COLOR
            
            # disegno la barca a schermo solo se è affondata o se non deve essere nascosta quando ancora a galla
            if boat.sunk or not hide_unsunk_boat:
                # interno barca
                pygame.draw.rect(self.screen, 
                    inner_color, 
                    pygame.Rect(graph_boat_p1_x, graph_boat_p1_y, graph_boat_width, graph_boat_heigth), 0, BOAT_BORDER_RADIUS)
                # contorno barca
                pygame.draw.rect(self.screen, 
                    border_color, 
                    pygame.Rect(graph_boat_p1_x, graph_boat_p1_y, graph_boat_width, graph_boat_heigth), BOAT_BORDER_WIDTH, BOAT_BORDER_RADIUS)
        
            # colpi a segno sulla barca
            for shot in boat.shots_received:
                # pallino che rappresenta il colpo andato a segno
                graph_shot_x = self.graph_origin_x + shot.x * self.graph_cell_size + self.graph_cell_size/2
                graph_shot_y = self.graph_origin_y + shot.y * self.graph_cell_size + self.graph_cell_size/2
                pygame.draw.circle(screen, SHOT_HIT_COLOR, (graph_shot_x, graph_shot_y), self.graph_cell_size/3)

                # croce che rappresenta la cella di una barca colpita
                shot_p1_x = self.graph_origin_x + shot.x * self.graph_cell_size
                shot_p1_y = self.graph_origin_y + shot.y * self.graph_cell_size
                shot_p2_x = self.graph_origin_x + shot.x * self.graph_cell_size + self.graph_cell_size
                shot_p2_y = self.graph_origin_y + shot.y * self.graph_cell_size + self.graph_cell_size
                pygame.draw.line(screen, BOAT_HIT_COLOR, (shot_p1_x, shot_p1_y), (shot_p2_x, shot_p2_y), 3)
                pygame.draw.line(screen, BOAT_HIT_COLOR, (shot_p2_x, shot_p1_y), (shot_p1_x, shot_p2_y), 3)
        

# Coordinate di un punto
class Coord:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

# Sparo: contiene le coordinate del punto in cui si è sparato e se ha colpito qualcosa
class Shot(Coord):
    def __init__(self):
        super().__init__()
        self.hit = False                        # True se ha colpito qualcosa, False è acqua

# Barca
class Boat:
    def __init__(self, p1, is_horizontal, length):
        self.p1 = p1                            # coordinate del punto di inizio della nave (nelle coordinate del campo di battaglia, non nelle coordinate grafiche)
        self.is_horizontal = is_horizontal      # True se la nave è orizzontale, False se è verticale
        self.length = length                    # lunghezza/altezza della nave (nel sistema di riferimento del campo di battaglia, non in quello grafico)
        self.p2 = self.get_point_end()          # coordinate del punto di fine della nave (nelle coordinate del campo di battaglia, non nelle coordinate grafiche)
        self.sunk = False                       # True se è affondata, False se è ancora a galla
        self.shots_received = []                # lista di copli (di tipo Shot) ricevuti che hanno colpito la nave (non vengono memorizzati i colpi a vuoto)

    # Funzione per ricavare le coordinate del punto finale della nave
    # (nel sistema di riferimento del campo di battaglia, non coord grafiche)
    def get_point_end(self):
        # ricava le coordinate del punto di fine della nave
        p2 = Coord()
        if self.is_horizontal:
            p2.x = self.p1.x + self.length
            p2.y = self.p1.y
        else:
            p2.x = self.p1.x
            p2.y = self.p1.y + self.length
        return p2

    # Funzione che verifica se si è già sparato nelle coordinate del punto shot passato
    def already_shooted(self, shot):
        for s in self.shots_received:
            if s.x == shot.x and s.y == shot.y:
                return True
        return False

    # Funzione per determinare se la nave è affondata
    def is_sunk(self):
        # verifica se tutti i colpi ricevuto hanno affondato la nave
        if len(self.shots_received)-1 == self.length:
            return True
        else:
            return False

    # Funzione per determinare se un punto appartiene alla nave
    def is_shot_on_boat(self, shot):
        # verifico se la nave è verticale (è un caso particolare di retta con eq x=n)...
        if self.p1.x != self.p2.x:
            # ... la nave non è verticale
            # ricavo l'equazione delle retta calcolando m e q dell'equazione: y = mx + q
            m = (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)
            q = (self.p1.x * self.p2.y - self.p2.x * self.p1.y) / (self.p1.x - self.p2.x)
            # verifico se il punto in cui si è sparato appartiene alla retta...
            if shot.y == (m * shot.x + q):
                # ... appartiene alla retta, verifico se è interno alla nave...
                if shot.x >= self.p1.x and shot.x <= self.p2.x and shot.y >= self.p1.y and shot.y <= self.p2.y:
                    # ... il colpo  all'interno del segmento delle nave
                    return True
        else:
            # ... la nave è verticale, verifico se il colpo è sulla retta della nave...
            if shot.x==self.p1.x:
                # ... il colpo è sulla retta della nave, verifico se è all'interno delle coord y di inizio e fine...
                if shot.y >= self.p1.y and shot.y <= self.p2.y:
                    # ... il colpo è tra l'inizio e la fine della nave, significa che l'ha colpita
                    return True
        # se sono arrivato funo qui senza un return prima significa che il colpo non è sul segmento della nave
        return False

    # Funzione che riceve un colpo sparato:
    # determina se lo shot sparato ha colpito la nave, se si lo memorizza sulla nave, altrimenti lo ignora
    # La funzione restituisce:
    # True:     se il colpo ricevuto ha colpito la nave
    # False:    se il colpo è andato a vuoto, o se la nave era già affondata
    def get_shot(self, shot):
        # shot contiene le coordinate in cui si è sparato
        if DEBUG:
            print("boat.get_shot(", shot.x, ";", shot.y, ")")
        if self.sunk:
            # la nave è già stata affondata, restituisco false
            return False
        elif self.already_shooted(shot):
            # si è già sparato in questo punto, restituisco false 
            # non si passa mai da qui, la verifica è fatta dalla funzione get_shot contenuta in battlefield, la lascio per sicurezza e completezza dell'oggetto Boat
            return False
        else:
            # Verifico se il colpo ha colpito la nave...
            if self.is_shot_on_boat(shot):
                # ... Il colpo ha colpito la nave, memorizzo che è andato a segno
                shot.hit = True
                # salvo il colpo tra quelli che hanno colpito la nave
                self.shots_received.append(shot)
                # verifico se la nave è anche affondata con questo colpo
                self.sunk = self.is_sunk()
                return True
            else:
                # ... il colpo NON ha colpito la nave
                return False


# Classe giocatore
class Player:
    def __init__(self, name):
        self.name = name                      # Titolo (nome) del campo di battaglia
        self.shots = []                       # Lista di spari effettuati dal player

    # Funzione che verifica se il player ha già sparato nelle coordinate passate
    def already_shooted(self, shot):
        for s in self.shots:
            if s.x == shot.x and s.y == shot.y:
                return True
        return False

    # Funzione che identifica le coordinate di un punto in cui sparare, senza sparare nuovamente in un punto in cui si è già sparato
    def new_shot(self):
        #TODO: creare un algoritmo che, se l'ultimo colpo ha colpito una nave, spari in un punto in cui ci possano essere altre caselle della nave da affondare
        #   per farlo interrogare il campo di battaglia sui colpi sparati che hanno colpito

        # Verifico che non si sia già sparato nel punto scelto
        already_shooted = True
        while already_shooted:
            # creo uno sparo con coordinate casuali
            shot = Coord(randint(0, BATTLEFIELD_WIDTH-1), randint(0, BATTLEFIELD_HEIGHT-1))
            already_shooted = self.already_shooted(shot)
        return shot


# Classe per disegnare un bottone sullo schermo
# TODO: in position passare le coordinate del punto centrale del bottone
def Button(screen, position, text):
    font = pygame.font.SysFont(TEXT_FONT, 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))

# Funzione per scrivere sullo schermo un dato testo nella posizione, dimensione e colore passati (non legato ad uno dei campi di battaglia)
# screen:       display grafico di pygame
# text:         testo da scrivere
# pos:          coordinate del punto in cui scrivere il testo
# pos_type:     tipo di punto in cui scrivere il testo:
#               1: center
#               2: bottomleft
# text_height:  altezza del testo
# text_color:   colore RGB del testo
def print_to_screen(screen, text, pos, pos_type, text_height, text_color):
    font = pygame.font.SysFont(TEXT_FONT, text_height)
    img = font.render(text, True, text_color)
    text_rect = img.get_rect()
    if pos_type==1:
        text_rect.center = pos
    elif pos_type==2:
        text_rect.bottomleft=pos
    screen.blit(img, text_rect)

# Funzione per visualizzare a monitor il messaggio passato nella barra di stato (riga in basso a sinistra dell'area grafica)
def print_status_message(screen, message):
    print_to_screen(screen, message, (5, screen_height-5), 2, 20, (0,0,255))

# Funzione per creare il pulsante restart alla fine di una partita
# screen:       display grafico di pygame
# pos:          posizione del pulsante (angolo alto sx)
# restituisce l'area del pulsante (servirà per intercettare il click del mouse)
def show_restart_button(screen, pos):
    btn_restart = Button(screen, pos, "Restart")
    return btn_restart

# Funzione per l'inizializzazione del campo di battaglia del computer
# Viene richiamata all'inizio di ogni nuova partita, definisce la posizione del campo di battaglia nell'area grafica di pygame e crea le barche in pos. casuale
# screen:       display grafico di pygame
def setup_computer_field(screen):
    computer_field = Battlefield("Computer", 
        BATTLEFIELD_WIDTH, 
        BATTLEFIELD_HEIGHT, 
        screen, 
        GRAPHIC_MARGIN_LEFT, 
        GRAPHIC_MARGIN_TOP, 
        GRAPHIC_CELL_SIZE)
    computer_field.populate_field(BATTLEFIELD_BOATS_NUM_AND_SIZE)
    return computer_field

# Funzione per l'inizializzazione del campo di battaglia dello user
# Viene richiamata all'inizio di ogni nuova partita, definisce la posizione del campo di battaglia nell'area grafica di pygame e crea le barche in pos. casuale
# screen:       display grafico di pygame
def setup_user_field(screen):
    user_field = Battlefield("User", 
        BATTLEFIELD_WIDTH, 
        BATTLEFIELD_HEIGHT, 
        screen, 
        GRAPHIC_MARGIN_LEFT + (BATTLEFIELD_WIDTH * GRAPHIC_CELL_SIZE) + GRAPHIC_DISTANCE_BETWEEN_FIELDS, 
        GRAPHIC_MARGIN_TOP, 
        GRAPHIC_CELL_SIZE)
    user_field.populate_field(BATTLEFIELD_BOATS_NUM_AND_SIZE)
    return user_field

# Funzione per determinare se la prima mossa della partita è dello user o del computer
# True:     Prima mossa dello user
# False:    Prima mossa del computer
def select_if_user_start():
    user_start_choices = True, False
    return choice(user_start_choices)

######## MAIN ########
# inizializzo pygame
pygame.init()

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# creo il display grafico della dimensione stabilita nelle costanti per i due campi di battaglia
screen_width = GRAPHIC_MARGIN_LEFT + 2 * (BATTLEFIELD_WIDTH * GRAPHIC_CELL_SIZE) + GRAPHIC_DISTANCE_BETWEEN_FIELDS + GRAPHIC_MARGIN_RIGHT
screen_height = GRAPHIC_MARGIN_TOP + (BATTLEFIELD_HEIGHT * GRAPHIC_CELL_SIZE) + GRAPHIC_MARGIN_BOTTOM
screen = pygame.display.set_mode((screen_width, screen_height))

# Inizializzo i campi di battaglia del computer e dello user
computer_field = setup_computer_field(screen)
user_field = setup_user_field(screen)

# Inizializzo i giocatori
computer_player = Player(computer_field.title)
user_player = Player(user_field.title)

# determino se inizierà la prima mossa lo user o il computer
user_turn = select_if_user_start()

# imposto la posizione in cui rappresentare il pulsante restart
btn_restart_position = (screen_width//2, screen_height//2+50)
# inizializzo il pulsante restart a None
# Se è None significa che non è visibile, se valorizzato all'oggeto Button (area del pulsante) vule dire che la partita è finita ed il pulsante è visibile
btn_restart = None

# inizializzo la variabile per contenere i messaggi da visualizzare nella barra di stato (riga in basso a sinistra dell'area grafica)
message = "First turn to " + user_player.name if user_turn else computer_player.name

# Eseguo all'infinito finchè l'utente non chiude la finestra del gioco
running = True
print("Running")
if DEBUG:
    print("#### DEBUG MODE ####")
while running:
    current_time = pygame.time.get_ticks()

    # Intercetto gli eventi pygame
    for event in pygame.event.get():
        # Se l'utente chiude la finestra termino l'esecuzione impostando running afalse
        if event.type == pygame.QUIT:
            running = False

        # intercetto gli eventi relativi al click dei pulsanti del mouse..
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            # ... verifico se l'utente ha cliccato il pulsante sx
            if mouse_presses[0]:
                # ricavo il punto in cui si è cliccato
                click_pos = pygame.mouse.get_pos()

                # verifico se il pulsante restart è attivo e se lo si è cliccato (click nell'area del pulsante)
                if btn_restart and btn_restart.collidepoint(click_pos):
                    # cliccato resart, riavvio il gioco, nascondendo il pulsante e reinizializzando i campi di battaglia
                    btn_restart=None
                    computer_field = setup_computer_field(screen)
                    user_field = setup_user_field(screen)
                    user_turn = select_if_user_start()
                else:
                    # Verifico se la mossa spetta allo user o al computer...
                    if user_turn:
                        # ... La mossa spetta allo user
                        # ricavo le coordinate in cui si è cliccato nel campo di battaglia del computer (nel sistema di coordinate del campo di battaglia non nel sistma grafico)
                        comp_field_pos = computer_field.coord_from_graph_coord(click_pos)
                        # ricavo le coordinate in cui si è cliccato nel campo di battaglia dell'utente (nel sistema di coordinate del campo di battaglia non nel sistma grafico)
                        user_field_pos = user_field.coord_from_graph_coord(click_pos)
                        if comp_field_pos!=None:
                            # se si è cliccato sul campo di battaglia del computer...
                            computer_field.get_shot(comp_field_pos)
                            user_player.shots.append(comp_field_pos)
                            message = "User shot in: " + "(" + computer_field.get_ascissa_to_print(comp_field_pos.x) + ", " + computer_field.get_ordinata_to_print(comp_field_pos.y) + ")"
                            # assegno la prossima mossa al computer
                            user_turn = not user_turn
                            message = message + " - Now it's " + (user_player.name if user_turn else computer_player.name) + " turn"
                        # Commento la possibilità per l'utente di sparare nel proprio campo di battaglia
                        # elif user_field_pos!=None:
                        #     # se si è cliccato sul campo di battaglia dello user...
                        #     user_field.get_shot(user_field_pos)
                        #     message = "Computer shot in: " + "(" + user_field.get_ascissa_to_print(user_field_pos.x) + ", " + user_field.get_ordinata_to_print(user_field_pos.y) + ")"
                        if DEBUG:
                            print("Mouse position: ", click_pos, end ="")
                            if comp_field_pos!=None:
                                print(" - ", computer_field.title, "coord: (", comp_field_pos.x, ";", comp_field_pos.y, ")", end ="")
                            if user_field_pos!=None:
                                print(" - ", user_field.title, "coord: (", user_field_pos.x, ";", user_field_pos.y, ")", end ="")
                            print()

                        

    # Verifico se è il turno del computer
    if not user_turn:
        computer_shot = computer_player.new_shot()
        computer_player.shots.append(computer_shot)
        user_field.get_shot(computer_shot)
        user_turn = not user_turn
        message = "Computer shot in: " + "(" + user_field.get_ascissa_to_print(computer_shot.x) + ", " + user_field.get_ordinata_to_print(computer_shot.y) + ")" + " - Now it's " + (user_player.name if user_turn else computer_player.name) + " turn"

    # Fill the background
    screen.fill(BATTLEFIELD_BACKGROUND_COLOR)

    # Disegno il campo di battaglia del computer
    computer_field.draw_field(GRAPHIC_BATTLEFIELD_COMPUTER_GRID_COLOR, True)
    # Disegno il campo di battaglia dello user
    user_field.draw_field(GRAPHIC_BATTLEFIELD_USER_GRID_COLOR, False)

    # Scrivo nella barra di stato il messaggio da mostrare        
    print_status_message(screen, message)

    # Verifico se in uno dei campi di battaglia sono state affondate tutte le navi
    if computer_field.are_all_boats_sunk():
        # ha vinto lo user
        print_to_screen(screen, user_field.title + " WINS!!", (screen_width//2, 15), 1, 40, (0,0,255))
        print(user_field.title + " WINS!!")
        btn_restart = show_restart_button(screen, btn_restart_position)
    if user_field.are_all_boats_sunk():
        # ha vinto il computer
        print_to_screen(screen, computer_field.title + " WINS!!", (screen_width//2, 15), 1, 40, (0,0,255))
        print(computer_field.title + " WINS!!")
        btn_restart = show_restart_button(screen, btn_restart_position)

    # Flip the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)

# Done! Time to quit.
pygame.quit()