import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(
            temperature = 0,
            groq_api_key = os.getenv("groq_api_key"),
            model_name = "llama-3.1-70b-versatile"
            )
    def extract_jobs(self,cleaned_data):                  ###Funnction to extract the jobs from the links
        prompt_scrape = PromptTemplate.from_template(
            """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}
        ### INSTRUCTION:
        The scraped text is from the career's page of a website.
        Your job is to extract the job postings and return them in JSON format containing the 
        following keys: `role`, `experience`, `skills` and `description`.
        Only return the valid JSON.
        ### VALID JSON (NO PREAMBLE):    
        """
        )
        chain_extract = prompt_scrape| self.llm
        res = chain_extract.invoke({"page_data": cleaned_data})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Content too big, Unable to parse Jobs")
        return res if isinstance(res,list) else [res]
    

    def write_email(self,job,links):                     ###Function for the email writing
        prompt_email = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}
        
        ### INSTRUCTION:
        You are Abhishek, a student passionate about machine learning and data analysis.
        You are writing a cold email as part of your coursework or internship to the client 
        regarding the job mentioned above, showcasing your understanding of how machine learning 
        solutions can fulfill their needs. You will demonstrate how your knowledge, projects,
        and experience with tools like neural networks, data preprocessing, and predictive modeling
        can contribute to solving real-world challenges.If applicable, mention some of the projects 
        you've worked on, like Twitter sentiment analysis, house price prediction, or fruit classification.
        Make sure to align your projects with the client's needs.
        Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
        Remember you are Abhishek, a student passionate about machine learning and data analysis.
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
        
        """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("groq_api_key"))