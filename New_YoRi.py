# import required modules/classes
import random
import pygame
import board
import piece
import dice
import sys
import os
from pygame import mixer
from collections import deque

pygame.mixer.init()

# red player path
r_piece_path = [(293, 566), (293, 525), (293, 484), (293, 443), (293, 401), (250, 360),
                (206, 360), (161, 360), (118, 360), (74, 360), (31, 360), (31, 319),
                (31, 276), (75, 276), (118, 276), (161, 276), (206, 276), (250, 276),
                (292, 235), (292, 194), (292, 153), (292, 112), (292, 70), (292, 28),
                (335, 28), (379, 28), (379, 70), (379, 112), (379, 154), (379, 195),
                (379, 236), (422, 277), (466, 277), (510, 277), (554, 277), (597, 277),
                (640, 277), (640, 319), (640, 359), (597, 359), (554, 359), (511, 359),
                (467, 359), (423, 359), (380, 400), (380, 442), (380, 484), (380, 526),
                (380, 567), (380, 608), (336, 608), (336, 567), (336, 526), (336, 484),
                (336, 442), (336, 400), (336, 348)
                ]

# green player path
g_piece_path = [(597, 359), (554, 359), (511, 359), (467, 359), (423, 359), (380, 400),
                (380, 442), (380, 484), (380, 526), (380, 567), (380, 608), (336, 608),
                (293, 608), (293, 566), (293, 525), (293, 484), (293, 443), (293, 401),
                (250, 360), (206, 360), (161, 360), (118, 360), (74, 360), (31, 360),
                (31, 319), (31, 276), (75, 276), (118, 276), (161, 276), (206, 276),
                (250, 276), (292, 235), (292, 194), (292, 153), (292, 112), (292, 70),
                (292, 28), (335, 28), (379, 28), (379, 70), (379, 112), (379, 154),
                (379, 195), (379, 236), (422, 277), (466, 277), (510, 277), (554, 277),
                (597, 277), (640, 277), (640, 319), (597, 319), (554, 319), (510, 319),
                (466, 319), (422, 319), (367, 319)
                ]

# blue player path
b_piece_path = [(75, 276), (118, 276), (161, 276), (206, 276), (250, 276), (292, 235),
                (292, 194), (292, 153), (292, 112), (292, 70), (292, 28), (335, 28),
                (379, 28), (379, 70), (379, 112), (379, 154), (379, 195), (379, 236),
                (422, 277), (466, 277), (510, 277), (554, 277), (597, 277), (640, 277),
                (640, 319), (640, 359), (597, 359), (554, 359), (511, 359), (467, 359),
                (423, 359), (380, 400), (380, 442), (380, 484), (380, 526), (380, 567),
                (380, 608), (336, 608), (293, 608), (293, 566), (293, 525), (293, 484),
                (293, 443), (293, 401), (250, 360), (206, 360), (161, 360), (118, 360),
                (74, 360), (31, 360), (31, 319), (75, 319), (118, 319), (161, 319),
                (206, 319), (250, 319), (304, 319)]

# yellow player path
y_piece_path = [(379, 70), (379, 112), (379, 154), (379, 195), (379, 236), (422, 277),
                (466, 277), (510, 277), (554, 277), (597, 277), (640, 277), (640, 319),
                (640, 359), (597, 359), (554, 359), (511, 359), (467, 359), (423, 359),
                (380, 400), (380, 442), (380, 484), (380, 526), (380, 567), (380, 608),
                (336, 608), (293, 608), (293, 566), (293, 525), (293, 484), (293, 443),
                (293, 401), (250, 360), (206, 360), (161, 360), (118, 360), (74, 360),
                (31, 360), (31, 319), (31, 276), (75, 276), (118, 276), (161, 276),
                (206, 276), (250, 276), (292, 235), (292, 194), (292, 153), (292, 112),
                (292, 70), (292, 28), (335, 28), (335, 70), (335, 112), (335, 153),
                (335, 194), (335, 235), (335, 288)
                ]
# music file 1
current_dir = os.path.dirname(__file__)
background_music = os.path.join(current_dir, 'the-weekend-117427.mp3')

# music file 2
current_dir2 = os.path.dirname(__file__)
background_music_2 = os.path.join(current_dir, 'walk-together-123281.mp3')

# music file 3
current_dir3 = os.path.dirname(__file__)
background_music_3 = os.path.join(current_dir, 'uplifting-piano-79-mix-20674.mp3')

"""
The code first defines the three background music files. 
Then, it chooses a random music file from the list of background music files. 
Finally, it loads the music file and plays it with a volume of 0.3.
"""
background_music_files = [background_music, background_music_2, background_music_3]
play_random_music = background_music_files[random.randint(0, len(background_music_files) - 1)]
mixer.music.load(play_random_music)
mixer.music.set_volume(0.1)
mixer.music.play(3)


class YoRi:
    """Main Game Class"""

    def __init__(self, screen):
        """
        Initialize game with provided screen
        :param screen: pygame display screen object
        """
        self.screen = screen
        self.board = board.Board()
        self.pieces = {
            "red": [piece.Piece(x, (255, 60, 0), (144, 555), r_piece_path, 0) for x in range(2)],
            "green": [piece.Piece(x, (40, 255, 0), (587, 509), g_piece_path, 0) for x in range(2)],
            "blue": [piece.Piece(x, (0, 0, 255), (85, 129), b_piece_path, 0) for x in range(2)],
            "yellow": [piece.Piece(x, (255, 255, 110), (535, 81), y_piece_path, 0) for x in range(2)],
        }
        self.dice = dice.Dice()
        # load the dice sound
        current_dir = os.path.dirname(__file__)
        dice_music = os.path.join(current_dir, 'ONEDICE.wav')
        self.dice_roll_sound = pygame.mixer.Sound(dice_music)
        self.dice_roll_sound.set_volume(.3)
        self.turn = 0
        self.players = deque(["red", "green", "yellow", "blue"])
        self.clock = pygame.time.Clock()
        current_dir_ = os.path.dirname(__file__)
        self.font = pygame.font.Font(None, 35)

    def draw(self):
        """
        Draws the game board, pieces, dice, current turn and remaining pieces
        """
        self.board.draw_board(self.screen)
        for p_list in self.pieces.values():
            for piece in p_list:
                piece.draw_piece(self.screen)
        self.dice.draw_dice(self.screen)
        self.display_turn()
        self.display_key_inputs()
        pygame.display.update()

    # handle a situation where there is a collision between 2 different pieces
    def is_collision(self, other_piece):
        """
        Checks if there is a collision between two different pieces
        :param other_piece: The piece to check for collision
        :return: Tuple of Boolean indicating collision and the collided piece
         """
        for piece_color, pieces in self.pieces.items():
            if piece_color != self.players[0]:
                for piece in pieces:
                    if other_piece.is_collision(piece):
                        return True, piece
        return False, None

    # change turn after piece moves
    def change_turn(self):
        """
        Changes the turn of the player
         """
        # rotating the dequeue
        self.players.rotate(-1)

    # play the player's turn
    def play_turn(self, selected_piece):
        """
        Plays the turn for the selected piece
        :param selected_piece: The selected piece to play the turn for
        """
        piece = selected_piece
        self.dice.roll_dice()
        # Play dice roll sound
        self.dice_roll_sound.play()
        if piece.state == 'in' and self.dice.value == 6:
            piece.state = "on_board"
        elif piece.state == "on_board":
            piece.move_piece(self.dice.value)
            has_collision, collided_piece = self.is_collision(piece)
            if has_collision:
                # Handle the crash
                collided_piece.state = "in"
                collided_piece.ini_pos = 0
            if piece.reached_home():
                piece.state = "out"
        if piece.state != "out":
            self.change_turn()

    def display_turn(self):
        """
        Displays the current turn
        """
        # load the font
        current_dir = os.path.dirname(__file__)
        font = pygame.font.Font(None, 40)
        dis_turn = f"{self.players[0].capitalize()} Player Turn"
        text = font.render(dis_turn, True, (0, 0, 0))
        text_r = text.get_rect()
        text_r.topright = (458, 23)
        self.screen.blit(text, text_r)

    def display_key_inputs(self):
        """
        Display the key inputs to play the game
        """
        font = pygame.font.Font(None, 28)
        x, y = 723, 400
        spacing = 40
        text = ["  MOUSE KEY INPUTS :",
                "• LEFT OR RIGHT CLICK",
                "  ON THE PIECE TO",
                "  ROLL THE DICE AND",
                "  MOVE THE PIECE"
                ]
        for key in text:
            disp_text = font.render(key, True, (0, 0, 0))
            self.screen.blit(disp_text, (x, y))
            y += spacing

    def display_instructions(self):
        """
        Display the instructions on the side of the screen.
        Also include key inputs needed.
        """
        font = pygame.font.Font(None, 26)
        current_dir = os.path.dirname(__file__)
        image_path = os.path.join(current_dir, '1131w--cSCTzEGFxc.png')
        border_image = pygame.image.load(image_path)
        border_image = pygame.transform.scale(border_image, (600, 650))
        self.screen.blit(border_image, (10, 10))
        instructions = [
            "",
            "                               YoRi Instructions:",
            "• There are four players in the game.",
            "• There are two pieces for each player.",
            "• Each piece goes across the board according to the ",
            "  number thrown on the dice.",
            "• A piece must first roll a 6 to leave its base.",
            "• A piece may only enter the house after traveling the",
            "  entire length of the board.",
            "• If a piece lands on another piece of a different color,",
            "  the collided piece is returned to its base.",
            "• The winner of the game is the first player to get both",
            "  of their pieces to 'home'.",
            "• Roll the dice by pressing the piece you want to move."
        ]
        instructions_input = [
            "• PRESS 'ESC' TO GO BACK TO THE ",
            "  MAIN MENU SCREEN."]
        x, y = 80, 20
        a, b = 625, 50
        spacing = 40
        for rules in instructions:
            disp_text = font.render(rules, True, (0, 0, 0))
            self.screen.blit(disp_text, (x, y))
            y += spacing
        for input in instructions_input:
            text = font.render(input, True, (0, 0, 0))
            self.screen.blit(text, (a, b))
            b += spacing

    # handle user_input
    def user_input(self, event):
        """
        Handles user input for the game
        :param event: pygame event object
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            uniq_piece = self.postion_piece(x, y)
            if uniq_piece is not None:
                self.play_turn(uniq_piece)

    def get_selected_p(self):
        """
        Gets the selected piece from user input
        :return: Selected piece
        """
        selected_p = None
        while selected_p is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        selected_p = 0
                    elif event.key == pygame.K_2:
                        selected_p = 1
                    elif event.key == pygame.K_3:
                        selected_p = 2
                    elif event.key == pygame.K_4:
                        selected_p = 3
        return selected_p

    def postion_piece(self, x, y):
        """
        Positions the piece based on provided coordinates
        :param x: x-coordinate
        :param y: y-coordinate
        :return: Piece at the given position
        """
        for piece in self.pieces[self.players[0]]:
            if piece.state == 'in':
                piece_r = pygame.Rect(piece.position, (30, 30))
            else:
                if piece.color == (255, 60, 0):
                    piece_r = pygame.Rect(r_piece_path[piece.ini_pos], (30, 30))
                elif piece.color == (40, 255, 0):
                    piece_r = pygame.Rect(g_piece_path[piece.ini_pos], (30, 30))
                elif piece.color == (0, 0, 255):
                    piece_r = pygame.Rect(b_piece_path[piece.ini_pos], (30, 30))
                elif piece.color == (255, 255, 110):
                    piece_r = pygame.Rect(y_piece_path[piece.ini_pos], (30, 30))

            if piece_r.collidepoint(x, y):
                return piece
        return None

    def reached_home(self):
        """
        Checks if the piece has reached home
        :return: Boolean indicating if the piece has reached home
        """
        return self.ini_pos == len(self.piece_path) - 1

    def check_winner(self):
        """
        Checks if any player has won
        :return: Player indicating if the player has won
        """
        for player, pieces in self.pieces.items():
            if all(piece.state == "out" for piece in pieces):
                return player
        return None

    def draw_winner(self, text, font, color, x, y):
        """
        :param text: Text font passed by the game_loop method
        :param font: Font size passed by the game_loop method
        :param color: Color of the text passed by the game_loop method
        :param x: x-coordinate of the text
        :param y: x-coordinate of the text
        :return: add the text to the screen
        """
        winner_text = font.render(text, 1, color)
        winner_rect = winner_text.get_rect(center=(x, y))
        self.screen.blit(winner_text, winner_rect)

    def instructions(self):
        """
        displays the instructions screen and manages user input.
        Until the user quits the instructions screen, the loop continues.
        The exit event and the key press event for the ESCAPE key to return to the main menu
        are among the events in Pygame that are checked.
        The display_instructions function is used to show the instructions while filling the screen
        with a backdrop color.
        The loop's frame rate is limited to 60 per second.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_menu()
            self.screen.fill((205, 170, 125))
            self.display_instructions()
            pygame.display.update()
            pygame.time.Clock().tick(60)

    def draw_text(self, text, x, y):
        # draw main menu options
        surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(surface, (x, y))

    def display_menu_inputs(self):
        """
        Display the key inputs to display the
        key inputs on the main menu screen
        """
        font = pygame.font.Font(None, 28)
        x, y = 728, 50
        spacing = 40
        text = ["  KEYBOARD INPUTS :",
                "• PRESS '1' TO START THE ",
                "  GAME",
                "• PRESS '2' TO SEE THE ",
                "  INSTRUCTIONS",
                "• PRESS '3' TO QUIT THE ",
                "  GAME",
                ]
        for input in text:
            disp_text = font.render(input, True, (0, 0, 0))
            self.screen.blit(disp_text, (x, y))
            y += spacing

    def main_menu(self):
        """
        Manages user input and displays the main menu.
        The main menu screen is continually shown throughout a while loop.
        A background color is loaded, scaled, and blitted into the screen before a border picture is loaded.
        The draw_text function is used to display the primary menu items and their locations.
        The process monitors key presses while watching for user input events.
        If the user chooses one of the three options (options 1, 2, or 3), the relevant action
        (starting the game, displaying instructions, or quitting the game) is taken.
        Until the player quits the game, the loop keeps running.
        """
        while True:
            self.screen.fill((205, 170, 125))
            current_dir = os.path.dirname(__file__)
            image_path = os.path.join(current_dir, '1131w--cSCTzEGFxc.png')
            border_image = pygame.image.load(image_path)
            border_image = pygame.transform.scale(border_image, (600, 650))
            self.screen.blit(border_image, (10, 10))
            self.draw_text('MAIN MENU', 240, 60)
            self.draw_text('1. Start YoRi', 120, 150)
            self.draw_text('2. YoRi Instructions', 120, 250)
            self.draw_text('3. Quit YoRi', 120, 350)
            self.display_menu_inputs()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_1:
                        self.game_loop()
                        return
                    elif event.key == pygame.K_2:
                        self.instructions()
                        return
                    elif event.key == pygame.K_3:
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            self.clock.tick(60)

    def game_loop(self):
        """
        The program's main game loop launches and manages game events.
        Until the game is ended, the loop keeps going. It looks for pygame events, such as the exit event.
        To handle user input, it invokes the user_input method.
        To update the game display, the draw method is used.
        If a winner has been determined, the check_winner method plays the winning music and
        displays the winner message.
        The loop's frame rate is restricted at 60 fps.
        The pygame is terminated when the loop is ended.
        """
        running = True
        while running:
            # check for the event happen in pygame
            for event in pygame.event.get():
                # check if exit key is pressed
                if event.type == pygame.QUIT:
                    running = False
                self.user_input(event)
            self.draw()
            winner = self.check_winner()
            if winner is not None:
                # load the font
                current_dir = os.path.dirname(__file__)
                self.draw_winner(f"{winner.capitalize()} IS THE WINNER! ", pygame.font.Font
                (None, 48), (28, 28, 28), 370, 300)
                pygame.display.update()
                current_dir_ = os.path.dirname(__file__)
                winning_music = os.path.join(current_dir_, 'the-weekend-117427.mp3')
                mixer.music.load(winning_music)
                mixer.music.set_volume(0.7)
                mixer.music.play()
                pygame.time.wait(7000)
                mixer.music.stop()
                break
            pygame.time.Clock().tick(60)
        pygame.quit()
