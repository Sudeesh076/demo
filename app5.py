
from datetime import date
import streamlit as st
import pickle
import pandas as pd



st.set_page_config(page_title='Flight Price calculator',page_icon="✈")


model = pickle.load(open("flight_rf.pkl", "rb"))




st.markdown("<h1 style='text-align: center; color: red;'>Flight Price calculator</h1>", unsafe_allow_html=True)

st.image("1.jpeg")

st.write('Enter your details:')

with st.form("my_form"):

    D_date = st.date_input("Departure Date", date.today(),min_value = date.today() )

    D_time = st.time_input('Departure Time')

    A_date = st.date_input("Arrival Date", date.today(),min_value = date.today() )

    A_time = st.time_input('Arrival Time')

    stop = st.selectbox('Stop',(0,1,2,3,4))
    
    Source = st.selectbox('Source',('Delhi','Kolkata','Mumbai','Chennai'))
    
    Destination = st.selectbox('Destination',('Delhi','Kolkata','Mumbai','Chennai'))

    f_class = st.radio('Class',('economy','business','first'))
    
    airline_lst = ['Jet Airways','IndiGo','Air India','Multiple carriers','SpiceJet','Vistara','Air Asia','GoAir','Trujet']

    submitted = st.form_submit_button("Calculate")

    if submitted:

        Journey_month=D_date.month
        Journey_day=D_date.day
        Dep_hour = D_time.hour
        Dep_min= D_time.minute
        Arrival_hour = A_time.hour
        Arrival_min =  A_time.minute
        dur_hour  = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        Total_stops = stop
        Source1 = Destination

        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        if (Source1 == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source1 == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source1 == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source1 == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0
        elif (Source1 == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1
        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        prices = []
        for airline in airline_lst:
            if (airline == 'Jet Airways'):
                Jet_Airways = 1
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline == 'IndiGo'):
                Jet_Airways = 0
                IndiGo = 1
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline == 'Air India'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 1
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline == 'Multiple carriers'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 1
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline == 'SpiceJet'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 1
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline == 'Vistara'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 1
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline == 'GoAir'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 1
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline == 'Multiple carriers Premium economy'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 1
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0
            elif (airline == 'Jet Airways Business'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 1
                Vistara_Premium_economy = 0
                Trujet = 0

            elif (airline == 'Vistara Premium economy'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 1
                Trujet = 0

            elif (airline == 'Trujet'):
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 1

            else:
                Jet_Airways = 0
                IndiGo = 0
                Air_India = 0
                Multiple_carriers = 0
                SpiceJet = 0
                Vistara = 0
                GoAir = 0
                Multiple_carriers_Premium_economy = 0
                Jet_Airways_Business = 0
                Vistara_Premium_economy = 0
                Trujet = 0


            prediction = model.predict([[
                Total_stops,
                Journey_day,
                Journey_month,
                Dep_hour,
                Dep_min,
                Arrival_hour,
                Arrival_min,
                dur_hour,
                dur_min,
                Air_India,
                GoAir,
                IndiGo,
                Jet_Airways,
                Jet_Airways_Business,
                Multiple_carriers,
                Multiple_carriers_Premium_economy,
                SpiceJet,
                Trujet,
                Vistara,
                Vistara_Premium_economy,
                s_Chennai,
                s_Delhi,
                s_Kolkata,
                s_Mumbai,
                d_Cochin,
                d_Delhi,
                d_Hyderabad,
                d_Kolkata,
                d_New_Delhi
            ]])

            output = prediction[0]

            if f_class == 'business':
                output = output*2.5
            elif f_class == 'first':
                output = output * 4.2
            prices.append(round(output, 2))

        df = pd.DataFrame(
            {'Airline': airline_lst,
             'Price': prices
             })


        india_holidays = {
            '2024-01-01' : 'New Year',
            '2024-01-26': 'Republic Day',
            '2023-02-08': 'Holi',
            '2023-04-14' : 'Baisakhi',
            '2023-05-01': 'Maharashtra Day',
            '2023-08-15': 'Independence Day',
            '2023-08-29' : 'Onam',
            '2023-08-30': 'Raksha Bandhan',
            '2023-09-19': 'Ganesh Chaturthi',
            '2023-10-24' : 'Dussehra',
            '2023-11-12': 'Diwali',
            '2023-12-25': 'Merry Christmas'


        }


        try :
            p = "Congratulations! you got 10% of all flight on " + india_holidays.get(str(D_date))
            st.success(p)
            df["Discount_price"] = df["Price"] * 0.1

            st.dataframe(df.reset_index(drop=True), use_container_width=True)

        except:
            st.dataframe(df.reset_index(drop=True), use_container_width=True)













