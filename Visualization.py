import matplotlib.pyplot as plot
import matplotlib

matplotlib.style.use('seaborn-paper')

def main():

    proteinChain = "HHPH"
    output = {'x-cor': [0,0,1,1], 'y-cor': [0,1,1,0], 'type': ['H','H','P','H']}

    plot.scatter(output['x-cor'], output['y-cor'], zorder = 0)
    plot.plot(output['x-cor'], output['y-cor'], zorder = 0)

    for acids in range(len(proteinChain)):
        if output['type'][acids] == 'H':
            plot.scatter(output['x-cor'][acids], output['y-cor'][acids]\
            , color='r', s=2000, zorder = 1)
        else:
            plot.scatter(output['x-cor'][acids], output['y-cor'][acids]\
            , color='b', s=2000, zorder = 1)


    plot.title('Protein shizzle')
    plot.ylabel('Y axis')
    plot.xlabel('X axis')

    plot.show()

main()
