def solveTowerOfHanio(height,fromPole,toPole, auxPole):
    if height >=1:
        solveTowerOfHanio(height - 1,fromPole, auxPole, toPole)
        moveDisk(toPole,fromPole)
        solveTowerOfHanio(height -1, auxPole, toPole, fromPole)


def moveDisk(toPole, fromPole):
    print('Moving from Pole {} to Pole {}'.format(fromPole, toPole))


solveTowerOfHanio(3, 'A', 'B', 'C')
