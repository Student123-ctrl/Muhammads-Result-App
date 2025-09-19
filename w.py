import streamlit as st
import speedtest

# App title
st.set_page_config(page_title="Internet Speed Tester", page_icon="⚡", layout="centered")
st.title("⚡ Muhammad's Internet Speed Tester")

st.write("Click the button below to check your internet speed.")

# Button to check speed
if st.button("Check Speed"):
    st.info("Testing... please wait ⏳")
    st.spinner("Running speed test...")

    try:
        st_test = speedtest.Speedtest()
        st_test.get_servers()
        download_speed = round(st_test.download() / (10**6), 2)  # in Mbps
        upload_speed = round(st_test.upload() / (10**6), 2)      # in Mbps

        st.success("✅ Test Completed")
        st.metric(label="Download Speed", value=f"{download_speed} Mbps")
        st.metric(label="Upload Speed", value=f"{upload_speed} Mbps")

    except Exception as e:
        st.error(f"⚠️ Error: {e}")