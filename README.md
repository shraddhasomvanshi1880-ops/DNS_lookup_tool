🌐 DNS Lookup Tool — Discover the IP Behind Any Domain

Ever wondered what happens when you type a website's name into your browser?

Every time you visit a website, your system needs to find its IP address. This is where the Domain Name System (DNS) comes in!

🚀 DNS Lookup Tool is a beginner-friendly web application that converts domain names into IPv4 addresses using Python. It combines networking concepts with a clean, user-friendly web interface built using Flask, HTML, and CSS.

🔎 Enter a domain name, click Lookup, and discover its IP address in seconds!


✨ Features

- 🌍 Domain-to-IP Lookup  — Resolve domain names into IPv4 addresses.
- ⚡ Fast Resolution  — Uses Python's built-in 'socket' module.
- 🎨 Clean Web Interfac — A simple, attractive design using HTML and CSS.
- 🐍 Python Powered — Implements real domain name resolution.
- 🛡️ Error Handling — Displays helpful messages for empty or invalid domains and DNS resolution failures.
- 🖥️ Interactive Experience — Enter a domain directly in your browser instead of using a command-line interface.


🖼️ How It Works
        User Enters Domain
                |
       Flask Web Application
                |
       Python socket Module
                |
       DNS Resolution
                |
       IPv4 Address Retrieved
                |
       Display Result on Screen

      
🔍 Example

Input:
www.google.com
Output:
Domain Name: www.google.com
IP Address: 142.251.150.119

🛠️ Technologies Used

Python: Core programming and DNS lookup logic 
Flask: Connects Python functionality to the web interface
Socket Module: Resolves domain names into IP addresses 
HTML5: Structures the web page 
CSS3: Styles the interface and improves presentation 


⚙️ Getting Started

Follow these steps to run the project on your local machine.

1. Clone the Repository

git clone YOUR_REPOSITORY_URL

Replace 'YOUR_REPOSITORY_URL' with your GitHub repository URL.

2. Open the Project Folder

cd DNS_lookup_tool

3. Install Flask

bash
python -m pip install flask

4. Run the Application

python app.py

5. Open It in Your Browser

Visit:

http://127.0.0.1:5000


🎉 Your DNS Lookup Tool is ready to use!


📁 Project Structure


DNS_lookup_tool/
│
├── app.py                 # Python DNS lookup and Flask logic
│
├── templates/
│   └── index.html         # Web page structure
│
├── static/
│   └── style.css          # Styling and visual design
│
└── README.md              # Project documentation

🧠 What I Learned

Building this project helped me explore practical concepts in computer networking and web development:

- Understanding DNS and domain name resolution.
- Learning the difference between domain names and IP addresses.
- Using Python's 'socket' module and 'getaddrinfo()' function.
- Building a web application with Flask.
- Connecting HTML forms with Python backend logic.
- Applying exception handling using 'try-except'.
- Organizing a project using templates and static files.

🎯 Why This Project?

This project demonstrates how **computer networking concepts can be implemented through a real, interactive application.

Instead of only learning DNS theoretically, this tool provides a practical way to explore how domain names are resolved into IP addresses.

It is a useful beginner project for students interested in Computer Networks, Python Programming, and Web Development.

🚀 Future Improvements

Here are some features that could make the project even more powerful:

- Support for both IPv4 and IPv6 addresses.
- Display multiple IP addresses for a domain.
- Add DNS record lookups such as A, AAAA, MX, and TXT.
- Add a lookup history feature.
- Improve the interface with loading indicators and animations.
- Display clearer diagnostics for DNS resolution errors.

👩‍💻 Author

Shraddha Somvanshi

💡Explore. Learn. Resolve. Discover the network behind every domain.
