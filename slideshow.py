# Mustafa Kaptan
# Slideshow programi
#first eclipse commit

import pygame,sys

# Colors
BLACK = (0 , 0 , 0)

class Image(pygame.sprite.Sprite):
    def __init__(self, picture, time, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./slideshow/" + picture).convert()
        self.time = int(time)
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_width() / 2
        self.rect.centery = screen.get_height() / 2
            
    def update(self):
        self.time = self.time
    
def main():
    # Initialize
    pygame.init()
    
    # The FPS the game runs at.
    DELAY = 0
    
    # Screen
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Slideshow")
    
    # List of sprite images
    slideShow = pygame.sprite.OrderedUpdates()
    currentSlide = pygame.sprite.OrderedUpdates()
    
    # Read from file and save
    slideFile = open("./slideshow/slideshow.sld")
    line_list = slideFile.readlines()
    slideFile.close()
    
    # Length of line_list
    length = len(line_list)
    
    # Control
    # print( "There were ",length," lines in the file.")

    # Save lines to Image class and Slideshow list
    for i in range (0, length, 2):
        slideImage = Image(line_list.pop(0).replace('\n', ''), line_list.pop(0), screen)
        slideShow.add(slideImage)
        
    i = -1
    
    # Use a timer to control FPS.
    clock = pygame.time.Clock()
    # Main loop    
    while True:
        # Empty the list
        currentSlide.empty()
        i += 1
        
        if i < length / 2:
            for image in slideShow.sprites():
                currentSlide.add(image)
                slideShow.remove_internal(image)
                break
        else:
            # TODO : do something!
            return False
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  # If user hit ESC
                return False
            if event.type == pygame.QUIT:  # If user clicked close 
                return False
        
        # Draw the screen based on the timer.
        screen.fill(BLACK)
        for slide in currentSlide.sprites():
            DELAY = slide.time
        currentSlide.draw(screen)
        pygame.display.flip()
        pygame.time.delay(DELAY * 1000)
        clock.tick(25)
        
    pygame.quit()
            
# This doesn't run on Android.
if __name__ == "__main__":
    main()