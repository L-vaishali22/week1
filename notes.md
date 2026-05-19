Kafka + Docker + Python Producer
Date: 11-05-2026
INDEX
1. Hum Kya Bana Rahe Hain?
2. Tools Jo Use Kar Rahe Hain
3. Docker Kya Hai?
4. YAML Kya Hai?
5. Kafka Kya Hai?
6. Kafka Ke Concepts
7. Hamara Setup
8. Python Producer
9. Poora Code
10. Commands
11. Kya Achieve Kiya?


1. HUM KYA BANA RAHE HAIN?
Image Mein Tha:                Hum Bana Rahe Hain:
──────────────────────────────────────────────────
Factory Machines               Python Script
      │                              │
OPC Server                         │
      │                              │
   Kafka                 ==>      Kafka
      │                              │
  Database                        AWS S3
      │                              │
  Dashboard                      Dashboard
Data Pipeline Kya Hoti Hai?
Jaise Paani Ki Pipeline:
──────────────────────────────────────────────────
Tanki      →    Pipe    →    Ghar
(Source)       (Path)       (Destination)

Hamari Data Pipeline:
──────────────────────────────────────────────────

[Python Script] → [Kafka] → [Terminal/S3/Dashboard]
  (Producer)      (Pipe)      (Consumer)

Matlab:
└── Python Script = Factory Sensor Ka Kaam Karega
└── Kafka = Data Ko Ek Jagah Se Doosri Jagah Le Jayega
└── Terminal = Abhi Dekhne Ke Liye
└── S3/Dashboard = Future Mein Store Karne Ke Liye
Week By Week Plan
Week 1: Python → Kafka → Terminal     ✅ DONE
Week 2: Kafka → AWS S3 Store
Week 3: PySpark Se Data Clean
Week 4: Airflow Se Automate
Week 5: Dashboard Banana
Week 6: API Banana
Week 7: Monitoring
Week 8: Poora System Integrate
2. TOOLS JO USE KAR RAHE HAIN
Tool 1: Docker
──────────────────────────────────────────────────
Kya Hai: Applications Ko Container Mein Chalana
Kyun:    Kafka Ko Easily Setup Karne Ke Liye
Port:    -

Tool 2: Kafka
──────────────────────────────────────────────────
Kya Hai: Message/Data Pipeline System
Kyun:    Factory Data Ko Handle Karne Ke Liye
Port:    9092

Tool 3: Zookeeper
──────────────────────────────────────────────────
Kya Hai: Kafka Ka Manager
Kyun:    Kafka Ko Chalane Ke Liye Zaroori
Port:    2181

Tool 4: Python
──────────────────────────────────────────────────
Kya Hai: Programming Language
Kyun:    Data Banane Aur Kafka Ko Bhejne Ke Liye
Port:    -
3. DOCKER KYA HAI?
Simple Definition:
──────────────────────────────────────────────────
Docker = Ek Aisa System
         Jo Applications Ko
         Ek Box (Container) Mein Bandh Karke
         Chalata Hai

Real Life Example:
──────────────────────────────────────────────────
Jaise Tiffin Box:
└── Har Cheez Apne Box Mein Band
└── Ek Box Doosre Ko Effect Nahi Karta
└── Kahin Bhi Le Jaao - Same Rahega

Docker Mein:
└── Har Application Apne Container Mein
└── Ek Application Doosre Ko Effect Nahi Karta
└── Kisi Bhi Computer Pe Chalao - Same Rahega
Docker Compose Kya Hai?
Simple Definition:
──────────────────────────────────────────────────
Docker Compose = Ek Recipe File
                 Jo Batati Hai:
                 - Kaun Si Apps Chalani Hain
                 - Kaise Chalani Hain
                 - Kaun Sa Port Use Karna Hai

Real Life Example:
──────────────────────────────────────────────────
Jaise Shopping List:
└── Kya Kya Chahiye  = Applications
└── Kitna Chahiye    = Resources
└── Kahan Rakhna Hai = Ports

File Ka Naam: docker-compose.yml
File Ka Type: YAML Format
Docker Ke Important Commands
Command 1: docker-compose up
──────────────────────────────────────────────────
Kya Karta Hai:
└── docker-compose.yml File Padhta Hai
└── Saari Applications Start Karta Hai
└── Logs Terminal Mein Dikhata Hai

Command 2: docker ps
──────────────────────────────────────────────────
Kya Karta Hai:
└── Dikhata Hai Kaun Si Apps Chal Rahi Hain
└── Status Batata Hai (Up/Down)
└── Ports Dikhata Hai

Command 3: docker-compose down
──────────────────────────────────────────────────
Kya Karta Hai:
└── Saari Applications Band Karta Hai
└── Containers Delete Karta Hai
└── Network Delete Karta Hai
4. YAML KYA HAI?
Simple Definition:
──────────────────────────────────────────────────
YAML = Ek Tarika Hai Settings Likhne Ka
       Jo Humans Ko Easily Samajh Aaye

Kahan Use Hota Hai:
└── Docker Compose Files
└── Kubernetes Files
└── CI/CD Pipeline Files
└── Configuration Files
YAML Ke 4 Basic Rules
Rule 1: LOWERCASE
──────────────────────────────────────────────────
Sab Chhote Letters Mein Likhte Hain

Sahi:    services: ✅
Galat:   Services: ❌

──────────────────────────────────────────────────
Rule 2: INDENTATION (SPACES)
──────────────────────────────────────────────────
Parent-Child Relation Spaces Se Dikhate Hain

services:            → 0 Space  (Level 1)
  zookeeper:         → 2 Spaces (Level 2)
    image: xyz       → 4 Spaces (Level 3)
      port: 2181     → 6 Spaces (Level 4)

Real Life:
└── Jaise Family Tree
└── Dada → Papa → Beta
└── Har Level Pe 2 Space Zyada

──────────────────────────────────────────────────
Rule 3: COLON (:)
──────────────────────────────────────────────────
key: value Format Mein Likhte Hain

port: 2181
│      │
│      └── Value (Kya Hai)
└── Key (Kiska Hai)

──────────────────────────────────────────────────
Rule 4: DASH (-)
──────────────────────────────────────────────────
List Items Ke Liye Dash Use Karte Hain

ports:
  - "2181:2181"   ← Pehla Item
  - "9092:9092"   