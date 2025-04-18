import requests
from time import sleep

def fetch_jobs_json(tech):
    print(f"\n🔍 Searching Jobs for {tech.upper()} on Internshala")
    page = 1
    total_jobs = 0
    index = 1

    while True:
        url = f"https://internshala.com/jobs_ajax/keywords-{tech}/page-{page}"
        headers = {"User-Agent": "Mozilla/5.0"}

        try:
            res = requests.get(url, headers=headers)
            if res.status_code != 200 or not res.text.strip():
                print(f"⚠️ Failed to fetch page {page} or empty response.")
                break

            data = res.json()

            jobs = (
                data.get("seo", {})
                    .get("rich_text_item_list", {})
                    .get("itemListElement", [])
            )

            if not jobs:
                break

            for job in jobs:
                name = job.get("name", "N/A")
                url = job.get("url", "N/A")

                print(f"\n{index}. {name}")
                print(f"   Link: {url}")
                index += 1
                total_jobs += 1

            page += 1
            sleep(1)

        except Exception as e:
            print(f"❌ Error parsing JSON: {e}")
            break

    print(f"\n✅ {tech.upper()} Jobs Found: {total_jobs}")
    print("=" * 40)

if __name__ == "__main__":
    techs = input("Enter technologies to search (comma-separated): ").strip().split(",")
    for tech in techs:
        fetch_jobs_json(tech.strip())
