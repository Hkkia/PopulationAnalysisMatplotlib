import csv
from matplotlib import pyplot
import matplotlib as mpl
import mplcursors
from matplotlib.widgets import Button
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

mpl.rcParams['toolbar'] = 'None'
ifile = open("WP.csv", "rt")
reader = csv.reader(ifile)
x=[]
y=[]
for row,j in zip(reader,range(1951,2019)):
    x.append(row[1])
    y.append(j)
h=x[68:0:-1]
y=y[1:69]
choice=0
while choice!=3:
    print("\nChoose from following:\n(1)Line Graph for World Population over the years\n(2)Histogram for World Population growth witnessed over the years\n(3)Exit")
    choice=int(input())
    if choice==1:
        h=[int(i) for i in h]
        ax = pyplot.subplot(111)
        fig = pyplot.gcf()
        fig.canvas.set_window_title('Line Graph of World Population from 1950 to 2018')
        pyplot.xlabel("x=Year")
        pyplot.ylabel("y=Population")
        ax.plot(y,h,color='black',linewidth=2,label='World')
        axcut=pyplot.axes([0.3, 0.9, 0.1, 0.075],label='axcut')
        axcut1=pyplot.axes([0.45, 0.9, 0.2, 0.075],label='axcut1')
        def _yes(event):
            sum=0
            for i in h:
                sum=sum+i
            sum=sum/len(h)
            sum=float("{0:.2f}".format(sum))
            ax.annotate('Mean= '+str(sum),xy=(1950,sum),xytext=(1955,sum),arrowprops=dict())
        def _yes1(event):
            contifile = open("Conti.csv", "rt")
            reader = csv.reader(contifile)
            oc=[]
            eu=[]
            asi=[]
            na=[]
            sa=[]
            af=[]
            years=[]
            ax1 = pyplot.subplot(111)
            for row,j in zip(reader,range(1940,2021,10)):
                oc.append(row[1])
                eu.append(row[2])
                asi.append(row[3])
                na.append(row[4])
                sa.append(row[5])
                af.append(row[6])
                if j!=2020:
                    years.append(j)
                if j==2020:
                    years.append(2016)
            oc=oc[1:9]
            eu=eu[1:9]
            asi=asi[1:9]
            na=na[1:9]
            sa=sa[1:9]
            af=af[1:9]
            oc=[int(i) for i in oc]
            eu=[int(i) for i in eu]
            asi=[int(i) for i in asi]
            na=[int(i) for i in na]
            sa=[int(i) for i in sa]
            af=[int(i) for i in af]
            years=years[1:9]

            ax1.plot(years,oc,linewidth=2,label='Oceania')
            ax1.plot(years,eu,linewidth=2,label='Europe')
            ax1.plot(years,asi,linewidth=2,label='Asia')
            ax1.plot(years,na,linewidth=2,label='North America')
            ax1.plot(years,sa,linewidth=2,label='South America')
            ax1.plot(years,af,linewidth=2,label='Africa')
            pyplot.xlabel("x=Year")
            pyplot.ylabel("y=Population")
            ax1.axis((1949,2020,10000000,8000000000),label='conti')
            mplcursors.cursor(hover=True)
            pyplot.show()


        mean = Button(axcut, 'Mean', color='grey', hovercolor='white')
        mean.on_clicked(_yes)
        continent=Button(axcut1, 'Continent Wise', color='grey', hovercolor='white')
        continent.on_clicked(_yes1)
        axcut=None
        ax.axis((1950,2020,2000000000,8000000000),label='world')
        mplcursors.cursor(hover=True)
        pyplot.show()



    if choice==2:
        h2=[float(i) for i in h]
        h1=max(h2)-min(h2)
        h2=[((h2[i+1]-h2[i])/h1) for i in range(0,66) ]
        h2=[i*100 for i in h2]
        bins=[0.0,0.011,0.012,0.013,0.014,0.015,0.016,0.017,0.018,0.019,1.0]
        bins=[i*100 for i in bins]
        l=[];l1=[]
        for j in range(0,10):
            for i in range(0,66):
                if h2[i]>bins[j] and h2[i]<=bins[j+1]:
                    l1.append(y[i])
            l.append(l1[0:])
            l1.clear()
        l=[str(i) for i in l]
        a=[]
        j=0

        for i in range(0,10):
            if i==0:
                a=pyplot.annotate(l[i],xy=(j,j+0.011*100),xytext=(j+0.0005*100,i))
                a.set_visible(False)
                j=j+0.011*100
            else:
                a=pyplot.annotate(l[i],xy=(j,j+0.001*100),xytext=(j+0.0005*100,i))
                a.set_visible(False)
                j=j+0.001*100
        pyplot.xlabel("x=Percentage Growth in Population")
        pyplot.ylabel("y=Number of Years")
        ax = pyplot.subplot(111)
        fig = pyplot.gcf()
        fig.canvas.set_window_title('Histogram of Population Growth from 1953 to 2017')
        axcut=pyplot.axes([0.3, 0.9, 0.1, 0.075])
        axcut1=pyplot.axes([0.45, 0.9, 0.3, 0.075])

        def _yes(event):
            sum=0
            for i in h2:
                sum=sum+i
            sum=sum/len(h2)
            sum=float("{0:.2f}".format(sum))
            ax.annotate(str(sum)+'%',xy=(sum,0),xytext=(sum,-1.5),arrowprops=dict())
            ax.annotate('Mean= '+str(sum)+'%',xy=(0.47,19),xytext=(0.47,19))
        def _yes1(event):
            sum=0
            for i in h2:
                sum=sum+i
            sum=sum/len(h2)
            sum1=0
            for i in h2:
                sum1=sum1+(i-sum)**2
            sum1=sum1/len(h2)
            sum1=float("{0:.2f}".format(sum1))
            ax.annotate('Standard Deviation= +/-'+str(sum1)+'%',xy=(0.47,18),xytext=(0.47,18))
        mean = Button(axcut, 'Mean', color='grey', hovercolor='white')
        mean.on_clicked(_yes)
        sd = Button(axcut1, 'Standard Deviation', color='grey', hovercolor='white')
        sd.on_clicked(_yes1)
        ax.axis((0,0.02*100,0,20))

        for i in range(0,10):
            ax.hist(h2,bins=[bins[i],bins[i+1]],color='orange',ec='black',label=l[i], lw=1, fc=(0.3, 0.99, 0.25,0.8))
        pyplot.text(x="Percentage Growth",y="Number of Years",s="")
        mplcursors.cursor(hover=True)
        pyplot.show();
ifile.close()
