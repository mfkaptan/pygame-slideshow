# # Mustafa Kaptan
# # Slideshow programi
import pygame, sys , ConfigParser
from pygame import gfxdraw

# Colors
BLACK = (0 , 0 , 0)
WHITE = (255, 255, 255)

class Image(pygame.sprite.Sprite):
    def __init__(self, filename, picture, time, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./experiments/" + filename + "/" + picture).convert()
        self.time = int(time)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width() / 2
        self.rect.centery = screen.get_height() / 2
        
def start_countdown(screen):    
    # Get screens width,height -> center
    centerX = screen.get_width() / 2
    centerY = screen.get_height() / 2
    
    # Font
    countfont = pygame.font.Font('turkish.ttf', 150)
    
    for i in range (4, 0, -1):
        screen.fill(BLACK)
        if i > 1:
			# Draw an anti-aliased circle
            pygame.gfxdraw.aacircle(screen, centerX, centerY, 150, WHITE)
            counttext = countfont.render("" + str(i - 1) , True, WHITE)
            screen.blit(counttext, (centerX - 40, centerY - 90))
        pygame.display.flip()
        pygame.time.delay(1000)
    
def main():
    # Initialize
    pygame.init()
    
    # The FPS the game runs at.
    DELAY = 0
    
    # Screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Slideshow")
    
	# Invisible mouse
    pygame.mouse.set_visible(False)

    # List of sprite images
    slideShow = pygame.sprite.OrderedUpdates()
    currentSlide = pygame.sprite.OrderedUpdates()
    
    # Get file name
    filename = sys.argv[1]
    
    config = ConfigParser.RawConfigParser()
    try:
        config.readfp(open("./experiments/" + filename + "/config.ini"))
    except IOError: 
        print "Error: can\'t find file or read data"
        pygame.quit()
    
    lineList = config.items('sequence')
    length = len(lineList)
    
    # Save lines to Image class and Slideshow list
    for line in lineList:
        slideImage = Image(filename, line[0], line[1], screen)
        slideShow.add(slideImage)
        
    i = -1
    
    # Use a timer to control FPS.
    clock = pygame.time.Clock()
    
	# Start the countdown
    start_countdown(screen)
    # Main loop    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # If user hit ESC
                return False
            if event.type == pygame.QUIT:  # If user clicked close 
                return False
            
        # Empty the list
        currentSlide.empty()
        i += 1
        
		# Just add 1 sprite into it
        if i < length:
            for image in slideShow.sprites():
                currentSlide.add(image)
                slideShow.remove_internal(image)
                break
        else:
            # TODO : do something?!
            return False
        
        # Draw the screen based on the timer.
        screen.fill(BLACK)
        for slide in currentSlide.sprites():
            DELAY = slide.time
        currentSlide.draw(screen)
        pygame.display.flip()
        pygame.time.delay(DELAY)
        clock.tick(25)
        
    pygame.quit()
            
if __name__ == "__main__":
    main()
