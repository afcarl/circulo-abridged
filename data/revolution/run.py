# This template should be copied and modified as necessary to become the 
# `run.py` in each directory. 
# 
# Do not modify this file unless the template needs changing -- modify
# its copies in each data directory. 


import igraph
from igraph import VertexClustering
import os
import sys
import urllib.request
import csv
from subprocess import call


GIT_URL = 'https://github.com/kjhealy/revere.git'
GIT_DIR = 'revere'
CSV_DIR = 'data'
CSV_FILE = 'PaulRevereAppD.csv'

GRAPH_NAME = "REVOLUTION"
GRAPH_TYPE = ".graphml" 

def __download__(data_dir):
    """
    TEMPLATE COMMENT: downloads the graph from DOWNLOAD_URL into data_dir/GRAPH_NAME
    """
    if not os.path.exists(data_dir):
        os.mkdir(data_dir)

    if not os.path.exists(os.path.join(data_dir, GIT_DIR)):
        try:
            call(["git", "clone", GIT_URL, os.path.join(data_dir, GIT_DIR)])
        except Exception as e:
            print("Git clone failed to retrieve data. Please try again.")
            raise(e)
    else:
        print("Downloaded data already exists at %s" % os.path.join(data_dir, GIT_DIR))

def __prepare__(data_dir):
    """
    TEMPLATE COMMENT: prepare the data into graphml format.
    """
    csv_path = os.path.join(data_dir, os.path.join(GIT_DIR, os.path.join(CSV_DIR,CSV_FILE)))
    csv_file = open(csv_path)
    reader = csv.DictReader(csv_file)

    g = igraph.Graph()

    clubs = reader.fieldnames[:]
    clubs.remove('')
    
    for club in clubs:
        g.add_vertex(name=club)

    for patriot in reader:
        g.add_vertex(name=patriot[''])
        for club in clubs:
            if(patriot[club] == '1'):
                g.add_edge(patriot[''], club)

    csv_file.close()

    g.to_undirected()
    g.write_graphml(os.path.join(data_dir, GRAPH_NAME + GRAPH_TYPE))

def get_graph():
    """
    TEMPLATE COMMENT: Downloads and prepares a graph
    """
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    graph_path = os.path.join(data_dir, GRAPH_NAME + GRAPH_TYPE)

    if not os.path.exists(graph_path):
        __download__(data_dir)
        __prepare__(data_dir)
    else:
        print(graph_path, "already exists. Using old file.")

    return igraph.load(graph_path)


def get_ground_truth(G=None):
    """
    TEMPLATE COMMENT: returns a VertexClustering object of the 
    ground truth of the graph G.
    """
    raise(NotImplementedError)


def main():
    G = get_graph()
#    get_ground_truth(G)

if __name__ == "__main__":
    main()
