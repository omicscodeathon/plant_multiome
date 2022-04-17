def hgt (x,y, size):
  """
  This script aims to calculate the HGT, 
  x : genbank id of Mitochondrion
  y: genebank ido Chloroplast
  size: Mitochondrion size
  Output will the the proportion of HGT %
  """
  from Bio.Blast import NCBIWWW,NCBIXML
  res = NCBIWWW.qblast('blastn',x, y)
  aa = res
  ln=0
  for record in NCBIXML.parse(aa):
    for i in record.alignments:
      ln = ln + len (i)
   return (ln/size)*100
