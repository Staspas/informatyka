import streamlit as st
import datetime

# st.title("Tytuł")

# st.write("test")

# st.toggle("On off")

col1, col2 = st.columns(2)

result = True #st.button("get data!")
if result:
    import http.client
    import json

    conn = http.client.HTTPSConnection("api-gory.imgw.pl")

    conn.request("GET", "/pages/pages?name=dolina_pieciu_stawow")

    r1 = conn.getresponse()

    r1.status, r1.reason

    data = json.loads(r1.read())

    with col1:
        data

    with col2:
        town_prop = data['town']

        town_name_prop = town_prop['name']

        st.header(town_name_prop)
        st.write(town_prop['county'])

        st.write("Wysokość "+str(town_prop['heightAboveSeaLevel'])+" n.p.m.")


        town_forecast_prop = data['townForecast']

        temp_kelvin = float(town_forecast_prop['analysis']['temperature'])
        temp_celc = temp_kelvin-273.15

        iso_date = town_forecast_prop['analysis']['date']
        town_forecast_date = datetime.datetime.fromisoformat(iso_date)

        tz = datetime.datetime.now().astimezone().tzinfo
        st.write("Timezone: "+str(tz))
        local_forecast_date = town_forecast_date.astimezone(tz)
        st.write(local_forecast_date.date())
        st.write(local_forecast_date.time())

        st.write(str(round(temp_celc, 1))+" °C")

        town_forecast_prop



    # st.header(data['town']['name'])

    import streamlit as st
    import pandas as pd
    import numpy as np

    lat = data['town']['lat']
    lon = data['town']['lon']

    df = pd.DataFrame(
        {"lat": [lat], "lon": [lon]},
        columns=["lat", "lon"],
    )
    st.map(df)

    # data


# number = st.slider("Pick a number", 0, 100)

# import pandas as pd
# import numpy as np
# import altair as alt

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# c = (
#    alt.Chart(chart_data)
#    .mark_circle()
#    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
# )

# st.altair_chart(c, use_container_width=True)


# xxxxx = {
#     "nazwa": "Alfred",
#     "rodzaj": "człowiek",
#     "wysokość": 7,
#     "": 1111

# }

# xxxxx

# lista = [ "jeden", "dwa", "czy"]

# lista