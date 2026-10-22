# Miller-Rabin Primality Testing Dashboard

An interactive modular Streamlit web application to test the primality of large numbers using an optimized deterministic Miller-Rabin algorithm adapted from one of our 2018 posts on Stack Overflow

## 🚀 Features
* **Interactive Tester**: Test individual numbers with pre-loaded presets or custom inputs.
* **Batch Prime Finder**: Scan a numerical range to find all prime numbers. (Addition to the intial post on Stack Overflow)
* **Algorithm Viewer**: Inspect the underlying Python implementation directly from the app.

## 📂 Project Structure
* `primality.py`: Core deterministic Miller-Rabin algorithm.
* `app.py`: Streamlit frontend dashboard interface.
* `requirements.txt`: Python package dependencies.

## 🔗 Attribution & License
* **Source:** [Stack Overflow Answer by Pozeidon](https://stackoverflow.com/a/43612128)
* **License:** [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)