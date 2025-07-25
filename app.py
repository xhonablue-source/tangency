# tangency_app.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import io
import math

# Page config
st.set_page_config(
    page_title="Advanced Tangency & Derivatives",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@st.cache_data
def generate_tangency_images():
    """Generate matplotlib plots for different tangency concepts"""
    images = {}
    
    plt.style.use('default')
    
    # Basic Tangent Line
    fig, ax = plt.subplots(figsize=(4, 3), facecolor='white')
    x = np.linspace(-2, 4, 100)
    y = x**2 - 2*x + 1  # (x-1)^2
    ax.plot(x, y, 'blue', linewidth=3, label='f(x) = (x-1)²')
    
    # Tangent at x = 2
    x_tan = 2
    y_tan = (x_tan - 1)**2
    slope = 2*(x_tan - 1)  # derivative
    x_line = np.linspace(0, 4, 100)
    y_line = slope * (x_line - x_tan) + y_tan
    ax.plot(x_line, y_line, 'red', linewidth=2, label=f'Tangent at x={x_tan}')
    ax.plot(x_tan, y_tan, 'ro', markersize=8)
    
    ax.set_xlim(-0.5, 4)
    ax.set_ylim(-0.5, 4)
    ax.grid(True, alpha=0.3)
    ax.legend()
    ax.set_title('Tangent Line to Curve', fontweight='bold')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='white', bbox_inches='tight', dpi=100)
    buf.seek(0)
    images['tangent_line'] = buf
    plt.close()
    
    # Circle Tangency
    fig, ax = plt.subplots(figsize=(4, 3), facecolor='white')
    theta = np.linspace(0, 2*np.pi, 100)
    x_circle = 2 * np.cos(theta)
    y_circle = 2 * np.sin(theta)
    ax.plot(x_circle, y_circle, 'purple', linewidth=3, label='Circle: x² + y² = 4')
    
    # Tangent at point (√2, √2)
    x_point = math.sqrt(2)
    y_point = math.sqrt(2)
    ax.plot(x_point, y_point, 'ro', markersize=8, label=f'Point ({x_point:.2f}, {y_point:.2f})')
    
    # Tangent line (perpendicular to radius)
    x_tan_line = np.linspace(-1, 3, 100)
    y_tan_line = -x_tan_line + 2*math.sqrt(2)  # slope = -x/y at point
    ax.plot(x_tan_line, y_tan_line, 'red', linewidth=2, label='Tangent Line')
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)
    ax.set_title('Tangent to Circle', fontweight='bold')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='white', bbox_inches='tight', dpi=100)
    buf.seek(0)
    images['circle_tangent'] = buf
    plt.close()
    
    # Derivative Visualization
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3), facecolor='white')
    
    # Original function
    x = np.linspace(-3, 3, 100)
    y = x**3 - 3*x
    ax1.plot(x, y, 'green', linewidth=3, label='f(x) = x³ - 3x')
    ax1.set_title('Original Function', fontweight='bold')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # Derivative
    y_prime = 3*x**2 - 3
    ax2.plot(x, y_prime, 'orange', linewidth=3, label="f'(x) = 3x² - 3")
    ax2.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    ax2.set_title('Derivative (Slope Function)', fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='white', bbox_inches='tight', dpi=100)
    buf.seek(0)
    images['derivative'] = buf
    plt.close()
    
    # Normal Line
    fig, ax = plt.subplots(figsize=(4, 3), facecolor='white')
    x = np.linspace(-1, 3, 100)
    y = 0.5 * x**2
    ax.plot(x, y, 'navy', linewidth=3, label='f(x) = ½x²')
    
    # Point and tangent
    x_point = 2
    y_point = 0.5 * x_point**2
    slope_tangent = x_point  # derivative at x=2
    slope_normal = -1/slope_tangent
    
    x_line = np.linspace(-1, 3, 100)
    y_tangent = slope_tangent * (x_line - x_point) + y_point
    y_normal = slope_normal * (x_line - x_point) + y_point
    
    ax.plot(x_line, y_tangent, 'red', linewidth=2, label='Tangent Line')
    ax.plot(x_line, y_normal, 'magenta', linewidth=2, label='Normal Line')
    ax.plot(x_point, y_point, 'ko', markersize=8)
    
    ax.set_xlim(-0.5, 3)
    ax.set_ylim(-1, 3)
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=8)
    ax.set_title('Tangent vs Normal Lines', fontweight='bold')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='white', bbox_inches='tight', dpi=100)
    buf.seek(0)
    images['normal_line'] = buf
    plt.close()
    
    # Ellipse Tangency
    fig, ax = plt.subplots(figsize=(4, 3), facecolor='white')
    
    # Create ellipse: x²/9 + y²/4 = 1 (a=3, b=2)
    theta = np.linspace(0, 2*np.pi, 100)
    a, b = 3, 2
    x_ellipse = a * np.cos(theta)
    y_ellipse = b * np.sin(theta)
    ax.plot(x_ellipse, y_ellipse, 'darkorange', linewidth=3, label='Ellipse: x²/9 + y²/4 = 1')
    
    # Point on ellipse at parameter t = π/4
    t = math.pi/4
    x_point = a * math.cos(t)
    y_point = b * math.sin(t)
    ax.plot(x_point, y_point, 'ro', markersize=8, label=f'Point ({x_point:.2f}, {y_point:.2f})')
    
    # Tangent line slope: dy/dx = -(b²x)/(a²y)
    if y_point != 0:
        slope = -(b**2 * x_point) / (a**2 * y_point)
        x_tan_line = np.linspace(-1, 4, 100)
        y_tan_line = slope * (x_tan_line - x_point) + y_point
        ax.plot(x_tan_line, y_tan_line, 'red', linewidth=2, label='Tangent Line')
    
    # Draw foci
    c = math.sqrt(a**2 - b**2)  # focal distance
    ax.plot(c, 0, 'bs', markersize=6, label='Foci')
    ax.plot(-c, 0, 'bs', markersize=6)
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=7)
    ax.set_title('Tangent to Ellipse', fontweight='bold')
    buf = io.BytesIO()
    plt.savefig(buf, format='png', facecolor='white', bbox_inches='tight', dpi=100)
    buf.seek(0)
    images['ellipse_tangent'] = buf
    plt.close()
    
    return images

# Header
st.markdown("""
    <div style="background: linear-gradient(to right, #667eea, #764ba2); padding: 30px; text-align: center;">
        <h1 style="color: white; margin-bottom: 5px;">
            📐 Advanced Tangency & Derivatives
        </h1>
        <div style="color: #f0f0f0; font-style: italic; font-size: 1.1rem;">
            From Geometric Tangent Lines to Calculus Applications
        </div>
    </div>
""", unsafe_allow_html=True)

# Description
st.markdown("""
<div style="background-color: #2c3e50; color: white; padding: 20px; font-size: 1rem;">
This comprehensive application explores tangency from multiple mathematical perspectives: geometric tangent lines to circles, 
calculus derivatives as slopes of tangent lines, normal lines, and real-world applications in physics and engineering. 
Students will discover how tangency connects algebra, geometry, and calculus through interactive visualizations and activities.
</div>
""", unsafe_allow_html=True)

# Learning Objectives
st.markdown("""
### 🎯 Learning Objectives
- Understand tangent lines as lines that touch curves at exactly one point
- Connect derivatives to slopes of tangent lines
- Distinguish between tangent lines and normal lines
- Apply tangency concepts to real-world problems
- Master the relationship between geometric and algebraic approaches

**Standards Alignment:**
- HSF.IF.B.4 – Interpret key features of graphs and tables
- HSA.CED.A.2 – Create equations in two or more variables to represent relationships
- HSF.IF.C.7 – Graph functions and analyze key features
- Calculus: Understanding derivatives as rates of change and slopes

---

### 📝 Key Concepts & Formulas

**Tangent Line:** A line that touches a curve at exactly one point and has the same slope as the curve at that point.

**Key Formulas:**
- **Point-Slope Form:** `y - y₁ = m(x - x₁)` where m is the slope at point (x₁, y₁)
- **Derivative as Slope:** `m = f'(x₁)` at point x₁
- **Normal Line Slope:** `m_normal = -1/m_tangent` (negative reciprocal)
- **Circle Tangent:** For circle x² + y² = r², tangent at (a,b) has slope `m = -a/b`
- **Ellipse Tangent:** For ellipse x²/A² + y²/B² = 1, tangent at (x₁,y₁) has slope `m = -(B²x₁)/(A²y₁)`
""")

# Visual Gallery
st.markdown("""
### 🖼️ Visual Gallery: Types of Tangency
""")

try:
    tangency_images = generate_tangency_images()
    
    col1, col2 = st.columns(2)
    with col1:
        st.image(tangency_images['tangent_line'], caption="Basic Tangent Line", use_container_width=True)
        st.markdown("**Concept:** Tangent line touches parabola at one point with matching slope")
        
        st.image(tangency_images['derivative'], caption="Function vs Derivative", use_container_width=True)
        st.markdown("**Concept:** Derivative gives slope of tangent at each point")
    
    with col2:
        st.image(tangency_images['circle_tangent'], caption="Circle Tangent", use_container_width=True)
        st.markdown("**Concept:** Tangent to circle is perpendicular to radius at point of contact")
        
        st.image(tangency_images['normal_line'], caption="Tangent vs Normal", use_container_width=True)
        st.markdown("**Concept:** Normal line is perpendicular to tangent line")
        
        st.image(tangency_images['ellipse_tangent'], caption="Ellipse Tangent", use_container_width=True)
        st.markdown("**Concept:** Ellipse tangent reflects between foci with equal angles")
        
except Exception as e:
    st.error(f"Error generating images: {e}")

# Interactive Tangent Calculator
st.markdown("""
### 🧮 Interactive Tangent Line Calculator
Find the equation of the tangent line to any quadratic function at a given point.
""")

col1, col2, col3 = st.columns(3)
with col1:
    a_coeff = st.number_input("Coefficient 'a'", value=1.0, step=0.1, help="For f(x) = ax² + bx + c")
    b_coeff = st.number_input("Coefficient 'b'", value=0.0, step=0.1)
    c_coeff = st.number_input("Coefficient 'c'", value=0.0, step=0.1)

with col2:
    x_point = st.number_input("x-coordinate of point", value=1.0, step=0.1)
    
with col3:
    if st.button("🔍 Calculate Tangent"):
        # Calculate y-coordinate
        y_point = a_coeff * x_point**2 + b_coeff * x_point + c_coeff
        
        # Calculate slope (derivative)
        slope = 2 * a_coeff * x_point + b_coeff
        
        # Display results
        st.success(f"**Point:** ({x_point}, {y_point:.2f})")
        st.success(f"**Slope:** {slope:.2f}")
        st.success(f"**Tangent Line:** y - {y_point:.2f} = {slope:.2f}(x - {x_point})")
        
        # Simplified form
        y_intercept = y_point - slope * x_point
        if y_intercept >= 0:
            st.info(f"**Simplified:** y = {slope:.2f}x + {y_intercept:.2f}")
        else:
            st.info(f"**Simplified:** y = {slope:.2f}x - {abs(y_intercept):.2f}")

# Concept Matching Activity
st.markdown("""
### 🎯 Concept Matching Challenge
Match each tangency concept with its correct description and application.
""")

col1, col2, col3 = st.columns(3)
with col1:
    concept = st.selectbox("🔸 Select Concept", [
        "Tangent Line", 
        "Normal Line", 
        "Derivative", 
        "Circle Tangent",
        "Rate of Change"
    ])

with col2:
    description = st.selectbox("📖 Match Description", [
        "Line perpendicular to tangent",
        "Instantaneous rate of change",
        "Line touching curve at one point",
        "Perpendicular to radius at contact point",
        "How fast something changes"
    ])

with col3:
    application = st.selectbox("🌍 Real-World Application", [
        "Satellite dish design",
        "Roller coaster safety",
        "Speed at specific moment",
        "Perpendicular parking",
        "Velocity calculations"
    ])

if st.button("✅ Check Concept Match"):
    # Define correct matches
    correct_matches = {
        "Tangent Line": ("Line touching curve at one point", "Roller coaster safety"),
        "Normal Line": ("Line perpendicular to tangent", "Perpendicular parking"),
        "Derivative": ("Instantaneous rate of change", "Velocity calculations"),
        "Circle Tangent": ("Perpendicular to radius at contact point", "Satellite dish design"),
        "Rate of Change": ("How fast something changes", "Speed at specific moment")
    }
    
    if concept in correct_matches:
        correct_desc, correct_app = correct_matches[concept]
        if description == correct_desc and application == correct_app:
            st.balloons()
            st.success("🎉 Perfect Match! You understand the concepts!")
        else:
            st.warning(f"Close! For {concept}: Description should be '{correct_desc}' and Application should be '{correct_app}'")

# Advanced Problem Solver
st.markdown("""
### 🔬 Advanced Problem Solver
Solve complex tangency problems step-by-step.
""")

problem_type = st.selectbox("Choose Problem Type", [
    "Find where two curves have parallel tangents",
    "Find tangent line equation",
    "Find normal line equation",
    "Circle tangent from external point"
])

if problem_type == "Find tangent line equation":
    st.markdown("**Problem:** Given f(x) = x³ - 2x² + x + 1, find the tangent line at x = 2")
    
    if st.button("👀 Show Solution Steps"):
        st.markdown("""
        **Step 1:** Find the y-coordinate
        - f(2) = 2³ - 2(2²) + 2 + 1 = 8 - 8 + 2 + 1 = 3
        - Point: (2, 3)
        
        **Step 2:** Find the derivative
        - f'(x) = 3x² - 4x + 1
        
        **Step 3:** Find slope at x = 2
        - f'(2) = 3(4) - 4(2) + 1 = 12 - 8 + 1 = 5
        
        **Step 4:** Use point-slope form
        - y - 3 = 5(x - 2)
        - y = 5x - 7
        
        **Answer:** The tangent line is y = 5x - 7
        """)

elif problem_type == "Find normal line equation":
    st.markdown("**Problem:** Find the normal line to y = x² at the point (3, 9)")
    
    if st.button("👀 Show Solution Steps"):
        st.markdown("""
        **Step 1:** Find the slope of tangent
        - f(x) = x², so f'(x) = 2x
        - At x = 3: f'(3) = 2(3) = 6
        
        **Step 2:** Find slope of normal
        - m_normal = -1/m_tangent = -1/6
        
        **Step 3:** Use point-slope form with (3, 9)
        - y - 9 = -1/6(x - 3)
        - y = -1/6 x + 1/2 + 9
        - y = -1/6 x + 19/2
        
        **Answer:** The normal line is y = -1/6 x + 19/2
        """)

# Ellipse Tangency Deep Dive
st.markdown("""
### 🥚 Ellipse Tangency: Advanced Concepts

Ellipses have fascinating tangency properties that connect geometry, algebra, and physics. Unlike circles, 
ellipses have **two focal points** that create unique reflection properties crucial in astronomy, optics, and engineering.
""")

# Ellipse Tangency Theory
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **🔸 Key Properties of Ellipse Tangents:**
    
    **1. Reflection Property**
    - Any ray from one focus reflects off the ellipse and passes through the other focus
    - The tangent line bisects the angle between the focal radii
    - This property is used in elliptical mirrors and whispering galleries
    
    **2. Mathematical Formula**
    - For ellipse: `x²/a² + y²/b² = 1`
    - Tangent at point (x₁, y₁): `(x₁·x)/a² + (y₁·y)/b² = 1`
    - Slope: `m = -(b²x₁)/(a²y₁)`
    
    **3. Focal Distance**
    - Distance between foci: `2c` where `c² = a² - b²`
    - Sum of distances from any point to both foci = `2a` (constant!)
    """)

with col2:
    st.markdown("""
    **🌍 Real-World Applications:**
    
    **🛰️ Satellite Orbits**
    - Planets orbit in ellipses with the Sun at one focus
    - Tangent to orbit gives instantaneous velocity direction
    
    **🏥 Medical Imaging**
    - Elliptical reflectors in lithotripsy focus sound waves
    - Tangent properties ensure precise targeting
    
    **🏛️ Architecture**
    - Whispering galleries use elliptical domes
    - Sound from one focus reflects to the other focus
    
    **🔭 Telescopes**
    - Elliptical mirrors collect and focus light
    - Tangent calculations optimize light gathering
    """)

# Interactive Ellipse Calculator
st.markdown("""
### 🧮 Interactive Ellipse Tangent Calculator
Calculate tangent lines to any ellipse at specified points.
""")

col1, col2, col3, col4 = st.columns(4)
with col1:
    a_ellipse = st.number_input("Semi-major axis (a)", value=3.0, min_value=0.1, step=0.1)
with col2:
    b_ellipse = st.number_input("Semi-minor axis (b)", value=2.0, min_value=0.1, step=0.1)
with col3:
    x_ellipse_point = st.number_input("x-coordinate", value=1.5, step=0.1)
with col4:
    if st.button("🔍 Calculate Ellipse Tangent"):
        # Check if point is on ellipse and calculate y
        discriminant = b_ellipse**2 * (1 - x_ellipse_point**2/a_ellipse**2)
        if discriminant >= 0:
            y_ellipse_point = math.sqrt(discriminant)
            
            # Calculate slope
            if y_ellipse_point != 0:
                slope_ellipse = -(b_ellipse**2 * x_ellipse_point) / (a_ellipse**2 * y_ellipse_point)
                
                # Display results
                st.success(f"**Point on ellipse:** ({x_ellipse_point:.2f}, {y_ellipse_point:.2f})")
                st.success(f"**Tangent slope:** {slope_ellipse:.3f}")
                
                # Tangent line equation
                y_intercept = y_ellipse_point - slope_ellipse * x_ellipse_point
                st.success(f"**Tangent equation:** y = {slope_ellipse:.3f}x + {y_intercept:.3f}")
                
                # Focal information
                if a_ellipse > b_ellipse:
                    c_focal = math.sqrt(a_ellipse**2 - b_ellipse**2)
                    st.info(f"**Foci located at:** (±{c_focal:.2f}, 0)")
                    
                    # Distance to foci
                    dist1 = math.sqrt((x_ellipse_point - c_focal)**2 + y_ellipse_point**2)
                    dist2 = math.sqrt((x_ellipse_point + c_focal)**2 + y_ellipse_point**2)
                    st.info(f"**Sum of focal distances:** {dist1 + dist2:.2f} (should equal 2a = {2*a_ellipse})")
            else:
                st.warning("Point is on the major axis - tangent is vertical")
        else:
            st.error("Point is outside the ellipse. Choose a smaller x-value.")

# Ellipse vs Circle Comparison
st.markdown("""
### ⚖️ Ellipse vs Circle Tangency Comparison
""")

comparison_data = {
    "Property": [
        "Basic Equation",
        "Tangent Formula",
        "Slope Formula", 
        "Focal Points",
        "Reflection Property",
        "Applications"
    ],
    "Circle": [
        "x² + y² = r²",
        "xx₁ + yy₁ = r²",
        "m = -x₁/y₁",
        "One center point",
        "Angle of incidence = Angle of reflection",
        "Radar dishes, mirrors"
    ],
    "Ellipse": [
        "x²/a² + y²/b² = 1",
        "(x₁x)/a² + (y₁y)/b² = 1",
        "m = -(b²x₁)/(a²y₁)",
        "Two foci (±c, 0)",
        "Ray from one focus → other focus",
        "Planetary orbits, medical devices"
    ]
}

import pandas as pd
df_comparison = pd.DataFrame(comparison_data)
st.table(df_comparison)

# Ellipse Practice Problems
st.markdown("""
### 📝 Ellipse Tangency Practice Problems

**🔸 Basic Level:**
1. Find the tangent to ellipse x²/25 + y²/9 = 1 at point (4, 9/5)
2. What is the slope of the tangent to x²/16 + y²/4 = 1 at x = 2?
3. Where are the foci of the ellipse x²/36 + y²/16 = 1?

**🔸 Intermediate Level:**
4. Find all points on x²/9 + y²/4 = 1 where the tangent has slope -1/2
5. Show that the tangent to an ellipse at any point bisects the angle between focal radii
6. Find the equation of the normal line to x²/25 + y²/16 = 1 at point (3, 16/5)

**🔸 Advanced Level:**
7. Prove that the product of the distances from the foci to any tangent line is constant
8. Find the envelope of all tangent lines to an ellipse (hint: it's another ellipse!)
9. Application: A satellite in elliptical orbit - find velocity direction at aphelion
""")

# Interactive Challenge
st.markdown("""
### 🎯 Ellipse Challenge: Whispering Gallery
""")

st.markdown("""
**Scenario:** You're designing a whispering gallery with an elliptical dome. A person stands at one focus 
and whispers. Where should the listener stand to hear the whisper most clearly?
""")

challenge_answer = st.radio(
    "Where should the listener stand?",
    [
        "At the center of the ellipse",
        "At the other focus",
        "Anywhere on the ellipse",
        "At the vertex of the ellipse"
    ],
    key="ellipse_challenge"
)

if st.button("🔍 Check Challenge Answer"):
    if challenge_answer == "At the other focus":
        st.balloons()
        st.success("""
        🎉 Correct! The listener should stand at the **other focus**!
        
        **Explanation:** Due to the reflection property of ellipses, sound waves from one focus 
        will reflect off the elliptical surface and converge at the other focus. This is why 
        whispering galleries work - the tangent line at any point on the ellipse bisects the 
        angle between the lines connecting that point to the two foci.
        
        **Famous Examples:**
        - St. Paul's Cathedral, London
        - The Capitol Building, Washington D.C.
        - Grand Central Terminal, New York
        """)
    else:
        st.error(f"""
        ❌ Not quite! You selected "{challenge_answer}".
        
        Think about the reflection property: tangent lines to an ellipse have a special 
        relationship with the two focal points. Sound from one focus reflects to where?
        """)

# Add to existing quiz section
st.markdown("""
### 🎮 Extended Quiz: Including Ellipse Tangency
""")

# Additional ellipse question
st.markdown("**Question 6:** For ellipse x²/9 + y²/4 = 1, what is the slope of the tangent at point (3cos(π/6), 2sin(π/6))?")
q6_answer = st.radio(
    "Select your answer:",
    ["-√3/3", "-√3", "-1/√3", "-3/√3"],
    key="tq6"
)

# Update the quiz submission section
if st.button("📊 Submit Extended Tangency Quiz"):
    score = 0
    total_questions = 6  # Updated to include ellipse question
    
    # Previous questions (1-5) remain the same...
    if q1_answer == "12":
        score += 1
        st.success("✅ Question 1: Correct! f'(x) = 3x², so f'(2) = 3(4) = 12")
    else:
        st.error(f"❌ Question 1: You selected {q1_answer}. Correct answer: 12 (derivative of x³ is 3x²)")
    
    if q2_answer == "-1/4":
        score += 1
        st.success("✅ Question 2: Correct! Normal slope = -1/tangent slope = -1/4")
    else:
        st.error(f"❌ Question 2: You selected {q2_answer}. Correct answer: -1/4 (negative reciprocal)")
    
    if q3_answer == "-3/4":
        score += 1
        st.success("✅ Question 3: Correct! For x² + y² = r², slope = -x/y = -3/4")
    else:
        st.error(f"❌ Question 3: You selected {q3_answer}. Correct answer: -3/4 (tangent perpendicular to radius)")
    
    if q4_answer == "Slope of tangent line":
        score += 1
        st.success("✅ Question 4: Correct! The derivative gives the slope of the tangent line")
    else:
        st.error(f"❌ Question 4: You selected {q4_answer}. Correct answer: Slope of tangent line")
    
    if q5_answer == "Instantaneous velocity":
        score += 1
        st.success("✅ Question 5: Correct! Tangent to position graph shows instantaneous velocity")
    else:
        st.error(f"❌ Question 5: You selected {q5_answer}. Correct answer: Instantaneous velocity")
    
    # New ellipse question
    if q6_answer == "-√3/3":
        score += 1
        st.success("✅ Question 6: Correct! At point (3√3/2, 1), slope = -(4·3√3/2)/(9·1) = -2√3/3 = -√3/3")
    else:
        st.error(f"❌ Question 6: You selected {q6_answer}. Correct answer: -√3/3 (use ellipse slope formula)")
    
    # Final score
    percentage = (score / total_questions) * 100
    if percentage >= 83:  # Adjusted for 6 questions
        st.balloons()
        st.success(f"🏆 Outstanding! You scored {score}/{total_questions} ({percentage:.0f}%) - You've mastered tangency!")
    elif percentage >= 67:  # Adjusted threshold
        st.info(f"📈 Good work! You scored {score}/{total_questions} ({percentage:.0f}%) - Review key concepts and try again!")
    else:
        st.warning(f"📚 You scored {score}/{total_questions} ({percentage:.0f}%) - Study the material above and retake the quiz.")

# Reset Quiz (updated)
if st.button("🔄 Reset Extended Quiz"):
    for key in ['tq1', 'tq2', 'tq3', 'tq4', 'tq5', 'tq6']:
        if key in st.session_state:
            del st.session_state[key]
    st.success("Quiz reset! Scroll up to retake the quiz.")

# Real-World Applications
st.markdown("""
### 🌍 Real-World Applications of Tangency

**🚗 Automotive Engineering**
- Car headlight reflectors use parabolic shapes where tangent lines help focus light beams
- Suspension systems use tangent calculations for optimal comfort and safety

**🛰️ Aerospace & Satellites**
- Satellite dish positioning requires precise tangent line calculations
- Rocket trajectory optimization uses tangent concepts for fuel efficiency

**🎢 Architecture & Construction**
- Roller coaster design ensures smooth transitions using tangent lines
- Bridge cable tensions calculated using tangent and normal forces

**📱 Technology**
- Smartphone screen curvature designed using tangent principles
- GPS navigation uses tangent calculations for shortest path algorithms

**⚡ Physics & Engineering**
- Electric field lines are always tangent to equipotential surfaces
- Velocity vectors are tangent to motion paths
""")

# Practice Problems
st.markdown("""
### 📝 Additional Practice Problems

**Problem Set A: Basic Tangent Lines**
1. Find the tangent line to y = 2x² - 3x + 1 at x = 1
2. Where does y = x³ have a horizontal tangent line?
3. Find the normal line to y = √x at x = 4

**Problem Set B: Circle Tangency**
1. Find the tangent to x² + y² = 13 at point (2, 3)
2. Find all tangent lines to x² + y² = 5 with slope = 2
3. Find the tangent from external point (5, 0) to circle x² + y² = 9

**Problem Set C: Applications**
1. A ball is thrown with height h(t) = -16t² + 32t + 6. Find its velocity at t = 1
2. Find the angle between two curves y = x² and y = x³ at their intersection
3. Design a parabolic mirror: find the tangent at any point on y = x²/4
""")

# Resources and References
st.markdown("""
### 📚 Study Resources & References

**📖 Textbook Resources**
- [Khan Academy - Derivatives as Slopes](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-intro)
- [Paul's Online Math Notes - Tangent Lines](https://tutorial.math.lamar.edu/Classes/CalcI/TangentLines.aspx)
- [MIT OpenCourseWare - Single Variable Calculus](https://ocw.mit.edu/courses/mathematics/18-01-single-variable-calculus-fall-2006/)

**🎥 Video Tutorials**
- [YouTube: Tangent Lines and Derivatives](https://www.youtube.com/watch?v=pQa_tWZmlGs)
- [Professor Leonard - Tangent and Normal Lines](https://www.youtube.com/watch?v=Qp8QUVOduro)
- [Khan Academy - Introduction to Derivatives](https://www.youtube.com/watch?v=5yfh5cf4-0w)

**🔧 Interactive Tools**
- [Desmos Graphing Calculator](https://www.desmos.com/calculator)
- [GeoGebra Calculus Tools](https://www.geogebra.org/graphing)
- [Wolfram Alpha Derivative Calculator](https://www.wolframalpha.com/)

**📱 Mobile Apps**
- Photomath (for step-by-step solutions)
- Calculus Tools (derivative practice)
- GeoGebra Mobile (graphing and visualization)

---

<center>Built by Xavier Honablue M.Ed for CognitiveCloud.ai</center>
<center>Advanced Mathematics Education • Calculus & Geometry Integration</center>
""")
