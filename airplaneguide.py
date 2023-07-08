import streamlit as st
import pandas as pd
from PIL import Image


def planechooser(choice) :
    if choice == "A220 Family" :
        st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a220-family/Airbus-A220-familly-2.jpg?wid=1920&fit=fit,1&qlt=85,0','The A220 Family. Photo: Airbus',use_column_width=True)
        choice2 = st.selectbox("Select Aircraft Model: ", ("","A220-100", "A220-300"))
        if choice2 == "A220-100" :
            st.write("# A220-100")
            st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a220-family/a220-100/Airbus-A220-100-1.jpg?wid=1920&fit=fit,1&qlt=85,0', 'Airbus A220-100. Photo: Airbus',use_column_width=True)
            st.write('The Airbus A220-100 is a small regional jet. This jet was originally was made by Bombardier, called the C-Series, but due to financial circumstances, Airbus then bought the program and renamed the CS100 to the A220-100.')
            st.write('## Quick Facts about the A220-100:   ')
            st.write('Range: 3450 nautical miles/6390 kilometers')
            st.write('Usual seating in a two-class configuration: 100-120 passengers')
            st.write('Length: 114 feet 9 inches/35 meters')
            st.write('Height: 37 feet 8 inches/11.5 meters')
            st.write('Wingspan: 115 feet 1 inch/35.1 meters')
            st.write('Engine Count: 2')
            st.write('Engine Type: Pratt and Whitney PurePower PW1500G')
            st.write('Engine Thrust: 23,300 pounds of thrust for each engine')
            st.write('Sets of Landing Gear: 3; 1 pair of 2 wheels for nose gear, 2 pairs of 2 wheels for main gear')
            st.write('Max Cruise Speed: 470 knots/870 kilometers per hour')
            st.write('Service Ceiling: 41,000 feet')
            st.write('Takeoff Distance Needed: 4800 feet/1463 meters')
            st.write('Landing Distance Needed: About 4600 feet/1387 meters')
            st.write('Manufacturer Price(No Discounts): from 81 million dollars')
            st.write('Current Status: In Production and Flying')
            st.write('#### All information is taken from the following websites: ')
            st.write('##### simpleflying.com')
            st.write('##### aerocorner.com')
            st.write('##### Airbus')
            st.write('##### Pratt and Whitney')
            st.write('## How to Identify the A220-100: ')
            st.write('The A220(Both Variants) has 4 cockpit windows and they form two curves when you look at it from the front.')
            st.write('The A220-100 is a very short plane with big engines. It is much more shorter than its bigger brother, the A220-300.')
            st.write('The A220-100 has 12 windows in the front before the emergency exit.')
            st.image('https://www.cpat.com/wp-content/uploads/2020/07/A220-100-to-300-diff-1-1024x569.png','The differences between the Airbus A220-100 and the Airbus A220-300 are miniscule. Photo: cpat.com', use_column_width=True)
            st.write('## The A220-100 has very few operators around the world. These are:')
            st.write('### Air Vanuata')
            st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a220-family/a220-100/A220-100-Air-Vanuatu-01.jpg?wid=3626&fit=constrain','Air Vanuata has yet to recieve its first A220-100. Photo: Airbus', use_column_width=True)
            st.write('### Delta Airlines')
            st.image('https://airlinesfleet.com/wp-content/uploads/2019/01/N101DU-Delta-Air-Lines-Aircraft-Fleet-Airbus-A220-100-Photos.jpg','Delta Airlines is largest operator of the A220-100. Photo: airlinesfleet.com', use_column_width=True)
            st.write('### Swiss International Air Lines')
            st.image('https://cdn.planespotters.net/04788/hb-jbe-swiss-airbus-a220-100_PlanespottersNet_872258_9107a6ef8c_o.jpg','Swiss International Air Lines was the launch customer of the Airbus A220-100/CS100. Photo: planespotters.net', use_column_width=True)
            st.write('##### Information from planespotters.net')
        if choice2 == "A220-300" :
            st.write("# A220-300")
            st.image('https://www.aero-mag.com/wp-content/uploads/2018/07/AMJuly18News-airbus-e1531310657717-1024x714.jpg', 'Airbus A220-300. Photo: aero-mag.com',use_column_width=True)
            st.write('The A220-300, like the A220-100 is a small regional jet designed by Bombardier. It was originally names the CS300, and later changed to the A220-300 when Airbus acquired the program.')
            st.write('Quick Facts about the A220-300:  ')
            st.write('Range: 3400 nautical miles/6297 kilometers')
            st.write('Usual seating in a two-class configuration: 120-150 passengers')
            st.write('Length: 127 feet/38.7 meters')
            st.write('Height: 37 feet 8 inches/11.5 meters')
            st.write('Wingspan: 115 feet 1 inch/35.1 meters')
            st.write('Engine Count: 2')
            st.write('Engine Type: Pratt and Whitney PurePower PW1500G')
            st.write('Engine Thrust: 23,300 pounds of thrust for each engine')
            st.write('Sets of Landing Gear: 3; 1 pair of 2 wheels for nose gear, 2 pairs of 2 wheels for main gear')
            st.write('Max Cruise Speed: 447 knots/828 kilometers per hour')
            st.write('Service Ceiling: 41,000 feet')
            st.write('Takeoff Distance Needed: About 6200 feet/1890 meters')
            st.write('Landing Distance Needed: About 4950 feet/1509 meters')
            st.write('Manufacturer Price(No Discounts): from 91.5 million dollars')
            st.write('Current Status: In Production and Flying')
            st.write('#### All information is taken from the following websites: ')
            st.write('##### aerocorner.com')
            st.write('##### Airbus')
            st.write('##### Pratt and Whitney')
            st.write('## How to Identify the A220-300: ')
            st.write('The A220-300 has 16-17 windows in the front before the emergency exit. This is the larger variant of the A220 Family')
            st.write('The A220-300 is also the more common variant of the two.')
            st.write('## The A220-300 has poured in interest from many different airlines. They are: ')
            st.write('### Air Austral')
            st.image('https://airwaysmag.com/wp-content/uploads/2019/10/A220-Air-Austal_.jpg','Air Austral is using the A220-300 to replace their older, inefficiet aircraft. Photo: aiwaysmag.com', use_column_width=True)
            st.write('### Air Baltic')
            st.image('https://airwaysmag.com/wp-content/uploads/2019/12/A220-AirBaltic-takeoff.jpg','Air Baltic has an all A220-300 fleet. It is also the launch operator of the type. Photo: airwaysmag.com', use_column_width=True)
            st.write('### Air Canada')
            st.image('https://www.ainonline.com/sites/ainonline.com/files/styles/ain30_fullwidth_large_2x/public/uploads/2021/04/a220-300-4.jpeg?itok=99RyKuMQ','Air Canada also a retro livery of the A220. Photo: ainonline.com', use_column_width=True)
            st.write('### Air Manas')
            st.image('https://www.ch-aviation.com/images/stockPhotos/8757/2cb396f1503cf141ebd022196100a530618b791b.jpg','Air Manas restarts its plans with the Airbus A220-300. Photo: ch-aviation.com', use_column_width=True)
            st.write('### Air Tanzania')
            st.image('https://cdn.aerotelegraph.com/production/uploads/2019/07/Airbus_A220_Air_Tanzania.jpg','Air Tanzania is the first African based operator of the A220-300. Photo: cdn.aerotelegraph.com', use_column_width=True)
            st.write('### Air Vanuatu')
            st.image('https://bloximages.chicago2.vip.townnews.com/dailypost.vu/content/tncms/assets/v3/editorial/2/62/26263c56-e7e8-11ea-86fd-fbe05f16e69d/5f46dd134e8b6.image.png','Air Vanuatu introduces a new business class with its A220-300. Photo: dailypost.vu', use_column_width=True)
            st.write('### Delta')
            st.image('https://cdn.planespotters.net/49779/n302du-delta-air-lines-airbus-a220-300_PlanespottersNet_1131638_c03e6327a4_o.jpg','Delta Airlines is the biggest operator of the A220-300. Photo: planespotters.net', use_column_width=True)
            st.write('### EgyptAir')
            st.image('https://cdn.planespotters.net/27932/su-gez-egyptair-airbus-a220-300_PlanespottersNet_1014633_d193b447f2_o.jpg','Egyptair is the first airline(between the Arab carriers) to operate the A220-300. Photo: planespotters.net', use_column_width=True)
            st.write('### Ibom Air')
            st.image('https://www.ibomair.com/wp-content/uploads/2021/06/WhatsApp-Image-2021-06-14-8.jpeg','Ibom Air is operating 2 ex-Air Sinai Airbus A220-300s. Photo: Ibom Air', use_column_width=True)
            st.write('### jetBlue')
            st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a220-family/a220-300/AIRBUS230-1st-JetBlue-206.jpg?wid=3626&fit=constrain','JetBlue is the third operator of the A220-300 in North America. Photo: Airbus', use_column_width=True)
            st.write('### Korean Air')
            st.image('https://i1.wp.com/en.aviation-report.com/wp-content/uploads/sites/2/2020/11/Airbus-A220-Korean-Air.jpg?resize=750%2C400','Korean Air uses the A220-300 to restore its domestic and regional network. Photo: en.aviation-report.com', use_column_width=True)
            st.write('### Swiss International Air Lines')
            st.image('https://airwaysmag.com/wp-content/uploads/2019/10/SwissA220.jpg','Swiss Interational Air Lines uses the A220-300 to help neutralize its carbon emissions by 2050. Photo: airwaysmag.com', use_column_width=True)
            st.write('##### Information from planespotters.net')
    if choice == "A300 Family" :
        st.write("Sorry! This page isn't built yet.")
    if choice == "A310 Family" :
        st.write("Sorry! This page isn't built yet.")
    if choice == "A320 Family" :
        choice5 = st.selectbox("Select Aircraft Model: ", ("","A318","A319","A320","A321"))
        if choice5 == "A318" :
            st.write("# A318")
            st.image('https://www.ch-aviation.com/images/stockPhotos/5152/c70092399367605f09aceb88e5627bf06b4f0212.jpg','Airbus A318. Photo: ch-aviation.com',use_column_width=True)
            st.write('The Airbus A318, or the \'Baby Bus\', is the smallest member of the Airbus A320 Family. It is the only member that does not have a new engine option(neo) version. It was not a commercial success, with only 81 aircraft being made for commercial use.')
            st.write('Quick Facts about the A318:  ')
            st.write('Range: 3100 nautical miles/5750 kilometers')
            st.write('Usual seating in a two-class configuration: 90-110 passengers')
            st.write('Length: 103 feet 2 inches/31.44 meters')
            st.write('Height: 41 feet 2 inches/12.56 meters')
            st.write('Wingspan: 111 feet 11 inches/34.1 meters')
            st.write('Engine Count: 2')
            st.write('Engine Types: CFM International CFM56-5B or Pratt and Whitney PW6000')
            st.write('Engine Thrust: CFM56-5B: 23,300, PW6000: 23,800')
            st.write('Sets of Landing Gear: 3; 1 pair of 2 wheels for nose gear, 2 pairs of 2 wheels for main gear')
            st.write('Max Cruise Speed: 516 knots/956 kilometers per hour')
            st.write('Service Ceiling: 39,000 feet')
            st.write('Takeoff Distance Needed: 4445.48 feet/1355 meters')
            st.write('Landing Distance Needed: 4448.76 feet/1356 meters')
            st.write('Manufacturer Price(No Discounts): from 77.4 million dollars')
            st.write('Current Status: Confusing, Airbus still hasn\'t stopped production, but most are retired. It\'s a very rare sight. Air France is the sole commercial operator of the A318 currently.')
            st.write('#### All information is taken from the following websites: ')
            st.write('##### aerocorner.com')
            st.write('##### Airbus')
            st.write('## How to Identify the A318: ')
            st.write('The A318 is very short. It has 11 windows in front of the emergency exit.')
            st.write('The A318 also will look like it has a gigantic tail for its size.')
            st.write('## The A318 is a niche offering of the A320 family and has not recieved much orders. However, these are the airlines that tried it:  ')
            st.write('### Air France')
            st.image('https://airlinesfleet.com/wp-content/uploads/2019/02/Air-France-Airbus-A318-111-F-GUGI-at-Frankfurt-Airport-1024x674.jpg','Air France is the largest operator of the A318. Photo: airlinesfleet.com',use_column_width=True)
            st.write('### British Airways')
            st.image('https://airwaysmag.com/wp-content/uploads/2020/06/British_Airways-G-EUNB-Airbus-A318-112-Anna-Zvereva-Tallinn-Estonia-1200x640-1.jpg','British Airways used A318s for London City Airport. Photo: airwaysmag.com', use_column_width=True)
            st.write('### Tarom')
            st.image('https://cdn.jetphotos.com/full/5/40798_1514198087.jpg','Tarom is starting to retire its A318s. Photo: jetphotos.com',use_column_width=True)
            st.write('### Frontier Airlines')
            st.image('https://cdn.jetphotos.com/full/2/82151_1236124162.jpg','Frontier was the launch customer for the A318. Photo: jetphotos.com')
            st.write('### Avianca Airlines')
            st.image('https://cdn.jetphotos.com/full/5/83276_1489494296.jpg','Avianca\'s youngest A318 is only 20 months old! Photo: jetphotos.com')
            st.write('### There is a private jet version of the A318. It is called the ACJ318')
            st.write('#### All information is taken from the following websites:  ')
            st.write('##### planespotters.net')
            st.write('##### simpleflying.com')
        if choice5 == "A319" :
            choice_5 = st.selectbox("Select Aircraft Type: ", ("","A319ceo", "A319neo"))
            if choice_5 == "A319ceo" :
                st.write("# A319ceo")
                st.image('https://jet.voyage/wp-content/uploads/2020/03/cfa8cce771042cbc3196c6da8b5e9581-1280x720.jpg','Airbus A319ceo. Photo: jet.voyage',use_column_width=True)
            if choice_5 == "A319neo" :
                st.write("# A319neo")
                st.image('https://worldairlinenews.files.wordpress.com/2019/04/airbus-a319neo-d-avwa-tkoairbushr.jpg?w=625&h=417','Airbus A319neo. Photo: worldairlinenews.com', use_column_width=True)
        if choice5 == "A320" :
            choice__5 = st.selectbox("Select Aircraft Type: ", ("","A320ceo", "A320neo"))
            if choice__5 == "A320ceo" :
                st.write("# A320ceo")
                st.image('https://airwaysmag.com/wp-content/uploads/2016/01/airbus-a320-house-colors-1.jpg','Airbus A320ceo. Photo: airwaysmag.com',use_column_width=True)
            if choice__5 == "A320neo" :
                st.write("# A320neo")
                st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a320-family/a320neo/A320neo_CFM_Airbus_neo_livery_V07.jpg?wid=1920&fit=fit,1&qlt=85,0','Airbus A320neo. Photo: Airbus',use_column_width=True)
        if choice5 == "A321" :
            choice___5 = st.selectbox("Select Aircraft Type: ", ("","A321ceo", "A321neo", "A321LR", "A321XLR"))
            if choice___5 == "A321ceo" :
                st.write("# A321ceo")
                st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a320-family/a321/A321_SHARKLET_IAE_AIRBUS_V02_300dpi.jpg?wid=3626&fit=constrain','Airbus A321ceo. Photo: Airbus', use_column_width=True)
            if choice___5 == "A321neo" :
                st.write("# A321neo")
                st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a320-family/a321neo/A321neo_TAKE_OFF_.jpg?wid=1920&fit=fit,1&qlt=85,0','Airbus A321neo. Photo: Airbus',use_column_width=True)
            if choice___5 == "A321LR" :
                st.write("# A321LR")
                st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/events/first-flight/20180131_P3499_A321LR_FF_ML_RAW_0041.jpg?wid=1920&fit=fit,1&qlt=85,0','Airbus A321LR. Photo: Airbus', use_column_width=True)
            if choice___5 == "A321XLR" :
                st.write("# A321XLR")
                st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a320-family/a321neo/A321XLR-02.jpg?wid=1920&fit=fit,1&qlt=85,0','Airbus A321XLR. Photo: Airbus', use_column_width=True)
    if choice == "A330 Family" :
        choice6 = st.selectbox("Select Aircraft Model: ", ("","A330-200","A330-300","A330-800neo","A330-900neo"))
        if choice6 == "A330-200" :
            st.write("# A330-200")
            st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a330-family/a330-200/A330-200_GE_AIRBUS_V10_300dpi.jpg?wid=1920&fit=fit,1&qlt=85,0','Airbus A330-200. Photo: Airbus', use_column_width=True)
        if choice6 == "A330-300" :
            st.write("# A330-300")
            st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a330-family/a330-300/A330-300_GE_AIRBUS_V08_300dpi.jpg?wid=1000&qlt=85,0','Airbus A330-300. Photo: Airbus', use_column_width=True)
        if choice6 == "A330-800neo" :
            st.write("# A330-800neo")
            st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a330-family/a330neo/a330-800/A330-800-first-flight-landing.jpg?wid=1920&fit=fit,1&qlt=85,0','Airbus A330-800neo. Photo: Airbus', use_column_width=True)
        if choice6 == "A330-900neo" :
            st.write("# A330-900neo")
            st.image('https://worldairlinenews.files.wordpress.com/2019/01/airbus-a330-900neo-f-wtte-fltairbuslrw.jpg?w=625&h=417','Airbus A330-900neo. Photo: worldairlinenews', use_column_width=True)
    if choice == "A340 Family" :
        choice7 = st.selectbox("Select Aircraft Model:", ("", "A340-200","A340-300","A340-500","A340-600"))
        if choice7 == "A340-200" :
            st.write("# A340-200")
            st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a340-family/a340-200/A340_200_Airbus_2009.jpg?wid=1000&qlt=85,0','Airbus A340-200. Photo: Airbus', use_column_width=True)
        if choice7 == "A340-300" :
            st.write("# A340-300")
            st.image('https://upload.wikimedia.org/wikipedia/commons/e/ec/Airbus_A340-300_Airbus_Industries_%28AIB%29_%22House_colors%22_F-WWAI_-_MSN_001_%2810223075916%29.jpg','Airbus A340-300. Photo: Airbus', use_column_width=True)
        if choice7 == "A340-500" :
            st.write("# A340-500")
            st.image('https://www.gmt-sales.com/wp-content/uploads/2016/10/1-5.jpg','Airbus A340-500. Photo: Airbus', use_column_width=True)
        if choice7 == "A340-600" :
            st.write("# A340-600")
            st.image('https://airbus-h.assetsadobe2.com/is/image/content/dam/products-and-solutions/commercial-aircraft/a340-family/a340-600/A340-600_RR_AIRBUS_V02_300dpi.jpg?wid=1000&qlt=85,0','Airbus A340-600. Photo: Airbus', use_column_width=True)
    if choice == "A350 Family" :
        choice8 = st.selectbox("Select Aircraft Model:", ("","A350-900","A350-1000"))
        if choice8 == "A350-900" :
            choice_8 = st.selectbox("Select Aircraft Type: ", ("","A350-900","A350-900ULR"))
            if choice_8 == "A350-900" :
                st.write("# A350-900")
                st.image('https://live.staticflickr.com/3870/15185062499_bba55fa0dc_b.jpg','Airbus A350-900. Photo: live.staticeflickr.com', use_column_width=True)
            if choice_8 == "A350-900ULR" :
                st.write("# A350-900ULR")
                st.image('https://transport-central.com/image78','There is no visual change between the Airbus A350-900 and the Airbus A350-900ULR. Photo: transport-central.com', use_column_width=True)
        if choice8 == "A350-1000" :
            st.write("# A350-1000")
            st.image('https://live.staticflickr.com/454/31505927700_7aaa04d9d1_b.jpg','Airbus A350-1000. Photo: live.staticflickr.com', use_column_width=True)
    if choice == "A380 Family" :
        choice9 = st.selectbox("Unfortunately, the A380-800 is the only model in this family.", ("","A380-800"))
        if choice9 == "A380-800" :
            st.write("# A380-800")
            st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Airbus_A380_blue_sky.jpg/600px-Airbus_A380_blue_sky.jpg','Airbus A380-800. Photo: upload.wikimedia.org', use_column_width=True)
    if choice == "707 Family" :
        st.write('wiw')
    if choice == "717 Family" :
        st.write('wiw')
    if choice == "727 Family" :
        st.write('wiw')
    if choice == "737 Family" :
        choose4 = st.selectbox('Select Aircraft Model: ',('','737-100','737-200','737-300','737-400','737-500','737-600','737-700','737-800','737-900ER','737 MAX 7','737 MAX 8','737 MAX 9','737 MAX 10'))
    if choice == "747 Family" :
        choose5=st.selectbox('Select Aircraft Model: ', ('','747-100','747-200','747-300','747-400','747-8i'))
    if choice == "757 Family" :
        st.write('wiw')
    if choice == "767 Family" :
        st.write('wiw')
    if choice == "777 Family" :
        st.write('wiw')
    if choice == "787 Family" :
        choose9 = st.selectbox('Select Aircraft Model: ', ('','787-8', '787-9','787-10'))
def main() :
    st.title("AeroGuide: A Guide to Identify Airplanes")
    choice = st.selectbox("What Aircraft Manufacturer would you like to identify?", ("", "Airbus", "Boeing"))
    if choice == "Airbus" :
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT256bV9yFaOmHKLJH1hQ9U5wrlF6WQw5-X_g&usqp=CAU', use_column_width=True)
        choice1 = st.selectbox("Select the Aircraft Family: ", ("","A220 Family","A300 Family","A310 Family","A320 Family", "A330 Family","A340 Family","A350 Family","A380 Family"))
        planechooser(choice1)
    if choice == "Boeing" : 
        st.image('https://static.wixstatic.com/media/834ef2_e7389fd86e6b45e5a2a67d478bd8a76c~mv2.jpg/v1/fill/w_849,h_278,al_c,q_90/file.jpg', use_column_width=True)
        choiceboeing = st.selectbox("Select the Aircraft Family: ", ("","707 Family","717 Family","727 Family","737 Family","747 Family","757 Family","767 Family","777 Family","787 Family"))
        planechooser(choiceboeing)




main()

