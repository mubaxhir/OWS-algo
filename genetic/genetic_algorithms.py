import base64
import math
import random
import re
import time
import zerorpc

import os
import sys
import json

ENDPOINT = 3000
totalWeights = 4
numTop = 2
gamesPer = 2
temp = numTop**totalWeights
POPULATION_SIZE = temp * 2
TOTAL_GENS = 1000

BOUNDS = {
    'splitX': 6,
    'splitY': 6,
    'splitZ': 20
}

INIT_Z = 15

COLLISION = { 'NONE': 0, 'WALL': 1, 'GROUND': 2 }
FIELD = { 'EMPTY': 0, 'ACTIVE': 1, 'PETRIFIED': 2 }

# class Rack():
#     def __init__(self, heuristics):
#         self.Board.init()
#         self.movesDone = []
#         self.gameOver = False
#         self.currentPoints = 0
#         self.heuristics = heuristics
#         self.data = json.dumps({ 'score': self.start(), 'moves': self.generateCode() })

#     def generateCode(self):
#         code = ""
#         for m in self.movesDone:
#             code += m.shape
#             code += ","
#             code += m.position.x + "|" + m.position.y
#             code += ","
#             code += math.floor(m.rotation.x / 90) + "|" + math.floor(m.rotation.y / 90) + "|" + math.floor(m.rotation.z / 90)
#             code += ""
        
#         code = base64.encodeURI(code[0:len(code)-1] if (code) > 0 else code)
#         return code

#     def start(self):
#         self.Block.generate()
#         return self.animate()

#     def animate(self):
#         while (not self.gameOver and self.makeMove()):
#             self.drop()
        
#         return self.finished()

#     def addPoints(self, n):
#         self.currentPoints += n

#     def drop(self, ):
#         while True:
#             move = self.Block.move(0, 0, -1)
#             if move:
#                 break
    
#     def makeMove(self):
#         best = None
#         b = float('-inf')
#         for move in self.allMoves():
#             u = self.Heuristic.utility(move.fields, self.heuristics)
#             if u > b or best is None:
#                 b = u
#                 best = move
        
#         if best is None:
#             return False
        
#         self.movesDone.append({ 'shape': self.Block.blockType, 'position': best.position, 'rotation': best.rotation })
#         self.Block.rotate(best.rotation.x, best.rotation.y, best.rotation.z)
#         self.Block.move(best.position.x - self.Block.position.x, best.position.y - self.Block.position.y, 0)
#         return True

#     def allMoves(self):
#         moves = []
#         rotations = self.Block.possibleRotations()
#         for i in range(len(rotations.rotates)):
#             rotation = rotations.rotates[i]
#             shape = rotations.shapes[i]
#             for x in range(BOUNDS.splitX):
#                 for y in range(BOUNDS.splitY):
#                     position = { 'x':x, 'y':y, 'z': INIT_Z }
#                     if (self.Board.testCollision(False, self.Board.fields, position, shape) != COLLISION.WALL):
#                         while (self.Board.testCollision(True, self.Board.fields, position, shape) != COLLISION.GROUND):
#                             position.z -= 1
                        
#                         fields = self.Utils.cloneField(self.Board.fields)
#                         self.Block.petrify(shape, fields, position, False)
#                         moves.append({ rotation, position, fields })
                    
#         return moves

#     def finished(self):
#         return self.movesDone.length


#     class Heuristic():
#         def utility(self, fields, heuristics):
#             s = 0
#             for key in range(len(heuristics)):
#                 if not re.match('/^_/', key) and heuristics.hasOwnProperty(key) and callable(self[key]):
#                     s += self[key](fields) * heuristics[key]
                
#             return s
        
#         def _holes_in_board(fields):
#             holes = []
#             block_in_col = False
#             for x in range(BOUNDS.splitX):
#                 for y in range(BOUNDS.splitY):
#                     for z in range(BOUNDS.splitZ-1,0):
#                         if block_in_col and fields[x][y][z] == FIELD.EMPTY:
#                             holes.push({ x, y, z })
#                         elif fields[x][y][z] != FIELD.EMPTY:
#                             block_in_col = True
                        
#                     block_in_col = False
                
#             return holes
        
#         def _heights(fields):
#             heights = {}

#             for y in range(BOUNDS.splitY):
#                 for x in range(BOUNDS.splitX):
#                     key = x + "-" + y
#                     for z in range(BOUNDS.splitZ-1,0):
#                         if fields[x][y][z] != FIELD.EMPTY:
#                             heights[key] = z + 1
#                             break
                        
                    
#                     heights[key] = 0
                
            
#             return heights
        
#         def num_holes(self, fields = Rack.Board.fields):
#             return self._holes_in_board(fields).length
        
#         def num_blocks_above_holes(self, fields = Rack.Board.fields):
#             c = 0
#             for hole in self._holes_in_board(fields):
#                 for z in range(hole.z + 1,BOUNDS.splitZ):
#                     if fields[hole.x][hole.y][z] != FIELD.EMPTY:
#                         c+=1
#                     else:
#                         break
                    
#             return c

#         def num_gaps(self, fields = Rack.Board.fields):
#             gaps = 0
#             for z in range(BOUNDS.splitZ):
#                 for y in range(BOUNDS.splitY):
#                     sequence = 1
#                     for x in range(BOUNDS.splitX):
#                         if sequence == 0 and fields[x][y][z] != FIELD.EMPTY:
#                             sequence = 1
#                         elif (sequence == 1 and fields[x][y][z] == FIELD.EMPTY):
#                             sequence = 2
#                         elif (sequence == 2):
#                             if (fields[x][y][z] != FIELD.EMPTY):
#                                 gaps+=1
#                                 sequence = 1
#                             else:
#                                 sequence = 0
                            
#                     if (sequence == 2):
                        
#                         gaps+=1
                    
#             return gaps
        
#         def max_height(self, fields = Rack.Board.fields):
#             for z in range(BOUNDS.splitZ,0):
#                 for y in range(BOUNDS.splitY):
#                     for x in range(BOUNDS.splitX):
#                         if (fields[x][y][z] != FIELD.EMPTY):
#                             return z + 1
                        
#             return 0
        
#         def avg_height(self, fields = Rack.Board.fields):
#             len = 0
#             total = 0

#             for y in range(BOUNDS.splitY):
#                 for x in range(BOUNDS.splitX):
#                     for z in range(BOUNDS.splitZ-1,0):
#                         if fields[x][y][z] != FIELD.EMPTY:
#                             total += z + 1
#                             len+=1
#                             break
                    
#             return total / len
        
#         def num_blocks(self, fields = Rack.Board.fields):
#             c = 0
#             for z in range(BOUNDS.splitZ):
#                 for y in range(BOUNDS.splitY):
#                     for x in range(BOUNDS.splitX):
#                         if (fields[x][y][z] != FIELD.EMPTY):
#                             c+=1  
#             return c
        
#         def completed_lines(fields = Rack.Board.fields):
#             return len(Rack.Board.checkCompleted(fields))
        
#         def bumpiness(self, fields = Rack.Board.fields):
#             total_bumpy = 0
#             obj = self._heights(fields)
#             for y in range(BOUNDS.splitY-1):
#                 for x in range(BOUNDS.splitX):
#                     if (x < BOUNDS.splitX - 1):
#                         total_bumpy += math.abs(obj[x + "-" + y] - obj[(x + 1) + "-" + y])
                    
#                     total_bumpy += math.abs(obj[x + "-" + y] - obj[x + "-" + (y + 1)])
                
#             return total_bumpy
        
#         class Utils():
#             def cloneVector(v):
#                 return Object.assign({}, v)
            
#             def roundVector(v):
#                 v.x = math.round(v.x)
#                 v.y = math.round(v.y)
#                 v.z = math.round(v.z)
            
#             def cloneField(f):
#                 fields = Rack.Board.initFields()
#                 for x in range(BOUNDS.splitX):
#                     for y in range(BOUNDS.splitY):
#                         for z in range(BOUNDS.splitZ):
#                             fields[x][y][z] = f[x][y][z]
                        
#                 return fields



#     class Block():
#         def generate(self):
#             type = math.floor(math.random() * (len(CUBE_SHAPES)))
#             self.blockType = type

#             self.shape = []
#             for i in range(CUBE_SHAPES[type].length):
#                 self.shape[i] = Rack.Utils.cloneVector(CUBE_SHAPES[type][i])
#                 self.shape[i].z = 0
            

#             self.position = {
#                 'x': math.floor(BOUNDS.splitX / 2) - 1,
#                 'y': math.floor(BOUNDS.splitY / 2) - 1,
#                 'z': INIT_Z
#             }

#             if (Rack.Board.testCollision(True) == COLLISION.GROUND):
#                 Rack.gameOver = True
            
#             self.rotation = { 'x': 0, 'y': 0, 'z': 0 }
        
#         def rotate(self, x, y, z):
#             oldRotation = Rack.Utils.cloneVector(self.rotation)
#             self.rotation.x += x * math.PI / 180
#             self.rotation.y += y * math.PI / 180
#             self.rotation.z += z * math.PI / 180

#             oldShapes = []

#             for i in range(self.shape.length):
#                 oldShapes.push(self.shape[i])
            
#             self.shape = self.rotateShape(self.rotation.x, self.rotation.y, self.rotation.z)

#             if (Rack.Board.testCollision(False) == COLLISION.WALL):
#                 self.shape = oldShapes
#                 self.rotation = oldRotation
            

#         def rotateShape(self, x, y, z):
#             rotateX = new THREE.Vector3(1, 0, 0)
#             rotateY = new THREE.Vector3(0, 1, 0)
#             rotateZ = new THREE.Vector3(0, 0, 1)
#             shapes = []
#             for i in range(self.shape.length):
#                 shape = CUBE_SHAPES[self.blockType][i]

#                 vector = new THREE.Vector3(shape.x, shape.y, 0)
#                 vector.applyAxisAngle(rotateX, x)
#                 vector.applyAxisAngle(rotateY, y)
#                 vector.applyAxisAngle(rotateZ, z)
#                 shapes.push({ x: vector.x, y: vector.y, z: vector.z })

#                 Rack.Utils.roundVector(shapes[i])
            
#             return shapes
        
#         def possibleRotations(self):
#             types = [0, 90, -90, 180]
#             coords = [
#                 [0, 0, 1],
#                 [0, 1, 0],
#                 [1, 0, 0]
#             ]
#             ret = []
#             rotates = []
#             for t in types:
#                 for c in coords:
#                     shapes = self.rotateShape(c[0] * t * math.PI / 180, c[1] * t * math.PI / 180, c[2] * t * math.PI / 180)
#                     cmp = json.stringify(shapes)
#                     # if (not ret.some( =>  == cmp)):
#                     if cmp in ret.map(lambda ele : json.stringify(ele)):
#                         ret.push(shapes)
#                         rotates.push({ 'x': c[0] * t, 'y': c[1] * t, 'z': c[2] * t })
                    
#             return { 'shapes': ret, 'rotates': rotates }
        
#         def move(self, x, y, z):
#             oldPos = Rack.Utils.cloneVector(self.position)
#             self.position.x += x
#             self.position.y += y
#             self.position.z += z

#             collision = Rack.Board.testCollision(z != 0)

#             if (collision == COLLISION.WALL):
#                 self.position = oldPos
            
#             if (collision == COLLISION.GROUND):
#                 self.hitBottom()
#                 Rack.Board.complete()
#                 return True
            
#             return False
        
#         def petrify(self, shape=None, fields=None, position=None, other=None):

#             if not shape: shape = self.shape
#             if not fields: fields = Rack.Board.fields
#             if not position: position = self.position
#             if not other: other = True
            
#             for i in shape:
#                 fields[position.x + i.x][position.y + i.y][position.z + i.z] = FIELD.PETRIFIED
                
#         def hitBottom(self):
#             self.petrify()
#             self.generate()


    
#     class Board():
#         def __init__(self, heuristics):
#             self.fields = self.initFields()

#         def initFields():
#             fields = []
#             for x in range(BOUNDS.splitX):
#                 fields.append([])
#                 for y in range(BOUNDS.splitY):
#                     fields[x].append([])
#                     for z in range(BOUNDS.splitZ):
#                         fields[x][y].append(FIELD.EMPTY)
            
#             return fields

#         def testCollision(ground_check, fields = self.fields, position = Rack.Block.position, shape = Rack.Block.shape):
#             posx = position.x
#             posy = position.y
#             posz = position.z

#             for i in shape:
#                 if (i.x + posx) < 0 or (i.y + posy) < 0 or (i.x + posx) >= BOUNDS.splitX or (i.y + posy) >= BOUNDS.splitY:
#                     return COLLISION.WALL

#                 if fields[i.x + posx][i.y + posy][i.z + posz - 1] == FIELD.PETRIFIED:
#                     return COLLISION.GROUND if ground_check else COLLISION.WALL
                
#                 if (i.z + posz) <= 0:
#                     return COLLISION.GROUND
                
#             return COLLISION.NONE
        
#         def complete(self):
#             bonus = 0
#             for c in self.checkCompleted(self.fields):
#                 bonus += 1 + bonus
#                 for y2 in range(BOUNDS.splitY):
#                     for x2 in range(BOUNDS.splitX):
#                         for z2 in range(c, BOUNDS.splitZ-1):
#                             self.fields[x2][y2][z2] = self.fields[x2][y2][z2 + 1]

#                         self.fields[x2][y2][BOUNDS.splitZ - 1] = FIELD.EMPTY
                    
#             Rack.addPoints(bonus * 1000)
        
#         def checkCompleted(fields):
#             rebuild = False
#             expected = BOUNDS.splitY * BOUNDS.splitX
#             c = []

#             for z in range(BOUNDS.splitZ):
#                 found = True
#                 for y in range(BOUNDS.splitY) and found:
#                     for x in range(BOUNDS.splitX):
#                         if (fields[x][y][z] != FIELD.PETRIFIED):
#                             found = False
#                             break
#                 if found: c.append(z)
        
#             return c
        
            




class Simulation():
    def __init__(self):
        self.client = zerorpc.Client(timeout=30000, heartbeat=None)
        self.client.connect('tcp://127.0.0.1:' + str(ENDPOINT))

    def simulate(self, heuristics=None):
        if heuristics == None:
            heuristics = {}
        try:
            return json.loads(self.client('simulate', json.dumps(heuristics)))
        except zerorpc.exceptions.LostRemote:
            self.__init__()
            return self.simulate(heuristics)


def getRand(range=1):
    return random.uniform(-range, range)

class Chromosome(object):

    def avg_fitness(self):
        return self.total_fitness / self.games

    def __init__(self, weights, cond):
        self.weights = []
        if cond != 1:
            self.weights = weights
        else:
            for i in range(totalWeights):
                self.weights.append(getRand())
        self.total_fitness = 0
        self.games = 0
        self.time = 0
        self.code = ''


class GeneticAlgorithm(object):

    def genScore(self, weights):
        myMap = {}
        myMap['num_holes'] = weights[0] #110, 0.64s
        myMap['avg_height'] = weights[1] #110, 0.82s
        myMap['num_blocks_above_holes'] = weights[2] #110, 0.73s
        myMap['num_gaps'] = weights[3] #64, 0.26s

    #     ###myMap['num_blocks'] = weights[0] #46, 0.26s
    #     ####myMap['bumpiness'] = weights[0] # 40, 0.46s <-- no better than random
    #     ####myMap['max_height'] = weights[0] #41, 0.17s <-- no better than random
    #     ####myMap['completed_lines'] = weights[0] #40, 0.17s <-- no better than random

        t = time.time()
        result = self.sim.simulate(myMap)
        return (time.time() - t, result['score'], result['moves']) # moves ki jaga apny boxes bhejo

    def __init__(self):
        self.population = []
        for i in range(POPULATION_SIZE):
            self.population.append(Chromosome(None,1))
        self.current_chromosome = 0
        self.current_generation = 1
        self.sim = Simulation()
        self.totalScore = 0

    def next_generation(self):
        if self.current_generation >= TOTAL_GENS:
            return None
        #where the gen algorithm goes
        print("__________________\n")
        print("GEN: " + str(self.current_generation))
        result = str(self.current_generation) + '\n'
        population = self.population
        self.totalScore = 0
        self.totalTime = 0
        for i in population:
            for q in range(gamesPer):
                i.games += 1
                # i.total_fitness = self.genScore(i.weights)
                res = self.genScore(i.weights)
                i.time += res[0]
                i.total_fitness += res[1]
                i.code = res[2]
        print("got scores")
        top = self.getTop(population)
        for i in top:
            self.totalScore += i.avg_fitness()
            self.totalTime += i.time
            result += str(i.avg_fitness()) + '\n'
            result += i.code + '\n'
            result += str(i.weights) + '\n'
        result += str(self.totalScore / len(top)) + '\n'
        print("score: " + str(self.totalScore / len(top)))
        print("time: " + str(self.totalTime / len(top)))
        weights = []

        #get n^k from breeding
        breed = self.cross(top)
        for v in breed:
            weights.append(v)
        #randomly gen 4 more
        for v in range(POPULATION_SIZE- temp):
            weights.append(Chromosome(None, 1).weights)
        self.current_generation = self.current_generation + 1
        if self.current_generation == TOTAL_GENS:
            return result
        self.population = []
        for i in range(POPULATION_SIZE):
            self.population.append(Chromosome(weights[i],0))
        return result

    def cross(self, top):
        weightList = []
        numVars = len(top[0].weights)
        for i in range(len(top)**numVars):
            tempList = []
            invert = random.randint(0,numVars)

            for j in range(numVars):
                w = top[(i // (len(top) ** j)) % len(top)].weights[j]
                if j == invert and random.uniform(0,1) < 0.2:
                    w = -w
                tempList.append(w)
            weightList.append(tempList)
        return weightList

    def nextChrome(self):
        self.current_chromosome += 1
        if self.current_chromosome >= POPULATION_SIZE:
            self.current_chromosome = 0
            self.next_generation()

    def getTop(self, population):
        return sorted(population,key = lambda x: x.avg_fitness())[-numTop:]

GA = GeneticAlgorithm()

if __name__ == '__main__':
    f = open('file.txt', 'w')
    f2 = open('file2.txt', 'w')
    while True:
        s = GA.next_generation()
        if s is None:
            break
        f.write(s)
        print(s, file=f2)
    f.close()
    f2.close()
