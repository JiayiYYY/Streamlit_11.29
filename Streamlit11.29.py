import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset for main analysis
file_path = 'dogs_dataset.csv'
dogs_data = pd.read_csv(file_path)

# Custom CSS for gradual header effect
st.markdown(
    """
    <style>
    .fade-in-text {
        animation: fadeIn 3s ease-in-out;
        color: #ff6347;
        font-size: 40px;
        text-align: center;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("Explore Cute Angels 🐾")
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Breed Analysis", "Breed Distribution", "Age and Weight Insights", "Color Distribution"]
)

# Home Page
if page == "Home":
    st.markdown('<h1 class="fade-in-text">Welcome to Cute Angels 🐶🐾</h1>', unsafe_allow_html=True)
    st.image(
        "WechatIMG27.png",
        caption="Exploring the cutest companions!",
        width=500
    )

    choice = st.radio(
        "Are you a DOG🐶 lover or a CAT🐱 lover?", 
        ["", "Dog", "Cat"]
    )
    if choice == "Dog":
        st.success(
            "Great, me too! This app explores insights about our beloved dogs, "
            "including breeds, ages, weights, colors, and more. Let’s dive in!"
        )
    elif choice == "Cat":
        st.error("Oops, sorry, choose again.")
    else:
        st.write("Please make a choice to continue!")

# Breed Analysis Page
elif page == "Breed Analysis":
    st.header("Now Let's Explore These Cuties Together 🐕")

    # Load the breed details dynamically
    breed_file_path = 'image.csv'
    breed_data = pd.read_csv(breed_file_path, header=0)

    # Breed Selection
    selected_breed = st.selectbox("Select a Breed to Explore:", breed_data["Breed"].unique())

    # Display Selected Breed Details
    breed_info = breed_data[breed_data["Breed"] == selected_breed].iloc[0]
    st.write(f"### {selected_breed}")

    # Breed Image
    image_path = breed_info["Image"]
    if pd.notna(image_path) and image_path.strip():
        try:
            st.image(image_path, width=400, caption=selected_breed)
        except Exception:
            st.write("Image not available or path is invalid.")
    else:
        st.write("Image not available.")

    # Dynamic Details
    st.write(f"**Country of Origin:** {breed_info['Country of Origin']}")
    st.write(f"**Fur Color:** {breed_info['Fur Color']}")
    st.write(f"**Height (in):** {breed_info['Height (in)']}")
    st.write(f"**Color of Eyes:** {breed_info['Color of Eyes']}")
    st.write(f"**Longevity (yrs):** {breed_info['Longevity (yrs)']}")
    st.write(f"**Character Traits:** {breed_info['Character Traits']}")
    st.write(f"**Common Health Problems:** {breed_info['Common Health Problems']}")

# Breed Distribution Page
elif page == "Breed Distribution":
    st.header("Map of Breed Distribution")

    # Display the main map image
    st.image(
        "https://cdn.householdquotes.co.uk/cdn-cgi/image/format=auto/15/2023/06/01_Most-Popular-Dog-Breed-in-Every-Country.png",
        caption="Most Popular Dog Breeds Around the World",
        use_container_width=True  # Replaced use_column_width
    )

    # Introductory text
    st.write(
        "The Rottweiler is number one dog in 34 countries – the highest number of appearances for any breed. "
        "However, the Australian Shepherd is the most-searched breed in the world, with 913,000 monthly hits across the 4 countries where it is number one. "
        "The most popular dog in the UK is the cockapoo. The 150 territories in our study share a love for just 27 different dog breeds."
    )

    # Add selection for different regions
    region = st.selectbox(
        "Choose a region to explore:",
        ["Middle East and Central Asia", "Rest of Asia and Oceania", "Europe", "North America", "South America", "Africa"]
    )

    # Region-specific content
    region_content = {
        "Middle East and Central Asia": {
            "text": (
                "The German shepherd is the most popular dog in seven countries of the region "
                "(plus a further 22 around the world). This working dog with a heart of gold is also "
                "known as an Alsatian, after British troops refused to call their four-legged colleagues "
                "‘Germans’ during World War II."
            ),
            "image": "https://cdn.householdquotes.co.uk/cdn-cgi/image/format=auto/15/2023/06/05_Most-Popular-Dog-Breed-in-Middle-East-and-Central-Asia.png"
        },
        "Rest of Asia and Oceania": {
            "text": (
                "Asian breeds such as the shiba inu have made their way west, partly thanks to how internet-friendly "
                "this neat little dog (or doge) is. But the shiba makes its biggest mark in Asia, where she is top dog "
                "in Hong Kong, Japan, Korea, and Singapore."
            ),
            "image": "https://cdn.householdquotes.co.uk/cdn-cgi/image/format=auto/15/2023/06/06_Most-Popular-Dog-Breed-in-Rest-of-Asia-and-Oceania.png"
        },
        "Europe": {
            "text": (
                "The UK is known as a nation of dog-lovers, with around a quarter of UK adults sharing a population "
                "of 10.1 million dogs. Their favourite? The cockapoo. What-apoo? For the uninitiated, the cockapoo is "
                "a cross between a cocker spaniel and a poodle. In other words, intelligent, fun – and manageable! "
                "Just make sure you get your cross-breed from an ethical breeder."
            ),
            "image": "https://cdn.householdquotes.co.uk/cdn-cgi/image/format=auto/15/2023/06/02_Most-Popular-Dog-Breed-in-Europe.png"
        },
        "North America": {
            "text": (
                "The ultimate family dog has climbed up on top of the continent: the golden retriever takes Canada! "
                "This “intelligent, confident worker”/friendly pillow is the second-most searched breed in our study, "
                "and the most popular breed in 22 countries – beaten only by the Rottweiler (34) and German shepherd (29)."
            ),
            "image": "https://cdn.householdquotes.co.uk/cdn-cgi/image/format=auto/15/2023/06/03_Most-Popular-Dog-Breed-in-North-America.png"
        },
        "South America": {
            "text": (
                "The number one dog in our study is especially beloved by South Americans. But the powerful Rottweiler counts "
                "the mastiffs of the Roman legions as her ancestors. Today, she is valued as a dog that does both: offers a fierce warning "
                "to potential intruders while coveting a bit of sofa time with her family."
            ),
            "image": "https://cdn.householdquotes.co.uk/cdn-cgi/image/format=auto/15/2023/06/04_Most-Popular-Dog-Breed-in-South-America.png"
        },
        "Africa": {
            "text": (
                "The German shepherd is most popular in 14 African countries, just edging out the Rottweiler, who is most-searched "
                "in 13 places. But the Boerboel makes a good effort too: all four of her number one appearances are in African countries "
                "(Mozambique, Namibia, South Africa, and Zimbabwe). In fact, this tough, intelligent dog originated in South Africa."
            ),
            "image": "https://cdn.householdquotes.co.uk/cdn-cgi/image/format=auto/15/2023/06/07_Most-Popular-Dog-Breed-in-Africa.png"
        }
    }

    # Display content based on selection
    selected_region = region_content[region]
    st.write(selected_region["text"])
    st.image(selected_region["image"], caption=region, use_container_width=True)

# Age and Weight Insights Page
elif page == "Age and Weight Insights":
    st.header("Age and Weight Insights")
    
    # Gender filter
    selected_gender = st.selectbox("Filter by Gender:", ["All", "Male", "Female"])
    
    # Weight category filter
    weight_category = st.selectbox(
        "Filter by Weight Category:",
        ["All", "Small (<10 kg)", "Medium (10-25 kg)", "Large (>25 kg)"]
    )
    
    # Sliders for filtering age
    min_age, max_age = st.slider(
        "Select Age Range (Years):", 
        0, 
        dogs_data['Age (Years)'].max(), 
        (0, 15)
    )
    
    # Apply filters to dataset
    filtered_data = dogs_data[
        (dogs_data['Age (Years)'] >= min_age) & 
        (dogs_data['Age (Years)'] <= max_age)
    ]
    if selected_gender != "All":
        filtered_data = filtered_data[filtered_data['Gender'] == selected_gender]
    if weight_category == "Small (<10 kg)":
        filtered_data = filtered_data[filtered_data['Weight (kg)'] < 10]
    elif weight_category == "Medium (10-25 kg)":
        filtered_data = filtered_data[
            (filtered_data['Weight (kg)'] >= 10) & 
            (filtered_data['Weight (kg)'] <= 25)
        ]
    elif weight_category == "Large (>25 kg)":
        filtered_data = filtered_data[filtered_data['Weight (kg)'] > 25]
    
    # Filtered scatter plot
    scatter_fig = px.scatter(
        filtered_data,
        x="Age (Years)",
        y="Weight (kg)",
        color="Breed",
        title="Age vs. Weight (Filtered)",
        labels={"Age (Years)": "Age (Years)", "Weight (kg)": "Weight (kg)"},
        hover_data=["Breed", "Color", "Gender"],
        opacity=0.7,  # Add transparency to reduce density effect
        size_max=10,  # Adjust maximum dot size
    )
    st.plotly_chart(scatter_fig, use_container_width=True)

# Color Distribution Page
elif page == "Color Distribution":
    st.header("Color Distribution")
    
    # Pie chart for color proportions
    selected_gender_color = st.selectbox("Filter by Gender:", ["All", "Male", "Female"])
    color_data = dogs_data if selected_gender_color == "All" else dogs_data[dogs_data['Gender'] == selected_gender_color]
    color_counts = color_data['Color'].value_counts()
    pie_fig = px.pie(
        names=color_counts.index,
        values=color_counts.values,
        title="Color Distribution",
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    st.plotly_chart(pie_fig, use_container_width=True)
