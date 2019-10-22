STEP = 20

def peano_curve(_, direction, r):
    
    if r < 1:
        return

    if direction:
        angle = 90
    else:
        angle = -90
    
    peano_curve(_, direction, r-1)
    _.forward(STEP)
    peano_curve(_, not direction, r-1)
    _.forward(STEP)
    peano_curve(_, direction, r-1)
    
    _.right(angle)
    _.forward(STEP)
    _.right(angle)

    peano_curve(_, not direction, r-1)
    _.forward(STEP)
    peano_curve(_, direction, r-1)
    _.forward(STEP)
    peano_curve(_, not direction, r-1)
    
    _.left(angle)
    _.forward(STEP) 
    _.left(angle)
    
    peano_curve(_, direction, r-1)
    _.forward(STEP)
    peano_curve(_, not direction, r-1)
    _.forward(STEP)
    peano_curve(_, direction, r-1) 
    	
def hilbert_curve(_, direction, r):

    if r < 1:
        return

    if direction:
    	angle = 90
    else:
    	angle = -90

    _.left(angle)
    hilbert_curve(_, not direction, r-1)
    
    _.forward(STEP)
    
    _.right(angle)
    hilbert_curve(_, direction, r-1)
    
    _.forward(STEP)
    
    hilbert_curve(_, direction, r-1)
    _.right(angle)
    
    _.forward(STEP)
    
    hilbert_curve(_, not direction, r-1)
    _.left(angle)

def gosper_curve(_, direction, r):
    
    if r < 1:
        _.forward(STEP)
        return
    
    angle = 60
    
    if direction:
        gosper_curve(_, direction, r-1)     
        _.left(angle)
        gosper_curve(_, not direction, r-1)     
        _.left(angle)      
        _.left(angle)
        gosper_curve(_, not direction, r-1)      
        _.right(angle)
        gosper_curve(_, direction, r-1)
        _.right(angle)     
        _.right(angle)
        gosper_curve(_, direction, r-1)
        gosper_curve(_, direction, r-1)      
        _.right(angle)      
        gosper_curve(_, not direction, r-1)     
        _.left(angle)

    else:
        _.right(angle)
        gosper_curve(_, not direction, r-1)
        _.left(angle)
        gosper_curve(_, direction, r-1)
        gosper_curve(_, direction, r-1)
        _.left(angle)
        _.left(angle)
        gosper_curve(_, direction, r-1)
        _.left(angle)
        gosper_curve(_, not direction, r-1)     
        _.right(angle)
        _.right(angle)
        gosper_curve(_, not direction, r-1)
        _.right(angle)
        gosper_curve(_, direction, r-1)
