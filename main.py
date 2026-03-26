print("===================================")
print("      ✈️ Flight Delay Predictor     ")
print("===================================")

# Taking user inputs
time = input("Enter time of flight (morning/evening/night): ").lower()
weather = input("Enter weather (clear/rainy/foggy): ").lower()
traffic = input("Enter air traffic (low/high): ").lower()

print("\nAnalyzing conditions...\n")

# Logic for prediction
if weather == "rainy" and traffic == "high":
    result = "⚠️ High chance of flight delay"
elif weather == "foggy":
    result = "⚠️ Possible delay due to low visibility"
elif traffic == "high":
    result = "⚠️ Delay possible due to heavy traffic"
else:
    result = "✅ Flight is likely on time"

# Final output
print("Result:", result)
print("\nThank you for using Flight Delay Predictor ✈️")
