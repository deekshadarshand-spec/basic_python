# =========================================
# IPL Analytics Project
# analysis.py
# =========================================

# Import Libraries
import os
import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------
# Create visuals folder if not exists
# -----------------------------------------

os.makedirs("../visuals", exist_ok=True)

# -----------------------------------------
# Extract ZIP File
# -----------------------------------------

zip_path = "../archive.zip"

extract_path = "../data"

# Create data folder if not exists
os.makedirs(extract_path, exist_ok=True)

# Unzip archive.zip
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("\n========== ZIP FILE EXTRACTED ==========\n")

# -----------------------------------------
# Load Dataset
# -----------------------------------------

matches_path = os.path.join(extract_path, "matches.csv")
deliveries_path = os.path.join(extract_path, "deliveries.csv")

matches = pd.read_csv(matches_path)
deliveries = pd.read_csv(deliveries_path)

print("\n========== DATASET LOADED ==========\n")

print("Matches Dataset Shape:", matches.shape)
print("Deliveries Dataset Shape:", deliveries.shape)

# -----------------------------------------
# View Dataset
# -----------------------------------------

print("\n========== MATCHES DATASET ==========\n")
print(matches.head())

print("\n========== DELIVERIES DATASET ==========\n")
print(deliveries.head())

# -----------------------------------------
# Dataset Information
# -----------------------------------------

print("\n========== DATASET INFO ==========\n")
print(matches.info())

# -----------------------------------------
# Missing Values
# -----------------------------------------

print("\n========== MISSING VALUES ==========\n")
print(matches.isnull().sum())

# Fill Missing Winner Values
matches['winner'] = matches['winner'].fillna("No Result")

# -----------------------------------------
# Total IPL Matches
# -----------------------------------------

total_matches = matches.shape[0]

print("\n========== TOTAL MATCHES ==========\n")
print("Total IPL Matches:", total_matches)

# -----------------------------------------
# Total Teams
# -----------------------------------------

teams = matches['team1'].unique()

print("\n========== TOTAL TEAMS ==========\n")
print("Total Teams:", len(teams))

print("\nTeams List:\n")
print(teams)

# -----------------------------------------
# Team Wins Analysis
# -----------------------------------------

team_wins = matches['winner'].value_counts()

print("\n========== TEAM WINS ==========\n")
print(team_wins)

# -----------------------------------------
# Team Wins Visualization
# -----------------------------------------

plt.figure(figsize=(12, 6))

team_wins.plot(kind='bar')

plt.title("IPL Team Wins")
plt.xlabel("Teams")
plt.ylabel("Wins")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("../visuals/team_wins.png")

plt.show()

# -----------------------------------------
# Toss Decision Analysis
# -----------------------------------------

toss_decision = matches['toss_decision'].value_counts()

print("\n========== TOSS DECISION =
