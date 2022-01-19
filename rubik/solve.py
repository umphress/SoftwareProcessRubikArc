import rubik.cube as rubik

def _solve(parms):
    encodedCube = parms.get('cube',None)       #get "cube" parameter if present
    result = 'FfRrBbLlUuDd'                    #example rotations
    return result