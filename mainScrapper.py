import requests
import pandas as pd
from bs4 import BeautifulSoup as bs 
from datetime import date
import os


URL = "http://www.qcb.gov.qa/english/publications/statistics/realestate/pages/realestatepriceindex.aspx"



def loadWebPage():
    # Load the webpage
    r = requests.get(URL)
    soup = bs(r.content, "html.parser")
    return soup




def createDataFrame(soup):
    # extract the table data as a list of DataFrames
    dfs = pd.read_html(str(soup.find("table", class_="TableNewStyle")))

    # select the first DataFrame in the list (assuming there is only one table)
    df = dfs[0]

    # Rename the DataFrame because of this weird tab syntax
    df = df.rename(columns={"t\u200b\u200b\u200bYear": "Year"})
    # remove \u200b from the empty year row
    df['Year'] = df['Year'].replace('\u200b', pd.np.nan)
    
    # replace NaN's
    df["Year"].fillna(method="ffill",  limit=len(df), inplace=True)
    return df

def saveCSV(df):
    # save the file
    today = date.today()

    PATH = "IndexData/"+ 'RIPIQ_'+str(today)+".csv"
    #check if directory exists
    if os.path.exists("IndexData"):
        df.to_csv(PATH, index=False)
        print("File saved")
        return
    print("Creating new directory")
    os.mkdir("IndexData")
    print("Successfully created directory")
    df.to_csv(PATH, index=False)
    print("File saved")
    return

    



if __name__ == "__main__":
    soup = loadWebPage()
    df = createDataFrame(soup)
    # save the file
    saveCSV(df)


