
# 📧 Cold Email Generator

Cold Email Generator is a powerful tool designed to automate the process of generating personalized cold emails based on job postings. It uses natural language processing and a machine learning-based language model to extract job descriptions from a given URL, align them with your portfolio, and generate well-structured cold emails to potential clients or employers.

##Example
![image](https://github.com/user-attachments/assets/3834e129-7d2a-4b0f-afa8-b55edafd12e5)


## Features
- **Job Posting Scraper**: Scrapes job postings from URLs provided by users.
- **Skills Matching**: Matches job requirements with your portfolio projects and relevant skills.
- **Personalized Cold Emails**: Automatically generates personalized cold emails based on the job description and relevant skills.
- **Streamlit Interface**: User-friendly interface built using Streamlit for easy interaction.

## Project Structure
```bash
📦 COLD EMAIL GENERATOR
├── __pycache__
├── myenv
├── resource
│   └── my_portfolio.csv  # CSV file containing your portfolio links and tech stack
├── vectorstore
├── .env  # Environment variables including Groq API key
├── app.py  # Main Streamlit app
├── chains.py  # Handles job extraction and email generation using Groq LLM
├── portfolio.py  # Loads portfolio data and matches it with job descriptions
├── requirements.txt  # Required Python libraries
└── utils.py  # Utility for cleaning scraped text
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/devil3515/Cold-Email-Generator.git
cd Cold-Email-Generator
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment for dependency management.

```bash
python3 -m venv myenv
source myenv/bin/activate  # For Linux/Mac
myenv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
All required libraries are listed in the `requirements.txt` file. Install them using pip:

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root of your project and add the following:

```
groq_api_key=YOUR_GROQ_API_KEY
```

Replace `YOUR_GROQ_API_KEY` with your actual API key from Groq.

### 5. Prepare Portfolio Data
Update the `resource/my_portfolio.csv` file with your tech stack and portfolio links. It should contain two columns:
- **Techstack**: Skills you have experience in.
- **Links**: Portfolio or project links showcasing your expertise in the respective tech stack.

### 6. Run the Application
Once everything is set up, you can run the app using Streamlit:

```bash
streamlit run app.py
```

## Usage
1. **Enter Job URL**: Input the URL of the job posting you want to target.
2. **Submit**: Click the submit button to scrape the job description and match your skills with the job.
3. **Generated Cold Email**: The app will display a tailored cold email that you can send to the employer.

## Example Output

```markdown
Dear [Employer Name],

I hope this email finds you well. My name is Abhishek, and I’m a passionate machine learning enthusiast. I came across your job posting for a [Job Role] and was excited to see that the position involves [Skill 1], [Skill 2], and [Skill 3].

In my recent projects, I’ve developed solutions such as a Twitter sentiment analysis model and a house price prediction system using neural networks. I believe my experience and passion for predictive modeling and data analysis would allow me to contribute significantly to [Company Name] in tackling [Company's Needs].

I’d love to discuss how my skill set aligns with your goals.

Best regards,  
Abhishek Kumar
```

## Technologies Used
- **Python**
- **Streamlit**: For building the front-end interface.
- **Langchain**: For constructing LLM-powered chains.
- **ChromaDB**: For managing portfolio data as a vector database.
- **Pandas**: For handling portfolio data.
- **Groq LLM**: The language model used for scraping job postings and writing emails.

## Contributing
Feel free to submit issues or pull requests if you'd like to contribute to the project.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
