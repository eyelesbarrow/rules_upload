import pandas as pd
from pandas import *
import logging 

from bwproject import BWProject
from bwresources import BWRules, BWQueries

logger = logging.getLogger("bwapi")



YOUR_ACCOUNT = ""
YOUR_PASSWORD = ""
YOUR_PROJECT = ""



def uploadRules (filepath)
	"""creates and uploads rules to brandwatch"""

	rules_df = pd.read_csv(r"filepath", sep=';')
	project = BWProject(username=YOUR_ACCOUNT, password=YOUR_PASSWORD, project=YOUR_PROJECT)
	rules_df = pd.read_csv(r"filepath", sep=';')
	queries = BWQueries(project)

	queryName_list = rules_df['queryName'].tolist()
	tags_list = rules_df['tags'].tolist()
	name_list = rules_df['name'].tolist()
	search_list = rules_df['search'].tolist()
	ruleAction_list = rules_df['action'].tolist()


	filter_list = []


	for q, s in zip(queryName_list, search_list):
		   	filter_f = rules.filters(queryName=q, search=s)
		    filter_list.append(filter_f)
	    
	names = []

	for n in name_list:
    	names.append(n)

	for t in tags_list:
    	action_rules = rules.rule_action(action='addTag', setting=[t])

	rules_list = []
		
	for f, n, t, a in zip(filter_list, names,  tags_list, action_rules):

	    n_rule = rules.rule(filter=f, name=n, action=a, scope='project', backfill=False)
	    rules_list.append(n_rule)

	rules.upload_all([rules_list])


