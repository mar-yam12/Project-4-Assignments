import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

# Set page title and favicon
st.set_page_config(
    page_title="Pet Boarding & Breeding Services",
    page_icon="🐾",
    layout="centered"
)

# Adding custom styles
st.markdown("""
    <style>
        .main {
            background-color: #F0F8FF;
            padding: 20px;
        }
        .header {
            color: #FF6347;
            font-size: 3rem;
            font-weight: bold;
            text-align: center;
        }
        .subheader {
            color: #4CAF50;
            font-size: 2rem;
        }
        .service-section {
            background-color: #FFFAF0;
            padding: 20px;
            border-radius: 10px;
            margin-top: 10px;
        }
        .button {
            background-color: #FF6347;
            color: white;
            padding: 10px;
            border-radius: 5px;
            font-size: 1.2rem;
        }
        .footer {
            text-align: center;
            margin-top: 50px;
            font-size: 1.2rem;
            color: #0f035c;
        }
    </style>
""", unsafe_allow_html=True)

# Homepage Content
def homepage():
    st.markdown('<h1 class="header">🐾 Welcome to Our Pet Boarding & Breeding Services! 🐾</h1>', unsafe_allow_html=True)
    st.markdown("""
    We offer safe and comfortable accommodations for your pets. Book a stay or find a companion for breeding!
    """)
    
    st.markdown("### 🐶 Our Services 🐱")
    st.markdown("""
    - **Cat & Dog Boarding**: Give your pets a safe and comfortable place to stay when you're away.
    - **Pet Breeding**: Professional and caring breeding services for cats and dogs.
    """)
    
    st.markdown("""
    **Book Now** your pet's stay or breeding services by choosing from the menu above!
    """)
    
    st.image("https://www.dogtagart.com/cdn/shop/articles/dogcat1.jpg?v=1724266347", use_container_width=True)

# Booking Page Content
def booking_page():
    st.markdown('<h1 class="header">📝 Book Our Services 📝</h1>', unsafe_allow_html=True)
    st.markdown("### Choose Your Service and Pet Type")
    
    service_type = st.selectbox("Choose Service Type", ["Boarding", "Breeding"], key="service_type")
    pet_type = st.selectbox("Pet Type", ["Cat", "Dog"], key="pet_type")
    pet_name = st.text_input(f"Enter Your {pet_type}'s Name", key="pet_name")
    pet_age = st.number_input("Pet's Age", min_value=1, max_value=20, key="pet_age")
    boarding_dates = st.date_input("Select Boarding Dates", key="boarding_dates")
    
    if st.button("Book Now", key="book_now"):
        st.success(f"🎉 Your booking for a {service_type} for {pet_type} {pet_name} is confirmed! 🎉")
    
    st.image("https://c02.purpledshub.com/uploads/sites/41/2024/08/Cats-vs-dogs-whos-smarter.jpg?w=1200", use_container_width=True)

# Adoption Page Content
def adoption_page():
    st.markdown('<h1 class="header">🐕 Available Pets for Adoption 🐈</h1>', unsafe_allow_html=True)
    st.markdown("""
    These cats and dogs are looking for a new home! Contact us for more details and adoption processes.
    """)
    
    pets = [
        {"name": "Max", "type": "Dog", "breed": "Golden Retriever", "age": "2 years", "image": "https://cdn.prod.website-files.com/651577594cea61d37cb19467/65b823fc36f0844f29fa704f_Golden%20Retriever.jpg"},
        {"name": "Bella", "type": "Cat", "breed": "Persian", "age": "1 year", "image": "https://cdn.shopify.com/s/files/1/1199/8502/files/persian-doll-face.jpg"},
        {"name": "Charlie", "type": "Dog", "breed": "Beagle", "age": "3 years", "image": "https://images.squarespace-cdn.com/content/v1/5b3fc87b45776e887e966e82/ea4b3853-7558-4048-8051-d986e71ec39d/beagle-on-meadow-2021-08-26-15-58-22-utc.jpg"}
    ]
    
    for pet in pets:
        st.subheader(f"{pet['name']} - {pet['type']} ({pet['breed']})")
        st.markdown(f"**Age**: {pet['age']}")
        st.image(pet['image'], width=200)
        st.markdown("**Contact us to adopt this pet!**")
        st.markdown("---")

# Contact Page Content
def contact_page():
    st.markdown('<h1 class="header">📬 Contact Us 📬</h1>', unsafe_allow_html=True)
    name = st.text_input("Your Name", key="contact_name")
    email = st.text_input("Your Email", key="contact_email")
    message = st.text_area("Your Message", key="contact_message")
    
    if st.button("Send Message", key="send_message"):
        send_email(name, email, message)
        st.success("✅ Your message has been sent successfully!")
    
    st.image("https://www.intelligencesquared.com/wp-content/uploads/3-10.png", use_container_width=True)

def send_email(name, email, message):
    try:
        sender_email = "maryamshahid772@gmail.com"  # Your email address
        receiver_email = "abc@example.com"  # Recipient's email
        password = "123456789"  # Your email password

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = f"New Inquiry from {name}"

        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        st.error(f"Error: {e}")

# Main Function
def main():
    # Create tabs for navigation
    tab1, tab2, tab3, tab4 = st.tabs(["Homepage", "Book a Service", "Adopt a Pet", "Contact Us"])
    
    with tab1:
        homepage()
    with tab2:
        booking_page()
    with tab3:
        adoption_page()
    with tab4:
        contact_page()
    
    # Add footer
    st.markdown("""
    <div class="footer">
        <p>© 2025 Pet Boarding & Breeding Services. All rights reserved.</p>
        <p>Powered by Maryam Shahid </p>
        <p>Contact us: info@petboarding.com | Phone: (123) 456-7890</p>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
