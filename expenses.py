import streamlit as st

st.title("💸 Expense Tracker")
st.write("Track your daily expenses easily")

# Expense list ko session me rakho
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# ===== Add Expense =====
st.subheader("➕ Add New Expense")

date = st.date_input("Date")
category = st.selectbox("Category", ["Food", "Travel", "Books", "Other"])
description = st.text_input("Description")
amount = st.number_input("Amount", min_value=0.0, step=1.0)

if st.button("Add Expense"):
    expense = {
        "date": date,
        "category": category,
        "description": description,
        "amount": amount
    }
    st.session_state.expenses.append(expense)
    st.success("Expense added successfully ✅")

# ===== View Expenses =====
st.subheader("📋 All Expenses")

if len(st.session_state.expenses) == 0:
    st.info("No expenses added yet")
else:
    for i, e in enumerate(st.session_state.expenses, start=1):
        st.write(
            f"{i}. {e['date']} | {e['category']} | {e['description']} | ₹{e['amount']}"
        )

# ===== Total Spending =====
st.subheader("💰 Total Spending")

total = sum(e["amount"] for e in st.session_state.expenses)
st.success(f"Total Spending: ₹ {total}")
