from datacollection.scrape_hyp_tsv2csv import *


#################
# scraping tsv files from model output

ran_languages = 'gml+50p+eng gml+50p+deu gml+50p+nno gml+75p+isl gml+25p+isl nno+50p+eng nno+50p+deu nno+50p+isl nno+75p+isl nno+25p+isl gml+25p+eng gml+25p+deu gml+25p+nno gml+75p+eng gml+75p+deu gml+75p+nno nno+25p+eng nno+25p+deu nno+75p+eng nno+75p+deu'
modeloutput_fp = 'modeloutput/customdata/'

# pass in list of langugae names to scrape, model output file path
# filename for csv (if you dont want the basic name), and false for creating hypothesis files
create_hyp_tsvcsv(languages=ran_languages.split(' '),
                  tsvfilepath=modeloutput_fp, tsvfout='7-27-20.lemma.predictions.csv', createhyp=False)
