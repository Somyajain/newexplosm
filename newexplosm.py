import requests
import bs4
import re
import os
start=raw_input('Enter the date of first comic(yyyy.mm.dd):')   # start from this date
end=raw_input('Enter the date of last comic(yyyy.mm.dd):')      # end at this date
beg_year=int(start[0:4]) #taking first year as int
end_year=int(end[0:4])   #taking last year as int
beg_month=int(start[5:7])
end_month=int(end[5:7])
beg_day=int(start[8:])
end_day=int(end[8:])
#------------- making or opening  folder on desktop-----------
os.chdir('C:\Users\sony\Desktop')
if not os.path.exists("C:\Users\sony\Desktop\cyanide comics"):
    os.mkdir('cyanide comics')
os.chdir('C:\Users\sony\Desktop\cyanide comics')
#-----------------------------------------------


for x in range(beg_year,end_year+1):  # starting with 2005 , then 2006,then 2007 etc
    if (x== end_year):               # checking if this is the last year
        for g in range(int(start[5:7]),int(end[5:7])+1 ):    # then the months would be till the required end month
            month_url=requests.get('http://explosm.net/comics/archive/'+str(x)+'/'+str(g)) 
            url_soup=bs4.BeautifulSoup(month_url.content)
            dates=url_soup.find_all(text=re.compile(str(x)+'.'+str(g)))
            for e in dates:
                year=int(e[0:4])
                month=int(e[5:7])
                day=int(e[8:])
                if (month<end_month):
                    if (day>beg_day
                
                div=url_soup.find('a',text=re.compile(e))
                comic_url=div.get('href')
                print comic_url
                url_source=requests.get('http://explosm.net'+comic_url)
                print url_source
                com_soup=bs4.BeautifulSoup(url_source.content,'lxml')
                main_com_div=com_soup.find(id='main-comic')
                src=main_com_div.get('src')
                finallycom=open(e+'.jpeg',"wb+")
                final2=requests.get('https:'+src)
                finallycom.write(final2.content)
                finallycom.close()
            
    else:
        for c in range(int(start[5:7]),13): # starting from given month till december of same year as next year too would have months
            month_url=requests.get('http://explosm.net/comics/archive/'+str(x)+'/'+str(c))
            url_soup=bs4.BeautifulSoup(month_url.content)
            dates=url_soup.find_all(text=re.compile(str(x)+'.'+str(c)))
            for e in dates:
                div=url_soup.find('a',text=re.compile(e))
                comic_url=div.get('href')
                print comic_url
                url_source=requests.get('http://explosm.net'+comic_url)
                print url_source
                com_soup=bs4.BeautifulSoup(url_source.content,'lxml')
                main_com_div=com_soup.find(id='main-comic')
                src=main_com_div.get('src')
                finallycom=open(e+'.jpeg',"wb+")
                final2=requests.get('https:'+src)
                finallycom.write(final2.content)
                finallycom.close()
        
            
            
            
       
