import streamlit as st
import google.generativeai as genai

genai.configure(api_key='')
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to interact with Google Generative AI
def generate_response(prompt):
    response = model.generate_content(f"{prompt} with markdown formatting")
    output= response.text
    return output

# Function to gather user preferences and generate itinerary
def get_user_preferences():
    st.title("AI Travel Planner")
    st.write("Plan your perfect trip with a personalized itinerary!")

    # Collect user inputs
    destination = st.text_input("Where would you like to travel?")
    duration = st.number_input("How many days will your trip last?", min_value=1, step=1)
    budget = st.text_input("What is your approximate budget for the trip?")
    activities = st.text_area("What activities do you enjoy? (e.g., sightseeing, adventure, shopping, relaxing)")
    dietary = st.text_input("Do you have any dietary preferences or restrictions?")
    mobility = st.text_input("Any mobility concerns or walking tolerance?")
    accommodation = st.selectbox("What type of accommodation do you prefer?", ["Luxury", "Budget", "Centrally Located"])

    # Generate itinerary when the button is clicked
    if st.button("Generate Itinerary"):
        with st.spinner("Creating your itinerary..."):
            # Prepare user details for the prompt
            user_details = (
                f"Destination: {destination}\n"
                f"Duration: {duration} days\n"
                f"Budget: {budget}\n"
                f"Activities: {activities}\n"
                f"Dietary Preferences: {dietary}\n"
                f"Mobility Concerns: {mobility}\n"
                f"Accommodation Preference: {accommodation}"
            )

            # Define the prompt
            prompt = (
                "You are an AI travel planner. Based on the following user inputs, create a detailed day-by-day itinerary.\n"
                f"{user_details}\n"
                "Ensure the itinerary includes top-rated attractions, dining options, and timing for activities."
            )

            
            itinerary = generate_response(prompt)
            st.success("Here's your personalized itinerary:")
            st.text(itinerary)

if __name__ == "__main__":
    get_user_preferences()
