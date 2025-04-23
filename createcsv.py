import pandas as pd
import random

# List of valid countries and companies
COUNTRIES = ["USA", "Germany", "Japan", "UK", "Canada", "Australia", "France", "India", "China", "Brazil"]
COMPANIES = ["TechCorp", "AutoGmbH", "ElectronicsInc", "FinanceCo", "HealthPlus", "EnergySolutions", "RetailWorld", "LogisticsHub", "AgriTech", "PharmaCare"]

# Function to generate random but valid data
def generate_loan_pricing_data(num_rows=200):
    data = {
        "Country": [],
        "Company": [],
        "BaseRate": [],
        "Inflation": [],
        "GDP": [],
        "RegulationScore": [],
        "LoanAmount": [],
        "LoanTerm": [],
        "LoanRate": []
    }

    for _ in range(num_rows):
        # Randomly select country and company
        country = random.choice(COUNTRIES)
        company = random.choice(COMPANIES)

        # Generate random values for numerical columns
        base_rate = round(random.uniform(1.0, 10.0), 4)  # BaseRate between 1.0 and 10.0
        inflation = round(random.uniform(0.5, 5.0), 4)    # Inflation between 0.5 and 5.0
        gdp = round(random.uniform(0.5, 5.0), 4)          # GDP between 0.5 and 5.0
        regulation_score = round(random.uniform(5.0, 10.0), 4)  # RegulationScore between 5.0 and 10.0
        loan_amount = random.randint(100000, 10000000)    # LoanAmount between 100,000 and 10,000,000
        loan_term = random.randint(5, 25)                 # LoanTerm between 5 and 25 years
        loan_rate = round(random.uniform(2.0, 12.0), 2)   # LoanRate between 2.0 and 12.0, rounded to 2 decimal places

        # Append data to the dictionary
        data["Country"].append(country)
        data["Company"].append(company)
        data["BaseRate"].append(base_rate)
        data["Inflation"].append(inflation)
        data["GDP"].append(gdp)
        data["RegulationScore"].append(regulation_score)
        data["LoanAmount"].append(loan_amount)
        data["LoanTerm"].append(loan_term)
        data["LoanRate"].append(loan_rate)

    # Create a DataFrame
    df = pd.DataFrame(data)
    return df

# Save the generated data to a CSV file
def save_to_csv(df, filename="loan_pricing_data.csv"):
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Main function
if __name__ == "__main__":
    # Generate 200 rows of data
    loan_pricing_data = generate_loan_pricing_data(200)

    # Save the data to a CSV file
    save_to_csv(loan_pricing_data)