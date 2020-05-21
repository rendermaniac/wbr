import os
import argparse
import logging

import microfs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def download(*args, **kwargs):
    dryrun = kwargs['dryrun'] or False
    for f in microfs.ls():
        logging.info('Downloading file %s', f)
        if not dryrun:
            microfs.get(f)

def clear(*args, **kwargs):
    dryrun = kwargs['dryrun'] or False
    for f in microfs.ls():
        if not f.endswith('.py'):
            logging.info('Removing file %s', f)
            if not dryrun:
                microfs.rm(f)

def plot(*args, **kwargs):
    dryrun = kwargs['dryrun'] or False
    for f in os.listdir():
        if f.endswith('.csv'):
            logging.info('Plotting file %s', f)
            if not dryrun:
                data = pd.read_csv(f)
                ax = data.plot(kind='line', x='time', y='altitude')

                #Annotate maximum height
                xmax = data['time'][np.argmax(data['altitude'])]
                ymax = data['altitude'].max()
                ax.annotate('Max altitude {}'.format(ymax), xy=(xmax, ymax))

                plt.savefig(f.replace('.csv','.png'))

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description='Water bottle rocket utility')
    parser.add_argument('mode', type=str,
                    help='The mode to run. download, clear or plot')
    parser.add_argument('--dryrun', action="store_true",
                    help='Print result without performing action')

    args = parser.parse_args()
    {'download' : download,
    'clear' : clear,
    'plot' : plot}[args.mode](dryrun=args.dryrun)