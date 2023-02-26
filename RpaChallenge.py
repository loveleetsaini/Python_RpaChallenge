# Import module
import rpa as r
import pandas as pd

#read the excel
dt = pd.read_excel('challenge.xlsx')

#Start the tagUi
r.init(turbo_mode = True)

#Open the Website
r.url('https://www.rpachallenge.com/')
r.wait(10)


# Click on Start Btn
r.click('//button[text ()="Start"]')

for index, row in dt.iterrows():
    r.type('//input[@ng-reflect-name = "labelFirstName"]', row['First Name'])
    r.type('//input[@ng-reflect-name = "labelLastName"]', row['Last Name '])
    r.type('//input[@ng-reflect-name = "labelCompanyName"]', row['Company Name'])
    r.type('//input[@ng-reflect-name = "labelRole"]', row['Role in Company'])
    r.type('//input[@ng-reflect-name = "labelAddress"]', row['Address'])
    r.type('//input[@ng-reflect-name = "labelEmail"]', row['Email'])
    r.type('//input[@ng-reflect-name = "labelPhone"]', str(row['Phone Number']))
    r.click('//input[@value="Submit"]')

#Screenshot of Webpage
r.snap('/html/body/app-root/div[2]/app-rpa1/div', 'results.png')

#Stop the TagUi
r.close()