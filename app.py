import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
try:
    df = pd.read_csv("data.csv")
except FileNotFoundError:
    print("File not found!")
    exit()

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("✅ CSV Loaded Successfully\n")
print(df.head())

print("\nYou can ask:")
print("1. total sales")
print("2. average revenue")
print("3. highest sales region")
print("4. plot sales")
print("5. plot revenue")
print("6. monthly sales")
print("7. total revenue")
print("8. region sales")
print("9. Type 'exit' to stop\n")

while True:
    query = input("👉 Question: ").lower()

    if query == "exit":
        print("Exiting...")
        break

    elif query in["1", "total sales" ]:
        print("Total Sales:", df["Sales"].sum())

    elif query in ["2" ,"average revenue" ]:
        print("Average Revenue:", df["Revenue"].mean())

    elif query in ["3" ,"highest sales" ]:
        max_region = df.loc[df["Sales"].idxmax()]["Region"]
        print("Region with Highest Sales:", max_region)

    elif query in ["4", "plot sales"]:
        plt.figure()
        plt.plot(df["Date"], df["Sales"], marker='o')
        plt.grid(True)
        plt.title("Sales Over Time")
        plt.xlabel("Date")
        plt.ylabel("Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("sales_plot.png")
        plt.show()
        print("📊 Graph saved as sales_plot.png")

    elif query in [ "5" , "plot revenue" ]:
        plt.figure()
        plt.plot(df["Date"], df["Revenue"])
        plt.title("Revenue Over Time")
        plt.xlabel("Date")
        plt.ylabel("Revenue")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("revenue_plot.png")
        plt.show()
        print("📊 Revenue graph saved as revenue_plot.png")

    elif query in ["6", "monthly sales"]:
        monthly = df.resample("M", on="Date")["Sales"].sum()
        print(monthly)

    elif query in ["7", "total revenue"]:
        print("Total Revenue:", df["Revenue"].sum())
    
    elif query in ["8", "region sales"]:
        print(df.groupby("Region")["Sales"].sum())

    else:
        print("❌ Sorry, I don't understand that question yet.") 
