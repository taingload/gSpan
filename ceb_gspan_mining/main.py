"""The main program that runs gSpan."""
# -*- coding=utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
from random import random
import sys

from .config import parser
from .gspan import gSpan
import numpy as np
import pandas as pd
def main(FLAGS=None):
    """Run gSpan."""

    if FLAGS is None:
        FLAGS, _ = parser.parse_known_args(args=["graphdata/graph.data.5"])

    if not os.path.exists(FLAGS.database_file_name):
        print('{} does not exist.'.format(FLAGS.database_file_name))
        sys.exit()

    gs = gSpan(
        database_file_name=FLAGS.database_file_name,
        min_support=FLAGS.min_support,
        min_num_vertices=FLAGS.lower_bound_of_num_vertices,
        max_num_vertices=FLAGS.upper_bound_of_num_vertices,
        max_ngraphs=FLAGS.num_graphs,
        is_undirected=(not FLAGS.directed),
        verbose=FLAGS.verbose,
        visualize=FLAGS.plot,
        where=FLAGS.where
    )

    gs.run()
    gs.time_stats()
    return gs

import random 
def generate_graph(file_name):
    
    graph = []
    vertexes = []
    edges = []
    # graph
    for g in range(10):
        #vertex
        rand_v = int(random.random()*100)
        if rand<=10:continue
        for v in range(rand):
            graph.append(g)
            vertexes.append(v)
        rand_e = int(random.random()*rand_v*rand_v)
        for e in range(rand_e):
            src = int(random.random()*rand_v)
            dst = int(random.random()*rand_v)
            if src!=dst:
                edges.append([g,src,dst])


    df_vertex = pd.DataFrame(np.array([[1, 1, 1], [4, 5, 6]]),
                   columns=['graph', 'vertex'])
    df_edge = pd.DataFrame(np.array([[1,1,1],[1, 2, 3], [4, 5, 6]]),
                   columns=['graph', 'src', 'dst'])
    return df_vertex, df_edge

if __name__ == '__main__':
    main()
