import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

series ="TP.DK.USD.S.YTL"
series_name="Dolar_Kuru"
startDate= "01-03-2023"
endDate="06-05-2023"
typee="csv"
key="fkxbpmXEld"
aggregationTypes="avg"
formulas="0"
frequency = "2"

url= 'https://evds2.tcmb.gov.tr/service/evds/series={}&startDate={}&endDate={}&type={}&key={}&aggregationTypes={}&formulas={}&frequency={}'.format(series,startDate,endDate,typee,key,aggregationTypes,formulas,frequency)

dolar = pd.read_csv(url)
dolar.head()

dolar.drop("UNIXTIME", axis=1,inplace=True)
dolar.set_index("Tarih",inplace=True)
dolar.rename(columns={series.replace(".","_"):series_name},inplace=True)
dolar.dropna(how="any",inplace=True) 
dolar=round(dolar,2)
dolar.head()

# Görselleştirme
#Grafik Boyutu
plt.figure(figsize=(16,8))
#çizimi
sns.set_style("whitegrid")
p1 = sns.pointplot(x=dolar.index,
              y=dolar[series_name],
              color='#22b2da',
              alpha=0.5)
#grafik üzerine değerlerin yazılması
for line in range(0,dolar.shape[0]):
     p1.text(line, dolar[series_name].iloc[line]+0.03, dolar[series_name].iloc[line], 
             horizontalalignment='left', size='medium', color='black', weight='semibold')
#x eksenindeki yazıları 90 derece açıyla yazdırma
plt.xticks(rotation= 90)
# x ve y eksenini isimlendirme
plt.xlabel('\nTarih',fontsize = 15)
plt.ylabel(series_name+"\n",fontsize = 15)
#Grafiğe isim verme
plt.title(series_name+"\n",fontsize = 20, weight='semibold')
#Grafiği kaydetme
resimadi= "Dolar Kuru.png".format(series_name, dolar.iloc[dolar.shape[0]-1].name)
plt.savefig(resimadi,dpi=200)
plt.show()