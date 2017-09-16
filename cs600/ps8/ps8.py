# 6.00 Problem Set 8
#
# Name: Haoyu Yun
# Collaborators:
# Time: 3:00

# BUG: Python 2 gives twice the viruses??

import numpy
import random
import pylab
from ps7 import *

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):

    """
    Representation of a virus which can have drug resistance.
    """      

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        

        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb


    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances[drug]


    def reproduce(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                raise NoChildException

        child_resistances = {}
        if random.random() < self.maxBirthProb * (1 - popDensity):
            for drug in self.resistances:
                child_resistances[drug] = self.resistances[drug]
                if random.random() < self.mutProb:
                    child_resistances[drug] = True if child_resistances[drug] == False else False
            return ResistantVirus(self.maxBirthProb, self.clearProb, child_resistances, self.mutProb)

        raise NoChildException
            

class Patient(SimplePatient):

    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        self.activeDrugs = []
        self.vnum = len(viruses)
    

    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if newDrug not in self.activeDrugs:
            self.activeDrugs.append(newDrug)


    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.activeDrugs
        

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistPop = self.getTotalPop()
        for v in self.viruses:
            for d in drugResist:
                if not v.isResistantTo(d):
                    resistPop -= 1
                    break
        return resistPop


    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        for v in self.viruses:
            if v.doesClear():
                self.viruses.remove(v)
                self.vnum -= 1
        self.popDensity = self.vnum/self.maxPop
        
        nextViruses = self.viruses

        for v in self.viruses:
            try:
                nextViruses.append(v.reproduce(self.popDensity, self.activeDrugs))
                self.vnum += 1
            except NoChildException:
                pass

        self.viruses = nextViruses
        return self.vnum



#
# PROBLEM 2
#

def simulationWithDrug():

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    trials = 3
    time = 300
    timesteps = [x for x in range(time)]
    v_avgs = [0]*time
    r_avgs = [0]*time

    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    startPop = 100
    maxPop = 1000

    for t in range(trials):
        simulate(maxBirthProb, clearProb, resistances, mutProb, startPop, maxPop, time, v_avgs, r_avgs)
    for t in timesteps:
        v_avgs[t] /= float(trials)
        r_avgs[t] /= float(trials)

    pylab.plot(timesteps, v_avgs, '-b', label="total")
    pylab.plot(timesteps, r_avgs, '-g', label="resistant")
    pylab.xlabel('Time Steps')
    pylab.ylabel('Virus Population')
    pylab.title('Virus Numbers Across Time')
    pylab.show()    


def simulate(maxBirthProb, clearProb, resistances, mutProb, startPop, maxPop, time, v_avgs, r_avgs):
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)]*startPop
    patient = Patient(viruses, maxPop)

    timesteps = [x for x in range(time)]
    vnum = []
    rnum = []

    for t in range(time//2):
        vnum.append(patient.update())
        rnum.append(patient.getResistPop(['guttagonol']))#patient.getPrescriptions()))
    patient.addPrescription('guttagonol')
    for t in range(time//2):
        vnum.append(patient.update())
        rnum.append(patient.getResistPop(patient.getPrescriptions()))

    for t in timesteps:
        v_avgs[t] += vnum[t]
        r_avgs[t] += rnum[t]

#simulationWithDrug()
# Non-resistant drug virus number drops sharply once drug introduced,
# but resistant virus numbers increase sharply

#
# PROBLEM 3
#        

def simulationDelayedTreatment():

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    delays = [300,150,75,0]
    finalResults = {}

    for d in delays:
        timePre = d
        timePost = 150
        trials = 500
        timesteps = [x for x in range(timePre+timePost)]
        v_res = []
        r_res = []

        maxBirthProb = 0.1
        clearProb = 0.05
        resistances = {'guttagonol': False}
        mutProb = 0.005
        startPop = 100
        maxPop = 1000

        for t in range(trials):
            simulate2(maxBirthProb, clearProb, resistances, mutProb, startPop, maxPop, timePre, timePost, v_res, r_res)
        finalResults[d] = v_res

    plotNum = 1
    for n in delays:
        pylab.subplot(2, 2, plotNum)
        pylab.title("delay: " + str(n))
        pylab.xlabel("final virus counts")
        pylab.ylabel("# trials")
        pylab.hist(finalResults[n], bins=12, range=(0, 600)) # each bin of size 50
        plotNum += 1

    pylab.show()
        

def simulate2(maxBirthProb, clearProb, resistances, mutProb, startPop, maxPop, timePre, timePost, v_res, r_res):
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)]*startPop
    patient = Patient(viruses, maxPop)

    #v_avg = []

    for t in range(timePre):
        patient.update()
        #v_avg.append(patient.update())
    patient.addPrescription('guttagonol')
    for t in range(timePost):
        patient.update()
        #v_avg.append(patient.update())

    v_res.append(patient.getTotalPop())
    r_res.append(patient.getResistPop(patient.getPrescriptions()))

#simulationDelayedTreatment()

#
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment():

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    delays = [300,150,75,0]
    finalResults = {}
    trials = 2

    for d in delays:
        timePre = 150
        timePre2 = d
        timePost = 150
        v_res = []
        r_res = []

        maxBirthProb = 0.1
        clearProb = 0.05
        resistances = {'guttagonol': False, 'grimpex': False}
        mutProb = 0.005
        startPop = 100
        maxPop = 1000

        for t in range(trials):
            simulate3(maxBirthProb, clearProb, resistances, mutProb, startPop, maxPop, timePre, timePre2, timePost, v_res, r_res)
            if (t%10==0):
                print("at delay", d, "|| at trial", t)
        finalResults[d] = v_res

    plotNum = 1
    for d in delays:
        pylab.subplot(2, 2, plotNum)
        pylab.title("delay: " + str(d))
        pylab.xlabel("final virus counts")
        pylab.ylabel("# trials")
        pylab.hist(finalResults[d], bins=12, range=(0, 600)) # each bin of size 50
        plotNum += 1

        cured = finalResults[d].count(0)
        print("Delay:", d, "Cured(%): ", cured/trials*100)

    pylab.show()

def simulate3(maxBirthProb, clearProb, resistances, mutProb, startPop, maxPop, timePre, timePre2, timePost, v_res, r_res):
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)]*startPop
    patient = Patient(viruses, maxPop)
    time = timePre+timePre2+timePost

    #v_avg = []

    for t in range(time):
        if (t == timePre):
            patient.addPrescription('guttagonol')
        if (t == timePre+timePre2):
            patient.addPrescription('grimpex')
        patient.update()
        #v_avg.append(patient.update())

    v_res.append(patient.getTotalPop())
    r_res.append(patient.getResistPop(patient.getPrescriptions()))

#simulationTwoDrugsDelayedTreatment()

#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations():

    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        

    """
    finalResults = {}
    trials = 100

    timePre = 150
    timePre2 = 300
    timePost = 150
    time = timePre+timePre2+timePost
    timesteps = [x for x in range(time)]

    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    startPop = 100
    maxPop = 1000

    v_avgs=[0]*time
    rgut_avgs=[0]*time
    rgri_avgs=[0]*time
    rboth_avgs=[0]*time

    for t in range(trials):
        if (t % 20 == 0):
            print("running trial", t)
        trial_avgs = simulate4(maxBirthProb, clearProb, resistances, mutProb, startPop, maxPop, timePre, timePre2, timePost)
        for t in range(time):
            v_avgs[t] += trial_avgs[0][t]
            rgut_avgs[t] += trial_avgs[1][t]
            rgri_avgs[t] += trial_avgs[2][t]
            rboth_avgs[t] += trial_avgs[3][t]

    for t in timesteps:
        v_avgs[t] /= float(trials)
        rgut_avgs[t] /= float(trials)
        rgri_avgs[t] /= float(trials)
        rboth_avgs[t] /= float(trials)

    pylab.plot(timesteps, v_avgs, '-b', label="total")
    pylab.plot(timesteps, rgut_avgs, '-g', label="guttagonol-resistant")
    pylab.plot(timesteps, rgri_avgs, '-r', label="grimpex-resistant")
    pylab.plot(timesteps, rboth_avgs, '-y', label="both-resistant")
    pylab.legend(loc='upper right')
    pylab.xlabel('Time Steps')
    pylab.ylabel('Virus Population')
    pylab.title('Virus Numbers Across Time')
    pylab.show() 

def simulate4(maxBirthProb, clearProb, resistances, mutProb, startPop, maxPop, timePre, timePre2, timePost):
    viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)]*startPop
    patient = Patient(viruses, maxPop)
    time = timePre+timePre2+timePost

    vals = [[0 for x in range(time)] for y in range(4)]

    for t in range(time):
        if (t == timePre):
            patient.addPrescription('guttagonol')
        if (t == timePre+timePre2):
            patient.addPrescription('grimpex')
        patient.update()
        vals[0][t] = patient.getTotalPop()
        vals[1][t] = patient.getResistPop(['guttagonol'])
        vals[2][t] = patient.getResistPop(['grimpex'])
        vals[3][t] = patient.getResistPop(['grimpex','guttagonol'])
    return vals

simulationTwoDrugsVirusPopulations()


'''
To simulate patient non-compliance, I could
1) Randomly take or not take given drugs during a certain timestep
2) Randomly remove or add the drug during a certain timestep

Both would give the same non-compliance rate (both give binary based on random)
but 1) would be better organized

'''