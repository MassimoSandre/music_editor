from matplotlib import offsetbox
import pygame

class Piano:
    def __init__(self,*, octaves=5, firstoctave=2, position, white_size, black_size, margin):
        self.__octaves = octaves
        self.__firstoctave = firstoctave
        self.__white_size = white_size
        self.__black_size = black_size
        self.__margin = margin
        self.__pos = position
        self.__notes = ['DO','RE','MI','FA','SOL','LA','SI']

    def get_note_by_pos(self, pos):
        k = self.__octaves*7
        right = k*self.__white_size[0] + (k-1)*self.__margin

        if pos[0]-self.__pos[0]< 0 or pos[0]-self.__pos[0] > right:
            return None
        
        if pos[1]-self.__pos[1] < 0 or pos[1]-self.__pos[1] > self.__white_size[1]:
            return None

        bx,by = self.__pos
        result = None
        for i in range(self.__octaves):
            for j in range(7):
                if pos[0]-bx > 0 and pos[0]-bx< self.__white_size[0] and pos[1]-by > 0 and pos[1]-by < self.__white_size[1]:
                    result = self.__notes[j] + str(self.__firstoctave+i)
                if j != 0 and j != 3:
                    black_x = bx - (self.__black_size[0]//2 + self.__margin//2)
                    if pos[0]-black_x > 0 and pos[0]-black_x< self.__black_size[0] and pos[1]-by > 0 and pos[1]-by < self.__black_size[1]:
                        return self.__notes[j] + str(self.__firstoctave+i) + "b"

                bx+=self.__margin+self.__white_size[0]
        return result

    def show(self,screen, font):
        
        bx,by = self.__pos
        for i in range(self.__octaves):
            for j in range(7):
                pygame.draw.rect(screen,[240,240,240], pygame.Rect((bx,by),self.__white_size),0,4)

                cx = bx + self.__white_size[0]//2

                text = font.render(self.__notes[j], False, (20,20,20))
                offset_x = text.get_rect().width//2
                offset_y = text.get_rect().height + 10
                screen.blit(text, (cx-offset_x, by+self.__white_size[1]-offset_y))

                if j == 0:
                    text = font.render(str(i+self.__firstoctave), False, (20,20,20))
                    offset_x = text.get_rect().width//2
                    offset_y = text.get_rect().height + 30
                    screen.blit(text, (cx-offset_x, by+self.__white_size[1]-offset_y))

                if j != 0 and j != 3:
                    black_x = bx - (self.__black_size[0]//2 + self.__margin//2)
                    pygame.draw.rect(screen,[20,20,20], pygame.Rect((black_x,by),self.__black_size),0,3)
                bx+=self.__margin+self.__white_size[0]



