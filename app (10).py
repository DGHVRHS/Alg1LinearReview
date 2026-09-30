
import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Math Grand Prix 🏎️️", page_icon="🏁", layout="centered")

st.markdown("""
    <style>
    .track-container {
        background-color: #2b2b2b;
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 22px;
        font-weight: bold;
        letter-spacing: 2px;
    }
    .stButton>button {
        width: 100%;
        font-size: 18px;
        padding: 10px;
    }
    .explanation-box {
        background-color: #f0f2f6;
        border-left: 5px solid #1f77b4;
        padding: 12px;
        border-radius: 5px;
        margin-bottom: 15px;
        color: #111;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# QUESTION GENERATOR ENGINE
# -----------------------------------------------------------------------------

def generate_level_1():
    """Level 1 (Laps 0-4): Proportional relationships, unit rates, horizontal/vertical lines."""
    q_type = random.choice([
        "spotify_rate", "gas_prop", "kfc_sides", "horiz_vert_slope", 
        "simple_slope", "deli_meat", "binge_watch"
    ])
    
    if q_type == "spotify_rate":
        rate = random.randint(35, 60)
        mins = random.randint(2, 5)
        downloaded = rate * mins
        q = f"Jenin downloaded {downloaded} songs in {mins} minutes. What is the download rate in songs per minute?"
        correct = f"{rate} songs/min"
        wrongs = [f"{rate + 10} songs/min", f"{max(10, rate - 15)} songs/min", f"{downloaded} songs/min"]
        exp = f"**Step-by-Step Solution:**\nDivide total songs by total time: $\\frac{{{downloaded}\\text{{ songs}}}}{{{mins}\\text{{ minutes}}}} = {rate}\\text{{ songs/min}}$."

    elif q_type == "gas_prop":
        price = random.choice([3.20, 3.50, 3.80, 4.10])
        gals = random.randint(4, 12)
        total = round(price * gals, 2)
        q = f"Malik paid ${total:.2f} for {gals} gallons of premium gas. What is the unit cost per gallon?"
        correct = f"${price:.2f}"
        wrongs = [f"${price + 0.40:.2f}", f"${max(1.0, price - 0.50):.2f}", f"${total:.2f}"]
        exp = f"**Step-by-Step Solution:**\nDivide total cost by gallons: $\\frac{{\\${total:.2f}}}{{{gals}}} = \\${price:.2f}\\text{{ per gallon}}$."

    elif q_type == "kfc_sides":
        q = "Meal 1 (Bucket + 1 side) costs $19.88. Meal 2 (Bucket + 3 sides) costs $25.66. What is the cost of 1 side?"
        correct = "$2.89"
        wrongs = ["$3.20", "$5.78", "$2.50"]
        exp = "**Step-by-Step Solution:**\n1. Find the cost difference: $\\$25.66 - \\$19.88 = \\$5.78$ for 2 extra sides.\n2. Divide by 2: $\\frac{\\$5.78}{2} = \\$2.89$ per side."

    elif q_type == "horiz_vert_slope":
        is_horiz = random.choice([True, False])
        if is_horiz:
            y_val = random.randint(-8, 8)
            q = f"What is the slope of the horizontal line given by $y = {y_val}$?"
            correct = "0"
            wrongs = ["Undefined", f"{y_val}", "1"]
            exp = f"**Step-by-Step Solution:**\nHorizontal lines have zero vertical change (rise = 0), so the slope $m = 0$."
        else:
            x_val = random.randint(-8, 8)
            q = f"What is the slope of the vertical line given by $x = {x_val}$?"
            correct = "Undefined"
            wrongs = ["0", f"{x_val}", "1"]
            exp = f"**Step-by-Step Solution:**\nVertical lines have zero horizontal change (run = 0). Division by zero gives an **undefined** slope."

    elif q_type == "simple_slope":
        m = random.randint(2, 6)
        x1, y1 = random.randint(1, 5), random.randint(1, 5)
        x2 = x1 + random.randint(1, 3)
        y2 = y1 + m * (x2 - x1)
        q = f"Find the slope of the line passing through $({x1}, {y1})$ and $({x2}, {y2})$."
        correct = str(m)
        wrongs = [str(m + 1), str(max(1, m - 1)), str(m * 2)]
        exp = f"**Step-by-Step Solution:**\nUse slope formula $m = \\frac{{y_2 - y_1}}{{x_2 - x_1}}$:\n$$m = \\frac{{{y2} - {y1}}}{{{x2} - {x1}}} = \\frac{{{y2 - y1}}}{{{x2 - x1}}} = {m}$$"

    elif q_type == "deli_meat":
        weight = random.choice([9, 12, 15, 18])
        sandwiches = weight // 3
        q = f"A deli uses {weight} ounces of meat to make {sandwiches} sandwiches. How many ounces of meat go on each sandwich?"
        correct = "3 ounces"
        wrongs = ["4 ounces", "2 ounces", "6 ounces"]
        exp = f"**Step-by-Step Solution:**\nDivide total meat by sandwiches: $\\frac{{{weight}}}{{{sandwiches}}} = 3\\text{{ ounces per sandwich}}$."

    else:
        eps = random.randint(3, 7)
        mins = eps * 20
        q = f"Each episode of a show is 20 minutes long. How many minutes does it take to watch {eps} episodes?"
        correct = f"{mins} minutes"
        wrongs = [f"{mins + 20} minutes", f"{mins - 10} minutes", f"{eps * 15} minutes"]
        exp = f"**Step-by-Step Solution:**\nMultiply episodes by length: ${eps} \\times 20 = {mins}\\text{{ minutes}}$."

    options = list(set([correct] + wrongs))
    random.shuffle(options)
    return {"question": q, "options": options, "answer": correct, "level": "Easy (Level 1)", "exp": exp}


def generate_level_2():
    """Level 2 (Laps 5-9): Slope-intercept form y = mx + b, negative slopes, contextual models."""
    q_type = random.choice([
        "snow_model", "catering_y_int", "negative_slope_pts", 
        "generator_fuel", "fast_charge", "lawn_care_table", "puppy_weight"
    ])

    if q_type == "snow_model":
        b = random.randint(3, 6)
        x = random.randint(3, 6)
        ans = b + 2 * x
        q = f"Snow height on a driveway is modeled by $y = {b} + 2x$, where $y$ is inches of snow and $x$ is hours after midnight. How many inches are on the ground at {x} AM?"
        correct = f"{ans} inches"
        wrongs = [f"{ans + 3} inches", f"{max(1, ans - 4)} inches", f"{2 * x} inches"]
        exp = f"**Step-by-Step Solution:**\nSubstitute $x = {x}$ into $y = {b} + 2x$:\n$$y = {b} + 2({x}) = {b} + {2*x} = {ans}\\text{{ inches}}$$"

    elif q_type == "catering_y_int":
        fee = random.choice([150, 250, 350, 400])
        rate = random.choice([20, 25, 28, 30])
        q = f"A event planner calculates total cost using $C = {rate}p + {fee}$, where $p$ is the number of guests. What is the fixed initial fee ($y$-intercept)?"
        correct = f"${fee}"
        wrongs = [f"${rate}", f"${fee + rate}", f"${fee * 2}"]
        exp = f"**Step-by-Step Solution:**\nIn slope-intercept form $y = mx + b$, $b$ represents the $y$-intercept (the initial/fixed cost when $p = 0$), which is **${fee}**."

    elif q_type == "negative_slope_pts":
        q = "Find the slope of the line passing through $(-4, 15)$ and $(8, 9)$."
        correct = "-1/2"
        wrongs = ["-2", "1/2", "2"]
        exp = "**Step-by-Step Solution:**\nUse slope formula $m = \\frac{y_2 - y_1}{x_2 - x_1}$:\n$$m = \\frac{9 - 15}{8 - (-4)} = \\frac{-6}{12} = -\\frac{1}{2}$$"

    elif q_type == "generator_fuel":
        start = 45
        rate = 1.5
        hrs = random.choice([6, 8, 10, 12])
        ans = start - int(rate * hrs)
        q = f"A generator tank starts with 45 gallons of fuel and consumes 1.5 gallons per hour ($F = 45 - 1.5t$). How much fuel remains after {hrs} hours?"
        correct = f"{ans} gallons"
        wrongs = [f"{ans + 5} gallons", f"{max(0, ans - 6)} gallons", f"{int(rate * hrs)} gallons"]
        exp = f"**Step-by-Step Solution:**\nSubstitute $t = {hrs}$ into $F = 45 - 1.5t$:\n$$F = 45 - 1.5({hrs}) = 45 - {1.5*hrs} = {ans}\\text{{ gallons}}$$"

    elif q_type == "fast_charge":
        q = "A tablet battery starts at 20% and charges at a constant rate of 2% per minute ($B = 20 + 2m$). How many minutes will it take to reach 100%?"
        correct = "40 minutes"
        wrongs = ["50 minutes", "30 minutes", "80 minutes"]
        exp = "**Step-by-Step Solution:**\nSet $B = 100$ and solve for $m$:\n$$100 = 20 + 2m \\implies 80 = 2m \\implies m = 40\\text{{ minutes}}$$"

    elif q_type == "lawn_care_table":
        q = "A lawn service charges $90 for 2 hours of work and $160 for 4 hours of work. What is their hourly labor rate?"
        correct = "$35 / hour"
        wrongs = ["$45 / hour", "$30 / hour", "$70 / hour"]
        exp = "**Step-by-Step Solution:**\nFind slope $m = \\frac{C_2 - C_1}{h_2 - h_1} = \\frac{160 - 90}{4 - 2} = \\frac{70}{2} = \\$35\\text{ per hour}$."

    else:
        w0 = 6
        rate = 1.8
        weeks = random.choice([4, 5, 10])
        ans = round(w0 + rate * weeks, 1)
        q = f"A puppy weighs 6 lbs when rescued and gains 1.8 lbs each week ($W = 6 + 1.8w$). How much will it weigh after {weeks} weeks?"
        correct = f"{ans} lbs"
        wrongs = [f"{ans + 2.0} lbs", f"{ans - 1.8} lbs", f"{round(rate * weeks, 1)} lbs"]
        exp = f"**Step-by-Step Solution:**\nSubstitute $w = {weeks}$ into $W = 6 + 1.8w$:\n$$W = 6 + 1.8({weeks}) = 6 + {1.8*weeks} = {ans}\\text{{ lbs}}$$"

    options = list(set([correct] + wrongs))
    random.shuffle(options)
    return {"question": q, "options": options, "answer": correct, "level": "Medium (Level 2)", "exp": exp}


def generate_level_3():
    """Level 3 (Laps 10-14): Standard form Ax + By = C, finding parameter A, systems/intersections."""
    q_type = random.choice([
        "standard_x_int", "standard_y_int", "missing_coeff_a", 
        "bake_sale_eq", "pizza_budget", "two_tanks", "horiz_pts_j"
    ])

    if q_type == "standard_x_int":
        q = "Find the $x$-intercept of the line given by $3x + 4y = 24$."
        correct = "(8, 0)"
        wrongs = ["(0, 6)", "(6, 0)", "(0, 8)"]
        exp = "**Step-by-Step Solution:**\nTo find the $x$-intercept, set $y = 0$:\n$$3x + 4(0) = 24 \\implies 3x = 24 \\implies x = 8$$\nCoordinates are **(8, 0)**."

    elif q_type == "standard_y_int":
        q = "Find the $y$-intercept of the line given by $-6x - 2y = 18$."
        correct = "(0, -9)"
        wrongs = ["(-3, 0)", "(0, 9)", "(-9, 0)"]
        exp = "**Step-by-Step Solution:**\nTo find the $y$-intercept, set $x = 0$:\n$$-6(0) - 2y = 18 \\implies -2y = 18 \\implies y = -9$$\nCoordinates are **(0, -9)**."

    elif q_type == "missing_coeff_a":
        q = "Find the value of $A$ so that the line $Ax + 10y = 20$ has an $x$-intercept of $-5$."
        correct = "-4"
        wrongs = ["4", "-2", "5"]
        exp = "**Step-by-Step Solution:**\nAn $x$-intercept of $-5$ means the line passes through $(-5, 0)$. Substitute $x = -5$ and $y = 0$:\n$$A(-5) + 10(0) = 20 \\implies -5A = 20 \\implies A = -4$$"

    elif q_type == "bake_sale_eq":
        q = "Magdalena uses 2 eggs per batch of cookies ($y$) and 3 eggs per cake ($x$). She uses all 24 eggs. Which linear equation models this?"
        correct = "3x + 2y = 24"
        wrongs = ["2x + 3y = 24", "3x - 2y = 24", "x + y = 24"]
        exp = "**Step-by-Step Solution:**\nTotal eggs = $(\\text{eggs per cake} \\cdot x) + (\\text{eggs per cookie batch} \\cdot y) = 24$.\nSince each cake takes 3 eggs and each cookie batch takes 2 eggs: **$3x + 2y = 24$**."

    elif q_type == "pizza_budget":
        q = "Little Caesars sells pizzas ($x$) for $5 and 2-Liters ($y$) for $1.50. You have $60 total. Which equation models spending your whole budget?"
        correct = "5x + 1.5y = 60"
        wrongs = ["1.5x + 5y = 60", "5x - 1.5y = 60", "6.5(x + y) = 60"]
        exp = "**Step-by-Step Solution:**\nMultiply unit prices by quantities to get total cost:\n$$\\text{Price}(x) + \\text{Price}(y) = 60 \\implies 5x + 1.5y = 60$$"

    elif q_type == "two_tanks":
        q = "Tank A starts with 100 gal and fills at 15 gal/min ($100 + 15t$). Tank B starts with 250 gal and fills at 10 gal/min ($250 + 10t$). After how many minutes will both tanks contain equal volume?"
        correct = "30 minutes"
        wrongs = ["15 minutes", "20 minutes", "50 minutes"]
        exp = "**Step-by-Step Solution:**\nSet the two equations equal to each other:\n$$100 + 15t = 250 + 10t \\implies 5t = 150 \\implies t = 30\\text{{ minutes}}$$"

    else:
        j_val = random.choice([5, 7, 9, -4])
        q = f"A horizontal line passes through points $(-3, j)$ and $(6, {j_val})$. What is the value of $j$?"
        correct = str(j_val)
        wrongs = [str(j_val + 2), str(-j_val), "0"]
        exp = f"**Step-by-Step Solution:**\nHorizontal lines have a constant $y$-value for all points ($y = c$). Since it passes through $(6, {j_val})$, $y$ must be {j_val} everywhere, so $j = {j_val}$."

    options = list(set([correct] + wrongs))
    random.shuffle(options)
    return {"question": q, "options": options, "answer": correct, "level": "Hard (Level 3)", "exp": exp}


def get_next_question(score):
    if score < 5:
        return generate_level_1()
    elif score < 10:
        return generate_level_2()
    else:
        return generate_level_3()

# -----------------------------------------------------------------------------
# GAME STATE MANAGEMENT
# -----------------------------------------------------------------------------

TARGET_LAPS = 15

if "score" not in st.session_state:
    st.session_state.score = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0
if "current_q" not in st.session_state:
    st.session_state.current_q = get_next_question(0)
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "feedback" not in st.session_state:
    st.session_state.feedback = None

def reset_game():
    st.session_state.score = 0
    st.session_state.total_questions = 0
    st.session_state.game_over = False
    st.session_state.feedback = None
    st.session_state.current_q = get_next_question(0)

def submit_answer(selected_option):
    st.session_state.total_questions += 1
    curr_q = st.session_state.current_q
    
    if selected_option == curr_q["answer"]:
        st.session_state.score += 1
        st.session_state.feedback = {
            "status": "correct",
            "msg": "🎉 **Correct! You advance 1 lap!**",
            "explanation": curr_q["exp"]
        }
        if st.session_state.score >= TARGET_LAPS:
            st.session_state.game_over = True
    else:
        st.session_state.feedback = {
            "status": "incorrect",
            "msg": f"❌ **Incorrect.** The right answer was **{curr_q['answer']}**.",
            "explanation": curr_q["exp"]
        }
    
    if not st.session_state.game_over:
        st.session_state.current_q = get_next_question(st.session_state.score)

# -----------------------------------------------------------------------------
# USER INTERFACE
# -----------------------------------------------------------------------------

st.title("🏎️ Math Grand Prix: Linear Equations Rally")
st.write("Answer linear equation problems correctly to push your race car 15 laps to victory!")

if st.session_state.game_over:
    st.balloons()
    st.success(f"🏆 **CHAMPION!** You crossed the finish line in {st.session_state.total_questions} total attempts!")
    
    if st.session_state.feedback:
        st.markdown("### Final Question Breakdown")
        # Displaying the explanation with LaTeX rendering enabled
    
   with st.container(border=True):
    st.markdown(fb["explanation"])
        
        
    st.button("Play Again 🔄", on_click=reset_game)

else:
    progress = st.session_state.score / float(TARGET_LAPS)
    st.subheader(f"Progress: {st.session_state.score} / {TARGET_LAPS} Laps")
    st.progress(progress)
    
    car_pos = st.session_state.score
    track = ["➖"] * TARGET_LAPS
    if car_pos < TARGET_LAPS:
        track[car_pos] = "🏎️"
    track_str = "🏁 " + "".join(track[::-1]) + " 🚦 START"
    st.markdown(f"<div class='track-container'>{track_str}</div>", unsafe_allow_html=True)
    
    st.divider()

    if st.session_state.feedback:
        fb = st.session_state.feedback
        if fb["status"] == "correct":
            st.success(fb["msg"])
        else:
            st.error(fb["msg"])
        
        st.markdown(f"<div class='explanation-box'>{fb['explanation']}</div>", unsafe_allow_html=True)
        st.divider()

    q_data = st.session_state.current_q
    st.caption(f"Current Difficulty: **{q_data['level']}**")
    st.markdown(f"### Question: {q_data['question']}")

    cols = st.columns(2)
    for idx, option in enumerate(q_data["options"]):
        with cols[idx % 2]:
            st.button(option, key=f"opt_{idx}", on_click=submit_answer, args=(option,))

    st.divider()
    st.button("Reset Game 🔄", on_click=reset_game)
