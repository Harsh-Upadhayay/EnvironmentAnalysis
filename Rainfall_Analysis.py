from numpy.core.fromnumeric import cumsum
import pandas as Pd
import numpy as np
import matplotlib.pyplot as Plt



Dict = {'Albania':'ALB','Afghanistan':'AFG','Algeria':'DZA','American Samoa':'ASM','Andorra':'AND','Angola':'AGO',
'Anguilla':'AIA','Antigua and Barbuda':'ATG','Argentina':'ARG','Armenia':'ARM','Aruba':'ABW','Australia':'AUS',
'Austria':'AUT','Azerbaijan':'AZE','Bahrain':'BHR','Bangladesh':'BGD','Barbados':'BRB','Belarus':'BLR','Belgium':'BEL',
'Belize':'BLZ','Benin':'BEN','Bermuda':'BMU','Bhutan':'BTN','Bolivia':'BOL','Bosnia and Herzegovina':'BIH','Botswana':'BWA',
'Brazil':'BRA','British Indian Ocean Territory':'IOT','British Virgin Islands':'VGB','Brunei':'BRN','Bulgaria':'BGR',
'Burkina Faso':'BFA','Burundi':'BDI','Cambodia':'KHM','Cameroon':'CMR','Canada':'CAN','Cape Verde':'CPV','Cayman Islands':'CYM',
'Central African Republic':'CAF','Chad':'TCD','Chile':'CHL','China':'CHN','Christmas Island':'CXR','Cocos (Keeling) Islands':'CCK',
'Colombia':'COL','Comoros':'COM','Congo (Republic of the)':'COG','Congo (Democratic Republic of the)':'COD',
'Congo (Democratic Republic of the)':'ZAR','Cook Islands':'COK','Costa Rica':'CRI','Croatia':'HRV','Cuba':'CUB','Cyprus':'CYP',
'Czech Republic':'CZE','Denmark':'DNK','Djibouti':'DJI','Dominica':'DMA','Dominican Republic':'DOM','Ecuador':'ECU','Egypt':'EGY',
'El Salvador':'SLV','Equatorial Guinea':'GNQ','Eritrea':'ERI','Estonia':'EST','Ethiopia':'ETH','Falkland Islands (Islas Malvinas)':'FLK',
'Faroe Islands':'FRO','Fiji':'FJI','Finland':'FIN','France':'FRA','French Guiana':'GUF','French Polynesia':'PYF','Gabon':'GAB',
'West Bank and Gaza':'PSE','Georgia':'GEO','Germany':'DEU','Ghana':'GHA','Gibraltar':'GIB','Greece':'GRC','Greenland':'GRL',
'Grenada':'GRD','Guadeloupe':'GLP','Guam':'GUM','Guatemala':'GTM','Guinea':'GIN','Guinea-Bissau':'GNB','Guyana':'GUY','Haiti':'HTI',
'Honduras':'HND','Hungary':'HUN','Iceland':'ISL','India':'IND','Indonesia':'IDN','Iran':'IRN','Iraq':'IRQ','Ireland':'IRL',
'Israel':'ISR','Italy':'ITA','Jamaica':'JAM','Japan':'JPN','Jordan':'JOR','Kazakhstan':'KAZ','Kenya':'KEN','Kiribati':'KIR',
'Kosovo':'XRK','Kuwait':'KWT','Kyrgyz Republic':'KGZ','Laos':'LAO','Latvia':'LVA','Lebanon':'LBN','Lesotho':'LSO',
'Liberia':'LBR','Libya':'LBY','Liechtenstein':'LIE','Lithuania':'LTU','Luxembourg':'LUX','Macao SAR, China':'MAC',
'Republic of North Macedonia':'MKD','Madagascar':'MDG','Malawi':'MWI','Malaysia':'MYS','Maldives':'MDV','Mali':'MLI',
'Malta':'MLT','Marshall Islands':'MHL','Martinique':'MTQ','Mauritania':'MRT','Mauritius':'MUS','Mayotte':'MYT','Mexico':'MEX',
'Federated States of Micronesia':'FSM','Moldova':'MDA','Monaco':'MCO','Mongolia':'MNG','Republic of Montenegro':'MNE',
'Montserrat':'MSR','Morocco':'MAR','Mozambique':'MOZ','Myanmar (Burma)':'MMR','Namibia':'NAM','Nauru':'NRU',
'Nepal':'NPL','Netherlands':'NLD','Netherlands Antilles':'ANT','New Caledonia':'NCL','New Zealand':'NZL','Nicaragua':'NIC',
'Niger':'NER','Nigeria':'NGA','Niue':'NIU','Norfolk Island':'NFK','South Korea':'PRK','Northern Mariana Islands':'MNP',
'Norway':'NOR','Oman':'OMN','Pakistan':'PAK','Palau':'PLW','Panama':'PAN','Papua New Guinea':'PNG','Paraguay':'PRY','Peru':'PER',
'Philippines':'PHL','Pitcairn Islands':'PCN','Poland':'POL','Portugal':'PRT','Puerto Rico':'PRI','Qatar':'QAT','Reunion':'REU',
'Romania':'ROU','Russia':'RUS','Rwanda':'RWA','Samoa':'WSM','San Marino':'SMR','Sao Tome and Principe':'STP','Saudi Arabia':'SAU',
'Senegal':'SEN','Republic of Serbia':'SRB','Seychelles':'SYC','Sierra Leone':'SLE','Singapore':'SGP','Slovakia':'SVK',
'Slovenia':'SVN','Solomon Islands':'SLB','Somalia':'SOM','South Africa':'ZAF','North Korea':'KOR','South Sudan':'SSD',
'Spain':'ESP','Sri Lanka':'LKA','St. Helena':'SHN','St. Kitts and Nevis':'KNA','St. Lucia':'LCA','St. Vincent and the Grenadines':'VCT',
'Sudan':'SDN','Suriname':'SUR','Svalbard':'SJM','Eswatini':'SWZ','Sweden':'SWE','Switzerland':'CHE','Syria':'SYR',
'Tajikistan':'TJK','Tanzania':'TZA','Thailand':'THA','Bahamas':'BHS','Gambia':'GMB','Timor Leste':'TLS','Togo':'TGO',
'Tokelau':'TKL','Tonga':'TON','Trinidad and Tobago':'TTO','Tunisia':'TUN','Turkey':'TUR','Turkmenistan':'TKM',
'Turks and Caicos Islands':'TCA','Tuvalu':'TUV','Uganda':'UGA','Ukraine':'UKR','United Arab Emirates':'ARE',
'United Kingdom':'GBR','United States':'USA','Uruguay':'URY','Uzbekistan':'UZB','Vanuatu':'VUT','Venezuela':'VEN',
'Vietnam':'VNM','Virgin Islands':'VIR','Western Sahara':'ESH','Wallis and Futuna':'WLF','Yemen':'YEM',
'Zimbabwe':'ZWE','Zambia':'ZMB'}



def Analyse_Rain_Countries(Country = ['India','China'],Start_Year = 1901 , End_Year = 2020):
    

    Flag = 0
    Frame = Pd.DataFrame
    for country in Country:

        # Reading the Csv File
        File = Pd.read_csv(r'datasets/Precipitation_Datasets/pr_timeseries_annual_cru_1901-2020_' + str(Dict[country])  + '.csv',header= 1)
        
        #File.drop(labels = 'Variable:',axis = 0,inplace= True)
        #File = File.truncate(before = 1901 , after=2020)
        #File = File.drop(columns=File.index[0])
        File.rename(columns={'Unnamed: 0':'Year'},inplace=True)  # Setting unnamed column as Year
        
        File = File[(File['Year'] >= Start_Year) & (File['Year'] <= End_Year)]   # Taking data between given years
        File = File[['Year',country]]   # Dataframe for country along year
        File.reset_index(drop=True , inplace=True)

        if(Flag == 0):
            Frame = File
            Flag = 1
        else:
            Frame = Frame.merge(File)

    return Frame



File = Analyse_Rain_Countries(['India','China'],1901 ,2020)

#print(File.columns)


File.plot( x = 'Year', color='blue', marker = 'o', linestyle = 'dashed',linewidth = 2,markersize = 12,
            subplots = True ,title = 'Annual Rainfall in MM',figsize = (15,15),ylabel = 'Rainfall in MM')

#Avg = File[File.columns[1]].mean()
#Plt.axhline(y = Avg)
#Avg1 = File[File.columns[2]].mean()
#Plt.axhline(y = Avg1)
#Plt.title('Annual Rainfall in MM')

Plt.show()