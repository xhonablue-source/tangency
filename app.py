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

# Interactive Quiz
st.markdown("""
### 🎮 Tangency Mastery Quiz
Test your understanding with this comprehensive quiz!
""")

# Question 1
st.markdown("**Question 1:** What is the slope of the tangent line to f(x) = x³ at x = 2?")
q1_answer = st.radio(
    "Select your answer:",
    ["6", "8", "12", "16"],
    key="tq1"
)

# Question 2
st.markdown("**Question 2:** If a tangent line has slope 4, what is the slope of the normal line?")
q2_answer = st.radio(
    "Select your answer:",
    ["-4", "-1/4", "1/4", "4"],
    key="tq2"
)

# Question 3
st.markdown("**Question 3:** For the circle x² + y² = 25, what is the slope of the tangent at point (3, 4)?")
q3_answer = st.radio(
    "Select your answer:",
    ["3/4", "-3/4", "4/3", "-4/3"],
    key="tq3"
)

# Question 4
st.markdown("**Question 4:** The derivative f'(x) represents which geometric concept?")
q4_answer = st.radio(
    "Select your answer:",
    ["Area under curve", "Slope of tangent line", "x-intercept", "Maximum value"],
    key="tq4"
)

# Question 5
st.markdown("**Question 5:** In real life, what does a tangent line to a position vs. time graph represent?")
q5_answer = st.radio(
    "Select your answer:",
    ["Acceleration", "Distance", "Instantaneous velocity", "Average speed"],
    key="tq5"
)

# Submit Quiz
if st.button("📊 Submit Tangency Quiz"):
    score = 0
    total_questions = 5
    
    # Check answers with detailed explanations
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
    
    # Final score
    percentage = (score / total_questions) * 100
    if percentage >= 80:
        st.balloons()
        st.success(f"🏆 Outstanding! You scored {score}/{total_questions} ({percentage:.0f}%) - You've mastered tangency!")
    elif percentage >= 60:
        st.info(f"📈 Good work! You scored {score}/{total_questions} ({percentage:.0f}%) - Review key concepts and try again!")
    else:
        st.warning(f"📚 You scored {score}/{total_questions} ({percentage:.0f}%) - Study the material above and retake the quiz.")

# Reset Quiz
if st.button("🔄 Reset Quiz"):
    for key in ['tq1', 'tq2', 'tq3', 'tq4', 'tq5']:
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
