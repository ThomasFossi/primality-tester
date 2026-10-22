import time
import streamlit as st
from primality import rabin_miller

# Page Configuration
st.set_page_config(
    page_title="Miller-Rabin Primality Tester", page_icon="🔢", layout="centered"
)

# Streamlit interface
st.title("🔢 Miller-Rabin Primality Tester")
st.write(
    "Test whether a large number is prime using an optimized deterministic"
    " Miller-Rabin primality test."
)

# Sidebar for presets
st.sidebar.header("Testing Presets")
preset = st.sidebar.selectbox(
    "Choose a test number:",
    [
        "Custom Input",
        "5547337572376305111955330958342147474062293202868155909393"
        " (StackOverflow Example)",
        "2147483647 (Mersenne Prime)",
        "100000000000000003 (Large Prime)",
        "100000000000000004 (Composite)",
    ],
)

if preset == "Custom Input":
  default_val = "5547337572376305111955330958342147474062293202868155909393"
else:
  default_val = preset.split(" ")[0]

number_str = st.text_input("Enter a positive integer:", value=default_val)

if st.button("Check Primality", type="primary"):
  try:
    num = int(number_str)
    if num < 0:
      st.error("Please enter a positive integer.")
    else:
      start_time = time.time()
      is_prime = rabin_miller(num)
      elapsed = (time.time() - start_time) * 1000

      st.markdown("---")
      col1, col2 = st.columns(2)
      with col1:
        st.metric("Execution Time", f"{elapsed:.2f} ms")
      with col2:
        st.metric("Digit Length", len(number_str))

      if is_prime:
        st.success(f"**{num}** is a **PRIME** number! 🎉")
      else:
        st.error(f"**{num}** is **COMPOSITE** (not prime). ⚠️")

  except ValueError:
    st.error("Invalid input. Please enter a valid integer.")

# Footer and source code attributions
st.markdown("---")
st.markdown(
    "*Source Code adapted from [Stack Overflow Post"
    " 43612128](https://stackoverflow.com/questions/43559224/primality-testing-how-to-make-sure-not-to-test-numbers-which-are-multiples-of-a/43612128#43612128)"
    " — Licensed under CC BY-SA 3.0*"
)