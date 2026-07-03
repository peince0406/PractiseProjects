blacklist = [
    "spam123@evil.com",
    "promo99@fakesite.com",
    "winner@lottery.net",
    "free.money@scam.org",
    "alert@phishing.com"
]

def is_spam(email, blacklist):
    for sender in blacklist:         
        if sender == email:        
            return True              
    return False                     

incoming_emails = [
    "friend@gmail.com",
    "winner@lottery.net",
    "boss@company.com",
    "spam123@evil.com",
    "student@college.edu"
]

print("="*45)
print("      SPAM DETECTOR - Email Scanner")
print("="*45)

for email in incoming_emails:
    if is_spam(email, blacklist):
        print(f"  🚫 SPAM    : {email}")
    else:
        print(f"  ✅ SAFE    : {email}")

print("="*45)
