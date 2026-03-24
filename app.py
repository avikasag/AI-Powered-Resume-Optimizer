from flask import Flask, render_template, request, jsonify
from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

HF_API_KEY = os.getenv("HF_API_KEY")

# ✅ provider="auto" lets HuggingFace pick the best available provider
client = InferenceClient(
    api_key=HF_API_KEY,
    provider="auto",
)

def query_huggingface(job_desc, resume_points):
    try:
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=[
                {
                    "role": "system",
                    "content": """You are an expert ATS resume optimizer. 
When given a job description and resume points, you will:
1. Organize the rewritten resume points by company/institution section exactly as provided by the user.
2. Rewrite each bullet point to be ATS-friendly using keywords from the job description.
3. Start each bullet with a strong action verb.
4. Quantify achievements where possible to demonstrate impact. For example, "Increased sales by 20%" or "Managed a team of 5".
5. Remove any unnecessary words or jargon to keep the points concise, aim for 17-20 words max.
6. Add relevant skills and tools mentioned in the job description to the bullet points where appropriate.
7. Ensure the rewritten points are tailored to the specific job description, highlighting the most relevant experience and skills for the role.
8. Add extra resume points (1 0r 2) if necessary to better match the job description, but keep the total number of points per company/institution reasonable (no more than 5-6 points per section) to maintain readability and focus on the most important achievements.
9. At the end, add a Skills Section with the most relevant skills for the job based on the job description.

Always follow this exact output format:

[Company/Institution Name]:
- Rewritten bullet point 1
- Rewritten bullet point 2

[Next Company/Institution Name]:
- Rewritten bullet point 1
- Rewritten bullet point 2

Skills Section:
- Technical Skills: skill1, skill2, skill3
- Tools & Technologies: tool1, tool2, tool3
- Soft Skills: skill1, skill2, skill3

Do not add any extra explanation or commentary outside this format."""
                },
                {
                    "role": "user",
                    "content": f"""Here is the Job Description:
{job_desc}

Here are my resume points organized by company/institution:
{resume_points}

Please rewrite my resume points section by section (one section per company/institution), and at the end provide the best suited Skills Section based on the job description."""
                }
            ],
            max_tokens=1000,
        )
        return completion.choices[0].message.content

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return f"Error: {str(e)}"

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return f"Error: {str(e)}"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.json
    job_desc = data.get("job_description", "")
    resume_points = data.get("resume_points", "")

    if not job_desc or not resume_points:
        return jsonify({"result": "Error: Please provide both job description and resume points."})

    result = query_huggingface(job_desc, resume_points)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)