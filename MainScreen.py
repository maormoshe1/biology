import copy
import random
import time
import tkinter as tk
import ParameterScreen
from ParameterScreen import *

greed_side = 100
rect_side = 5
greed_size = greed_side * greed_side
gray1 = '#404040'
gray2 = '#808080'
gray3 = '#b0b0b0'
bordeaux = '#a00000'
reds = []

class People:
    def __init__(self, doubt, isSpreader, isAccept, not_spread):
        self.doubt = doubt
        self.isSpreader = isSpreader
        self.isAccept = isAccept
        self.not_spread = not_spread

class MainScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.population = []
        self.generationNum = 0
        self.generate_population()
        #self.generate_strategic_population()
        self.labelGenerationNum = tk.Label(self, text="Generation Num:" + str(self.generationNum), font=("Arial", 12))
        self.labelGenerationNum.pack()
        self.canvas = tk.Canvas(self, width=greed_side*rect_side, height=greed_side*rect_side)
        self.canvas.pack(padx=10, pady=10)
        self.draw_grid()
        tk.Button(self, text="Go back to Main Screen", command=self.goto_param_screen).pack()
        tk.Button(self, text="Next Generation", command=self.next_generation).pack()
        tk.Button(self, text="Next 10 Generations", command=self.next_generation_loop).pack()

    #people cell - People(), empty cell - 0
    def generate_population(self):
        params = ParameterScreen.params
        for i in range(greed_size):
            self.population.append(0)
        sum_of_people = greed_size*int(params.population) / 100
        S1 = sum_of_people * int(params.S1) / 100
        S2 = sum_of_people * int(params.S2) / 100
        S3 = sum_of_people * int(params.S3) / 100
        S4 = sum_of_people * int(params.S4) / 100
        while S1 != 0:
            index = random.randint(0, greed_size-1)
            if (self.population[index] == 0):
                self.population[index] = People(3, False, False, 0)
                S1 -= 1
        while S2 != 0:
            index = random.randint(0, greed_size-1)
            if (self.population[index] == 0):
                self.population[index] = People(2, False, False, 0)
                S2 -= 1
        while S3 != 0:
            index = random.randint(0, greed_size - 1)
            if (self.population[index] == 0):
                self.population[index] = People(1, False, False, 0)
                S3 -= 1
        while S4 != 0:
            index = random.randint(0, greed_size - 1)
            if (self.population[index] == 0):
                self.population[index] = People(0, False, False, 0)
                S4 -= 1
        self.population[random.randint(0,greed_size-1)] = People(4, True, True, 0)

    def generate_strategic_population(self):
        params = ParameterScreen.params
        bool = True
        for i in range(greed_size):
            self.population.append(0)
        print(len(self.population))
        sum_of_people = greed_size * int(params.population) / 100
        S1 = sum_of_people * int(params.S1) / 100
        S2 = sum_of_people * int(params.S2) / 100
        S3 = sum_of_people * int(params.S3) / 100
        S4 = sum_of_people * int(params.S4) / 100
        while S1 != 0:
            list1 = [*range(0,1250)]
            list11 = [*range(8750,10000)]
            rand = random.randint(0, 1249)
            if bool:
                index = list1[rand]
                bool = False
            else:
                index = list11[rand]
                bool = True
            print(index)
            if (self.population[index] == 0):
                self.population[index] = People(3, False, False, 0)
                S1 -= 1
        while S2 != 0:
            list2 = [*range(1250, 2500)]
            list21 = [*range(7500,8750)]
            rand = random.randint(0, 1249)
            if bool:
                index = list2[rand]
                bool = False
            else:
                index = list21[rand]
                bool = True
            if (self.population[index] == 0):
                self.population[index] = People(2, False, False, 0)
                S2 -= 1
        while S3 != 0:
            list3 = [*range(2500, 3750)]
            list31 = [*range(6250,7500)]
            rand = random.randint(0, 1249)
            if bool:
                index = list3[rand]
                bool = False
            else:
                index = list31[rand]
                bool = True
            if (self.population[index] == 0):
                self.population[index] = People(1, False, False, 0)
                S3 -= 1
        while S4 != 0:
            list4 = [*range(3750, 6250)]
            rand = random.randint(0, 2499)
            index = list4[rand]
            if (self.population[index] == 0):
                self.population[index] = People(0, False, False, 0)
                S4 -= 1
        '''outer_list1 = [*range(0, 2500)]
        outer_list2 = [*range(7500, 10000)]
        inner_list = [*range(2500,7500)]
        while S1 != 0:
            rand = random.randint(0, 2499)
            if bool:
                index = outer_list1[rand]
                bool = False
            else:
                index = outer_list2[rand]
                bool = True
            if (self.population[index] == 0):
                self.population[index] = People(3, False, False, 0)
                S1 -= 1
        while S2 != 0:
            rand = random.randint(0, 2499)
            if bool:
                index = outer_list1[rand]
                bool = False
            else:
                index = outer_list2[rand]
                bool = True
            if (self.population[index] == 0):
                self.population[index] = People(2, False, False, 0)
                S2 -= 1
        while S3 != 0:
            rand = random.randint(0, 4999)
            index = inner_list[rand]
            if (self.population[index] == 0):
                self.population[index] = People(1, False, False, 0)
                S3 -= 1
        while S4 != 0:
            rand = random.randint(0, 4999)
            index = inner_list[rand]
            if (self.population[index] == 0):
                self.population[index] = People(0, False, False, 0)
                S4 -= 1'''
        #
        # outer_list1 = [*range(0, 2500)]
        # outer_list2 = [*range(7500, 10000)]
        # inner_list = [*range(2500, 7500)]
        # while S4 != 0:
        #     rand = random.randint(0, 2499)
        #     if bool:
        #         index = outer_list1[rand]
        #         bool = False
        #     else:
        #         index = outer_list2[rand]
        #         bool = True
        #     if (self.population[index] == 0):
        #         self.population[index] = People(0, False, False, 0)
        #         S4 -= 1
        # while S3 != 0:
        #     rand = random.randint(0, 2499)
        #     if bool:
        #         index = outer_list1[rand]
        #         bool = False
        #     else:
        #         index = outer_list2[rand]
        #         bool = True
        #     if (self.population[index] == 0):
        #         self.population[index] = People(1, False, False, 0)
        #         S3 -= 1
        # while S2 != 0:
        #     rand = random.randint(0, 4999)
        #     index = inner_list[rand]
        #     if (self.population[index] == 0):
        #         self.population[index] = People(2, False, False, 0)
        #         S2 -= 1
        # while S1 != 0:
        #     rand = random.randint(0, 4999)
        #     index = inner_list[rand]
        #     if (self.population[index] == 0):
        #         self.population[index] = People(3, False, False, 0)
        #         S1 -= 1
        self.population[5050] = People(4, True, True, 0)


    def draw_grid(self):
        #redNum = 0
        for i in range(greed_side):
            for j in range(greed_side):
                x1 = j * rect_side
                y1 = i * rect_side
                x2 = x1 + rect_side
                y2 = y1 + rect_side
                #if self.get_color(i, j) == 'red' or self.get_color(i, j) == '#a00000':
                 #   redNum += 1
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.get_color(i, j), outline='black')
        #reds.append(redNum)

    #people cell - levels of gray, empty cell - white
    def get_color(self, i, j):
        index = i*greed_side + j
        if (self.population[index] == 0):
            return 'white'
        if (self.population[index].isSpreader):
            return bordeaux
        if (self.population[index].isAccept):
            return 'red'
        if (self.population[index].doubt == 0):
            return 'black'
        if (self.population[index].doubt == 1):
            return gray1
        if (self.population[index].doubt == 2):
            return gray2
        if (self.population[index].doubt == 3):
            return gray3

    def next_generation_loop(self):
        self.show_next_generation()

    def show_next_generation(self, count=0):
        if count == 10:
            return
        self.next_generation()
        self.after(1, lambda: self.show_next_generation(count + 1))

    def next_generation(self):
        next_pop = copy.deepcopy(self.population)
        #pass all population and spread rumor
        #first row
        for i in range(1, greed_side-1):
            neighbors = self.get_neighbors(i)
            self.spread_rumor(i, next_pop, neighbors)
        #last row
        for i in range((greed_side-1)*greed_side+1, greed_size-1):
            neighbors = self.get_neighbors(i)
            self.spread_rumor(i, next_pop, neighbors)
        #left coulmn
        for i in range(0, greed_size, greed_side):
            neighbors = self.get_neighbors(i)
            self.spread_rumor(i, next_pop, neighbors)
        #right coulmn
        for i in range(greed_side - 1, greed_size, greed_side):
            neighbors = self.get_neighbors(i)
            self.spread_rumor(i, next_pop, neighbors)
        #center
        for i in range(1, greed_side - 1):
            for j in range(1, greed_side - 1):
                k = i*greed_side + j
                neighbors = [k-greed_side-1,k-greed_side,k-greed_side+1,k-1,k+1,k+greed_side-1,k+greed_side,k+greed_side+1]
                self.spread_rumor(k, next_pop, neighbors)
        # pass all next population and update L parameter
        for i in range(greed_size):
            if (next_pop[i] != 0):
                if (next_pop[i].not_spread != 0):
                    next_pop[i].not_spread -= 1
                if (self.population[i].isSpreader and self.population[i].doubt != 4):
                    next_pop[i].not_spread = int(ParameterScreen.params.L)
                    if (int(ParameterScreen.params.L) != 0):
                        next_pop[i].isSpreader = False

        self.population = next_pop
        self.generationNum += 1
        self.draw_grid()
        self.labelGenerationNum.config(text="Generation Num:" + str(self.generationNum))

    def get_neighbors(self, i):
        neighbors = [i-greed_side-1,i-greed_side,i-greed_side+1,i-1,i+1,i+greed_side-1,i+greed_side,i+greed_side+1]
        if (i<=greed_side-1):
            neighbors[0] = -1
            neighbors[1] = -1
            neighbors[2] = -1
        if (i>=(greed_side - 1)*greed_side):
            neighbors[5] = -1
            neighbors[6] = -1
            neighbors[7] = -1
        if (i%greed_side == 0):
            neighbors[0] = -1
            neighbors[3] = -1
            neighbors[5] = -1
        if (i%greed_side == greed_side-1):
            neighbors[2] = -1
            neighbors[4] = -1
            neighbors[7] = -1
        return neighbors

    def spread_rumor(self, i, next_pop, neighbors):
        if (self.population[i] != 0):
            spreader_neighbor = 0
            for neighbor in neighbors:
                if (neighbor >= 0 and self.population[neighbor] != 0 and self.population[neighbor].isSpreader):
                    spreader_neighbor += 1
            if (spreader_neighbor > 0):
                doubt = next_pop[i].doubt
                if (spreader_neighbor >= 2):
                    doubt += 1
                if (not next_pop[i].isAccept):
                    next_pop[i].isSpreader = self.prob_to_sprade(doubt)
                    next_pop[i].isAccept = True
                elif (next_pop[i].not_spread == 0):
                    next_pop[i].isSpreader = self.prob_to_sprade(doubt)

    def prob_to_sprade(self, prob):
        if (prob == 0):
            return False
        if (prob >= 3):
            return True
        rand = random.randint(0,2)
        if (prob == 1):
            if (rand == 0):
                return True
            return False
        if (prob == 2):
            if (rand == 0):
                return False
            return True

    def goto_param_screen(self):
        self.master.switch_frame(ParameterScreen.ParamScreen)