# import required modules/classes
import pygame


class Piece:
    """
    The class representing a game piece.
    Attributes
    ----------
    uniq : int
        A unique identifier for the piece.
    color : tuple
        The color of the piece in RGB format.
    position : tuple
            The current position of the piece on the screen.
    path : list
        The path the piece should follow on the board.
    ini_pos : int
        The initial position of the piece on its path.
    fin_pos : int
        The final position of the piece on its path, by default 0.
    state : str
        The current state of the piece, by default 'in'.
    surface : pygame.Surface
        The surface on which the piece is drawn.
    """
    def __init__(self, uniq, color, position, path, ini_pos, fin_pos=0, state='in'):
        self.uniq = uniq
        self.color = color
        self.position = position
        self.piece_path = path
        self.ini_pos = ini_pos
        self.fin_pos = fin_pos
        self.state = state
        self.surface = pygame.Surface((30, 30))
        self.surface.fill(self.color)

    def draw_piece(self, screen):
        """
        Draws the piece on the given screen.
        Parameters:
        screen : pygame.Surface
        The surface on which to draw the piece.
        """
        if self.state == 'in':
            screen.blit(self.surface, self.position)
        else:
            screen.blit(self.surface, self.piece_path[self.ini_pos])

    def move_piece(self, roll):
        """
        Moves the piece along its path based on the roll of a die.
        Parameters
        roll : int
            The result of a die roll.
        """
        if self.state == 'in':
            if roll == 6:
                self.state = 'out'
                self.ini_pos = 0
        else:
            new_pos = self.ini_pos + roll
            if new_pos < len(self.piece_path):
                self.ini_pos = new_pos


    def reached_home(self):
        """
        Checks if the piece has reached the end of its path.
        Returns:
        bool:
            True if the piece has reached the end of its path, False otherwise.
        """
        return self.ini_pos == len(self.piece_path) - 1

    def is_collision(self, other_piece):
        """
        Checks if this piece has collided with another piece.
        Parameters
        other_piece : Piece
            The other piece to check for a collision with.
        Returns:
        bool:
            True if this piece has collided with the other piece, False otherwise.
        """
        if self.state != "on_board" or other_piece.state != "on_board":
            return False
        return self.piece_path[self.ini_pos] == other_piece.piece_path[other_piece.ini_pos]
