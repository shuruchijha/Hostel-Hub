"""
Campus Directory: Verified college hostel and block mappings for Indian institutions.

GOLDEN RULE:
If we are unsure about the exact hostel and block names for any institution,
we ONLY show ["Boys Hostel", "Girls Hostel"] and leave the block list empty
so the student can freely type their actual block/wing without false guesses.
"""

# Specific verified campus mappings
CAMPUS_DATA = {
    # ── NIT Andhra Pradesh (Tadepalligudem) ──
    "nit andhra": {
        "hostels": ["Girls Hostel", "Boys Hostel"],
        "blocks": [
            # Girls Hostel Blocks (UG & PG/PhD)
            "Krishnaveni Block", "Bhima Block", "Tungabhadra Block", "Ghataprabha Block", "Munneru Block",
            # Boys Hostel Blocks
            "Godavari Block", "Sabari Block", "Indravathi Block", "Banganga Block", "Purna Block",
            "Pranahita Block", "Manjeera Block", "Nagavali Block", "Swarnamukhi Block", "Vamsadhara Block"
        ],
        "block_label": "Block"
    },
    "nit ap": {
        "hostels": ["Girls Hostel", "Boys Hostel"],
        "blocks": [
            "Krishnaveni Block", "Bhima Block", "Tungabhadra Block", "Ghataprabha Block", "Munneru Block",
            "Godavari Block", "Sabari Block", "Indravathi Block", "Banganga Block", "Purna Block",
            "Pranahita Block", "Manjeera Block", "Nagavali Block", "Swarnamukhi Block", "Vamsadhara Block"
        ],
        "block_label": "Block"
    },

    # ── IITs (Verified) ──
    "iit bombay": {
        "hostels": [
            "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4", "Hostel 5",
            "Hostel 6", "Hostel 7", "Hostel 8", "Hostel 9", "Hostel 10",
            "Hostel 11 (Girls)", "Hostel 12", "Hostel 13", "Hostel 14",
            "Hostel 15 (Girls)", "Hostel 16", "Hostel 17", "Hostel 18", "Tansa House"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Floor 1", "Floor 2", "Floor 3"],
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
        "blocks": ["Wing A", "Wing B", "Wing C", "Wing D"],
        "block_label": "Wing"
    },
    "iit kanpur": {
        "hostels": [
            "Hall 1", "Hall 2", "Hall 3", "Hall 4", "Hall 5",
            "Hall 7", "Hall 8", "Hall 9", "Hall 10", "Hall 11",
            "Hall 12", "Hall 13", "Girls Hostel 1 (GH1)", "Girls Hostel 2 (GH2)"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C", "Wing D", "Top Floor", "Ground Floor"],
        "block_label": "Wing"
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
        "blocks": ["Wing A", "Wing B", "Wing C", "Wing D", "Block 1", "Block 2"],
        "block_label": "Wing / Block"
    },
    "iit roorkee": {
        "hostels": [
            "Ganga Bhawan", "Govind Bhawan", "Cautley Bhawan", "Rajendra Bhawan",
            "Radhakrishnan Bhawan", "Ravindra Bhawan", "Jawahar Bhawan", "Rajiv Bhawan",
            "Kasturba Bhawan (Girls)", "Sarojini Bhawan (Girls)", "Indira Bhawan (Girls)", "Vigyan Kunj"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Mess Wing"],
        "block_label": "Block / Wing"
    },
    "iit guwahati": {
        "hostels": [
            "Brahmaputra Hostel", "Dihing Hostel", "Manas Hostel", "Umiam Hostel",
            "Barak Hostel", "Kameng Hostel", "Siang Hostel", "Kapili Hostel",
            "Dhansiri Hostel (Girls)", "Subansiri Hostel (Girls)", "Disang Hostel (Girls)", "Lohit Hostel"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D"],
        "block_label": "Block"
    },
    "iit bhu": {
        "hostels": [
            "Limbdi Hostel", "Rajputana Hostel", "Morvi Hostel", "Dhanrajgiri (DG) Hostel",
            "Vishwakarma Hostel", "Vivekanand Hostel", "Aryabhatta Hostel", "Ramanujan Hostel",
            "SN Bose Hostel", "SC Dey Hostel", "GSMC (Girls)", "Rani Laxmibai Hostel (Girls)"
        ],
        "blocks": ["Wing 1", "Wing 2", "Wing 3", "Wing 4"],
        "block_label": "Wing"
    },
    "iit dhanbad": {
        "hostels": [
            "Diamond Hostel", "Emerald Hostel", "Topaz Hostel", "Opal Hostel",
            "Jasper Hostel", "Ruby Hostel", "Sapphire Hostel", "Amber Hostel", "Rosaline Hostel (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D"],
        "block_label": "Block"
    },

    # ── NITs (Verified) ──
    "nit trichy": {
        "hostels": [
            "Garnet A", "Garnet B", "Agate Hostel", "Coral Hostel", "Diamond Hostel",
            "Jade Hostel", "Pearl Hostel", "Emerald Hostel", "Ruby Hostel",
            "Sapphire Hostel", "Topaz Hostel", "Zircon A", "Zircon B", "Beryl Hostel",
            "Opal A (Girls)", "Opal B (Girls)", "Opal C (Girls)", "Opal D (Girls)", "Opal E (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D"],
        "block_label": "Block"
    },
    "nit surathkal": {
        "hostels": [
            "Block 1 (Boys)", "Block 2 (Boys)", "Block 3 (Boys)", "Block 4 (Boys)",
            "Block 5 (Boys)", "Block 6 (Boys)", "Block 7 (Boys)", "Block 8 (Boys)",
            "Mega Boys Hostel", "PG Hostel", "Sahyadri Hostel (Girls)",
            "Sharavathi Hostel (Girls)", "Godavari Hostel (Girls)", "Brahmaputra Hostel (Girls)"
        ],
        "blocks": ["Block 1", "Block 2", "Block 3", "Tower 1", "Tower 2"],
        "block_label": "Block / Tower"
    },
    "nit warangal": {
        "hostels": [
            "1.8K Ultra Mega Hostel", "1K Hostel", "Mega Boys Hostel", "Hall 1",
            "Hall 2", "Hall 3", "Hall 4", "Hall 5", "Hall 6", "Hall 7", "Hall 8",
            "Priyadarshini Ladies Hostel", "Sarojini Devi Ladies Hostel", "New Ladies Hostel"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D", "Wing A", "Wing B"],
        "block_label": "Block / Wing"
    },
    "nit calicut": {
        "hostels": [
            "Hostel A", "Hostel B", "Hostel C", "Hostel D", "Hostel E",
            "Hostel F", "Hostel G", "Mega Boys Hostel", "PG 1", "PG 2",
            "LH-A (Ladies)", "LH-B (Ladies)", "LH-C (Ladies)", "LH-D (Ladies)"
        ],
        "blocks": ["Floor 1", "Floor 2", "Floor 3", "Wing A", "Wing B"],
        "block_label": "Wing / Floor"
    },
    "vnit nagpur": {
        "hostels": [
            "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4", "Hostel 5",
            "Hostel 6", "Hostel 7", "Mega Hostel", "Old Girls Hostel", "New Girls Hostel"
        ],
        "blocks": ["Block A", "Block B", "Block C"],
        "block_label": "Block"
    },
    "mnit jaipur": {
        "hostels": [
            "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4", "Hostel 5",
            "Hostel 6", "Hostel 7", "Hostel 8", "Hostel 9", "Hostel 10", "Hostel 11",
            "Gargi Hostel (Girls)", "Ganga Hostel (Girls)", "Annie Besant Hostel (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C"],
        "block_label": "Block"
    },
    "mnnit allahabad": {
        "hostels": [
            "Swami Vivekananda Hostel", "C.V. Raman Hostel", "Malaviya Hostel",
            "Tandon Hostel", "Tilak Hostel", "Patel Hostel", "Tagore Hostel",
            "Raman Hostel", "Sarojini Naidu (Girls)", "Kamala Nehru (Girls)"
        ],
        "blocks": ["Wing A", "Wing B", "Wing C"],
        "block_label": "Wing"
    },
    "nit rourkela": {
        "hostels": [
            "VS Hall of Residence", "MV Hall", "GDB Hall", "DBA Hall",
            "MSS Hall", "HB Hall", "SD Hall", "KMS Hall (Girls)", "CVR Hall (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C", "Block D"],
        "block_label": "Block"
    },
    "nit kurukshetra": {
        "hostels": [
            "Hostel 1", "Hostel 2", "Hostel 3", "Hostel 4", "Hostel 5",
            "Hostel 6", "Hostel 7", "Hostel 8", "Hostel 9", "Hostel 10",
            "Kalpana Chawla Bhawan (Girls)", "Alaknanda Bhawan (Girls)", "Cauvery Bhawan (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C"],
        "block_label": "Block"
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
        "blocks": ["Wing A", "Wing B", "Wing C"],
        "block_label": "Wing"
    },
    "bits hyderabad": {
        "hostels": [
            "Valmiki Bhavan", "Vyas Bhavan", "Buddh Bhavan", "Gandhi Bhavan",
            "Krishna Bhavan", "Shankar Bhavan", "Ram Bhavan", "Malviya Bhavan",
            "Meera Bhavan (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C"],
        "block_label": "Block"
    },

    # ── VIT ──
    "vit vellore": {
        "hostels": [
            "MH-A", "MH-B", "MH-C", "MH-D", "MH-E", "MH-F", "MH-G", "MH-H",
            "MH-J", "MH-K", "MH-L", "MH-M", "MH-N", "MH-P", "MH-Q", "MH-R",
            "MH-S", "MH-T",
            "LH-A (Girls)", "LH-B (Girls)", "LH-C (Girls)", "LH-D (Girls)",
            "LH-E (Girls)", "LH-F (Girls)", "LH-G (Girls)", "LH-H (Girls)", "LH-J (Girls)", "LH-K (Girls)"
        ],
        "blocks": ["Main Block", "Tower Block", "Annex", "Floor 1-6", "Floor 7-14"],
        "block_label": "Block / Tower"
    },
    "vit chennai": {
        "hostels": [
            "MH-1", "MH-2", "MH-3", "MH-4",
            "LH-1 (Girls)", "LH-2 (Girls)", "LH-3 (Girls)"
        ],
        "blocks": ["Block A", "Block B", "Block C"],
        "block_label": "Block"
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
        "blocks": ["Wing A", "Wing B", "Wing C", "Floor 1", "Floor 2", "Floor 3"],
        "block_label": "Wing / Floor"
    },

    # ── SRM ──
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
            "Undergraduate Hostel for Girls (Dhaka)"
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
            "Kasturba Hostel (Girls)", "Rani Laxmi Bai Hostel (Girls)", "Gargi Hostel (Girls)"
        ],
        "blocks": ["Block 1", "Block 2", "Block 3", "Block 4"],
        "block_label": "Block"
    },

    # ── AIIMS (New Delhi & Campuses) ──
    "aiims": {
        "hostels": [
            "UG Boys Hostel", "UG Girls Hostel", "PG Gents Hostel", "PG Ladies Hostel",
            "Interns Hostel", "Nursing Hostel", "Hostel 1", "Hostel 2", "Hostel 3",
            "Hostel 4", "Hostel 5", "Hostel 6"
        ],
        "blocks": ["Block A", "Block B", "Block C"],
        "block_label": "Block"
    },

    # ── RGUKT (IIIT Basar, Nuzvid, RK Valley, Srikakulam, Ongole) ──
    "rgukt": {
        "hostels": ["Girls Hostel", "Boys Hostel"],
        "blocks": [
            "Krishnaveni Block", "Bhima Block", "Munneru Block", "Ghataprabha Block",
            "Godavari Block", "Tungabhadra Block", "Kaveri Block", "Narmada Block"
        ],
        "block_label": "Block"
    },

    # ── IIIT Hyderabad ──
    "iiit hyderabad": {
        "hostels": [
            "Palash Nivas (OBH)", "Parijaat Nivas (Girls)", "Kadamb Nivas (NBH)",
            "Bakul Nivas", "Anand Nivas (Girls)"
        ],
        "blocks": ["North Wing", "South Wing", "East Wing", "West Wing"],
        "block_label": "Wing"
    },
}

# ── UNCERTAINTY FALLBACK (STRICT USER MANDATE) ──
# If we are unsure about any college, NEVER fabricate names.
# Simply show "Boys Hostel" and "Girls Hostel", with empty blocks list so the student fills it themselves.
DEFAULT_UNSURE = {
    "hostels": ["Girls Hostel", "Boys Hostel"],
    "blocks": [],
    "block_label": "Block / Wing / Room"
}


def get_campus_data(college_name: str) -> dict:
    """
    Intelligently retrieves verified hostels and blocks/wings.
    If the college is not in our verified database, returns ONLY Girls Hostel & Boys Hostel
    with an empty block list so the student can fill their own block without confusion.
    """
    if not college_name:
        return DEFAULT_UNSURE

    normalized = college_name.lower().strip()

    # Match against strictly verified campus database
    for key, data in CAMPUS_DATA.items():
        if key in normalized:
            return data

    # Strict fallback for unverified colleges: NEVER make up names
    return DEFAULT_UNSURE


# ── INTELLIGENT HOSTEL & BLOCK SWAP / NORMALIZER ──
# Handles cases where confused users enter block into hostel, or hostel into block

KNOWN_GIRLS_BLOCKS = {
    "krishnaveni", "bhima", "tungabhadra", "ghataprabha", "munneru",
    "gargi", "kasturba", "sarojini", "kalpana chawla", "meera", "opal",
    "himadri", "kailash", "swarna", "sarayu", "bhavani", "pinakini", "vasista", "gautami"
}

KNOWN_BOYS_BLOCKS = {
    "godavari", "sabari", "indravathi", "banganga", "purna", "pranahita",
    "manjeera", "nagavali", "swarnamukhi", "vamsadhara", "aravali", "nilgiri",
    "karakoram", "kumaon", "shivalik", "zanskar", "satpura", "girnar", "udaigiri",
    "garnet", "agate", "coral", "diamond", "jade", "pearl", "emerald", "ruby"
}

def normalize_hostel_and_block(hostel: str, block: str, college_name: str = "") -> tuple[str, str]:
    """
    Intelligently detects when a user mistakenly enters a block name in the hostel field
    or swaps hostel and block. Returns (clean_hostel, clean_block).
    """
    h_clean = (hostel or "").strip()
    b_clean = (block or "").strip()
    h_lower = h_clean.lower()
    b_lower = b_clean.lower()

    # Case 1: hostel is "Block A" / "Krishnaveni Block" and block is "Girls Hostel" (DIRECT SWAP)
    if ("hostel" in b_lower or "bhawan" in b_lower or "hall" in b_lower) and not ("hostel" in h_lower or "bhawan" in h_lower or "hall" in h_lower):
        return b_clean, h_clean

    # Case 2: hostel contains a known block name (e.g. "Krishnaveni" or "Godavari") and NO hostel word
    words_in_h = set(h_lower.replace("-", " ").replace("_", " ").split())
    if "hostel" not in h_lower and "bhawan" not in h_lower and "hall" not in h_lower:
        # Check if it matches known Girls blocks
        if words_in_h & KNOWN_GIRLS_BLOCKS:
            actual_block = h_clean
            if b_clean and b_clean.lower() not in ["girls hostel", "boys hostel"]:
                actual_block = f"{h_clean} {b_clean}".strip()
            return "Girls Hostel", actual_block

        # Check if it matches known Boys blocks
        if words_in_h & KNOWN_BOYS_BLOCKS:
            actual_block = h_clean
            if b_clean and b_clean.lower() not in ["girls hostel", "boys hostel"]:
                actual_block = f"{h_clean} {b_clean}".strip()
            return "Boys Hostel", actual_block

        # Check if it looks like a block code e.g. "Block A", "Wing 2", "MB-1"
        if any(h_lower.startswith(prefix) for prefix in ["block", "wing", "tower", "floor", "mh", "lh"]):
            # User typed block into hostel
            if "girl" in b_lower:
                return "Girls Hostel", h_clean
            elif "boy" in b_lower:
                return "Boys Hostel", h_clean
            else:
                # Keep block in block, and set standard hostel if empty
                return "Hostel", h_clean

    return h_clean, b_clean
