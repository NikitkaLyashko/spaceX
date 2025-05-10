
import pygame,random,rock_space,messenger




class Start_yrovnei():
    def __init__(self,waves):

        self.waves=waves
        self.rocks = []
        colichstvo_voln = len(waves)
        for volna in range(colichstvo_voln):
            self.next_level(volna)

        messenger.add_sub_def(self.mess)


    def next_level(self,index):

            first_rock = pygame.event.custom_type()
            dictionary = self.waves[index]
            dictionary["номер события таймера"]=first_rock
            ###закинет фест рок через врем отведенное дикшинари###
            pygame.time.set_timer(first_rock, dictionary["начаьная_задержка"], 1)



    def spawn_rock(self,coordination):
        global  del_rock_from_model

        next_rock=rock_space.Rock_space(random.randint(coordination[0],coordination[1]),30,50)
        self.rocks.append(next_rock)
        for del_rock in self.rocks:

            if del_rock.rock.y >= 700:
                self.rocks.remove(del_rock)
                del_rock_from_model=1


    def controller(self, events):
        for event in events:
            for wave in self.waves:

                # IF дает понять какая сейчас волна
                if event.type == wave["номер события таймера"]:
                    ###move_rock-создание нового ключа и запись свободного события для начавшейся волны
                    wave["move_rock"] = pygame.event.custom_type()
                    pygame.time.set_timer(wave["move_rock"], wave["задержка_меж_камней"])

                    # в пременную запись значения ключа  , 48,49 создание 1го камня
                    koord = wave["координаты"]
                    self.spawn_rock(koord)
            for s_rock in self.rocks:
                s_rock.controller(events)



            for wave in self.waves:

                if "move_rock" in wave and event.type == wave["move_rock"]:
                    self.spawn_rock(wave["координаты"])
                    wave["кол-во_камней"] - 1
                    if wave["кол-во_камней"] == 1:
                        pygame.time.set_timer(wave["move_rock"], 0)


    def mess(self,mess,who,plus_dok):
        if mess == "камень достиг пола":
            self.rocks.remove(who)


    def draw(self, place: pygame.Surface):

        for rk in self.rocks:

            rk.draw(place)




