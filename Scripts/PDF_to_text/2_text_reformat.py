"""
2_text_reformat.py
Author: Justin Rush (GRC-LTE0, LERCIP)
Updated: 18 Sept 2020
Permanent Contact: Paht Juanphanich (GRC-LTE0) or Karsten Look (GRC-LTE0)

This script takes the text csv from textricator and reformatted it to be useable. 
For this script to work effectively there must be no demicals in the headers of the pdfs 
and in the text csv the headers and their units must be in different cells (you can see this on the text csv from textricator)

Most pdfs fit these credentials but if not please separate them and run this script with the modified varable (look out of comments)

Make sure that textricator's input format is set to pdf.itext5
"""




import pandas as pd
import string 
import re
import sys
import glob


runpath = sys.argv[1]
#Example Run Commandment: python 2_text_reformat.py ".\\data_folder\\"

print('=== reformat_csv.py === : Processing File: {}'.format(runpath))

allfiles = glob.glob(runpath+"*_extracted.csv")

bad=[]
for f in allfiles:
    print(f"now processing {f}")
    try:
        


        df = pd.read_csv(f, encoding= "ISO-8859-1")

        #Cleaning 
        df.drop(columns= ["width","height","font","fontSize"], inplace=True)

        def check (value):
            for letter in value:
                if letter not in string.ascii_letters + string.digits + ' '+'/.()-|"':
                    value = value.replace(letter,"")
                
            return value

        df["content"]= df["content"].apply(lambda x: check(str(x)))
        df["fontColor"] = df["fontColor"].apply(lambda x: check(str(x)))
        df["bgcolor"]= df["bgcolor"].apply(lambda x: check(str(x)))

        df.drop(columns = ["fontColor","bgcolor"], inplace=True)



        #Receiving the Pre-Existing Headers and values from the Dataframe
        data ={}
        data["PN"]= df["content"][df["ulx"]== df[df["content"] == "P/N"]["ulx"].values[0] ].reset_index(drop=True).drop(labels=0).values 
        lry = df["lry"][(df['content'].str.contains(r'^Height.*', regex=True)) & (df["lry"]> 500)].values[0]

        """
        For headers that have units in the same cell in the text csv set lry to
        df["lry"][df['content'] == "Height in(mm)"].values[0]
        """
        
        
        headers = df[df["lry"]==lry]["content"].values


        for i in headers:
            ulx = df[df["content"] == i]["ulx"].values[0]
            data[i]= df["content"][df["ulx"]== ulx ].reset_index(drop=True).drop(labels=[0,1]).values





        final_df = pd.DataFrame(data)

        #create new columns 

        mask = df['content'].str.contains(r'^[0-9]*[0-9]+(?:\(|[ CFMLFM])', regex=True)

        """
        For pdfs that have headers that are demical set mask to
        df['content'].str.contains(r'^[0-9]+\.[0-9][ CFMLFM]', regex=True)
        """

        lry = df["lry"][mask].max()

        ulx_perfy = df["ulx"][mask][df["lry"]== lry].reset_index(drop=True)

        perf = df["content"][mask][df["lry"]== lry]

        for idx,i in enumerate(perf):
            final_df[f"Perf{idx+1}x"] = re.sub(r"\((.*)\)|[ CFM]","",i)
            
            

        mask_xunit= df["content"].apply(lambda x: True if ("LFM" in x or "CFM" in x) else False)

        final_df["xUnits"]= df["content"][mask_xunit].str.extract(r"(LFM | CFM)").values[0][0]

        for idx,i in enumerate(perf):
            final_df[f"Perf{idx+1}y"]= df["content"][df["ulx"]==ulx_perfy[idx]].reset_index(drop=True).drop(labels=0).values

        final_df["yUnits"] ="Thermal Resistance in C/W"

        final_df["Footprint_Inches"]= df["content"][df['lry']==df["lry"].min()].apply(lambda x: x.replace("FOOTPRINT","").strip()).values[0]

        final_df["Configuration"]= df.nsmallest(2,"lry")["content"].str.extract(r"(\w+.*)\|").values[1][0]
        final_df["Material"]= df["content"][df["content"].str.contains(pat="Material",regex=False)].apply(lambda x: x.replace("Material","").strip()).values[0]

        
        #Cleans the headers and separate the units 
        number =2
        for i in headers:
            final_df.insert(number,re.sub(r"\s","_",i)+'_MM',final_df[i].apply(lambda x: re.search(r"\((.*)\)",str(x)).group(1) ))
            final_df[i] = [re.sub(r"\((.*)\)","",str(i)) for i in final_df[i]]
            final_df= final_df.rename(columns= {i: re.sub(r"\s","_",i)+"_Inches"})
            number+=2

        """
        For headers that have units in the same cell in the text csv change the block above to
        final_df.insert(number,re.sub(r"\s*\w+\(\w+\)","_MM",i),final_df[i].apply(lambda x: re.search(r"\((.*)\)",str(x)).group(1) ))
        final_df[i] = [re.sub(r"\((.*)\)","",str(i)) for i in final_df[i]]
        final_df= final_df.rename(columns= {i: re.sub(r"\s*\w+\(\w+\)","_Inches",i)})
        number+=2
        """

        #For the case of weight
        final_df = final_df.rename(columns= {"Weight_Inches":"Weight_lbs","Weight_MM":"Weight_Grams"}) #If the pdf has a different units then Inches and MM add the units like weight
        
        
        final_df.to_csv(f[:-4]+'_formatted.csv',index=False)


        print(f"COMPLETE {f[:-4]}_newformatted.csv")
        

    except:
        # For debugging 
        bad.append(f[:-4])
        print("NOT GOOD")
        

print(bad)
print(len(bad))