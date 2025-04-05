import streamlit as st
from PIL import Image
import io

# Set app config
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")

# Header
st.title("💪 Body Mass Index (BMI) Calculator")
st.markdown("Welcome! Use this tool to calculate your BMI and get health insights based on your result.")

st.markdown("---")

# Input section
st.subheader("🧍🧍‍♀️ Enter Your Details")

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=1, max_value=120, value=25, step=1)
weight = st.number_input("Weight (kg)", min_value=1.0, value=60.0, step=0.5)
height = st.number_input("Height (m)", min_value=0.5, value=1.65, step=0.01)

# BMI Calculation
def calculate_bmi(weight, height):
    return weight / (height ** 2)

def get_bmi_status(bmi):
    if bmi < 18.5:
        return "Underweight", "Consider gaining weight through a healthy diet."
    elif 18.5 <= bmi < 24.9:
        return "Normal weight", "Great job! Keep maintaining your lifestyle."
    elif 25 <= bmi < 29.9:
        return "Overweight", "Consider regular exercise and balanced meals."
    else:
        return "Obese", "Seek guidance from a healthcare provider."

# Age and Gender Based Advice
def age_based_advice(age):
    if age < 18:
        return "BMI interpretations vary for children. Consider consulting a pediatrician."
    elif age >= 60:
        return "In older adults, BMI should be considered along with other factors like muscle mass."
    else:
        return "Maintain a healthy lifestyle with exercise and good nutrition."

def gender_based_advice(gender):
    if gender == "Female":
        return "Females often have higher body fat %. Consider muscle mass too."
    elif gender == "Male":
        return "Males generally have more muscle mass; BMI may not reflect that."
    else:
        return "Everyone's body is unique. Use BMI as one of several health indicators."

# Calculate button
if st.button("🎯 Calculate My BMI"):
    bmi = calculate_bmi(weight, height)
    status, advice = get_bmi_status(bmi)
    age_advice = age_based_advice(age)
    gender_advice = gender_based_advice(gender)

    st.markdown("---")
    st.subheader("📊 Results")
    st.success(f"**Your BMI is:** `{bmi:.2f}`")
    st.info(f"**Health Status:** {status}")
    st.write(f"💬 **Advice:** {advice}")
    st.write(f"🧠 **Age Tip:** {age_advice}")
    st.write(f"🌈 **Gender Insight:** {gender_advice}")

    # Display BMI Chart
    st.markdown("### 🧾 BMI Classification Chart")
    bmi_image = Image.open("BMI-Chart.jpg")  # You can download a BMI chart image and place it in the same folder
    st.image(bmi_image, use_container_width=True)

    # Generate report text
    report = f"""
🎯 BMI REPORT
-----------------------
👤 Gender: {gender}
🎂 Age: {age} years
⚖️ Weight: {weight} kg
📏 Height: {height} m

📌 BMI: {bmi:.2f}
🧠 Health Status: {status}

💬 Advice:
- {advice}
- {age_advice}
- {gender_advice}
"""

    # Download button
    st.download_button(
        label="📥 Download My BMI Report",
        data=report,
        file_name="bmi_report.txt",
        mime="text/plain"
    )

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Maryam Shahid")
