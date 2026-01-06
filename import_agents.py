import json
import firebase_admin
from firebase_admin import credentials, firestore
import glob
import os

# Initialize Firebase Admin SDK
if not firebase_admin._apps:
    service_account_file = None
    if os.path.exists("serviceAccountKey.json"):
        service_account_file = "serviceAccountKey.json"
    else:
        dreproxy_files = glob.glob("dreproxy-*.json")
        if dreproxy_files:
            service_account_file = dreproxy_files[0]
    
    if service_account_file:
        cred = credentials.Certificate(service_account_file)
        firebase_admin.initialize_app(cred)
        print(f"Firebase initialized with {service_account_file}")
    else:
        print("Error: Firebase credentials not found")
        exit(1)

db = firestore.client()

# Agent data from the JSON
agent_data = {
    "success": True,
    "total_agents": 12,
    "agents": [
        {
            "name": "Aadesh 'Adam' Niraula",
            "location": None,
            "profile_url": "https://onereal.com/profile/aniraula",
            "phone": "+1 (817) 789-3885",
            "email": "an.txrealty@gmail.com",
            "bio": None,
            "specialties": ["Login\nInvestors", "Login\nInvestors", "Login", "Investors", "Real Estate\nMortgage\nTitle/Escrow\nAbout Us\nFor Agents", "Real Estate\nMortgage\nTitle/Escrow\nAbout Us\nFor Agents", "Real Estate\nMortgage\nTitle/Escrow\nAbout Us\nFor Agents", "Real Estate", "Mortgage", "Title/Escrow", "About Us", "For Agents", "Menu", "Real EstateMortgageTitle/EscrowAbout UsAgentsInvestorsTake me to Canada", "Real EstateMortgageTitle/EscrowAbout UsAgentsInvestorsTake me to Canada", "Real Estate", "Real Estate", "Mortgage", "Mortgage", "Title/Escrow", "Title/Escrow", "About Us", "About Us", "Agents", "Agents", "Investors", "Investors", "Investors", "Take me to Canada", "Take me to Canada", "Take me to Canada", "Hi, I'm\n\nAadesh 'Adam' Niraula\nMy Service Areas\nColleyville\nLake Dallas\nEuless\nHaltom City\nHaslet\nDenton\nFort Worth\nHurst\nRoanoke\nCoppell\nSouthlake\nGrapevine\nBedford\nIrving\nKeller\nFlower Mound\nNorth Richland Hills\nJustin\nGrand Prairie\nArgyle\nArlington\nLewisville\nDFW real estate expert with 10+ years in civil engineering and land development, specializing in residential, commercial, and land properties. Passionate about investing, developing, and helping clients make strategic moves—here to guide every step of the way on their real estate journey!\nGet In Touch", "Hi, I'm\n\nAadesh 'Adam' Niraula\nMy Service Areas\nColleyville\nLake Dallas\nEuless\nHaltom City\nHaslet\nDenton\nFort Worth\nHurst\nRoanoke\nCoppell\nSouthlake\nGrapevine\nBedford\nIrving\nKeller\nFlower Mound\nNorth Richland Hills\nJustin\nGrand Prairie\nArgyle\nArlington\nLewisville\nDFW real estate expert with 10+ years in civil engineering and land development, specializing in residential, commercial, and land properties. Passionate about investing, developing, and helping clients make strategic moves—here to guide every step of the way on their real estate journey!", "Hi, I'm\n\nAadesh 'Adam' Niraula", "Aadesh 'Adam' Niraula", "My Service Areas", "Colleyville\nLake Dallas\nEuless\nHaltom City\nHaslet\nDenton\nFort Worth\nHurst\nRoanoke\nCoppell\nSouthlake\nGrapevine\nBedford\nIrving\nKeller\nFlower Mound\nNorth Richland Hills\nJustin\nGrand Prairie\nArgyle\nArlington\nLewisville", "Colleyville", "Colleyville", "Lake Dallas", "Lake Dallas", "Euless", "Euless", "Haltom City", "Haltom City", "Haslet", "Haslet", "Denton", "Denton", "Fort Worth", "Fort Worth", "Hurst", "Hurst", "Roanoke", "Roanoke", "Coppell", "Coppell", "Southlake", "Southlake", "Grapevine", "Grapevine", "Bedford", "Bedford", "Irving", "Irving", "Keller", "Keller", "Flower Mound", "Flower Mound", "North Richland Hills", "North Richland Hills", "Justin", "Justin", "Grand Prairie", "Grand Prairie", "Argyle", "Argyle", "Arlington", "Arlington", "Lewisville", "Lewisville", "DFW real estate expert with 10+ years in civil engineering and land development, specializing in residential, commercial, and land properties. Passionate about investing, developing, and helping clients make strategic moves—here to guide every step of the way on their real estate journey!", "Get In Touch", "Get In Touch", "License #:\nTexas - 0826789", "License #:", "Texas - 0826789", "Texas - 0826789", "Languages: English, Hindi", "Languages: English, Hindi", "+1 (817) 789-3885", "+1 (817) 789-3885", "an.txrealty@gmail.com", "an.txrealty@gmail.com", "https://onereal.com/aniraula", "https://onereal.com/aniraula", "My Socials", "Get In Touch", "Get In Touch", "Aadesh 'Adam' Niraula\n+1 (817) 789-3885\nan.txrealty@gmail.com\nhttps://onereal.com/aniraula\nGet In Touch", "Aadesh 'Adam' Niraula\n+1 (817) 789-3885\nan.txrealty@gmail.com\nhttps://onereal.com/aniraula\nGet In Touch", "Aadesh 'Adam' Niraula\n+1 (817) 789-3885\nan.txrealty@gmail.com\nhttps://onereal.com/aniraula\nGet In Touch", "Aadesh 'Adam' Niraula", "Aadesh 'Adam' Niraula", "Aadesh 'Adam' Niraula", "+1 (817) 789-3885\nan.txrealty@gmail.com\nhttps://onereal.com/aniraula\nGet In Touch", "+1 (817) 789-3885\nan.txrealty@gmail.com\nhttps://onereal.com/aniraula", "+1 (817) 789-3885", "+1 (817) 789-3885", "an.txrealty@gmail.com", "an.txrealty@gmail.com", "https://onereal.com/aniraula", "https://onereal.com/aniraula", "Get In Touch", "Get In Touch"],
            "languages": ["English", "Hindi"],
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "Texas - 0826789",
            "website": "http://investors.onereal.com",
            "facebook": "https://www.facebook.com/AN.RealEstateShop",
            "instagram": "https://www.instagram.com/an.realestateshop/"
        },
        {
            "name": "Aankit Malhotra",
            "location": None,
            "profile_url": "https://onereal.com/profile/aankit-malhotra",
            "phone": "+1 (908) 656-2015",
            "email": "aankitm07@gmail.com",
            "bio": None,
            "specialties": None,
            "languages": None,
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "New Jersey - 1750946",
            "website": "http://investors.onereal.com",
            "facebook": "https://www.facebook.com/realbrokerage",
            "instagram": "https://www.instagram.com/realbrokerage/"
        },
        {
            "name": "Aaron Aker",
            "location": None,
            "profile_url": "https://onereal.com/profile/aaron-aker",
            "phone": "+1 (804) 852-1823",
            "email": "aaronakerrealtor@gmail.com",
            "bio": None,
            "specialties": None,
            "languages": ["English"],
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "Virginia - 0225272877,",
            "website": "http://investors.onereal.com",
            "facebook": "https://facebook.com/aaronakerrealtor",
            "instagram": "https://instagram.com/aaronakerrealtor/"
        },
        {
            "name": "Aaron Allina",
            "location": None,
            "profile_url": "https://onereal.com/profile/aaron-allina",
            "phone": "+1 (602) 935-9232",
            "email": "cbrkitten@gmail.com",
            "bio": None,
            "specialties": None,
            "languages": ["English"],
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "Arizona - SA714791000",
            "website": "http://investors.onereal.com",
            "facebook": "https://www.facebook.com/realbrokerage",
            "instagram": "https://www.instagram.com/realbrokerage/"
        },
        {
            "name": "Aaron Alonso",
            "location": None,
            "profile_url": "https://onereal.com/profile/aaronalonso",
            "phone": "+1 (210) 774-9590",
            "email": "aaronaaahomes@gmail.com",
            "bio": None,
            "specialties": None,
            "languages": ["English", "Spanish"],
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "Texas - 839088",
            "website": "http://investors.onereal.com",
            "facebook": "https://www.facebook.com/realbrokerage",
            "instagram": "https://instagram.com/aaronrealtorr"
        },
        {
            "name": "Aaron Arreola Moreno",
            "location": None,
            "profile_url": "https://onereal.com/profile/aaron_therealtor",
            "phone": "+1 (310) 756-8262",
            "email": "therealtoraaron@gmail.com",
            "bio": None,
            "specialties": None,
            "languages": ["English", "Spanish"],
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "Aaron Arreola Moreno",
            "website": "http://investors.onereal.com",
            "facebook": "https://facebook.com/AaronTheRealtor",
            "instagram": "https://instagram.com/Aaron_TheRealtor"
        },
        {
            "name": "Aaron Avila",
            "location": None,
            "profile_url": "https://onereal.com/profile/aaron-avila",
            "phone": "+1 (424) 622-4017",
            "email": "aaron@hubluegroup.com",
            "bio": None,
            "specialties": None,
            "languages": ["English", "Spanish"],
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "California - 02163977",
            "website": "http://investors.onereal.com",
            "facebook": "https://www.facebook.com/profile.php?id=100073738202713",
            "instagram": "https://www.instagram.com/doinggreatre/?hl=en"
        },
        {
            "name": "Aaron Baker",
            "location": None,
            "profile_url": "https://onereal.com/profile/aaron-baker",
            "phone": "+1 (215) 262-3171",
            "email": "aaronbaker.re@gmail.com",
            "bio": None,
            "specialties": None,
            "languages": None,
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "Pennsylvania - RS309988",
            "website": "http://investors.onereal.com",
            "facebook": "https://www.facebook.com/realbrokerage",
            "instagram": "https://www.instagram.com/realbrokerage/"
        },
        {
            "name": "My Listings",
            "location": None,
            "profile_url": "https://onereal.com/profile/aaron-bates",
            "phone": "+1 (516) 528-4824",
            "email": "aaron@aaronbatesrealestate.com",
            "bio": None,
            "specialties": None,
            "languages": None,
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "New York - 10401239872",
            "website": "http://investors.onereal.com",
            "facebook": "https://facebook.com/aaronbatesrealestateteam",
            "instagram": "https://instagram.com/aaronbatesrealestate"
        },
        {
            "name": "Aaron Bearden",
            "location": None,
            "profile_url": "https://onereal.com/profile/aaron-bearden",
            "phone": "+1 (310) 980-2017",
            "email": "aaronb@therise.group",
            "bio": None,
            "specialties": None,
            "languages": None,
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "California - 01961696",
            "website": "http://investors.onereal.com",
            "facebook": "https://www.facebook.com/realbrokerage",
            "instagram": "https://www.instagram.com/realbrokerage/"
        },
        {
            "name": "Aaron Brockup",
            "location": None,
            "profile_url": "https://onereal.com/profile/aaron-brockup",
            "phone": "+1 (228) 249-6229",
            "email": "aabrockup@gmail.com",
            "bio": None,
            "specialties": None,
            "languages": ["English"],
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "Mississippi - s-61396",
            "website": "http://investors.onereal.com",
            "facebook": "https://www.facebook.com/realbrokerage",
            "instagram": "https://www.instagram.com/realbrokerage/"
        },
        {
            "name": "Aaron Brown",
            "location": None,
            "profile_url": "https://onereal.com/profile/aaron-brown-1",
            "phone": "+1 (316) 730-9797",
            "email": "aaronhb1926@gmail.com",
            "bio": None,
            "specialties": None,
            "languages": ["Vietnamese", "English"],
            "years_experience": None,
            "image_url": "https://onereal.com/img/RealLogo.svg",
            "office": None,
            "license": "Kansas - 00250248",
            "website": "http://investors.onereal.com",
            "facebook": "https://www.facebook.com/profile.php?id=61554235706703",
            "instagram": "https://www.instagram.com/realbrokerage/"
        }
    ],
    "message": "Successfully scraped 12 agents with full details"
}

def import_agents():
    """Import agents from JSON data to Firestore"""
    agents_collection = db.collection("agents")
    imported_count = 0
    skipped_count = 0
    
    print(f"Starting import of {len(agent_data['agents'])} agents...\n")
    
    for agent in agent_data['agents']:
        try:
            # Map JSON fields to database fields
            name = agent.get('name', '').strip()
            email = agent.get('email', '').strip()
            phone = agent.get('phone', '').strip()
            license_info = agent.get('license', '').strip()
            
            # Validate required fields
            if not name or not email:
                print(f"⚠️  Skipping agent: Missing name or email")
                skipped_count += 1
                continue
            
            # Check if agent already exists (by email)
            existing_agents = agents_collection.where('email', '==', email).limit(1).stream()
            if list(existing_agents):
                print(f"⏭️  Skipping {name}: Already exists (email: {email})")
                skipped_count += 1
                continue
            
            # Prepare agent data for Firestore
            agent_doc = {
                'name': name,
                'email': email,
                'phone_number': phone if phone else '',
                'licence_number': license_info if license_info else ''
            }
            
            # Add to Firestore
            doc_ref = agents_collection.add(agent_doc)
            print(f"✅ Imported: {name} ({email})")
            imported_count += 1
            
        except Exception as e:
            print(f"❌ Error importing {agent.get('name', 'Unknown')}: {e}")
            skipped_count += 1
    
    print(f"\n{'='*50}")
    print(f"Import complete!")
    print(f"✅ Successfully imported: {imported_count}")
    print(f"⏭️  Skipped: {skipped_count}")
    print(f"📊 Total processed: {imported_count + skipped_count}")
    print(f"{'='*50}")

if __name__ == "__main__":
    import_agents()

