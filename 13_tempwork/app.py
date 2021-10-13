#Team Duck on a Rock - Jonathan W. [Loki] ,Patrick G. [Chris], Ryan W. [Jack] | Period 2
#SoftDev
#K13 - Template for Success/Jinja templates and flask/We worked in new trios to create a template to display jobs and percentages on the website as well as displaying the randomly selected job.
#2021-10-09

from flask import Flask, render_template
import csv
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Testing"


@app.route("/occupyflaskst")
def occupy():
    # will contain the all the key-value pairs (occupation-probability pairs) 
    data_dict = {}

    with open("data/occupations.csv", "r") as f:
            reader = csv.DictReader(f)

            # reads through each line and fills up data_dict with the key-value pairs
            for line in reader:
                data_dict[line["Job Class"]] = float(line["Percentage"])

            # removes the "Total" entry, which is useless
            del data_dict["Total"] 
            
            jobs = list(data_dict.keys())
            probs = list(data_dict.values())

            # randomList is a "list" of one choice (because k=1) among the jobs with weight probs
            # chosen_job is simply the  first (and only value) of randomList
            randomList = random.choices(jobs, weights=probs, k=1)
            chosen_job = randomList[0]
            print(chosen_job)

            return render_template(
                "tablified.html", 
                data_dict=data_dict,
                jobs=jobs, 
                chosen_job=chosen_job,
                chosen_job_prob=data_dict[chosen_job],
                )


if __name__ == "__main__":
    app.debug = True
    app.run()
