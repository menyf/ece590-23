"""
Math 590
Project 3
Fall 2018

Partner 1: Yuqiao Liang(yl543)
Partner 2: Yifan Men(ym129)
Date: 11/24/2018
"""

# Import math.
import math

################################################################################

"""
detectArbitrage function will calculate the shortest path with Bellman Ford
Algorithm, judge wether there is a arbitrage. If there is an arbitrage, it
would return such path, otherwise an empty list.

INPUTS
currencies: the "graph" information of currencies
tol: tolerance to float

OUTPUTS
circle: the path that consist of an arbitrage
"""
def detectArbitrage(currencies, tol=1e-15):
    ##### Your implementation goes here. #####
    # Set initial dist  and prev
    for vertex in currencies.adjList:
        vertex.dist = math.inf
        vertex.prev = None

    # Set initial dist to 0;
    currencies.adjList[0].dist = 0

    # Bellman Ford Algorithm
    # Iterate |V| − 1 times
    for iter in range(0, len(currencies.adjList) - 1):
        # Look at each vertex.
        for u in currencies.adjList:
            # Check each neighbor of u.
            # Update predictions and previous vertex. If the new dist is smaller
            # than previous dist, update the dist to the new dist.
            for v in u.neigh:
                if v.dist > u.dist + currencies.adjMat[u.rank][v.rank] + tol:
                    v.dist = u.dist + currencies.adjMat[u.rank][v.rank]
                    v.prev = u

    # detect negative circle, run the iteration one more time. If any value changes,
    # negative cycle exisits.
    circle_flag = None;
    for u in currencies.adjList:
        # Check each neighbor of u.
        # Update predictions and previous vertex.
        for v in u.neigh:
            if v.dist > u.dist + currencies.adjMat[u.rank][v.rank] + tol:
                circle_flag = u
                break

    # Backtracking the record circle in a reversed way
    circle = []
    if circle_flag:
        circle.append(circle_flag.rank)
        u = circle_flag.prev
        while not u.isEqual(circle_flag):
            circle.append(u.rank)
            u = u.prev
        circle.append(circle_flag.rank)

    # Reverse the reversed path
    circle  = [circle[i] for i in range((len(circle) - 1), -1, -1) ]

    # Return such circle.
    return circle
    ##### Your implementation goes here. #####

################################################################################

"""
rates2mat function will calculate negative logarithmatic value of currency rates, since
we need the the values to be added for Bellman Ford algorithm.

INPUTS
rates: A 2D list consist of currency rate from one currency to another.

OUTPUTS
logged rates: A 2D list consist of values that is a negative logarithmatic value to the
original ones.
"""
def rates2mat(rates):
    ##### Your implementation goes here. #####
    # The weight in graph is the negative log of the corresponding currency.
    return [[-math.log(R) for R in row] for row in rates]
    ##### Your implementation goes here. #####

################################################################################

"""
Vertex Class
"""
class Vertex:

    """
    Class attributes:

    rank    # The rank of this node.
    neigh   # The list of neighbors.
    dist    # The distance from start.
    prev    # The previous vertex in the path.
    """

    """
    __init__ function to initialize the vertex.
    """
    def __init__(self, rank):

        self.rank = rank     # Set the rank of this vertex.
        self.neigh = []      # Set the input neighbors.
        self.dist = math.inf # Infinite dist initially.
        self.prev = None     # No previous node on path yet.
        return

    """
    __repr__ function to print a vertex.
    Note: only prints the rank!
    """
    def __repr__(self):
        return '%d' % self.rank

    """
    isEqual function compares this Vertex to an input Vertex object.
    Note: only needs to compare the rank!
    """
    def isEqual(self,vertex):
        return self.rank == vertex.rank

################################################################################

"""
Currencies Class
"""
class Currencies:

    """
    Class attributes:

    rates   # A 2D list of the different exchange rates.
    currs   # A list of the currency names as strings.
    adjList # The adjacency list for the currencies.
    adjMat  # The adjacency matrix for the graph.
    negCyc  # List of vertex ranks in the (potential) negative cost cycle.
    """

    """
    __init__ function to initialize the Currencies.
    """
    def __init__(self, exchangeNum=0):
        # Get the exchange rates and currency names.
        self.rates, self.currs = getRates(exchangeNum)

        # Create the adjacency list.
        self.adjList = [Vertex(r) for r in range(0, len(self.currs))]

        # Loop through the adjacency list and set each vertex's neigh list.
        # Note that each currency can be exchanged for any other currency,
        # so the neigh list will be every other vertex.
        for vInd in range(0,len(self.adjList)):
            (self.adjList[vInd]).neigh = self.adjList[0:vInd] + \
                                         self.adjList[vInd+1:]

        # Now get the adjacency matrix using the exchange rates.
        # Note: you will write this function above.
        self.adjMat = rates2mat(self.rates)

        # Set the negative cost cycle (nothing yet).
        self.negCyc = []
        return

    """
    __repr__ function to print the Currencies.
    """
    def __repr__(self):
        for cInd in range(0,len(self.currs)):
            print('Rates for %s:' % self.currs[cInd])
            print(self.rates[cInd])
        return ''

    """
    printList function for cleanly printing the adjaceny list.
    Note: skips vertices with no neighbors.
    """
    def printList(self):
        for vertex in self.adjList:
            if len(vertex.neigh) > 0:
                print('Rank: %d' % vertex.rank)
                print('Neighbors:')
                print(vertex.neigh)
                print('')
        return

    """
    printMat function for cleanly printing the adjaceny matrix.
    Note: for the larger matrices, this will still likely be hard to read.
    """
    def printMat(self):
        for row in self.adjMat:
            print(row)
        return

    """
    printArb function prints out the currencies in the negative cycle in order.
    """
    def printArb(self):
        for ind in self.negCyc:
            print(self.currs[ind])
        print()
        return

    """
    arbitrage
    """
    def arbitrage(self):
        # First, use your detectArbitrage function to find a potential
        # negative cost cycle in the graph.
        self.negCyc = detectArbitrage(self)

        # Report if no cycle.
        if len(self.negCyc) == 0:
            print('No Cycle Detected')
            print()
            return False
        else:
            # If there was a cycle reported, check to make sure it was a cycle.
            if len(self.negCyc) < 2:
                raise Exception('Invalid cycle: only 1 vertex')
            elif self.negCyc[0] != self.negCyc[-1]:
                raise Exception('Invalid cycle: start != end')
            else:
                # There was a cycle, check to ensure arbitrage.
                arb = 1
                for cInd in range(0,len(self.negCyc)-1):
                    arb *= self.rates[self.negCyc[cInd]][self.negCyc[cInd+1]]
                if arb <= 1:
                    self.printArb()
                    print(arb)
                    raise Exception('No arbitrage in reported cycle!')
                else:
                    print('Arbitrage Cycle:')
                    print()
                    self.printArb()
                    print('For gain of: %f %ss' % \
                          ((arb-1),self.currs[self.negCyc[0]]))
                    print()
                    return True

################################################################################

"""
getRates function will provide the 2D array representing the exchange rates to
the Currencies class's __init__ function.

INPUTS
exchangeNum: which set of rates to select

OUTPUTS
rates: a 2D list representing the exchange rates
currs: the list of currency names
"""

def getRates(exchangeNum):
    # Get the exchange rates.
    if exchangeNum == 0:
        # Small example from class.
        rates = [[1 for x in range(0,4)] for x in range(0,4)]
        rates[0][1] = 0.82   # Dollar to Euro
        rates[1][2] = 129.7  # Euro to Yen
        rates[2][3] = 12     # Yen to Lira
        rates[3][0] = 0.0008 # Lira to Dollar
        rates[0][2] = rates[0][1]*rates[1][2] # Dollar to Yen
        rates[1][3] = rates[1][2]*rates[2][3] # Euro to Lira
        rates[1][0] = 1/rates[0][1]
        rates[2][1] = 1/rates[1][2]
        rates[3][2] = 1/rates[2][3]
        rates[0][3] = 1/rates[3][0]
        rates[2][0] = 1/rates[0][2]
        rates[3][1] = 1/rates[1][3]
        currs = ['Dollar','Euro','Yen','Lira']

    elif exchangeNum == 1:
        # Some actual currency rates as of 11/12/18.
        # Euro rates to 13 others.
        EUrates = [1.0000, 0.8750, 1.1342, 1.1245, 1.5630, 1.4857, 8.8100, \
                   81.9811, 127.9574, 4.2180, 1.5553, 16.2280, 10.2656, 4.1305]
        currs = ['EUR','GBP','CHF','USD','AUD','CAD','HKD',\
                 'INR','JPY','SAR','SGD','ZAR','SEK','AED']
        rates = [[1 for x in currs] for x in currs]
        rates[0] = EUrates # Fill in the Euro->other rates
        for r in range(0,len(currs)):
            # Fill in the other->Euro rates
            rates[r][0] = 1/EUrates[r]
        for r in range(1,len(currs)):
            for c in range(r+1,len(currs)):
                # The rate of GBP->USD = (GBP->EUR)*(EUR->USD).
                # Use this to find all other rates and their inverses.
                rates[r][c] = rates[r][0]*rates[0][c]
                rates[c][r] = 1/rates[r][c]

    elif exchangeNum == 2:
        # Get the real rates.
        rates, currs = getRates(1)
        # Underprice the dollar (3) with repect to the pound (1).
        rates[3][1] -= 0.01
        rates[1][3] = 1/rates[3][1]

    elif exchangeNum == 3:
        # Get the rates with undervalued USD.
        rates, currs = getRates(2)
        # Overprice the yen (8) with repect to the rupee (7).
        rates[8][7] += 0.01
        rates[7][8] = 1/rates[8][7]
        # Overprice the riyal (9) with repect to the HK dollar (6).
        rates[9][6] += 0.07
        rates[6][9] = 1/rates[9][6]

    else:
        raise Exception('Input exchangeNum not valid!')

    return rates, currs

################################################################################

"""
testRates function will test all of the exchange rate examples.
"""
def testRates():
    passed = 0
    print('Testing Exchange Rates 0')
    print()
    c = Currencies(0)
    if not c.arbitrage():
        print('Incorrect result for Exchange Rates 0')
        print()
    else:
        passed += 1
        print('Correct result for Exchange Rates 0')
        print()
    print('------------------------')
    print()
    print('Testing Exchange Rates 1')
    print()
    c = Currencies(1)
    if c.arbitrage():
        print('Incorrect result for Exchange Rates 1')
        print()
    else:
        passed += 1
        print('Correct result for Exchange Rates 1')
        print()
    print('------------------------')
    print()
    print('Testing Exchange Rates 2')
    print()
    c = Currencies(2)
    if not c.arbitrage():
        print('Incorrect result for Exchange Rates 2')
        print()
    else:
        passed += 1
        print('Correct result for Exchange Rates 2')
        print()
    print('------------------------')
    print()
    print('Testing Exchange Rates 3')
    print()
    c = Currencies(3)
    if not c.arbitrage():
        print('Incorrect result for Exchange Rates 3')
        print()
    else:
        passed += 1
        print('Correct result for Exchange Rates 3')
        print()
    print('------------------------')
    print()
    print('Passed %d/4 Tests' % passed)
    return
