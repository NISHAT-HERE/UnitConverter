import streamlit as st
from PIL import Image
import base64
import pandas as pd
import io
import numpy as np

# Set matplotlib backend to Agg for deployment environments
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Made by NISHAT",
    page_icon="🔄",
    layout="wide"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main {
        background-color: #f5f7fa;
    }
    .stTitle {
        color: #2c3e50;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0;
    }
    .stSubheader {
        color: #34495e;
        font-family: 'Helvetica Neue', sans-serif;
        text-align: center;
        margin-top: 0;
    }
    .css-1kyxreq {
        justify-content: center;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        border: none;
        padding: 0.5rem 1rem;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    .result-card {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        text-align: center;
    }
    .info-card {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .category-icon {
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    .stSelectbox label {
        color: #2c3e50;
        font-weight: bold;
    }
    .stNumberInput label {
        color: #2c3e50;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("UniConvert Pro")
st.markdown("### Instant Unit Conversion Tool")

# Create a two-column layout
col1, col2 = st.columns([1, 2])

# Conversion categories and their icons
categories = {
    "Length": "📏",
    "Weight/Mass": "⚖️",
    "Time": "⏱️",
    "Temperature": "🌡️",
    "Area": "📐",
    "Volume": "🧪",
    "Speed": "🚀",
    "Data": "💾",
    "Pressure": "🔄",
    "Energy": "⚡"
}

# Define conversion units for each category
conversion_options = {
    "Length": [
        "Kilometers to Miles", "Miles to Kilometers", 
        "Meters to Feet", "Feet to Meters",
        "Centimeters to Inches", "Inches to Centimeters",
        "Millimeters to Inches", "Inches to Millimeters",
        "Yards to Meters", "Meters to Yards",
        "Nautical Miles to Miles", "Miles to Nautical Miles"
    ],
    "Weight/Mass": [
        "Kilograms to Pounds", "Pounds to Kilograms",
        "Grams to Ounces", "Ounces to Grams",
        "Metric Tons to Pounds", "Pounds to Metric Tons",
        "Milligrams to Grains", "Grains to Milligrams"
    ],
    "Time": [
        "Seconds to Minutes", "Minutes to Seconds",
        "Hours to Minutes", "Minutes to Hours",
        "Hours to Days", "Days to Hours",
        "Days to Weeks", "Weeks to Days",
        "Days to Months", "Months to Days",
        "Days to Years", "Years to Days"
    ],
    "Temperature": [
        "Celsius to Fahrenheit", "Fahrenheit to Celsius",
        "Celsius to Kelvin", "Kelvin to Celsius",
        "Fahrenheit to Kelvin", "Kelvin to Fahrenheit"
    ],
    "Area": [
        "Square Meters to Square Feet", "Square Feet to Square Meters",
        "Square Kilometers to Square Miles", "Square Miles to Square Kilometers",
        "Hectares to Acres", "Acres to Hectares"
    ],
    "Volume": [
        "Liters to Gallons", "Gallons to Liters",
        "Milliliters to Fluid Ounces", "Fluid Ounces to Milliliters",
        "Cubic Meters to Cubic Feet", "Cubic Feet to Cubic Meters"
    ],
    "Speed": [
        "Kilometers per Hour to Miles per Hour", "Miles per Hour to Kilometers per Hour",
        "Meters per Second to Miles per Hour", "Miles per Hour to Meters per Second",
        "Knots to Miles per Hour", "Miles per Hour to Knots"
    ],
    "Data": [
        "Bytes to Kilobytes", "Kilobytes to Bytes",
        "Megabytes to Gigabytes", "Gigabytes to Megabytes",
        "Gigabytes to Terabytes", "Terabytes to Gigabytes"
    ],
    "Pressure": [
        "Pascal to Atmosphere", "Atmosphere to Pascal",
        "Bar to PSI", "PSI to Bar"
    ],
    "Energy": [
        "Joules to Calories", "Calories to Joules",
        "Kilowatt-hours to Megajoules", "Megajoules to Kilowatt-hours"
    ]
}

# Conversion formulas
def convert_unit(category, value, unit):
    # Length conversions
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371, "mi"
        elif unit == "Miles to Kilometers":
            return value * 1.60934, "km"
        elif unit == "Meters to Feet":
            return value * 3.28084, "ft"
        elif unit == "Feet to Meters":
            return value * 0.3048, "m"
        elif unit == "Centimeters to Inches":
            return value * 0.393701, "in"
        elif unit == "Inches to Centimeters":
            return value * 2.54, "cm"
        elif unit == "Millimeters to Inches":
            return value * 0.0393701, "in"
        elif unit == "Inches to Millimeters":
            return value * 25.4, "mm"
        elif unit == "Yards to Meters":
            return value * 0.9144, "m"
        elif unit == "Meters to Yards":
            return value * 1.09361, "yd"
        elif unit == "Nautical Miles to Miles":
            return value * 1.15078, "mi"
        elif unit == "Miles to Nautical Miles":
            return value * 0.868976, "nmi"
            
    # Weight/Mass conversions
    elif category == "Weight/Mass":
        if unit == "Kilograms to Pounds":
            return value * 2.20462, "lb"
        elif unit == "Pounds to Kilograms":
            return value * 0.453592, "kg"
        elif unit == "Grams to Ounces":
            return value * 0.035274, "oz"
        elif unit == "Ounces to Grams":
            return value * 28.3495, "g"
        elif unit == "Metric Tons to Pounds":
            return value * 2204.62, "lb"
        elif unit == "Pounds to Metric Tons":
            return value * 0.000453592, "t"
        elif unit == "Milligrams to Grains":
            return value * 0.0154324, "gr"
        elif unit == "Grains to Milligrams":
            return value * 64.7989, "mg"
            
    # Time conversions
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60, "min"
        elif unit == "Minutes to Seconds":
            return value * 60, "sec"
        elif unit == "Hours to Minutes":
            return value * 60, "min"
        elif unit == "Minutes to Hours":
            return value / 60, "hr"
        elif unit == "Hours to Days":
            return value / 24, "days"
        elif unit == "Days to Hours":
            return value * 24, "hr"
        elif unit == "Days to Weeks":
            return value / 7, "weeks"
        elif unit == "Weeks to Days":
            return value * 7, "days"
        elif unit == "Days to Months":
            return value / 30.436875, "months"
        elif unit == "Months to Days":
            return value * 30.436875, "days"
        elif unit == "Days to Years":
            return value / 365.25, "years"
        elif unit == "Years to Days":
            return value * 365.25, "days"
            
    # Temperature conversions
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32, "°F"
        elif unit == "Fahrenheit to Celsius":
            return (value - 32) * 5/9, "°C"
        elif unit == "Celsius to Kelvin":
            return value + 273.15, "K"
        elif unit == "Kelvin to Celsius":
            return value - 273.15, "°C"
        elif unit == "Fahrenheit to Kelvin":
            return (value - 32) * 5/9 + 273.15, "K"
        elif unit == "Kelvin to Fahrenheit":
            return (value - 273.15) * 9/5 + 32, "°F"
            
    # Area conversions
    elif category == "Area":
        if unit == "Square Meters to Square Feet":
            return value * 10.7639, "ft²"
        elif unit == "Square Feet to Square Meters":
            return value * 0.092903, "m²"
        elif unit == "Square Kilometers to Square Miles":
            return value * 0.386102, "mi²"
        elif unit == "Square Miles to Square Kilometers":
            return value * 2.58999, "km²"
        elif unit == "Hectares to Acres":
            return value * 2.47105, "acres"
        elif unit == "Acres to Hectares":
            return value * 0.404686, "ha"
            
    # Volume conversions
    elif category == "Volume":
        if unit == "Liters to Gallons":
            return value * 0.264172, "gal"
        elif unit == "Gallons to Liters":
            return value * 3.78541, "L"
        elif unit == "Milliliters to Fluid Ounces":
            return value * 0.033814, "fl oz"
        elif unit == "Fluid Ounces to Milliliters":
            return value * 29.5735, "mL"
        elif unit == "Cubic Meters to Cubic Feet":
            return value * 35.3147, "ft³"
        elif unit == "Cubic Feet to Cubic Meters":
            return value * 0.0283168, "m³"
            
    # Speed conversions
    elif category == "Speed":
        if unit == "Kilometers per Hour to Miles per Hour":
            return value * 0.621371, "mph"
        elif unit == "Miles per Hour to Kilometers per Hour":
            return value * 1.60934, "km/h"
        elif unit == "Meters per Second to Miles per Hour":
            return value * 2.23694, "mph"
        elif unit == "Miles per Hour to Meters per Second":
            return value * 0.44704, "m/s"
        elif unit == "Knots to Miles per Hour":
            return value * 1.15078, "mph"
        elif unit == "Miles per Hour to Knots":
            return value * 0.868976, "kn"
            
    # Data conversions
    elif category == "Data":
        if unit == "Bytes to Kilobytes":
            return value / 1024, "KB"
        elif unit == "Kilobytes to Bytes":
            return value * 1024, "B"
        elif unit == "Megabytes to Gigabytes":
            return value / 1024, "GB"
        elif unit == "Gigabytes to Megabytes":
            return value * 1024, "MB"
        elif unit == "Gigabytes to Terabytes":
            return value / 1024, "TB"
        elif unit == "Terabytes to Gigabytes":
            return value * 1024, "GB"
            
    # Pressure conversions
    elif category == "Pressure":
        if unit == "Pascal to Atmosphere":
            return value / 101325, "atm"
        elif unit == "Atmosphere to Pascal":
            return value * 101325, "Pa"
        elif unit == "Bar to PSI":
            return value * 14.5038, "psi"
        elif unit == "PSI to Bar":
            return value * 0.0689476, "bar"
            
    # Energy conversions
    elif category == "Energy":
        if unit == "Joules to Calories":
            return value * 0.239006, "cal"
        elif unit == "Calories to Joules":
            return value * 4.184, "J"
        elif unit == "Kilowatt-hours to Megajoules":
            return value * 3.6, "MJ"
        elif unit == "Megajoules to Kilowatt-hours":
            return value / 3.6, "kWh"
            
    return None, ""

def get_conversion_history_chart(history):
    if not history:
        return None
    
    try:
        fig, ax = plt.subplots(figsize=(8, 3))
        
        # Extract the most recent 5 conversions
        recent = history[-5:] if len(history) > 5 else history
        
        x = range(len(recent))
        values = [item['result'] for item in recent]
        labels = [f"{item['from_value']} {item['unit'].split(' to ')[0]} to {item['unit'].split(' to ')[1]}" for item in recent]
        
        ax.bar(x, values, color='#3498db')
        ax.set_xticks(x)
        ax.set_xticklabels([f"Conv {i+1}" for i in range(len(recent))], rotation=45)
        ax.set_title('Recent Conversion Results')
        ax.set_ylabel('Converted Value')
        plt.tight_layout()
        
        return fig
    except Exception as e:
        st.error(f"Unable to generate chart. Using simplified display instead.")
        return None

# Sidebar for category selection with icons
with st.sidebar:
    st.markdown("## Categories")
    
    category_list = list(categories.keys())
    category_icons = list(categories.values())
    
    # Create buttons for each category
    selected_category = None
    for i, (cat, icon) in enumerate(categories.items()):
        if st.sidebar.button(f"{icon} {cat}", key=f"cat_{i}"):
            selected_category = cat
    
    if selected_category is None:
        selected_category = "Length"  # Default category
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About UniConvert Pro")
    st.sidebar.markdown("""
    UniConvert Pro is a powerful unit conversion tool designed to make conversions quick and easy.
    
    Features:
    - 10 conversion categories
    - Modern, user-friendly interface
    - Conversion history tracking
    - Quick and accurate results
    """)

# Initialize session state for history
if 'conversion_history' not in st.session_state:
    st.session_state.conversion_history = []

# Main content area
with col1:
    st.markdown(f"<div class='info-card'><div class='category-icon'>{categories[selected_category]}</div><h2>{selected_category}</h2></div>", unsafe_allow_html=True)
    
    # Unit selection
    unit = st.selectbox("Select Conversion", conversion_options[selected_category])
    
    # Input value
    value = st.number_input("Enter the value to convert", value=1.0, step=0.1)
    
    # Convert button
    if st.button("Convert"):
        result, unit_symbol = convert_unit(selected_category, value, unit)
        
        if result is not None:
            # Add to history
            st.session_state.conversion_history.append({
                'category': selected_category,
                'unit': unit,
                'from_value': value,
                'result': result,
                'unit_symbol': unit_symbol
            })
            
            # Display result
            st.markdown(f"""
            <div class='result-card'>
                <h3>Result</h3>
                <h2>{value} {unit.split(' to ')[0]} = {result:.4f} {unit_symbol}</h2>
                <p>{unit}</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Conversion failed. Please check your inputs.")

# Results and history column
with col2:
    st.markdown("<h3>Conversion History</h3>", unsafe_allow_html=True)
    
    if not st.session_state.conversion_history:
        st.info("Your conversion history will appear here.")
    else:
        # Create a chart for the history
        try:
            chart = get_conversion_history_chart(st.session_state.conversion_history)
            if chart:
                st.pyplot(chart)
        except Exception:
            st.warning("Unable to display chart visualization. Showing data in table format only.")
        
        # Display history as a table
        history_data = [{
            'Category': item['category'],
            'From': f"{item['from_value']} {item['unit'].split(' to ')[0]}",
            'To': f"{item['result']:.4f} {item['unit_symbol']}",
            'Conversion': item['unit']
        } for item in st.session_state.conversion_history[-5:]]
        
        history_df = pd.DataFrame(history_data)
        st.dataframe(history_df, hide_index=True, use_container_width=True)
        
        if st.button("Clear History"):
            st.session_state.conversion_history = []
            st.experimental_rerun()
    
    # Quick reference card
    st.markdown("<h3>Quick Reference</h3>", unsafe_allow_html=True)
    
    # Get formulas for the selected category
    if selected_category == "Length":
        reference_text = """
        - 1 kilometer = 0.621371 miles
        - 1 meter = 3.28084 feet
        - 1 inch = 2.54 centimeters
        - 1 yard = 0.9144 meters
        """
    elif selected_category == "Weight/Mass":
        reference_text = """
        - 1 kilogram = 2.20462 pounds
        - 1 gram = 0.035274 ounces
        - 1 metric ton = 2204.62 pounds
        - 1 pound = 453.592 grams
        """
    elif selected_category == "Temperature":
        reference_text = """
        - °F = (°C × 9/5) + 32
        - °C = (°F - 32) × 5/9
        - K = °C + 273.15
        """
    else:
        reference_text = f"Quick reference formulas for {selected_category} category."
    
    st.markdown(f"<div class='info-card'>{reference_text}</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2024 UnitConverter Pro | Made by NISHAT</p>", unsafe_allow_html=True)