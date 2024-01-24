"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from .models import NearEarthObject, CloseApproach

#extracting seems very slow

def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """

    # load neos into set
    with open(neo_csv_path) as infile:
            reader = csv.DictReader(infile)
            NEO_set = set(NearEarthObject(**neo) for neo in reader)
    return NEO_set
    # load neos into a dict sorted according to primary designation
    # NEO_dict_des = {}
    # with open(neo_csv_path) as infile:
    #     reader = csv.DictReader(infile)
    #     for neo in reader:
    #         NEO_dict_des[neo['pdes']] = NearEarthObject(**neo)
    # return NEO_dict_des


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """

    # load close approaches in set or better in list according to date?? using a constructor here would prob be better
    with open(cad_json_path) as infile:
        reader = json.load(infile)
        CAD_list = [CloseApproach(**{'des':approach[0], 'cd':approach[3], 'dist':approach[4], 'v_rel':approach[7]}) for approach in reader['data']]
    return CAD_list
    # load close approaches into a dict sorted according to primary designations of the respective neos
    # CAD_dict_des = {}
    # with open(cad_json_path) as infile:
    #     reader = json.load(infile)
    #     for approach in reader['data']:
    #         info = {'des':approach[0], 'cd':approach[3], 'dist':approach[4], 'v_rel':approach[7]}
    #         close_approach = CloseApproach(**info)
    #         if close_approach._designation not in CAD_dict_des:
    #             CAD_dict_des[close_approach._designation] = []
    #         CAD_dict_des[close_approach._designation].append(close_approach)
    # return CAD_dict_des

            # if str(close_approach.time.date()) not in CAD_dict_date:
            #     CAD_dict_date[str(close_approach.time.date())] = []
            # CAD_dict_date[str(close_approach.time.date())].append(close_approach)