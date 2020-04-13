from math import *
import random

class robot:
    
    # --------
    # init:
    #   creates a robot with the specified parameters and initializes
    #   the location (self.x, self.y) to the center of the world
    #
    
    def __init__(self, world_size = 100.0, measurement_range = 30.0,
                 motion_noise = 1.0, measurement_noise = 1.0):
        self.measurement_noise = 0.0
        self.world_size = world_size
        self.measurement_range = measurement_range
        self.x = world_size / 2.0
        self.y = world_size / 2.0
        self.motion_noise = motion_noise
        self.measurement_noise = measurement_noise
        self.landmarks = []
        self.num_landmarks = 0
    
    
    # returns a positive, random float
    def rand(self):
        return random.random() * 2.0 - 1.0
    
    
    # --------
    # move: attempts to move robot by dx, dy. If outside world
    #       boundary, then the move does nothing and instead returns failure
    #
    
    def move(self, dx, dy):
        
        x = self.x + dx + self.rand() * self.motion_noise
        y = self.y + dy + self.rand() * self.motion_noise
        
        if x < 0.0 or x > self.world_size or y < 0.0 or y > self.world_size:
            return False
        else:
            self.x = x
            self.y = y
            return True


    # --------
    # sense: returns x- and y- distances to landmarks within visibility range
    #
    
    def sense(self):

        measurements = []
        dx = 0
        dy = 0
        # for each landmark sensed by the robot...
        for i in range(len(self.landmarks)):
            # calculate the distances between the robot(x,y) and landmark(x,y)...
            dx, dy = self.landmarks[i][0] - self.x, self.landmarks[i][1] - self.y
            # simulate noise in the robot's real-world sense measurements...
            noise_dx = self.rand() * self.measurement_noise
            noise_dy = self.rand() * self.measurement_noise
            # add the simulated noise values to the calculated distance values...
            dx = dx + noise_dx
            dy = dy + noise_dy
            
            # if the landmarks lie within the robot's built-in measurement range...
            if abs(dx) < self.measurement_range and abs(dy) < self.measurement_range:
                    # add the landmark and the calculated differences in distance to the meausrements array
                    measurements.append([i, dx, dy])
        
        return measurements

    # --------
    # make_landmarks:
    # randomly generate landmarks located in the world
    #
    
    def make_landmarks(self, num_landmarks):
        self.landmarks = []
        for i in range(num_landmarks):
            self.landmarks.append([round(random.random() * self.world_size),
                                   round(random.random() * self.world_size)])
        self.num_landmarks = num_landmarks


    # called when print(robot) is called; prints the robot's location
    def __repr__(self):
        return 'Robot: [x=%.5f y=%.5f]'  % (self.x, self.y)


####### END robot class #######