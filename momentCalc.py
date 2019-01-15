from math import *
#model the straw as a hollow cylinder simply supported beam
def main():
    print("Welcome to the straw designer")
    #VARIABLE DECLARATIONS _----------------------------
    #outside diameter
    D = 0.0095 #m
    #inner diameter
    d = []
    #from centre to outside
    c = D / 2 # m
    #length
    l = 0.2286 # m
    #force in N
    F = []
    #bending moment
    M = []
    #yield stress
    sigmaY = 276000000
    maxStress = sigmaY

    failureOccured = False
    roundTo = 7
    #--------------------------------------------------------

    startingForce = int(input("Enter a starting force (N): "))
    forceStepSize = int(input("Enter a step size: "))
    numberOfSteps = int(input("Enter a number of steps: "))

    #initialize increasingForce
    increasingForce = startingForce
    #generate force array
    for step in range(0, numberOfSteps):
        if step == 0:
            increasingForce = startingForce

        else:
            increasingForce = increasingForce + forceStepSize

        F.append(increasingForce)

    print("Forces applied to the straw are: ", F)

    for item in F:
        M.append(item * (l/4))

    print("Max bending moment is calculated as: ", M)

    for moment in M:
        #condition that anything under the fourth root must be positive
        if (64 * moment * c) / (pi * maxStress) < pow(D, 4):

            tempCalc = pow( ( pow(D, 4) + ( (-64 * moment * c) / (pi * maxStress) ) ), 1/4)
            #converts to mm
            d.append(tempCalc * 1000)
        #if this else executes, the design is not possible
        else:
            failureOccured = True

    print("Inner diameter calculated as: ", d)
    print("Therefore.. for the applied bending moments ")

    thicknesses = []

    for item in d:

        thicknesses.append( D * 1000 - item )

    print("The thicknesses are: ", thicknesses)
    print(" ")
    #print in table
    titles = ['Force (lb)', 'Inner diameter (mm)', 'Thicknesses (mm)']

    print(titles[0] + "   "  + titles[1] + "   " + titles[2] + "   ")

    for row in range(0, len(d)):
        poundForce = F[row] * 0.22481 # converts to pounds

        print('%.4f' % poundForce, end='')
        print('              %.4f' % d[row], end='')
        print('              %.4f' % thicknesses[row])

    if failureOccured == True:
        print("Design constraints have been exceeded.")
        print("The below values are the last ones before failure.")

        print(titles[0] + "   "  + titles[1] + "   " + titles[2] + "   ")
        poundForce = F[len(d)-1] * 0.22481
        print("%.4f" % poundForce, end='') #using d here as the F is generated fully before the d is calculated
        print("              %.4f" % d[len(d)-1], end='')
        print("              %.4f" % thicknesses[len(thicknesses)-1])


if __name__ =="__main__":
    main()
