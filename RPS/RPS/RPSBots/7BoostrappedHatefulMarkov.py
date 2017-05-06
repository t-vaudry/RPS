#email: schnej7@gmail.com
import random

def beats( a ):
    if a == 'R':
        return 'P'
    if a == 'P':
        return 'S'
    if a == 'S':
        return 'R'

choices = list(['R','P','S'] )
num_algos = 7
depth1 = 1
depth2 = 4
depth3 = 4
depth4 = 2
depth5 = 3
depth6 = 1
depth7 = 4
history = 300

max_depth = max( list( [ depth1, depth2, depth3, depth4, depth5, depth6, depth7 ] ) )

class bootstrap:
    def __init__( self, num ):
        self.quality_history = []
        self.guess_hist = []
        self.rite_hist = []
        self.prev = [None] * (num+1)
        self.cur_qual = [0] * (num+1)

    def update( self, actual_prev ):
        rite_hist_row = []
        for i in range( len(self.prev) ):
            if self.prev[i] != None and self.prev[i] == actual_prev:
                rite_hist_row.append( 1 )
                self.cur_qual[i] += 1
            elif self.prev[i] != None:
                rite_hist_row.append( 0 )
            else:
                rite_hist_row.append( None )

        self.rite_hist.append( rite_hist_row )
        if len( self.rite_hist ) > history:
            removing = self.rite_hist.pop( 0 ) 
            for i in range( len(removing) ):
                if removing[i] != None:
                    self.cur_qual[i] -= removing[i]

    def quality( self, index ):
        num_wins = self.cur_qual[index]
        num_total = len( self.quality_history )
        if num_total == 0:
            return 0
        return float( num_wins ) / float( num_total )

    def predict( self, guesses ):
        freq = dict()
        for choice in choices:
            freq[choice] = 0

        legit_guess = False
        quality_row = []
        ave_quality = 0
        if len( self.quality_history ) > 0:
            prev_qualities = self.quality_history[-1][0:num_algos]
            ave_quality = sum( prev_qualities ) / len( prev_qualities )

        included = 0
        for i in range( len(guesses) ):
            quality_row.append( self.quality( i ) )
            if guesses[i] != None:
                legit_guess = True
                if quality_row[-1] > ave_quality:
                    included += 1
                    freq[ guesses[i] ] += quality_row[-1]
            self.prev[i] = guesses[i]
        quality_row.append( self.quality( num_algos ) )
        self.quality_history.append( quality_row )

        #If no algorithm knows, then just guess
        if not legit_guess:
            return random.choice( choices )
        max_freq = max(freq.iterkeys(), key=lambda k: freq[k])
        sum_freq = sum( freq.values() )
        max_freq_val = freq[ max_freq ]
        if sum_freq > 0:
            self.guess_hist.append( max_freq_val / sum_freq )
        self.prev[ num_algos ] = max_freq
        return beats( self.prev[ num_algos ] )

    def plot( self ):
        n = 0

class marcov:
    def __init__( self ):
        self.hist_probs = dict()

    def record( self, prev, cur ):
        if prev not in self.hist_probs.keys():
            self.hist_probs[prev] = dict()
            self.hist_probs[prev][cur] = 1
        elif cur not in self.hist_probs[prev].keys():
            self.hist_probs[prev][cur] = 1
        else:
            self.hist_probs[prev][cur] += 1

    def predict( self, cur ):
        if cur not in self.hist_probs.keys():
            return None
        else:
            return max(self.hist_probs[cur].iterkeys(), key=lambda k: self.hist_probs[cur][k])


if input == '':
    turn = 0
    boot = bootstrap( num_algos )
    m1 = marcov()
    m2 = marcov()
    m3 = marcov()
    m4 = marcov()
    m5 = marcov()
    m6 = marcov()
    m7 = marcov()
    output = 'R'
    in_hist = list( ['x'] * max_depth )
    out_hist = list( ['x'] * (max_depth) ) + ['R']

else:
    turn += 1
    #if turn % 999 == 0:
    #    boot.plot()

    guesses = [None] * num_algos

    #record the last move
    in_hist += list( input )

    #train

    #m1
    depth_end1 = len( in_hist ) - ( 1 )
    depth_begin1 = len( in_hist ) - ( depth1 + 1 )
    prev1 = str( in_hist[ depth_begin1:depth_end1 ] ) + str( out_hist[ depth_begin1:depth_end1 ] )

    cur_end1 = len( in_hist )
    cur_begin1 = len( in_hist ) - ( depth1 )
    cur1 = str( in_hist[ cur_begin1:cur_end1 ] ) + str( out_hist[ cur_begin1:cur_end1 ] )

    m1.record( prev1, input )
    guesses[0] = m1.predict( cur1 )

    #m2
    depth_end2 = len( in_hist ) - ( 1 )
    depth_begin2 = len( in_hist ) - ( depth2 + 1 )
    prev2 = str( in_hist[ depth_begin2:depth_end2 ] )

    cur_end2 = len( in_hist )
    cur_begin2 = len( in_hist ) - ( depth2 )
    cur2 = str( in_hist[ cur_begin2:cur_end2 ] )

    m2.record( prev2, input )
    guesses[1] = m2.predict( cur2 )

    #m3
    depth_end3 = len( in_hist ) - ( 1 )
    depth_begin3 = len( in_hist ) - ( depth3 + 1 )
    prev3 = str( out_hist[ depth_begin3:depth_end3 ] )

    cur_end3 = len( in_hist )
    cur_begin3 = len( in_hist ) - ( depth3 )
    cur3 = str( out_hist[ cur_begin3:cur_end3 ] )

    m3.record( prev3, out_hist[-1] )
    guesses[2] = beats( m3.predict( cur3 ) )

    #m4
    depth_end4 = len( in_hist ) - ( 1 )
    depth_begin4 = len( in_hist ) - ( depth4 + 1 )
    prev4 = str( in_hist[ depth_begin4:depth_end4 ] ) + str( out_hist[ depth_begin4:depth_end4 ] )

    cur_end4 = len( in_hist )
    cur_begin4 = len( in_hist ) - ( depth4 )
    cur4 = str( in_hist[ depth_begin4:depth_end4 ] ) + str( out_hist[ cur_begin4:cur_end4 ] )

    m4.record( prev4, input )
    guesses[3] = m4.predict( cur4 )

    #m5
    depth_end5 = len( in_hist ) - ( 1 )
    depth_begin5 = len( in_hist ) - ( depth5 + 1 )
    prev5 = str( out_hist[ depth_begin5:depth_end5 ] )

    cur_end5 = len( in_hist )
    cur_begin5 = len( in_hist ) - ( depth5 )
    cur5 = str( out_hist[ cur_begin5:cur_end5 ] )

    m5.record( prev5, out_hist[-1] )
    guesses[4] = beats( m5.predict( cur5 ) )

    #m6
    depth_end6 = len( in_hist ) - ( 1 )
    depth_begin6 = len( in_hist ) - ( depth6 + 1 )
    prev6 = str( in_hist[ depth_begin6:depth_end6 ] ) + str( out_hist[ depth_begin6:depth_end6 ] )

    cur_end6 = len( in_hist )
    cur_begin6 = len( in_hist ) - ( depth6 )
    cur6 = str( in_hist[ cur_begin6:cur_end6 ] ) + str( out_hist[ cur_begin6:cur_end6 ] )

    m6.record( prev6, out_hist[-1] )
    guesses[5] = beats( m6.predict( cur6 ) )

    #m7
    depth_end7 = len( in_hist ) - ( 1 )
    depth_begin7 = len( in_hist ) - ( depth7 + 1 )
    prev7 = str( in_hist[ depth_begin7:depth_end7 ] )

    cur_end7 = len( in_hist )
    cur_begin7 = len( in_hist ) - ( depth7 )
    cur7 = str( in_hist[ cur_begin7:cur_end7 ] )

    m7.record( prev7, out_hist[-1])
    guesses[6] = beats( m7.predict( cur7 ) )

    #guess

    #boost on all marcov chains
    boot.update( input )
    output = boot.predict( guesses )

    #record guess
    out_hist += list( output )