import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((500, 500))


def getKey(keys):

    ret = False
    for events in pygame.event.get(): pass
    keyinp = pygame.key.get_pressed()
    mykey = getattr(pygame,'K_{}'.format(keys))
    if keyinp[mykey]:
        ret = True
    pygame.display.update()
    return ret

def main():
    if getKey("LEFT"):
        print("LEFT KEY PRESSED")

if __name__ == '__main__':
    init()
    while True:

        main()