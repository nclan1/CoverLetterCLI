

import argparse

def create_cover_letter(date, position_title, company_name, skill_1, skill_2, skill_3, project_1, project_1_desc, project_2, project_2_desc, strength_1, strength_2, position_res, company_mission):

    template = f"""
    Chanrithya Nolan Ngim
    ngimcnolan@gmail.com
    781-708-5881
    {date}
    
    Dear {company_name} Hiring Team,
    I am writing to express my strong interest in the {position_title} position at {company_name}! As a 3rd year student in Computer Science at Boston University, I am excited about the opportunity to contribute and especially learn from the team at {company_name}. Throughout my academic journey, I have developed a solid foundation in {skill_1}, {skill_2}, and {skill_3}. I have applied these skills in various projects, including {project_1} where {project_1_desc}. Additionally, in {project_2}, I have {project_2_desc}.
    
    These experiences have honed my ability to {strength_1} and {strength_2}, which I believe aligns well with the {company_name}'s values and mission. I am excited to not only {position_res}, but also learn from the experts at {company_name} and collaborate with the team! 
    
    I'm super passionate about {company_mission} and look forward to discuss how I can contribute to {company_name}'s success! Thank you for considering my application and hopefully we can discuss further soon.
    
    Sincerely,
    Chanrithya Nolan Ngim
    """
    return template
        

def main():
    date = input("dd/mm/yyyy: ")
    position_title = input("what position?: ")
    company_name = input("what company?: ")
    skill_1 = input("developed a strong foundation in (skill_1): ")
    skill_2 = input(",(skill_2): ")
    skill_3 = input(", and (skill_3): ")
    project_1 = input("applied these skills in various projects including (project_1):")
    project_1_desc = input("where (project_1_desc): ")
    project_2 = input("additionally, in (project_2): ")
    project_2_desc = input("I have (project_2_desc): ")
    strength_1 = input("my ability to (strength_1): ")
    strength_2 = input("and (strength_2): ")
    position_res = input("excited to not only (position_responsibility): ")
    company_mission = input("I'm super passionate about (company_mission): ")

    cover_letter = create_cover_letter(date, position_title, company_name, skill_1, skill_2, skill_3, project_1, project_1_desc, project_2, project_2_desc, strength_1, strength_2, position_res, company_mission)
    print(cover_letter)
    
    with open('cover_letter.text', 'w') as f:
        f.write(cover_letter)
    
if __name__ == "__main__":
    main()