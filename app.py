import math
import time
import streamlit as st
from primality import rabin_miller

#Page configuration
st.set_page_config(
    page_title="Miller-Rabin Primality Dashboard",
    page_icon="🛡️",
    layout="centered",
)

# Sidebar configuration
st.sidebar.title("Miller-Rabin Suite")
st.sidebar.caption("Advanced Primality Testing")

nav = st.sidebar.radio(
    "Navigation Menu",
    [
        "Interactive Tester",
        "Batch Prime Finder",
        "Algorithm & Source",
        "GitHub Guide",
    ],
)

# Tab 1: INTERACTIVE PRIMALITY TESTER
if nav == "Interactive Tester":
  st.title("🔢 Interactive Primality Tester")
  st.write(
      "Test whether large numbers are prime using an optimized deterministic"
      " Miller-Rabin primality test."
  )

  preset = st.selectbox(
      "Choose a test number preset:",
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

# Tab 2: BATCH PRIME FINDER
elif nav == "Batch Prime Finder":
  st.title("📋 Batch Prime Finder")
  st.write("Scan a numerical range for prime numbers.")

  col1, col2 = st.columns(2)
  with col1:
    start_range = st.number_input("Start Number", value=1, min_value=1)
  with col2:
    end_range = st.number_input(
        "End Number (Max 10,000)", value=500, min_value=1, max_value=10000
    )

  if st.button("Find Primes in Range", type="primary"):
    start_time = time.time()
    primes = [
        n for n in range(int(start_range), int(end_range) + 1) if rabin_miller(n)
    ]
    elapsed = (time.time() - start_time) * 1000

    st.success(
        f"Found **{len(primes)} primes** between {start_range} and {end_range}"
        f" (in {elapsed:.2f}ms)"
    )
    st.write(primes)

# Tab 3: ALGORITHM & SOURCE CODE
elif nav == "Algorithm & Source":
  st.title("📜 Algorithm & Source Code")
  st.write(
      "This implementation is based on the deterministic Miller-Rabin"
      " primality test."
  )
  st.markdown(
      "**Source Attribution:** [Stack Overflow Answer by"
      " Pozeidon](https://stackoverflow.com/questions/43559224/primality-testing-how-to-make-sure-not-to-test-numbers-which-are-multiples-of-a/43612128#43612128)"
      " — Licensed under CC BY-SA 3.0"
  )

  with open("primality.py", "r") as f:
    code_text = f.read()
  st.code(code_text, language="python")

# Tab 4: PROJECT ARCHITECTURE & LEARNING GUIDE (GitHub Guide)
elif nav == "GitHub Guide":
  st.title("🚀 Project Architecture & Learning Guide")
  st.markdown("""
    ### How this Streamlit project is structured:
    * **`primality.py`**: Contains the core deterministic math logic separate from the interface.
    * **`app.py`**: Renders the Streamlit multi-view dashboard.
    * **`requirements.txt`**: Tells Streamlit Cloud which dependencies to install.
    """)

# Footer Attribution
st.markdown("---")
st.markdown(
    "*Source Code adapted from [Stack Overflow Post"
    " 43612128](https://stackoverflow.com/questions/43559224/primality-testing-how-to-make-sure-not-to-test-numbers-which-are-multiples-of-a/43612128#43612128)"
    " — Licensed under CC BY-SA 3.0*"
)