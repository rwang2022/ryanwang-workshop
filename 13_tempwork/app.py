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
    job_and_prob = {}

    with open("occupations.csv", "r") as f:

            csv_reader = csv.reader(f, delimiter=",")
            next(csv_reader)
            sum = 0.0


            for value in csv_reader:
                            if(value[0] == "Total"):
                                    continue
                            sum = sum + (10 * float(value[1])) #adding the values
                            job_and_prob[sum] = value[0]

            randNum = random.randrange(998) #random number
            for percent in job_and_prob.keys():
                if(percent >= randNum):

                    '''
                    So you can convert a csv_reader into a list of lists
                    we just need to use the to list command
                    list() so this
                    list(csv.reader(open("occupations.csv", "r"), delimiter=","))[1:-1]
                    is us reading in the file again and converting it's content to a list of lists and this works fine because it's just
                    two items per row
                    '''
                    return render_template("template.html", jobAndPercentage=list(csv.reader(open("occupations.csv", "r"), delimiter=","))[1:-1], chosen_job=job_and_prob[percent])

                    #if it's below the value that means it's in between it and the value before it -
                    #elsewise we know it's above the value so we don't actually need another logic operator

            '''
            There is a dictionary command that turns the dictionary into a list of tuples
            dict.items()

            >>> d = { 'a': 1, 'b': 2, 'c': 3 }
            >>> d.items()
            [('a', 1), ('c', 3), ('b', 2)]
            '''
            
if __name__ == "__main__":
    app.debug = True
    app.run()
