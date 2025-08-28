import streamlit as st

def kalkulator(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            return "Error: Pembagi tidak boleh nol"
        return operand1 / operand2

def konversi_suhu(suhu, dari, ke):
    if dari == 'Celsius':
        if ke == 'Fahrenheit':
            return (suhu * 9/5) + 32
        elif ke == 'Kelvin':
            return suhu + 273.15
    elif dari == 'Fahrenheit':
        if ke == 'Celsius':
            return (suhu - 32) * 5/9
        elif ke == 'Kelvin':
            return (suhu - 32) * 5/9 + 273.15
    elif dari == 'Kelvin':
        if ke == 'Celsius':
            return suhu - 273.15
        elif ke == 'Fahrenheit':
            return (suhu - 273.15) * 9/5 + 32

def fibonacci(n):
    if n <= 0:
        return []
    fibo = [0, 1]
    if n == 1:
        return [0]
    while len(fibo) < n:
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

st.title("Aplikasi Multifungsi: Kalkulator, Konversi Suhu, dan Deret Fibonacci")

menu = st.sidebar.selectbox("Pilih Fitur", ["Kalkulator", "Konversi Suhu", "Deret Fibonacci"])

if menu == "Kalkulator":
    st.header("Kalkulator Sederhana")
    operand1 = st.number_input("Masukkan Operand 1", value=0)
    operand2 = st.number_input("Masukkan Operand 2", value=0)
    operator = st.selectbox("Pilih Operator", ['+', '-', '*', '/'])
    if st.button("Hitung"):
        hasil = kalkulator(operand1, operand2, operator)
        st.success(f"Hasil: {hasil}")

elif menu == "Konversi Suhu":
    st.header("Konversi Suhu")
    suhu = st.number_input("Masukkan Suhu", value=0.0)
    dari = st.selectbox("Dari", ['Celsius', 'Fahrenheit', 'Kelvin'])
    ke = st.selectbox("Ke", ['Celsius', 'Fahrenheit', 'Kelvin'])
    if st.button("Konversi"):
        if dari == ke:
            hasil = suhu
        else:
            hasil = konversi_suhu(suhu, dari, ke)
        st.success(f"Hasil: {hasil} {ke}")

elif menu == "Deret Fibonacci":
    st.header("Deret Fibonacci")
    n = st.number_input("Masukkan jumlah nilai Fibonacci", min_value=1, value=10)
    if st.button("Generate"):
        hasil = fibonacci(n)
        st.write(f"Deret Fibonacci hingga {n} nilai")
        st.write(hasil)