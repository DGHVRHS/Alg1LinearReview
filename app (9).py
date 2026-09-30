import streamlit as st
import random

# Page Configuration
st.set_page_config(page_title="Math Grand Prix 🏎️", page_icon="🏁", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .track-container {
        background-color: #2b2b2b;
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
    }
    .stButton>button {
        width: 100%;
        font-size: 18px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# QUESTION GENERATOR ENGINE (Based on Worksheet Topics)
# -----------------------------------------------------------------------------

def generate_level_1():
    """Level 1: Unit rates, proportional relationships, and simple slope types."""
    q_type = random.choice(["unit_rate", "slope_type", "simple_slope", "gas_prop"])

    if q_type == "unit_rate":
        rate = random.randint(3, 12)
        mins = random.randint(2, 5)
        total_songs = rate * mins
        q = f"Spotify downloads {total_songs} songs in {mins} minutes. What is the download rate in songs per minute?"
        correct = f"{rate} songs/min"
        wrongs = [f"{rate + 2} songs/min", f"{max(1, rate - 2)} songs/min", f"{total_songs} songs/min"]

    elif q_type == "slope_type":
        line_type = random.choice(["horizontal", "vertical"])
        if line_type == "horizontal":
            y_val = random.randint(-5, 5)
            q = f"What is the slope of the horizontal line $y = {y_val}$?"
            correct = "0"
            wrongs = ["Undefined", f"{y_val}", "1"]
        else:
            x_val = random.randint(-5, 5)
            q = f"What is the slope of the vertical line $x = {x_val}$?"
            correct = "Undefined"
            wrongs = ["0", f"{x_val}", "1"]

    elif q_type == "simple_slope":
        m = random.randint(1, 5)
        x1, y1 = random.randint(1, 4), random.randint(1, 4)
        x2 = x1 + random.randint(1, 3)
        y2 = y1 + m * (x2 - x1)
        q = f"Find the slope between the points $({x1}, {y1})$ and $({x2}, {y2})$."
        correct = str(m)
        wrongs = [str(m + 1), str(max(1, m - 1)), str(m * 2)]

    else: # gas_prop
        price_per_gal = random.choice([2.50, 3.00, 3.50, 4.00])
        gals = random.randint(5, 12)
        total_cost = price_per_gal * gals
        q = f"If {gals} gallons of gas cost ${total_cost:.2f}, how much does 1 gallon cost?"
        correct = f"${price_per_gal:.2f}"
        wrongs = [f"${price_per_gal + 0.50:.2f}", f"${max(1.0, price_per_gal - 0.50):.2f}", f"${total_cost:.2f}"]

    options = list(set([correct] + wrongs))
    random.shuffle(options)
    return {"question": q, "options": options, "answer": correct, "level": "Easy (Level 1)"}


def generate_level_2():
    """Level 2: Slope-Intercept form (y = mx + b), contextual word problems, negative slopes."""
    q_type = random.choice(["slope_intercept_val", "context_y_int", "two_point_slope", "battery_drain"])

    if q_type == "slope_intercept_val":
        m = random.randint(2, 4)
        b = random.randint(3, 8)
        x = random.randint(2, 6)
        ans = m * x + b
        q = f"The height of snow on a driveway is modeled by $y = {b} + {m}x$ (in inches after $x$ hours). How many inches of snow are on the ground after {x} hours?"
        correct = f"{ans} inches"
        wrongs = [f"{ans + 3} inches", f"{max(1, ans - 4)} inches", f"{m * x} inches"]

    elif q_type == "context_y_int":
        fee = random.choice([100, 150, 200, 350])
        rate = random.choice([15, 25, 30])
        q = f"A catering service calculates total cost using $C = {rate}p + {fee}$, where $p$ is the number of guests. What is the fixed initial fee (y-intercept)?"
        correct = f"${fee}"
        wrongs = [f"${rate}", f"${fee + rate}", f"${fee * 2}"]

    elif q_type == "two_point_slope":
        x1, y1 = -4, 15
        x2, y2 = 8, 9
        # slope = (9 - 15) / (8 - -4) = -6 / 12 = -1/2
        q = "Find the slope of the line passing through $(-4, 15)$ and $(8, 9)$."
        correct = "-1/2"
        wrongs = ["-2", "1/2", "2"]

    else: # battery_drain
        start = random.randint(80, 100)
        rate = random.randint(5, 10)
        hrs = random.randint(3, 6)
        ans = start - (rate * hrs)
        q = f"A battery starts at {start}% and drains at a constant rate of {rate}% per hour. What percentage remains after {hrs} hours?"
        correct = f"{ans}%"
        wrongs = [f"{ans + 10}%", f"{max(0, ans - 5)}%", f"{rate * hrs}%"]

    options = list(set([correct] + wrongs))
    random.shuffle(options)
    return {"question": q, "options": options, "answer": correct, "level": "Medium (Level 2)"}


def generate_level_3():
    """Level 3: Standard form (Ax + By = C), missing coefficients, multi-step systems."""
    q_type = random.choice(["standard_intercept", "missing_coeff", "bake_sale", "equal_tanks"])

    if q_type == "standard_intercept":
        A, B, C = 3, 4, 24
        # x-intercept: y=0 => 3x = 24 => x = 8
        q = f"Find the x-intercept of the line given by $3x + 4y = 24$."
        correct = "(8, 0)"
        wrongs = ["(0, 6)", "(6, 0)", "(0, 8)"]

    elif q_type == "missing_coeff":
        # Ax + 10y = 20 has x-intercept of -5 => A(-5) + 0 = 20 => A = -4
        q = "Find the value of $A$ so that the line $Ax + 10y = 20$ has an x-intercept of $-5$."
        correct = "-4"
        wrongs = ["4", "-2", "5"]

    elif q_type == "bake_sale":
        # Cookies need 2 eggs, cakes need 3 eggs. Total 24 eggs.
        q = "Magdalena uses 2 eggs per batch of cookies ($y$) and 3 eggs per cake ($x$). She has 24 eggs total. Which equation models using all 24 eggs?"
        correct = "3x + 2y = 24"
        wrongs = ["2x + 3y = 24", "3x - 2y = 24", "x + y = 24"]

    else: # equal_tanks
        # Tank A: 100 + 15t, Tank B: 250 + 10t => 5t = 150 => t = 30
        q = "Tank A starts with 100 gal and fills at 15 gal/min ($100 + 15t$). Tank B starts with 250 gal and fills at 10 gal/min ($250 + 10t$). After how many minutes will both tanks have equal volume?"
        correct = "30 minutes"
        wrongs = ["15 minutes", "20 minutes", "50 minutes"]

    options = list(set([correct] + wrongs))
    random.shuffle(options)
    return {"question": q, "options": options, "answer": correct, "level": "Hard (Level 3)"}


def get_next_question(score):
    """Adaptive difficulty logic based on current score."""
    if score < 3:
        return generate_level_1()
    elif score < 7:
        return generate_level_2()
    else:
        return generate_level_3()

# -----------------------------------------------------------------------------
# GAME STATE MANAGEMENT
# -----------------------------------------------------------------------------

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
    if selected_option == st.session_state.current_q["answer"]:
        st.session_state.score += 1
        st.session_state.feedback = ("correct", "🎉 Correct! Move 1 lap forward!")
        if st.session_state.score >= 10:
            st.session_state.game_over = True
    else:
        st.session_state.feedback = ("incorrect", f"❌ Oops! The correct answer was: {st.session_state.current_q['answer']}")

    if not st.session_state.game_over:
        st.session_state.current_q = get_next_question(st.session_state.score)

# -----------------------------------------------------------------------------
# USER INTERFACE
# -----------------------------------------------------------------------------

st.title("🏎️ Math Grand Prix: Linear Equations Rally")
st.write("Answer math problems correctly to speed toward the finish line! As you score points, the problems get harder.")

# Finish Line Victory Screen
if st.session_state.game_over:
    st.balloons()
    st.success(f"🏆 **CHAMPION!** You crossed the finish line in {st.session_state.total_questions} total attempts!")
    st.button("Play Again 🔄", on_click=reset_game)
else:
    # Track Visualizer
    progress = st.session_state.score / 10.0
    st.subheader(f"Progress: {st.session_state.score} / 10 Laps")
    st.progress(progress)

    # ASCII Track Visual
    car_pos = st.session_state.score
    track = ["➖"] * 10
    if car_pos < 10:
        track[car_pos] = "🏎️"
    track_str = "🏁 " + "".join(track[::-1]) + " 🚦 START"
    st.markdown(f"<div class='track-container'>{track_str}</div>", unsafe_allow_html=True)

    st.divider()

    # Show Feedback from last question
    if st.session_state.feedback:
        fb_type, fb_msg = st.session_state.feedback
        if fb_type == "correct":
            st.success(fb_msg)
        else:
            st.error(fb_msg)

    # Question Display
    q_data = st.session_state.current_q
    st.caption(f"Current Difficulty: **{q_data['level']}**")
    st.markdown(f"### Question: {q_data['question']}")

    # Answer Choices Buttons
    cols = st.columns(2)
    for idx, option in enumerate(q_data["options"]):
        with cols[idx % 2]:
            st.button(option, key=f"opt_{idx}", on_click=submit_answer, args=(option,))

    st.divider()
    st.button("Reset Game 🔄", on_click=reset_game)
