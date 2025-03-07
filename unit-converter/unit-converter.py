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
    page_icon="☠️",
    layout="wide"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, black 100%);
        font-family: 'Poppins', sans-serif;
        color: #000000;
    }
    
    .stTitle {
        color: #1a2f4e;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0;
        font-size: 2.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        background: linear-gradient(90deg, #2c3e50, #4a6491);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 10px 0;
    }
    
    .stSubheader {
        color: #34495e;
        font-family: 'Poppins', sans-serif;
        text-align: center;
        margin-top: 0;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    
    .css-1kyxreq {
        justify-content: center;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #0072ff 0%, #00c6ff 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.2rem;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 10px rgba(0, 114, 255, 0.2);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(0, 114, 255, 0.3);
    }
    
    .result-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.08);
        margin-top: 25px;
        text-align: center;
        border-left: 5px solid #0072ff;
        transition: all 0.3s ease;
    }
    
    .result-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.12);
    }
    
    .result-card h3 {
        font-weight: 600;
        color: #1a2f4e;
        margin-bottom: 15px;
    }
    
    .result-card h2 {
        font-size: 1.8rem;
        background: linear-gradient(90deg, #0072ff, #00c6ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0;
    }
    
    .info-card {
        background: linear-gradient(135deg, gray 20%, blue 100%);
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.06);
        margin-bottom: 25px;
        border-left: 5px solid #00c6ff;
        transition: all 0.3s ease;
    }
    
    .info-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
    }
    
    .category-icon {
        font-size: 2.5rem;
        margin-bottom: 10px;
    }
    
    .stSelectbox label {
        color: #1a2f4e;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 5px;
    }
    
    .stNumberInput label {
        color: #1a2f4e;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 5px;
    }
    
    .stSelectbox > div > div {
        border-radius: 8px;
        border: 1px solid #e0e5ec;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }
    
    .stNumberInput > div > div {
        border-radius: 8px;
        border: 1px solid #e0e5ec;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
    }
    
    /* Table styling */
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        border: none !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    }
    
    .dataframe thead tr th {
        background-color: #0072ff !important;
        color: white !important;
        font-weight: 600;
        padding: 12px 15px !important;
        border: none !important;
    }
    
    .dataframe tbody tr {
        transition: all 0.2s ease;
    }
    
    .dataframe tbody tr:hover {
        background-color: rgba(0, 114, 255, 0.05) !important;
    }
    
    .dataframe tbody tr td {
        padding: 12px 15px !important;
        border-bottom: 1px solid #e0e5ec !important;
        border-right: none !important;
        border-left: none !important;
    }
    
    /* Sidebar styling */
    .css-1d391kg, .css-163ttbj, .css-1qrvfrg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Radio buttons */
    .stRadio > div {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 10px;
    }
    
    .stRadio label:hover {
        border-left: 3px solid #00c6ff;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    }
    
    /* Footer styling */
    footer {
        margin-top: 50px;
        padding-top: 20px;
        text-align: center;
        border-top: 1px solid #e0e5ec;
        font-size: 0.9rem;
        color: #6c757d;
    }
    
    /* Animation for the header */
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.03); }
        100% { transform: scale(1); }
    }
    
    .stTitle {
        animation: pulse 2s infinite;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("UnitConvert Pro")
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
    try:
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
        
        # If we reach here, no conversion was found
        st.error(f"No conversion found for category: {category}, unit: {unit}")
        return None, ""
        
    except Exception as e:
        st.error(f"Conversion error: {str(e)}")
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

# Initialize session state for history and selected category
if 'conversion_history' not in st.session_state:
    st.session_state.conversion_history = []

if 'selected_category' not in st.session_state:
    st.session_state.selected_category = "Length"

# Sidebar for category selection with icons
with st.sidebar:
    st.markdown("## Categories")
    
    # Use radio buttons for more stable category selection
    category_options = [f"{categories[cat]} {cat}" for cat in categories.keys()]
    selected_option = st.sidebar.radio(
        "Select a category",
        category_options,
        index=list(categories.keys()).index(st.session_state.selected_category) if st.session_state.selected_category in categories else 0,
        label_visibility="collapsed"
    )
    
    # Extract the category name from the selected option
    selected_category = selected_option.split(" ", 1)[1]
    st.session_state.selected_category = selected_category
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### About UnitConvert Pro 🫡")
    st.sidebar.markdown("""
    UnitConvert Pro is a powerful unit conversion tool designed to make conversions quick and easy.
    
    Features: 💪🏻
    - 10 conversion categories
    - Modern, user-friendly interface
    - Conversion history tracking
    - Quick and accurate results
    """)

# Main content area
with col1:
    st.markdown(f"<div class='info-card'><div class='category-icon'>{categories[selected_category]}</div><h2>{selected_category}</h2></div>", unsafe_allow_html=True)
    
    # Unit selection
    unit = st.selectbox("Select Conversion", conversion_options[selected_category])
    
    # Input value
    value = st.number_input("Enter the value to convert", value=1.0, step=0.1)
    
    # Convert button
    if st.button("Convert"):
        with st.spinner("Converting..."):
            # Display debug info in development
            st.session_state.debug_info = {
                'category': selected_category,
                'unit': unit,
                'value': value
            }
            
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
                    <div style='background: rgba(0,114,255,0.1); padding: 8px; border-radius: 50px; width: 50px; height: 50px; margin: 0 auto; display: flex; align-items: center; justify-content: center;'>
                        <span style='font-size: 1.5rem; color: #000000;'>✓</span>
                    </div>
                    <h3 style='color: #000000;'>Conversion Result</h3>
                    <h2 style='color: #000000;'>{value} {unit.split(' to ')[0]} = {result:.4f} {unit_symbol}</h2>
                    <p style='color: #000000; font-size: 0.9rem;'>{unit}</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.error(f"Conversion failed. Please check your inputs. Category: {selected_category}, Unit: {unit}")

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
st.markdown("<div style='height: 3px; background: linear-gradient(90deg, rgba(0,114,255,0), rgba(0,114,255,0.8), rgba(0,114,255,0)); margin: 30px 0 10px 0;'></div>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; padding: 20px 0;'>
    <div style='display: inline-block; background: linear-gradient(135deg, #0072ff, #00c6ff); border-radius: 50px; width: 40px; height: 40px; line-height: 40px; margin-bottom: 10px;'>
        <span style='color: white; font-size: 1.2rem;'>🔄</span>
    </div>
    <p style='color: white; font-size: 0.9rem;'>© 2025 UnitConvert Pro | Made by NISHAT</p>
</div>
""", unsafe_allow_html=True)

# Debug section (hidden in production)
with st.expander("Debug Information", expanded=False):
    st.write("### Session State")
    st.write(f"Selected Category: {st.session_state.selected_category}")
    
    if 'debug_info' in st.session_state:
        st.write("### Last Conversion Attempt")
        st.write(st.session_state.debug_info)
    
    st.write("### Conversion History")
    st.write(f"Number of conversions: {len(st.session_state.conversion_history)}")
    
    if st.button("Clear Session State"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
