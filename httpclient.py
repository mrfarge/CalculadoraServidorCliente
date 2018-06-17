# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:12:37 2018

@author: Maria
"""



import requests
import csv
from re import sub, compile
import os


fileType = 'csv' #'txt'

def cleanhtml(raw_html):
  cleanr = compile('<.*?>')
  cleantext = sub(cleanr, '', raw_html)
  return cleantext


def main():

    with open('sample.csv', newline='') as File:  
        reader = csv.reader(File)
        for row in reader:
            
            valor1 = row[0]
            operador = row[1]
            valor2 = row[2]
            payload = {'valor1': valor1, 'Op': operador, 'valor2': valor2}
            r = requests.post('http://localhost:8181/', data = payload)
            

            print('La operación %s %s %s' %(str(valor1), str(operador), str(valor2)) )
            print(cleanhtml(r.text))

            if fileType =='txt':
                file.write('La operación %s %s %s '  %(str(valor1), str(operador), str(valor2)) )
                file.write(cleanhtml(r.text) + os.linesep)
            else:
                
                #result = cleanhtml(r.text)[14:]
                
                result = sub('The result is ', '', cleanhtml(r.text))
                writer.writerow([valor1] + [operador] + [valor2]+ ['='] + [result])



if __name__ == '__main__':
    
    if fileType == 'txt':
        
        file = open('Results.txt', 'w')
    else:

        file = open('Rsults.csv', 'w')
        writer = csv.writer(file, delimiter = ',',
                            quotechar=' ', quoting=csv.QUOTE_ALL)
    
    main()

    file.close()



