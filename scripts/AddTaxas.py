#This script requires biopython and pandas
from Bio import Entrez
import pandas as pd
import os


#Define the get_tax_id function
def get_tax_id(species):
	"""
	get_tax_id function aim to add a column of NCBI TaxIDs to a pandas dataframe that contains a column entitled 'Species'
	pd.DataFrame --> pd.DataFrame
	if the TaxID is not found the taxid will be replaced by '_'
	"""
	taxids = []
	if type(species) != pd.core.frame.DataFrame:
		rais TypeError('Only pandas DataFrame allowed')
	else:
		if 'Species' not in species:
			rais ValueError ('Column \'Species\' not in the given dataframe, \n check the spelling and the case of columns')
		else:
			for sp in species ['Species']:	
    			species = sp.replace(" ", "+").strip()
    			try :
      				search = Entrez.esearch(term = species, db = "taxonomy", retmode = "xml")
      				record = Entrez.read(search)
					taxids.append(record['IdList'][0])
    			except:
					taxids.append('_')
		species['TaxID'] = taxids
		return species
