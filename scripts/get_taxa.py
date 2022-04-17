from Bio import Entrez
import pandas is pd
def get_tax_data(taxids):
    dd={'TaxID':[],
        'Superkingdom':[],
          'Kingdom':[],
         'Phylum':[],
         'Class':[],
         'Order':[],
         'Family':[],
         'Genus':[]}
    for i in taxids:
      if i.isnumeric() == False:
        dd['TaxID'].append (i)
        dd['Class'].append(i)
        dd['Family'].append(i)
        dd['Genus'].append(i)
        dd['Kingdom'].append(i)
        dd['Order'].append(i)
        dd['Phylum'].append(i)
        dd['Superkingdom'].append(i)
      elif i.isnumeric():
          dd['TaxID'] .append(i)
          print(f'{i} processing started:')
          search = Entrez.efetch(id = i, db = "taxonomy", retmode = "xml")
          taxdata = Entrez.read(search)
          Ranks = [taxa['Rank'] for taxa in taxdata[0]['LineageEx']]
          if 'superkingdom' in Ranks:
            dd['Superkingdom'].append(taxdata[0]['LineageEx'][Ranks.index('superkingdom')]['ScientificName'])
          else:
            dd['Superkingdom'].append('')
          if 'class' in Ranks:
            dd['Class'].append(taxdata[0]['LineageEx'][Ranks.index('class')]['ScientificName'])
          else:
            dd['Class'].append('')
          if 'kingdom' in Ranks:
            dd['Kingdom'].append(taxdata[0]['LineageEx'][Ranks.index('kingdom')]['ScientificName'])
          else:
            dd['Kingdom'].append('')
          if 'phylum' in Ranks:
            dd['Phylum'].append(taxdata[0]['LineageEx'][Ranks.index('phylum')]['ScientificName'])
          else:
            dd['Phylum'].append('')
          if 'order' in Ranks:
            dd['Order'].append(taxdata[0]['LineageEx'][Ranks.index('order')]['ScientificName'])
          else:
            dd['Order'].append('')
          if 'family' in Ranks:
            dd['Family'].append(taxdata[0]['LineageEx'][Ranks.index('family')]['ScientificName'])
          else:
            dd['Family'].append('')
          if 'genus' in Ranks:
            dd['Genus'].append(taxdata[0]['LineageEx'][Ranks.index('genus')]['ScientificName'])
          else:
            dd['Genus'].append('')
    return pd.DataFrame.from_dict(dd)
