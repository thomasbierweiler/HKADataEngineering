import csv

output=open('materials.csv',mode='w')
mywriter=csv.writer(output)

# header=['Name','Spezifikation','E-Modul (N/mm2)','Schmelzpunkt (°C)'] # Character ° fails with pandas
# header=['Name','Spezifikation','E-Modul (N/mm2)','Übergangstemperatur (Grad C)'] # Character Ü fails with pandas
header=['Name','Spezifikation','E-Modul (N/mm2)','Schmelzpunkt (Grad C)']
mywriter=csv.writer(output)
mywriter.writerow(header)
# write Edelstahl
mywriter.writerow(['Edelstahl','1.4571','200000','1500'])
mywriter.writerow(['Glas','Glas','60000','1000'])
mywriter.writerow(['PVDF','PVDF','2500','171'])
output.close()
