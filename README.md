# Gym-Push


Gym-Push is an [OpenAI Gym](https://gym.openai.com/) environment for evaluating Reinforcement Learning algorithms on their performance managing push-notifications on behalf of a user. 

>Gym-push environments shall be used for evalutation in the [EvalUMAP 2019](http://evalumap.adaptcentre.ie/) challenge for personalised notification generation.


### Installation
Gym-push requires [gym](https://gym.openai.com/docs/#installation), [pandas](https://pandas.pydata.org/pandas-docs/stable/install.html) and [numpy](https://www.scipy.org/install.html)

Install via pip:
```sh
> pip install gym-push
```
Usage:
```sh
import gym
import gym_push
env = gym.make('push-v0')
```

### EvalUMAP Resources
---
1. Challenge Outline 
2. Data 
3. Model Guidelines
4. Using gym-push
5. Evaluation
---
##### 1. Challenge Outline

###### Challenge 1 
Participants are given 3 months of historical notification data. **The goal is to develop a user model, using the historical data, which takes a context as input and outputs a personalised notification for the given context**. Once the model is built, participants can test it using gym-push (see section 3). The environment provides an additional 3 months of contextual data to be used as input to the user model and will subsequently take the 3 months of personalised notifications generated and evaluate the results.

###### Challenge 2
Participants are asked to create a user model based on the same notification, context and engagement features but without historical notification data to train with. This user model should again take context as input and output a personalised notification. This user model will need to query the gym-push environment to receive a context feature and subsequently pass it a generated notification for evaluation.

As the environment steps through each context item and engagement history becomes available, it can be used by the user model to improve the generation of personalised notifications. **The goal is to develop a model which adapts and learns in real time how to generate personalised notifications without prior history of the user (cold-start problem).**

##### 2. Data

The data for the challenge can be found in the _data_ folder. Each folder therein contains 3 months of synthetic notification and context data for each user which can be used for creating the personalised model. A detailed breakdown of the features can be found in data/detail.ipynb.

##### 3. Model Guidelines

* For challenge 1, the user model should take a context as input and a personalised notification as output.
* Both the context and notification should be (strictly) represented by the following set of features (note: the names of features should not be changed):

  * **Notification:** 	{_postingApp, category, numberOfUpdates, subject, priority, ongoing, visibility_}
  * **Context:** 	{_day, time, place, activity, noise, batteryLevel, charging, headphonesIn,			 musicActive, proximity, ringerMode_}

* The values for each feature are also strictly limited to the sets provided [ref].
* For challenge 2, engagement history will also be available to the user model wishing to adapt in real time. Engagement history will be returned by the environment (as well as the context), when the environment is queried.
* Engagement history will be represented by the union of Notification and Context features (same as above) as well as an additional feature 'action', which conveys whether the notification was 'opened' or 'dismissed'.


##### 4. Using gym-push

To be added.

##### 5. Evaluation

The gym-push environment will evaluate the user models by deploying an agent to act as a user engaging with the generated personalised notifications. The agent will be trained on historical data of the user and decide, given the context, to open or dismiss the notification generated by the model. The following two metrics will be tracked in both challenge 1 and 2:

* _Diversity_ - This metric will evaluate the diversity of generated personalised notifications which have been accepted by the agent over the 3 months. Notification sets which boast greater diversity will be scored higher.
* _Performance_ - This metric will track and compare engagements resulting from the generated personalised notifications with those of the actual notifications. Scenarios which improve end-user engagements are scored higher (see table below).

| Actual Notification        | Personalised Generated Notification           | Reward  |
|:-------------:|:-------------:|:-----:|
| opened      | opened | +1 |
| dismissed      | dismissed      |   +0 |
| dismissed | opened      |    +2 |
| opened | dismissed      |    -1 |

Challenge 2 tracks additional metrics:

* _Response Time_ - This metric evaluates the time it takes the user model to generate a notification once given the context by the environment. Shorter times are scored higher. 
* _Learning Rate_ - This metric evaluates how quickly the performance metric (above) of the model improves over each step (context item) of the environment. 