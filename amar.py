import streamlit as st
import pandas as pd
import pickle
import os
#import dotenv
#dotenv.load_dotenv('.env')
#from sklearn.ensemble import RandomForestClassifier
# Load the order dataset

crew_edit_data = pd.read_csv("crew-edit-preprocessed.csv")

# Define custom CSS styles
custom_css = """
<style>
    body {
        background-color: #f5f5f5; /* Background color for the entire page */
        font-family: Arial, sans-serif; /* Font for the entire page */
    }

    .title {
        font-size: 30px; /* Font size for the title */
        color: #000; /* Set title color to black */
        text-align: center; /* Center the title */
        padding: 5px 0; /* Add some padding */
    }

    .container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .column {
        width: 45%; /* Adjust the width as needed */
        background-color: #fff; /* Background color for the columns */
        border: 1px solid #ddd; /* Add a border around columns */
        padding: 10px; /* Add padding to columns */
        margin: 10px 0; /* Add margin between columns */
    }

    .text-input {
        background-color: #eee; /* Background color for text inputs */
    }
</style>
"""


def display_day_of_week(choice):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    st.write(f"**You chose {days_of_week[choice]}.**")


def display_month(choice):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    st.write(f"**You chose {months[choice - 1]}.**")  # Adjusting for 1-based indexing of months


# Main function to run the Streamlit app
def main():
    st.set_page_config(
        page_title="Price Prediction",
        page_icon="✅",
        layout="wide"  # Use wide layout for fixed sidebar
    )
    
    # Include custom CSS styles

    # Sidebar style
    st.sidebar.title("Navigation Menu")
    menu = st.sidebar.selectbox("Choose an option:", ["Home", "Crew-Edit EDA", "Production EDA", "Transmission EDA", "Crew-Edit Price Prediction", "Production Price Prediction",
                                                      "Transmission Price Prediction"])

    if menu == "Home":
        image1 = "logo.jpg"
        image2 = "logo2.jpg"

        st.markdown(custom_css, unsafe_allow_html=True)
        # Display images on the top left and top right
        st.image(image1, width=200)
        st.image(image2, width=100)
        st.markdown('<p class="title"> Amar Abbani </p>', unsafe_allow_html=True)
        st.markdown('<p class="title"> Welcome to Predictive Dynamics: Crew-Edit, Production, Transmission, and Beyond </p>', unsafe_allow_html=True)
        st.write("Tailored Predictions Across Crew-Edit, Production, and Transmission Departments: Your Insights, Your Way!")
        
        col1, col2 = st.columns(2)
        # Display images in each column
        with col1:
            st.image("col2.png", use_column_width=True)
        with col2:
            st.image("col3.png", use_column_width=True)        
        
        st.write("The fast pace technological era we live in has forced industries of all sorts to constantly evolve at a rapid pace, "
                 "one industry who has to go through significant conversions is the broadcasting industry, it is crucial for companies in this segment "
                 "adjust and optimize their strategies constantly. Founded in the year 2000 in Beirut city, ISOL, a leading supplier of communications "
                 "solutions which includes specialist broadcast solutions, media facilities, and operational services stands at the head of this complex dynamic environment. "
                 "By offering a wide range of services, such as production, editing, and post-production, media monitoring, news gathering and transmission, and satellite "
                 "space capacity, ISOL has established out a unique place for itself in the market. Due to its wide range of services, "
                  "which it offers to both domestic and foreign customers, the company has established itself as a major participant in the market.")
        st.write("")  # This adds an empty line
        col3, col4 = st.columns(2)
        # Display images in the second row
        with col3:
            st.image("col5.png", use_column_width=True)        
        with col4:
            st.image("col6.png",  use_column_width=True)
        st.write("Although ISOL how's experienced success it still needs to overcome obstacles common to the broadcast sector this includes intricate "
                 "and ever-changing pricing schemes and the requirement for the efficient use of resources the dynamic character of the customer and the swift "
                 "advancements of the transmission technologies also leads to a more intricate and multifaceted pricing Scheme. Managing operational efficiency "
                 "requires optimizing the use of the resources such as the personnel equipment and studios needed for the job.")
    
        
    if menu == "Crew-Edit EDA":
        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown('<p class="title"> Crew-Edit EDA </p>', unsafe_allow_html=True)
        st.write("")
        st.image("crew1.png", caption="Distribution of Jobs Across Clients", use_column_width=True)
        st.write("The bar plot above showcases the number of jobs per client. The length of the bars clearly indicates which clients are bringing in the most work. ")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("crew2.png", caption="Distribution of Jobs by Type", use_column_width=True)
        st.write("The bar plot above visualizes the distribution of jobs by their type, showing the frequency of each service type offered by the company. ")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("crew3.png", caption="Jobs Trend Over Time", use_column_width=True)
        st.write("The line graph above visualizes the trend of jobs over time, aggregated by month. This visualization provides insights into how the demand for the company's services fluctuates throughout the year. ")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("crew4.png", caption="Pricing Analysis for Different Types of Services", use_column_width=True)
        st.write("The box plot visualizes the pricing structure for different types of services offered by the company, revealing critical insights into how pricing varies and how it might impact business strategy. ")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("crew5.png", caption="Crew Duration vs. Edit Duration", use_column_width=True)
        st.write("The scatter plot provided shows the relationship between 'Crew Duration' and 'Edit Duration' for various projects or jobs. Understanding the dynamics between crew and edit durations can provide strategic insights into operational efficiency, cost management, and potentially customer satisfaction through faster delivery times. ")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("crew6.png", caption="Client segmentation analysis", use_column_width=True)
        st.write("Distribution of Clients Across Segments: This bar chart presents the number of clients in each of the 'High Value', 'Moderate Value', and 'Low Value' segments. It shows a concentration of clients in the 'Moderate Value' segment. ")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("crew7.png", caption="Average Frequency and Pricing by segment", use_column_width=True)
        st.write("**Average Frequency by Segment**: The bar chart shows the average frequency of transactions for each segment, giving insights into how often clients in each segment engage with the services. ")
        st.write("")  # This adds an empty line
        st.write("")
        st.write("**Average Pricing by Segment**: This bar chart displays the average pricing within each segment, indicating the average spending level of clients in each category. ")
        
                
    if menu == "Production EDA":

        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown('<p class="title"> Production EDA </p>', unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.image("pr1.png", caption="Number of Jobs Over Time", use_column_width=True)
        st.write("The time series graph shows the number of jobs over time for ISOL. From the graph, it appears that the jobs are not evenly distributed over time. There are specific periods where the number of jobs spikes significantly, indicating a much higher workload during these times.")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("pr2.png", caption="Distribution of Job Types", use_column_width=True)
        st.write("The bar chart you've provided shows the distribution of job types for the broadcasting company.")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("pr3.png", caption="Top 10 Clients", use_column_width=True)
        st.write("The bar chart presents the distribution of the top clients for the broadcasting company, showing how many times services were provided to each over a given time period.")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("pr4.png", caption="Relationship between Job Duration and Price", use_column_width=True)
        st.write("The scatter plot illustrates the relationship between job duration and price for the broadcasting company's services. ")
        
        
    if menu == "Transmission EDA":

        st.markdown(custom_css, unsafe_allow_html=True)
        st.markdown('<p class="title"> Transmission EDA </p>', unsafe_allow_html=True)
        st.write("")
        st.image("tr1.png", caption="Frequency of transactions by client", use_column_width=True)
        st.write("Frequency of Transactions by Client: It highlights which clients use the services most frequently. Some clients have significantly higher transaction counts compared to others.")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("tr2.png", caption="Types of transactions", use_column_width=True)
        st.write("The graph shows specific transaction types like Live Studio Transmission, Space Segment, and others, each represented by a bar indicating its frequency. The variation in the frequency of different transaction types gives insights into how diversified the service offerings are and also reflect client preferences and needs.")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("tr3.png", caption="Duration analysis", use_column_width=True)
        st.write("The histogram shows the frequency of transactions across different duration intervals, The spread of the histogram shows the range of transaction durations. A wide spread indicates a diverse range of service durations, from very short to very long.")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("tr4.png", caption="Satellite usage", use_column_width=True) 
        st.write("Frequent usage of certain satellites may warrant strategic partnerships or negotiations for better rates or dedicated services. This information is key for strategic decisions regarding technology investments, partnerships with satellite providers, and understanding thelimitations of services")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("tr5.png", caption="Client segmentation analysis", use_column_width=True) 
        st.write("The visualizations provide a detailed view of the client segmentation analysis")
        st.write("Distribution of Clients Across Segments:")
        st.write("The bar graph shows the number of clients in each segment: 'High Value', 'Moderate Value', and 'Low Value'. It's evident that the majority of clients fall into the 'Moderate Value' category, with fewer clients in the 'High Value' and 'Low Value' segments.")
        st.write("")  # This adds an empty line
        st.write("")
        st.image("tr6.png", caption="Average Frequency and Pricing by segment", use_column_width=True) 
        st.write("**Average Frequency by Segment:**")
        st.write("This graph compares the average frequency of transactions for clients in each segment. 'High Value' clients have the highest average frequency, indicating they engage with the services more often.")
        st.write("**Average Pricing by Segment:**")
        st.write("This graph shows the average pricing for each segment.")
    
  
if __name__ == "__main__":
    main()
