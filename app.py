import streamlit as st
import pandas as pd
import os

# CSV file to store responses
DATA_FILE = "client_feedback.csv"

# Load existing data if file exists
if os.path.exists(DATA_FILE):
    feedback_data = pd.read_csv(DATA_FILE)
else:
    feedback_data = pd.DataFrame(columns=[
        "Client Name", "Organization", "Project/Service",
        "Satisfaction", "Communication", "Timeliness", "Quality", "Professionalism",
        "Testimonial", "Additional Comments"
    ])

st.title("📋 Client Feedback Form")

# --- General Information ---
st.header("General Information")
client_name = st.text_input("Client Name")
organization = st.text_input("Organization")
project = st.text_input("Project / Service")

# --- Satisfaction Rating ---
st.header("Satisfaction Rating")
satisfaction = st.radio("Overall satisfaction with our service:",
                        ["⭐⭐⭐⭐⭐ Excellent", "⭐⭐⭐⭐ Good", "⭐⭐⭐ Average", "⭐⭐ Poor", "⭐ Very Poor"])

communication = st.slider("Communication", 1, 5, 5)
timeliness = st.slider("Timeliness of Delivery", 1, 5, 5)
quality = st.slider("Quality of Work", 1, 5, 5)
professionalism = st.slider("Professionalism", 1, 5, 5)

# --- Testimonial Section ---
st.header("Testimonial (Optional but Appreciated 🙏)")
st.markdown(
    "When we present our solutions to prospective clients, "
    "they greatly value hearing about the experiences of our existing clients. "
    "We only use testimonial quotes in **PowerPoint presentations** — never on the internet or in public forums."
)
testimonial = st.text_area("Please provide a few sentences on the value you’ve received from Exavalu:")

# --- Additional Comments ---
st.header("Additional Comments")
comments = st.text_area("Any other suggestions or feedback?")

# --- Submit Button ---
if st.button("Submit Feedback"):
    new_entry = {
        "Client Name": client_name,
        "Organization": organization,
        "Project/Service": project,
        "Satisfaction": satisfaction,
        "Communication": communication,
        "Timeliness": timeliness,
        "Quality": quality,
        "Professionalism": professionalism,
        "Testimonial": testimonial,
        "Additional Comments": comments
    }

    # Append and save
    feedback_data = pd.concat([feedback_data, pd.DataFrame([new_entry])], ignore_index=True)
    feedback_data.to_csv(DATA_FILE, index=False)

    st.success("✅ Thank you for your valuable feedback!")
    st.write("Here’s what you submitted:")
    st.json(new_entry)

# --- Admin Section: Download Feedback ---
st.header("📂 Export Feedback Data")

if not feedback_data.empty:
    # Show table preview
    st.dataframe(feedback_data)

    # Download as CSV
    csv = feedback_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="⬇️ Download as CSV",
        data=csv,
        file_name='client_feedback.csv',
        mime='text/csv',
    )
else:
    st.info("No feedback submitted yet. Submissions will appear here for download.")