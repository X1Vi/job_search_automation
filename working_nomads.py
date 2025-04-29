import requests

def fetch_jobs_by_tech(tech: str, from_index: int = 0, size: int = 100):
    url = "https://www.workingnomads.com/jobsapi/_search"
    
    payload = {
        "track_total_hits": True,
        "from": from_index,
        "size": size,
        "_source": [
            "company",
            "company_slug",
            "category_name",
            "locations",
            "location_base",
            "salary_range",
            "salary_range_short",
            "number_of_applicants",
            "instructions",
            "id",
            "external_id",
            "slug",
            "title",
            "pub_date",
            "tags",
            "source",
            "apply_option",
            "apply_email",
            "apply_url",
            "premium",
            "expired",
            "use_ats",
            "position_type",
            "annual_salary_usd"
        ],
        "sort": [
            { "premium": { "order": "desc" } },
            { "pub_date": { "order": "desc" } }
        ],
        "query": {
            "bool": {
                "must": {
                    "query_string": {
                        "query": f"\"{tech}\"",
                        "fields": [
                            "title^2",
                            "description",
                            "company"
                        ]
                    }
                }
            }
        },
        "min_score": 2
    }

    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        hits = response.json().get("hits", {}).get("hits", [])
        for job in hits:
            source = job["_source"]
            print(f"{source['title']} at {source['company']} - https://www.workingnomads.com/jobs/{source['slug']}")
    else:
        print(f"Failed to fetch jobs: {response.status_code}")
        print(response.text)

# Example usage:
tech = "golang"
print(f"search query: {tech}")
fetch_jobs_by_tech(tech)
