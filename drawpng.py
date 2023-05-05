# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#import signal
import numpy
from scipy import signal
import struct
import string
from os.path import getsize
import numpy as np
import matplotlib.pyplot as plt
import datetime
import matplotlib.transforms as mtransforms
import matplotlib as mpl
from matplotlib import ticker
from matplotlib.dates import num2date
from matplotlib.font_manager import FontProperties


def readtmr(name,supressred):
    # Use a breakpoint in the code line below to debug your script.
    Colors03 = ["#000000", "#f1c40f", "#ff8ed0", "#888888", "#800080", "#00FF00", \
        "#ffffe0", "#ffe0ff", "#e0ffff", \
        "#0000ff", "#ff0000"];
    Colors13 = ["#000000", "#f1c40f", "#ff8ed0", "#888888", "#800080", "#00FF00", \
                "#000000", "#f1c40f", "#ff8ed0", "#888888", "#800080", "#00FF00", \
        "#ffffe0", "#ffe0ff", "#e0ffff", \
        "#0000ff", "#ff0000"];

    filelen = getsize(name)
    f=open(name, "rb")
	# 读入 4 个字节
    a = f.read(4)
    ad = struct.unpack("4b", a)
    # 小端有符号整数
	    #b = int.from_bytes(a, byteorder='little', signed=false)
    ver=ad[2]
    dtlen=ad[3]  #include movespeed but not CRC
    print(dtlen)
    pkglen=dtlen+4  #aa aa ver len
    print(pkglen)
    dtextra=dtlen%4
    if dtlen%4==0:
        chancount = int((dtlen - 4 ) / 4)
        wcrc="0b"
    else:
        chancount = int((dtlen - 4 - dtextra) / 4)
        wcrc = str(dtextra) + "b"  #should be 1b, i.e. movespeed
    print(wcrc)
    print(chancount)
    pkgTotal=int(filelen/pkglen)
    #teTime=np.zeros(shape=(pkgTotal,1))
    teTime=[]
    teData = np.zeros(shape=(pkgTotal,2*chancount+dtextra))
    teSmtData = np.zeros(shape=(2*chancount+dtextra,pkgTotal))
    to_ta = np.zeros(shape=(chancount,pkgTotal))

    f.seek(0)
    for i in range(0,pkgTotal): #range(1,filelen/pkglen):
        #print(teData)
        apkg = f.read(pkglen)
        fmt="4b1i"+str(2*chancount)+"H"+wcrc
        #print(fmt)
        data=struct.unpack(fmt, apkg)
        #print(data[4])
        teTime.append(datetime.datetime.fromtimestamp(data[4]))
        teData[i]=data[5:2*chancount+5+dtextra]
        #print(teData)
    print(teTime)
    teData = teData.transpose()
    #teData[2*chancount] = teData[2*chancount] * 0.02 - 273.15
    print(teData)
    f.close()

    #plt.figure(figsize=(16, 9))
    fig,ax = plt.subplots(1,1,figsize=(8,3.75))
    #plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.subplots_adjust(top=1)
    #plt.margins(0, 0)
    #ax[0][0].set_facecolor('#e0e0e0')
    #ax.plot(teTime, teSmtData)
    for i in range(0,chancount-1):
        #ax[1][0].plot(teTime[:pkgTotal-1], deriv[i],color=Colors13[i])
        #ax[1][0].plot(teTime[:pkgTotal-1], deriv[i+chancount],'--',color=Colors13[i])
        ax.plot(teTime, teData[i]* 0.02 - 273.15,color=Colors13[i])
        ax.plot(teTime, teData[i+chancount]* 0.02 - 273.15,'--',color=Colors13[i])
    if not supressred:
        ax.plot(teTime, teData[2*chancount]/256*10+20, '--', color='red')
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_date))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    plt.xlabel('Time')
    plt.ylabel('Temperature(℃)')
    plt.annotate('—:infrared temperature  - -:body surface temperature',xy=(0.4,0.15),xycoords='figure fraction')
    plt.annotate('Dec-27 2022', xy=(0.2, 0.01), xycoords='figure fraction')

    plt.show()
    #plt.savefig('fig.fig',bbox_inches='tight')

    return
   

def format_date(x, pos=None):
    dt=num2date(x)
    return dt.strftime('%H:%M') #%S





#font = FontProperties(fname=r"C:\Windows\Fonts\simsun.ttc")
#fig = plt.figure("Demo", figsize=(9, 6), dpi=100, constrained_layout=True )
#extent=[70.05, 139.95, 15.05, 59.95]
#bounds = [0.1, 0.5, 1, 2, 3, 4, 5, 6, 8, 10, 20, 40]
#ax.set_xlim((72, 135))
#ax.set_ylim((18, 55))
#ax.set_xticks(list(range(75, 136, 5)), PlateCarree)
#ax.set_yticks(list(range(20, 56, 5)), PlateCarree)
#ax.xaxis.set_major_formatter(lon_formatter)
#ax.yaxis.set_major_formatter(lat_formatter)
#y, x = southsea.shape[:2]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readtmr('20221214_200403_Wei_6399bbaeBF195D48.tmr',0)
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
