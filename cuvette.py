import requests
import time

def fetch_jobs_with_skill(skill="rust", delay=0, remote_only=False):
    base_url = "https://api.cuvette.tech/api/v1/externaljobs"
    page = 1
    matched_jobs = []
    skill = skill.lower()

    while True:
        response = requests.get(base_url, params={"search": "", "pageNumber": page})
        if response.status_code != 200:
            print(f"❌ Failed to fetch page {page}. Status code: {response.status_code}")
            break

        data = response.json()
        jobs = data.get("data", [])

        if not jobs:
            print("✅ No more jobs found. Stopping.")
            break

        for job in jobs:
            job_skills = job.get("skills", "").lower()
            job_type = job.get("type", "").lower()

            if skill in job_skills:
                if remote_only and "remote" not in job_type:
                    continue  # Skip non-remote jobs

                matched_jobs.append({
                    "title": job["title"],
                    "company": job["companyName"],
                    "location": job["location"],
                    "type": job["type"],
                    "salary": job["salary"],
                    "experience": job["requiredExperience"],
                    "skills": job["skills"],
                    "link": job["redirectLink"]
                })

        print(f"🔎 Page {page} scanned. Matched jobs so far: {len(matched_jobs)}")
        page += 1
        time.sleep(delay)  # Slow down between requests

    return matched_jobs

if __name__ == "__main__":
    skill_input = input("Enter skill to search (default: rust): ").strip() or "rust"
    remote_input = input("Only remote jobs? (y/N): ").strip().lower() == "y"
    results = fetch_jobs_with_skill(skill_input, remote_only=remote_input)

    if results:
        print(f"\n🎯 Found {len(results)} job(s) with skill '{skill_input}'{' (Remote only)' if remote_input else ''}:\n")
        for i, job in enumerate(results, 1):
            print(f"{i}. {job['title']} at {job['company']} ({job['location']})")
            print(f"   Skills: {job['skills']}")
            print(f"   Salary: {job['salary']}, Experience: {job['experience']}")
            print(f"   Type: {job['type']}")
            print(f"   Link: {job['link']}\n")
    else:
        print(f"🚫 No jobs found with skill: {skill_input}{' (Remote only)' if remote_input else ''}")
