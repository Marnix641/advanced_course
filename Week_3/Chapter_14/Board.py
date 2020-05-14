import pygame
import PIL
from PIL import Image


def draw_board(the_board):
    """ Draw a chess board with queens, as determined by the the_board. """

    pygame.init()
    colors = [(255,0,0), (0,0,0)] # Set up colors [red, black]

    n = len(the_board) # This is an NxN chess board.
    surface_size = 480 # Proposed physical surface size.
    square_size = surface_size // n # sq_sz is length of a square.
    surface_size = n * square_size # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_size, surface_size))

    ball_large = pygame.image.load("ball.jpg")
    #eigen code
    basewidth = surface_size // n
    wpercent = (basewidth / float(ball_large.size[0]))
    hsize = int((float(ball_large.size[1]) * float(wpercent)))
    ball = ball_large.resize((basewidth, h_size), PIL.Image.ANTIALIAS)
    ball.save("resized_ball.jpg")

    # Use an extra offset to centre the ball in its square.
    # If the square is too small, offset becomes negative,
    # but it will still be centered :-)
    ball_offset = (square_size-ball.get_width()) // 2

    while True:

        # Look for an event from keyboard, mouse, etc.
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break;

    # Draw a fresh background (a blank chess board)
        for row in range(n): # Draw each row of the board.
            color_index = row % 2 # Alternate starting color
            for col in range(n): # Run through cols drawing squares
                the_square = (col*square_size, row*square_size, square_size, square_size)
                surface.fill(colors[color_index], the_square)
                # Now flip the color index for the next square
                color_index = (color_index + 1) % 2

        # Now that squares are drawn, draw the queens.
        for (col, row) in enumerate(the_board):
            surface.blit(ball, (col*square_size+ball_offset,row*square_size+ball_offset))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    draw_board([0, 5, 3, 1, 6, 4, 2]) # 7 x 7 to test window size
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1]) # 13 x 13
    draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])
