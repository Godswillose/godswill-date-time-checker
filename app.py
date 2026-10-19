
import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
from babel import Locale
from babel.core import get_global


# PAGE SETTINGS
st.set_page_config(
    page_title="Godswill's Date and Time Checker",
    page_icon="🌍",
    layout="centered"
)


# APP HEADING
st.markdown(
    "<h1 style='text-align:center;'>"
    "🌍 Godswill's Date and Time<br>Checker"
    "</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>"
    "Discover the current date and time around the world."
    "</p>",
    unsafe_allow_html=True
)


# RETRIEVE COUNTRIES AND TIME ZONES
english = Locale.parse("en")
territory_zones = get_global("territory_zones")

countries = {}

for code, timezones in territory_zones.items():

    if code in english.territories and timezones:

        country_name = english.territories[code]

        countries[country_name] = {
            "code": code.lower(),
            "timezones": sorted(set(timezones))
        }


# SORT COUNTRIES ALPHABETICALLY
countries = dict(sorted(countries.items()))


# DISPLAY NUMBER OF COUNTRIES
st.write(
    f"🌐 Explore {len(countries)} countries and territories"
)


# COUNTRY SELECTION
country = st.selectbox(
    "🌍 Search or select a country",
    list(countries.keys()),
    index=None,
    placeholder="Type a country name..."
)


# DISPLAY SELECTED COUNTRY
if country:

    country_code = countries[country]["code"]
    timezones = countries[country]["timezones"]

    # FLAG IMAGE
    flag_url = (
        f"https://flagcdn.com/w160/{country_code}.png"
    )

    col1, col2 = st.columns([1, 5])

    with col1:
        if len(country_code) == 2:
            st.image(flag_url, width=75)

    with col2:
        st.subheader(country)


    # CITY OR TIME ZONE SELECTION
    selected_zone = st.selectbox(
        "📍 Select a city or time zone",
        timezones,
        format_func=lambda zone: (
            zone.split("/")[-1].replace("_", " ")
        )
    )


    # CHECK DATE AND TIME BUTTON
    if st.button(
        "⏰ Check Date and Time",
        type="primary",
        use_container_width=True
    ):

        current_time = datetime.now(
            ZoneInfo(selected_zone)
        )

        st.success(
            f"Showing local date and time for {country}"
        )

        st.divider()

        # DATE AND TIME RESULTS
        with st.container(border=True):

            st.markdown(
                "### 📅 Current Date"
            )

            st.markdown(
                f"## {current_time.strftime('%A, %d %B %Y')}"
            )

            st.divider()

            st.markdown(
                "### ⏰ Current Time"
            )

            st.markdown(
                f"# {current_time.strftime('%I:%M:%S %p')}"
            )

            st.caption(
                f"📍 Time zone: {selected_zone}"
            )

else:

    st.info(
        "🌍 Please select a country to begin."
    )


# FOOTER
st.divider()

st.markdown(
    "<p style='text-align:center;'>"
    "Developed by Godswill Ose ❤️"
    "</p>",
    unsafe_allow_html=True
)
