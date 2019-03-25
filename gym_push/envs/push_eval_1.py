import gym
from gym import error, spaces, utils
from gym.utils import seeding
import pandas as pd
import numpy as np
import os 
import json
from joblib import load

'''

EvalUMAP Challenge 1 Test Environment

'''

class PushEval1(gym.Env):
    metadata = {'render.modes': ['human']}
    

    def __init__(self):
        
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.currentUser = ''
        self.currentContextData = pd.DataFrame()
        self.userNames = []
                
        
        # Load test data 
        self.test_data = {}
        files = os.listdir(dir_path+'/test_data/')
        for name in files:
            self.userNames.append(str(name))
            n = pd.read_csv(dir_path+'/test_data/'+name+'/notifications.csv')
            n = n.drop([n.columns[0]], axis=1)
            self.test_data[name] = n
            
        
        # Load classifiers (to mimic user) trained on training data
        self.le = load(dir_path+'/classifiers/labelEncoders.joblib')
        self.ohe = load(dir_path+'/classifiers/ohe.joblib')
        self.classifiers = {}
        for name in files:
            clf = load(dir_path+'/classifiers/clf_'+name+'.joblib')
            self.classifiers[name] = clf
            
    
    def getContext(self, userId):
        self.currentUser = userId
        temp = self.test_data[self.currentUser]
        temp = temp[['activityContextPosted',
                     'averageNoisePosted', 'batteryLevelPosted', 'chargingPosted', 
                     'headphonesInPosted', 'lightIntensityPosted', 'musicActivePosted', 
                     'placeCategoryPosted', 'proximityPosted', 'ringerModePosted', 
                     'timeOfDayPosted', 'dayOfWeekPosted' ]]
        temp.columns = ['activity',
                     'noise', 'batteryLevel', 'charging', 
                     'headphonesIn', 'lightIntensity', 'musicActive', 
                     'place', 'proximity', 'ringerMode', 
                     'time', 'day']
        self.currentContextData = temp
        return self.currentContextData
    
    def testNotifications(self, data):
        if(len(data) == len(self.test_data)):
            # Use the classifier to predict open or dismiss
            # - combine context to data
            data = data.append(self.currentContextData)
            # - add original action for notification in this context (just need True/False to be present!)
            data['action'] = self.test_data[self.currentUser].action
            # - sort columns correctly
            data = data[['postingApp', 'category', 'numberOfUpdates', 'subject', 'priority',
                       'ongoing', 'visibility', 'activity', 'noise', 'batteryLevel',
                       'charging', 'headphonesIn', 'lightIntensity', 'musicActive', 'place',
                       'proximity', 'ringerMode', 'day', 'time', 'action']]
            # - convert data to labels
            # - convert label to ohe
            # - get results from classifier
        
        # Compare with original action taken for notification in that context
        
        # Compare with classifier prediction for notification in that context
        
        # Diversity metrics.. 
        
        return 'results'
    
    def getUserNames(self):
        return self.userNames
       
    def reset(self):
        return 'reset'
        
    def render(self, mode='human', close=False):
        print('do render push')