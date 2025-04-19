import pygame,text_on_screen,visual_obj

class Process(visual_obj.Visual_obj):
    def __init__(self,who_im_waiting=None):


        self.status="not_started"
        self.who_im_waiting=who_im_waiting
        if who_im_waiting!=None:
            self.who_im_waiting.who_waits_me.append(self)
        self.who_waits_me=[]

    def starter(self):

        self.status="started"

    def the_end_def(self):
        self.status="the_end"
        for member in self.who_waits_me:
            member.starter()
