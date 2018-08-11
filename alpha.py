import alpha1
import pandas as pd

def recommend(path_description,resume_data_path,read_type):
    # print("QQQEEEEXX")


    # print("SSSSEEEE")

    final_skills,sorted_index = getskills() #function to read all skills and their sorted index from file
    # print('8')
    #read resume data from csv file
    data = pd.read_csv(resume_data_path)
    # print('9')
    #extract skills from job decription document
    print("path_description",path_description)
    job_skills = alpha1.description_manipulation(path_description,read_type)

    print('job',job_skills)
    job_skills = alpha1.match(final_skills,sorted_index,job_skills)

    matched_skills= []
    for i in range(len(data)):
        matched_skills.append(alpha1.matchSkills(job_skills,data['skills'][i]))

    print(len(matched_skills))
    matched_perc = []
    ab = len(job_skills)
    print('ab',ab,job_skills)
    for i in range(len(matched_skills)):
        matched_perc.append(len(matched_skills[i])/ab)
        # print(data['filename'][i],len(known_skills[i]))

    db1 = { 'filename':     data['filename'],
            'known_skills': data['skills'],
            'mathced_skills':matched_skills,
            'perc_match':   matched_perc    }

    df = pd.DataFrame(db1, columns = ['filename', 'known_skills', 'mathced_skills', 'perc_match'])
    df.to_csv('allasdf.csv')
    return df
    # list1 = alpha1.sort_list(data['filename'], known_len)[-10:]
    # print(list1[:30])
 #   return alpha1.sort_list(data['filename'], known_len)

def getskills():
    print("EEEE")
    final_skills = alpha1.readSkills('all_skills.txt')
    final_skills=sorted(final_skills, key=lambda s: s.lower())
    print(final_skills[:10])
    # print(final_skills)
    print("EWWE")
    sorted_index = alpha1.alphabet_index_list(final_skills)
    print('index',sorted_index)
    print("QQE")
    # print(final_skills,sorted_index)
    return final_skills,sorted_index
# def sorting(known_skills):
#     a = sorted(known_skills, key=lambda s: len(s))
#




def resumeTocsv(resumes_dir_path):
    document_list = []
    documents = []
    for path, subdirs, files in os.walk(resumes_dir_path):
        for name in files:
            if(os.path.splitext(os.path.join(path, name))[1] == ".docx" or os.path.splitext(os.path.join(path, name))[1] == ".DOCX"):
                document_list.append(os.path.join(path, name))
                document = Document(os.path.join(path, name))
                documents.append(document)
    print(len(documents))

    a = experince_count(documents)

    print(a)
