import pygame,text_on_screen,visual_obj

class Process(visual_obj.Visual_obj):
    def __init__(self,text:str,live_time:int,who_im_waiting=None):

        self.text=text
        self.timer=live_time
        self.status="not_started"
        self.who_im_waiting=who_im_waiting
        if who_im_waiting!=None:
            self.who_im_waiting.who_waits_me.append(self)
        self.who_waits_me=[]
        self.the_end = pygame.event.custom_type()
    def starter(self):

        self.status="started"
        pygame.time.set_timer(self.the_end, self.timer,1)


    def the_end_def(self):
        self.status="the_end"
        for member in self.who_waits_me:
            member.starter()


    def controller(self,list_events):
        for event in list_events:
            if event.type==self.the_end:
                self.the_end_def()


    def draw(self,place: pygame.Surface):
        if self.status=="started":
            text_11=text_on_screen.Text_on_screen(self.text,pygame.display.get_window_size(),80)
            text_11.draw(place)