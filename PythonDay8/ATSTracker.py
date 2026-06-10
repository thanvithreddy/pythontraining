class Candidate:
    def __init__(self, cid, name, skills):
        self.cid = cid
        self.name = name
        self.skills = set(skills)
        self.jobs = []

    def apply_job(self, job):
        self.jobs.append(job)
class JobOpening:
    def __init__(self, job_id, title, required_skills):
        self.job_id = job_id
        self.title = title
        self.required_skills = set(required_skills)
class RecruitmentManager:
    def __init__(self):
        self.candidates = []         
        self.interview_scores = {}   
    def add_candidate(self, candidate):
        self.candidates.append(candidate)
    def conduct_interview(self, candidate, tech_score, hr_score):
        overall = (tech_score + hr_score) / 2
        self.interview_scores[candidate.cid] = overall
    def shortlist(self, job):
        print(f"\n--- Selected Candidates for {job.title} ---")
        for candidate in self.candidates:
            if (job in candidate.jobs and
                job.required_skills.issubset(candidate.skills) and
                self.interview_scores.get(candidate.cid, 0) >= 70):

                print(
                    f"ID: {candidate.cid}, "
                    f"Name: {candidate.name}, "
                    f"Score: {self.interview_scores[candidate.cid]}"
                )

job1 = JobOpening(101, "Python Developer", {"Python", "SQL"})
c1 = Candidate(1, "Rahul", {"Python", "SQL", "Java"})
c2 = Candidate(2, "Priya", {"Python"})
c3 = Candidate(3, "Amit", {"Python", "SQL"})
c1.apply_job(job1)
c2.apply_job(job1)
c3.apply_job(job1)
manager = RecruitmentManager()
manager.add_candidate(c1)
manager.add_candidate(c2)
manager.add_candidate(c3)
manager.conduct_interview(c1, 85, 80)
manager.conduct_interview(c2, 65, 70)
manager.conduct_interview(c3, 90, 85)
manager.shortlist(job1)

