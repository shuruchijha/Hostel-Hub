"""
Campus Directory: Accurate mapping of Indian Colleges to their specific Hostels,
Blocks, Wings, and Residences.

When a student selects a college, the app dynamically filters and shows ONLY the
hostels and blocks/wings associated with that college, eliminating confusion.
"""

# Specific mappings for prominent colleges and universities across India
CAMPUS_DATA = {
    # ── IITs ──
    "iit bombay": {
        "hostels": [
            "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4", "Hostel 5",
            "Hostel 6", "Hostel 7", "Hostel 8", "Hostel 9", "Hostel 10",
            "Hostel 11 (Girls)", "Hostel 12", "Hostel 13", "Hostel 14",
            "Hostel 15 (Girls)", "Hostel 16", "Hostel 17", "Hostel 18",
            "Tansa House"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Floor 1", "Floor 2", "Floor 3", "Floor 4", "Floor 5"],
        "block_label": "Wing / Floor"
    },
    "iit delhi": {
        "hostels": [
            "Aravali Hostel", "Karakoram Hostel", "Nilgiri Hostel", "Kumaon Hostel",
            "Vindhyachal Hostel", "Jwalamukhi Hostel", "Shivalik Hostel", "Zanskar Hostel",
            "Satpura Hostel", "Girnar Hostel", "Udaigiri Hostel",
            "Himadri Hostel (Girls)", "Kailash Hostel (Girls)", "New Girls Hostel"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Ground Floor", "1st Floor", "2nd Floor", "3rd Floor"],
        "block_label": "Wing / Floor"
    },
    "iit madras": {
        "hostels": [
            "Alakananda Hostel", "Brahmaputra Hostel", "Cauvery Hostel", "Ganga Hostel",
            "Godavari Hostel", "Jamuna Hostel", "Krishna Hostel", "Mahanadi Hostel",
            "Mandakini Hostel", "Narmada Hostel", "Pampa Hostel", "Saraswathi Hostel",
            "Sarayu Hostel (Girls)", "Sharavathi Hostel (Girls)", "Sindhu Hostel",
            "Tamiraparani Hostel", "Tapti Hostel", "Sabarmati Hostel", "Bhadra Hostel",
            "Swarna Hostel (Girls)"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Wing D", "Ground Floor", "1st Floor", "2nd Floor"],
        "block_label": "Wing / Section"
    },
    "iit kanpur": {
        "hostels": [
            "Hall 1", "Hall 2", "Hall 3", "Hall 4", "Hall 5",
            "Hall 7", "Hall 8", "Hall 9", "Hall 10", "Hall 11",
            "Hall 12", "Hall 13", "Girls Hostel 1 (GH1)", "Girls Hostel 2 (GH2)"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Wing D", "Top Floor", "Mid Floor", "Ground Floor"],
        "block_label": "Wing / Floor"
    },
    "iit kharagpur": {
        "hostels": [
            "Azad Hall", "Nehru Hall", "Patel Hall", "Rajendra Prasad Hall",
            "Radhakrishnan Hall", "Lal Bahadur Shastri Hall", "Homi Bhabha Hall",
            "Sir Ashutosh Mukherjee Hall", "Jagadish Chandra Bose Hall", "Vidyasagar Hall",
            "Zakir Hussain Hall", "Mother Teresa Hall (Girls)", "Sarojini Naidu Hall (Girls)",
            "Indira Gandhi Hall (Girls)", "Sister Nivedita Hall (Girls)", "Rani Laxmibai Hall (Girls)",
            "Meghnad Saha Hall", "BR Ambedkar Hall", "Vikram Sarabhai Hall"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Wing D", "Block 1", "Block 2", "Top Floor"],
        "block_label": "Wing / Block"
    },
    "iit roorkee": {
        "hostels": [
            "Ganga Bhawan", "Govind Bhawan", "Cautley Bhawan", "Rajendra Bhawan",
            "Radhakrishnan Bhawan", "Ravindra Bhawan", "Jawahar Bhawan", "Rajiv Bhawan",
            "Kasturba Bhawan (Girls)", "Sarojini Bhawan (Girls)", "Indira Bhawan (Girls)",
            "Vigyan Kunj"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Mess Wing", "1st Floor", "2nd Floor", "3rd Floor"],
        "block_label": "Block / Wing"
    },
    "iit guwahati": {
        "hostels": [
            "Brahmaputra Hostel", "Dihing Hostel", "Manas Hostel", "Umiam Hostel",
            "Barak Hostel", "Kameng Hostel", "Siang Hostel", "Kapili Hostel",
            "Dhansiri Hostel (Girls)", "Subansiri Hostel (Girls)", "Disang Hostel (Girls)",
            "Lohit Hostel"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D", "Ground Floor", "1st Floor", "2nd Floor"],
        "block_label": "Block / Floor"
    },
    "iit bhu": {
        "hostels": [
            "Limbdi Hostel", "Rajputana Hostel", "Morvi Hostel", "Dhanrajgiri (DG) Hostel",
            "Vishwakarma Hostel", "Vivekanand Hostel", "Aryabhatta Hostel", "Ramanujan Hostel",
            "SN Bose Hostel", "SC Dey Hostel", "GSMC (Girls)", "Rani Laxmibai Hostel (Girls)"
        ],
        "blocks": ["Wing 1", "Wing 2", "Wing 3", "Wing 4", "Block A", "Block B"],
        "block_label": "Wing / Block"
    },
    "iit dhanbad": {
        "hostels": [
            "Diamond Hostel", "Emerald Hostel", "Topaz Hostel", "Opal Hostel",
            "Jasper Hostel", "Ruby Hostel", "Sapphire Hostel", "Amber Hostel",
            "Rosaline Hostel (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D", "Floor 1", "Floor 2", "Floor 3"],
        "block_label": "Block / Floor"
    },
    "iit hyderabad": {
        "hostels": [
            "Charminar Hostel", "Golconda Hostel", "Qutub Shahi Hostel", "Kakatiya Hostel",
            "Hostel A (Boys)", "Hostel B (Boys)", "Hostel C (Girls)", "Hostel D (Girls)",
            "Kandi Block 1", "Kandi Block 2"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Floor 1", "Floor 2", "Floor 3", "Floor 4"],
        "block_label": "Block / Floor"
    },

    # ── NITs ──
    "nit trichy": {
        "hostels": [
            "Garnet A", "Garnet B", "Agate Hostel", "Coral Hostel", "Diamond Hostel",
            "Jade Hostel", "Pearl Hostel", "Emerald Hostel", "Ruby Hostel",
            "Sapphire Hostel", "Topaz Hostel", "Zircon A", "Zircon B", "Beryl Hostel",
            "Opal A (Girls)", "Opal B (Girls)", "Opal C (Girls)", "Opal D (Girls)", "Opal E (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D", "Wing 1", "Wing 2"],
        "block_label": "Block / Wing"
    },
    "nit surathkal": {
        "hostels": [
            "Block 1 (Boys)", "Block 2 (Boys)", "Block 3 (Boys)", "Block 4 (Boys)",
            "Block 5 (Boys)", "Block 6 (Boys)", "Block 7 (Boys)", "Block 8 (Boys)",
            "Mega Boys Hostel", "PG Hostel", "Sahyadri Hostel (Girls)",
            "Sharavathi Hostel (Girls)", "Godavari Hostel (Girls)", "Brahmaputra Hostel (Girls)"
        ],
        "blocks": ["Block 1", "Block 2", "Block 3", "Tower 1", "Tower 2", "Wing A", "Wing B"],
        "block_label": "Block / Tower"
    },
    "nit warangal": {
        "hostels": [
            "1.8K Ultra Mega Hostel", "1K Hostel", "Mega Boys Hostel", "Hall 1",
            "Hall 2", "Hall 3", "Hall 4", "Hall 5", "Hall 6", "Hall 7", "Hall 8",
            "Priyadarshini Ladies Hostel", "Sarojini Devi Ladies Hostel", "New Ladies Hostel"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D", "Wing A", "Wing B", "Floor 1-7"],
        "block_label": "Block / Wing"
    },
    "nit calicut": {
        "hostels": [
            "Hostel A", "Hostel B", "Hostel C", "Hostel D", "Hostel E",
            "Hostel F", "Hostel G", "Mega Boys Hostel", "PG 1", "PG 2",
            "LH-A (Ladies)", "LH-B (Ladies)", "LH-C (Ladies)", "LH-D (Ladies)"
        ],
        "blocks": ["Ground Floor", "1st Floor", "2nd Floor", "3rd Floor", "Wing A", "Wing B"],
        "block_label": "Wing / Floor"
    },
    "vnit nagpur": {
        "hostels": [
            "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4", "Hostel 5",
            "Hostel 6", "Hostel 7", "Mega Hostel", "Old Girls Hostel", "New Girls Hostel"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Wing A", "Wing B"],
        "block_label": "Block / Wing"
    },
    "mnit jaipur": {
        "hostels": [
            "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4", "Hostel 5",
            "Hostel 6", "Hostel 7", "Hostel 8", "Hostel 9", "Hostel 10", "Hostel 11",
            "Gargi Hostel (Girls)", "Ganga Hostel (Girls)", "Annie Besant Hostel (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Wing A", "Wing B"],
        "block_label": "Block / Wing"
    },
    "mnnit allahabad": {
        "hostels": [
            "Swami Vivekananda Hostel", "C.V. Raman Hostel", "Malaviya Hostel",
            "Tandon Hostel", "Tilak Hostel", "Patel Hostel", "Tagore Hostel",
            "Raman Hostel", "Sarojini Naidu (Girls)", "Kamala Nehru (Girls)"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Ground Floor", "1st Floor", "2nd Floor"],
        "block_label": "Wing / Floor"
    },
    "nit rourkela": {
        "hostels": [
            "VS Hall of Residence", "MV Hall", "GDB Hall", "DBA Hall",
            "MSS Hall", "HB Hall", "SD Hall", "KMS Hall (Girls)", "CVR Hall (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D", "Wing 1", "Wing 2"],
        "block_label": "Block / Wing"
    },
    "nit kurukshetra": {
        "hostels": [
            "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4", "Hostel 5",
            "Hostel 6", "Hostel 7", "Hostel 8", "Hostel 9", "Hostel 10",
            "Kalpana Chawla Bhawan (Girls)", "Alaknanda Bhawan (Girls)", "Cauvery Bhawan (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Ground Floor", "1st Floor", "2nd Floor"],
        "block_label": "Block / Floor"
    },
    "nit silchar": {
        "hostels": [
            "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4", "Hostel 5",
            "Hostel 6", "Hostel 7", "Hostel 8", "Hostel 9",
            "Girls Hostel 1", "Girls Hostel 2", "Girls Hostel 3"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Wing A", "Wing B"],
        "block_label": "Block / Wing"
    },
    "nit jamshedpur": {
        "hostels": [
            "Hostel A", "Hostel B", "Hostel C", "Hostel D", "Hostel E",
            "Hostel F", "Hostel G", "Hostel H", "Hostel I", "Hostel J", "Hostel K",
            "Rani Laxmi Bai Hall (Girls)", "Ambedkar Hall (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Wing A", "Wing B"],
        "block_label": "Block / Wing"
    },
    "nit durgapur": {
        "hostels": [
            "Hall 1", "Hall 2", "Hall 3", "Hall 4", "Hall 5",
            "Hall 6", "Hall 7", "Hall 8", "Hall 9", "Hall 10", "Hall 11",
            "Mother Teresa Hall (Girls)", "Priyadarshini Hall (Girls)"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Ground Floor", "1st Floor", "2nd Floor"],
        "block_label": "Wing / Floor"
    },

    # ── BITS Pilani ──
    "bits pilani": {
        "hostels": [
            "Ram Bhavan", "Budh Bhavan", "Krishna Bhavan", "Gandhi Bhavan",
            "Shankar Bhavan", "Vyas Bhavan", "Valmiki Bhavan", "Vishwakarma Bhavan",
            "Bhagirath Bhavan", "Ranapratap Bhavan", "Ashok Bhavan", "Malviya Bhavan",
            "Meera Bhavan (Girls)", "Srinivasa Ramanujan Bhavan"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Wing D", "Ground Floor", "1st Floor", "2nd Floor"],
        "block_label": "Wing / Floor"
    },
    "bits goa": {
        "hostels": [
            "AH 1", "AH 2", "AH 3", "AH 4", "AH 5", "AH 6", "AH 7", "AH 8", "AH 9",
            "CH 1", "CH 2", "CH 3", "CH 4", "CH 5", "CH 6", "CH 7",
            "DH 1 (Girls)", "DH 2 (Girls)", "DH 3 (Girls)", "DH 4 (Girls)"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Ground Floor", "1st Floor", "2nd Floor"],
        "block_label": "Wing / Floor"
    },
    "bits hyderabad": {
        "hostels": [
            "Valmiki Bhavan", "Vyas Bhavan", "Buddh Bhavan", "Gandhi Bhavan",
            "Krishna Bhavan", "Shankar Bhavan", "Ram Bhavan", "Malviya Bhavan",
            "Meera Bhavan (Girls)", "New Girls Bhavan"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Wing A", "Wing B"],
        "block_label": "Block / Wing"
    },

    # ── VIT (Vellore, Chennai, AP, Bhopal) ──
    "vit vellore": {
        "hostels": [
            "MH-A", "MH-B", "MH-C", "MH-D", "MH-E", "MH-F", "MH-G", "MH-H",
            "MH-J", "MH-K", "MH-L", "MH-M", "MH-N", "MH-P", "MH-Q", "MH-R",
            "MH-S", "MH-T",
            "LH-A (Girls)", "LH-B (Girls)", "LH-C (Girls)", "LH-D (Girls)",
            "LH-E (Girls)", "LH-F (Girls)", "LH-G (Girls)", "LH-H (Girls)", "LH-J (Girls)", "LH-K (Girls)"
        ],
        "blocks": ["Main Block", "Tower Block", "Annex", "Floor 1-6", "Floor 7-14"],
        "block_label": "Block / Tower / Floor"
    },
    "vit chennai": {
        "hostels": [
            "MH-1", "MH-2", "MH-3", "MH-4",
            "LH-1 (Girls)", "LH-2 (Girls)", "LH-3 (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Floor 1-10"],
        "block_label": "Block / Floor"
    },
    "vit-ap": {
        "hostels": ["Boys Hostel 1", "Boys Hostel 2", "Boys Hostel 3", "Girls Hostel 1", "Girls Hostel 2"],
        "blocks": ["Block A", "Block B", "Block C", "Wing A", "Wing B"],
        "block_label": "Block / Wing"
    },
    "vit bhopal": {
        "hostels": ["Boys Hostel 1", "Boys Hostel 2", "Boys Hostel 3", "Girls Hostel 1", "Girls Hostel 2"],
        "blocks": ["Block 1", "Block 2", "Block 3", "Wing A", "Wing B"],
        "block_label": "Block / Wing"
    },

    # ── Manipal (MAHE) ──
    "manipal": {
        "hostels": [
            "Block 5 (Boys)", "Block 6 (Boys)", "Block 7 (Boys)", "Block 10 (Boys)",
            "Block 14 (Boys)", "Block 15 (Boys)", "Block 16 (Boys)", "Block 17 (Boys)",
            "Block 18 (Boys)", "Block 19 (Boys)", "Block 20 (Boys)", "Block 21 (Boys)", "Block 22 (Boys)",
            "Block 1 (Girls)", "Block 2 (Girls)", "Block 3 (Girls)", "Block 4 (Girls)",
            "Block 11 (Girls)", "Block 12 (Girls)", "Block 13 (Girls)",
            "Sharada Hostel", "New Ladies Hostel"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Floor 1", "Floor 2", "Floor 3", "Floor 4"],
        "block_label": "Wing / Floor"
    },

    # ── SRM IST ──
    "srm": {
        "hostels": [
            "Pierre Fauchard (Boys)", "Paari (Boys)", "Kaari (Boys)", "Oori (Boys)",
            "Adhiyaman (Boys)", "Nelson Mandela (Boys)", "Manoranjitham (Girls)",
            "Mullai (Girls)", "Thamarai (Girls)", "Malligai (Girls)", "Sannasi (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D", "M-Block", "Tower 1", "Tower 2"],
        "block_label": "Block / Tower"
    },

    # ── Delhi University (DU) ──
    "delhi university": {
        "hostels": [
            "Jubilee Hall", "Gwyer Hall", "Mansarowar Hostel", "Post-Graduate Men's Hostel",
            "International Students House", "Meghdoot Hostel (Girls)", "Geetanjali Hostel (Girls)",
            "Rajiv Gandhi Hostel for Girls", "Ambedkar-Ganguly Hostel", "D.S. Kothari Hostel",
            "Undergraduate Hostel for Girls (Dhaka)", "Miranda House Hostel", "SRCC Hostel",
            "St. Stephen's Hostel", "Hindu College Hostel", "Hansraj College Hostel"
        ],
        "blocks": ["Block A", "Block B", "Block C", "North Wing", "South Wing"],
        "block_label": "Block / Wing"
    },

    # ── Banaras Hindu University (BHU) ──
    "banaras hindu university": {
        "hostels": [
            "Broacha Hostel", "Birla Hostel", "Ruiya Hostel", "Morvi Hostel",
            "Dhanrajgiri Hostel", "Rajputana Hostel", "Limbdi Hostel", "Vishwakarma Hostel",
            "Vivekanand Hostel", "Bhabha Hostel", "Dalmia Hostel", "Annie Besant Hostel (Girls)",
            "Kasturba Hostel (Girls)", "Rani Laxmi Bai Hostel (Girls)", "Gargi Hostel (Girls)",
            "Maitreyi Hostel (Girls)"
        ],
        "blocks": ["Block 1", "Block 2", "Block 3", "Block 4", "Wing A", "Wing B"],
        "block_label": "Block / Wing"
    },

    # ── AIIMS (All Campuses) ──
    "aiims": {
        "hostels": [
            "UG Boys Hostel 1", "UG Boys Hostel 2", "UG Girls Hostel 1", "UG Girls Hostel 2",
            "PG Gents Hostel", "PG Ladies Hostel", "Interns Hostel", "Nursing Hostel",
            "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4", "Hostel 5", "Hostel 6",
            "Masjid Moth Hostel", "Ayurvigyan Nagar Hostel"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Wing 1", "Wing 2", "Floor 1-4"],
        "block_label": "Block / Wing"
    },

    # ── RGUKT (IIIT Basar, Nuzvid, RK Valley, Srikakulam, Ongole) ──
    "rgukt": {
        "hostels": [
            "Boys Hostel 1", "Boys Hostel 2", "Boys Hostel 3",
            "Girls Hostel 1", "Girls Hostel 2", "Girls Hostel 3",
            "Mega Boys Hostel", "Mega Girls Hostel"
        ],
        "blocks": [
            "Krishnaveni Block", "Bhima Block", "Munneru Block", "Ghataprabha Block",
            "Godavari Block", "Tungabhadra Block", "Kaveri Block", "Narmada Block",
            "Mahanadi Block", "Brahmaputra Block"
        ],
        "block_label": "River Block"
    },

    # ── IIIT Hyderabad ──
    "iiit hyderabad": {
        "hostels": [
            "Palash Nivas (OBH)", "Parijaat Nivas (Girls)", "Kadamb Nivas (NBH)",
            "Bakul Nivas", "Anand Nivas (Girls)"
        ],
        "blocks": ["North Wing", "South Wing", "East Wing", "West Wing", "Floor 1-4"],
        "block_label": "Wing / Floor"
    },

    # ── IIIT Allahabad ──
    "iiit allahabad": {
        "hostels": [
            "Boys Hostel 1 (BH1)", "Boys Hostel 2 (BH2)", "Boys Hostel 3 (BH3)",
            "Boys Hostel 4 (BH4)", "Boys Hostel 5 (BH5)",
            "Girls Hostel 1 (GH1)", "Girls Hostel 2 (GH2)", "Girls Hostel 3 (GH3)"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Ground Floor", "1st Floor", "2nd Floor"],
        "block_label": "Wing / Floor"
    },

    # ── NIFTs (All 17 campuses) ──
    "nift": {
        "hostels": [
            "In-Campus Girls Hostel", "In-Campus Boys Hostel",
            "Off-Campus Girls Hostel", "Off-Campus Boys Hostel",
            "Senior Girls Hostel", "Junior Girls Hostel"
        ],
        "blocks": ["Block A", "Block B", "Wing 1", "Wing 2", "Floor 1", "Floor 2", "Floor 3"],
        "block_label": "Block / Wing"
    },
}

# Standard Category Fallbacks for any unmapped college
DEFAULT_IIT_NIT = {
    "hostels": [
        "Boys Hostel 1", "Boys Hostel 2", "Boys Hostel 3", "Boys Hostel 4",
        "Girls Hostel 1", "Girls Hostel 2", "Girls Hostel 3",
        "Mega Boys Hostel", "Mega Girls Hostel", "PG Hostel"
    ],
    "blocks": ["Block A", "Block B", "Block C", "Wing A", "Wing B", "Wing C", "Floor 1", "Floor 2", "Floor 3"],
    "block_label": "Block / Wing"
}

DEFAULT_MEDICAL = {
    "hostels": [
        "UG Boys Hostel", "UG Girls Hostel", "PG Boys Hostel", "PG Girls Hostel",
        "Interns Hostel", "Senior Residents Hostel", "Nursing Hostel"
    ],
    "blocks": ["Block A", "Block B", "Block C", "Wing A", "Wing B", "Floor 1", "Floor 2"],
    "block_label": "Block / Wing"
}

DEFAULT_STANDARD = {
    "hostels": [
        "Boys Hostel", "Girls Hostel", "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4",
        "New Boys Hostel", "New Girls Hostel", "PG Hostel", "International Hostel"
    ],
    "blocks": [
        "Block A", "Block B", "Block C", "Block D",
        "Wing A", "Wing B", "Wing C", "Wing D",
        "Ground Floor", "1st Floor", "2nd Floor", "3rd Floor"
    ],
    "block_label": "Block / Wing / Floor"
}


def get_campus_data(college_name: str) -> dict:
    """
    Intelligently retrieves the specific hostels and blocks/wings for a given college name.
    Falls back cleanly to targeted college-type archetypes so the student is never overwhelmed.
    """
    if not college_name:
        return DEFAULT_STANDARD

    normalized = college_name.lower().strip()

    # 1. Exact or keyword match against prominent colleges
    for key, data in CAMPUS_DATA.items():
        if key in normalized:
            return data

    # 2. Archetype detection based on college keywords
    if "iit" in normalized or "indian institute of technology" in normalized:
        return DEFAULT_IIT_NIT
    if "nit" in normalized or "national institute of technology" in normalized:
        return DEFAULT_IIT_NIT
    if "iiit" in normalized or "information technology" in normalized:
        return DEFAULT_IIT_NIT
    if any(med in normalized for med in ["medical", "aiims", "dental", "nursing", "pharmacy", "hospital"]):
        return DEFAULT_MEDICAL

    # 3. Clean universal standard fallback
    return DEFAULT_STANDARD
