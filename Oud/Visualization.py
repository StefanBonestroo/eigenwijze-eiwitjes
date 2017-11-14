import matplotlib.pyplot as plot
import matplotlib

matplotlib.style.use('seaborn-paper')

def main():

    proteinChain = "HHPH"
    output = {'x-cor': [0,0,1,1], 'y-cor': [0,1,1,0], 'type': ['H','H','P','H']}



    for one in range(len(proteinChain)):
        for two in range(len(proteinChain)):

            current_x = output['x-cor'][one]
            neighbor_x = output['x-cor'][two]
            current_y = output['y-cor'][one]
            neighbor_y = output['y-cor'][two]

            if (((abs(current_x - neighbor_x) == 1) and\
            (abs(current_y - neighbor_y) == 0)) or\
            ((abs(current_y - neighbor_y) == 1) and\
            (abs(current_x - neighbor_x) == 0))) and\
            (output['type'][one] == 'H' and output['type'][two] == 'H'):
                plot.plot([current_x, neighbor_x],[current_y,neighbor_y]\
                , 'r--', linewidth=0.5, zorder=-1)

    plot.plot(output['x-cor'],output['y-cor'], linewidth = 5.0, zorder = 0)

    for acids in range(len(proteinChain)):
        if output['type'][acids] == 'H':
            plot.scatter(output['x-cor'][acids], output['y-cor'][acids]\
            , color='r', s=2000, zorder=1)
        else:
            plot.scatter(output['x-cor'][acids], output['y-cor'][acids]\
            , color='b', s=2000, zorder=1)


    plot.title('Protein shizzle')
    plot.ylabel('Y axis')
    plot.xlabel('X axis')

    plot.show()

main()
