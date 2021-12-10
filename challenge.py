#!/usr/bin/python
# null,0,grandpa|0,1,son|0,2,daugther|1,3,grandkid|1,4,grandkid|2,5,grandkid|5,6,greatgrandkid
#Each node is a CSV with the values being "parent_id, node_id, node_name".
##############
#Version: 1.0
#Created by: Steve Sherman
#Date: 12/10/2021
##############


import json
import argparse
 
#List split Functions:

def create_list_from_pipe(input_string):
    input_list = input_string.split ('|')
    return (input_list)

def split_comma_delimited(input_string):
    input_list = input_string.split (",")
    return (input_list)

#########################

#Dict to Json Functions:

def create_json_from_dict(input_dict):
    input_json = json.dumps(input_dict, indent=4)
    return (input_json)

#########################

#Dictionary population commands
def add_items_to_dictionary(input_string, input_dict):
    input_dict['family'][input_string[1]] = {}
    input_dict['family'][input_string[1]]['parent_id'] = input_string[0]
    input_dict['family'][input_string[1]]['node_id'] = input_string[1]
    input_dict['family'][input_string[1]]['node_name'] = input_string[2]
    input_dict['family'][input_string[1]]['children'] = []
    return input_dict

def add_children_to_parents(input_string, input_dict):
    if input_string[0] != "null":
         input_dict['family'][input_string[0]]['children'].append(input_string[1])
    return input_dict


########################

#Main
def main():
    # Initialize parser
    parser = argparse.ArgumentParser()
    parser.add_argument("family_tree")
    args = parser.parse_args()
    ##

    family_dictionary = {"family": {}}

    convert_data = create_list_from_pipe(args.family_tree)
    for person in convert_data:
        person_data = split_comma_delimited(person)
        family_dictionary = add_items_to_dictionary(person_data, family_dictionary)

    for person in convert_data:
        person_data = split_comma_delimited(person)
        family_dictionary = add_children_to_parents(person_data, family_dictionary)

    print (create_json_from_dict(family_dictionary))

#######################

if __name__== "__main__" :
    main()
