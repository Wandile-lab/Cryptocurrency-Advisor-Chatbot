crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

def recommend_coin(user_query):
    if "profit" in user_query or "growth" in user_query or "long-term" in user_query:
        profitable_coins = [
            coin for coin, data in crypto_db.items()
            if data["price_trend"] == "rising" and data["market_cap"] == "high"
        ]
        if profitable_coins:
            best = max(profitable_coins, key=lambda c: crypto_db[c]["sustainability_score"])
            return f"{best} is trending up and has a strong market cap! 🚀"
        else:
            return "No top profitable coins found right now."

    elif "sustain" in user_query:
        sustainable_coins = [
            coin for coin, data in crypto_db.items()
            if data["energy_use"] == "low" and data["sustainability_score"] > 7/10
        ]
        if sustainable_coins:
            return f"{', '.join(sustainable_coins)} have low energy use and top sustainability scores! 🌱"
        else:
            return "No highly sustainable coins found right now."

    else:
        return None

user_query = input("Ask CryptoBuddy a question: ").lower()

response = recommend_coin(user_query)

if response:
    print(f"CryptoBuddy: {response}")
else:
    if "trending" in user_query or "price trend" in user_query:
        trending_coins = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        if trending_coins:
            print(f"CryptoBuddy: Trending up coins right now: {', '.join(trending_coins)} 🚀")
        else:
            print("CryptoBuddy: No coins are currently trending up.")

    elif "market cap" in user_query or "market capitalization" in user_query:
        cap_rank = {"high": 3, "medium": 2, "low": 1}
        max_cap_value = max(cap_rank[crypto_db[coin]["market_cap"]] for coin in crypto_db)
        top_caps = [coin for coin in crypto_db if cap_rank[crypto_db[coin]["market_cap"]] == max_cap_value]
        print(f"CryptoBuddy: Top market cap coins: {', '.join(top_caps)} 💰")

    else:
        print("CryptoBuddy: Sorry, I don't understand that yet. Try asking about sustainability, trends, market cap, or investment advice.")
