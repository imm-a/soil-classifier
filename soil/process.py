import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from PIL import Image

def dataset(): #returns individual columns as list
    df = pd.read_excel ('C:/Users/amrit/projects/soil/files/Final.xlsx')
    r=pd.DataFrame(df, columns= ['R'])
    g=pd.DataFrame(df, columns= ['G'])
    b=pd.DataFrame(df, columns= ['B'])
    h=pd.DataFrame(df, columns= ['H_GT'])
    v=pd.DataFrame(df, columns= ['V_GT'])
    c=pd.DataFrame(df, columns= ['C_GT'])
    r= r.values.tolist()
    g= g.values.tolist()
    b= b.values.tolist()
    h= h.values.tolist()
    v= v.values.tolist()
    c= c.values.tolist()
    h = [['5R'] if word == [5] else word for word in h]
    h = [['7.5R'] if word == [7] else word for word in h]
    h = [['10R'] if word == [10] else word for word in h]
    h = [['2.5YR'] if word == [12] else word for word in h]
    h = [['5YR'] if word == [15] else word for word in h]
    h = [['7.5YR'] if word == [17] else word for word in h]
    h = [['10YR'] if word == [20] else word for word in h]
    h = [['2.5Y'] if word == [22] else word for word in h]
    h = [['5Y'] if word == [25] else word for word in h]
    h = [['10Y'] if word == [30] else word for word in h]
    h = [['5GY'] if word == [35] else word for word in h]
    return r,g,b,h,v,c

def avgclr(pixellist): #returns average colour values of image
    pixels = pixellist
    #print(pixels)
    

    av_r=0
    av_g=0
    av_b=0
    for i in range(len(pixels)):
        av_r=av_r+pixels[i][0]
        av_g=av_g+pixels[i][1]
        av_b=av_b+pixels[i][2]
        

    av_r=av_r/(len(pixels))
    av_g=av_g/(len(pixels))
    av_b=av_b/(len(pixels))
    return av_r,av_g,av_b

def munsell(pixellist): #returns the munsell list of the image
    min = 255
    av_r,av_g,av_b = avgclr(pixellist)
    r,g,b,h,v,c = dataset()
    munsell_img=[]
    index=0
    length = len(r)
    for i in range (length):
        loss=2.5*np.abs(r[i][0]-av_r)+2.5*np.abs(g[i][0]-av_g)+np.abs(b[i][0]-av_b)
    
        if(loss<=min):
            min=loss
            index=i

    munsell_img.append(h[index])
    munsell_img.append(v[index])
    munsell_img.append(c[index])
    return munsell_img

def displayMunsell(muns):
    string=''
    if(muns[0][0]=='10YR' or muns[0][0]=='10Y'):
        if(muns[2][0]<=2):
            string="Could be Black soil"
    if(muns[0][0]=='2.5YR' and muns[1][0]==4 and muns[1][0]>4):
        string='Could be Red Soil'
    if((muns[0][0]=='5R' or '7.5R') and (muns[1][0]==4 or muns[1][0]==3) and muns[1][0]>=4):
        string='Could be Red soil'
    print('Done')
    return string