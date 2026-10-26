from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class AboutView(View):
    def get(self,request):
        data={
            "ID":"A101",
            "Full_name":"Arun dev",
            "profession":"Software Engineer",
            "Bio": " A passionate developer and researcher building scalable web applications.",
            "DOB":"1995-01-01",
            "Email":"arun.dev@example.com",
            "Phone":"9876543211",
            "Location":"cochin",
            "Github URL":"http://github.com/arundev",
            "LinkedIn URL":"http://linkedin.com/in/arundev",
        }
        return JsonResponse(data)
    
class EducationView(View):
    def get(self,request):
        data={
            "Id":"E101",
            "Institution":"Indira Gandhi Institute of Engineering and Technology",
            "Degree":"B.Tech in Computer Science",
            "university":"ktu",
            "Location":"kochi",
            "Start Date":"2022-08-01",
            "End Date":"2026-05-01",
            "GPA":"8.5",
            "Description":"Studied various computer science subjects and completed projects in web development and machine learning."
        }
        return JsonResponse(data)    

class ProjectsView(View):
    def get(self,request):
        projects=[
            {
            
                "Id":1,
                "title":"DietLense",
                "short_description":"A web application that uses computer vision to analyze food images and provide nutritional information.",
                "long_description":"DietLense is a web application that leverages computer vision techniques to analyze images of food and provide users with detailed nutritional information. The application allows users to upload images of their meals, and it uses machine learning algorithms to identify the food items present in the image. Once identified, the application retrieves nutritional data such as calories, macronutrients, and micronutrients from a comprehensive database and presents it to the user in an easy-to-understand format. DietLense aims to help users make informed dietary choices and maintain a healthy lifestyle by providing accurate and personalized nutritional insights.",
                "technologies_used":["Python","Django","OpenCV","TensorFlow","HTML","CSS","JavaScript"],
                "live_url": "http://dietlense.example.com",
                "github_url": "http://github.com/dietlense",
                "image_url": "http://example.com/images/dietlense.png",
                "featured":"Yes",
           
            },
            {
                "Id":2,
                "title":"Interview prep Blog",
                "short_description":"A blog platform that provides resources and tips for preparing for technical interviews.",
                "long_description":"A blog platform that offers a wide range of resources, articles, and tips to help individuals prepare for technical interviews.",
                "technologies_used":["Python","Django","HTML","CSS","JavaScript"],
                "featured":"No",

            }
        ]
        return JsonResponse(projects,safe=False)  

class SkillsView(View):
    def get(self,request):
        skills=[
            {
                "Id":1,
                "Skill_name":"Python",
                "Category":"Programming Language",
                "Proficiency":"Advanced",
                "years_of_experience":4
            },
            {
                "Id":2,
                "Skill_name":"Django",
                "category":"Backend",
                "Proficiency":"Intermediate",
                "years_of_experience":3
            },
            {
                "Id":3,
                "Skill_name":"JavaScript",
                "category":"Frontend",
                "Proficiency":"Intermediate",
                "years_of_experience":3
            }
        ]
        return JsonResponse(skills,safe=False)

class ExperienceView(View):
    def get(self,request):
        experience=[
            {
                "Id":1,
                "Job Title":"Software Engineer",
                "Company_Name":"TcS",
                "Location":"Bangalore",
                "Employment Type":"Full-time",
                "Start Date":"2020-01-01",
                "End Date":"2022-12-31",
                "currently_working":"No",
                "Description":"Worked on developing and maintaining web applications using Django and React."
            },
            {
                "Id":2,
                "Job Title":"Senior Software Engineer",
                "Company_Name":"Infosys",
                "Location":"Bangalore",
                "Employment Type":"Full-time",
                "Start Date":"2023-01-01",
                "End Date":"Present",
                "currently_working":"Yes",
                "Description":"Working on developing and maintaining web applications using Django and React."      
            }
        ]
        return JsonResponse(experience,safe=False)

class CertificationView(View):
    def get(self,request):
        certifications=[
            {
                "Id":1,
                "Certification Name":"AWS Certified Solutions Architect",
                "Issuing Organization":"Amazon Web Services",
                "Issue Date":"2021-06-01",
            },
            {
                "Id":2,
                "Certification Name":"Certified Kubernetes Administrator",
                "Issuing Organization":"Cloud Native Computing Foundation",
                "Issue Date":"2022-03-15",
            }
        ]
        return JsonResponse(certifications,safe=False)

class ServicesView(View):
    def get(self,request):
        services=[
            {
                "Id":1,
                "Service_Name":"Web Development",
                "Description":"Building responsive and scalable web applications using modern technologies.",
                "technologies_used":["Python","Django","React","HTML","CSS","JavaScript"],
            },
            {
                "Id":2,
                "Service_Name":"Web Development",
                "Description":"Building responsive and scalable web applications using modern technologies.",
                "technologies_used":["Python","Django","React","HTML","CSS","JavaScript"],

            },
            {
                "Id":3,
                "Service_Name":"Web Development",
                "Description":"Building responsive and scalable web applications using modern technologies.",
                "technologies_used":["Python","Django","React","HTML","CSS","JavaScript"],    
            }
        ]  
        return JsonResponse(services,safe=False)  
    