import random

push_exercise = ["bench press", "incline bench press", "overhead press", "pushup", "dip", "tricep pushdown"," push press", "floor press", "skull crusher"]

pull_exercise = ["seated row", "lat pulldown", "bentover row", "pull-up", "chin-up", "bicep curl", "face pull", "pendlay row", "upright row"]

squat_exercise = ["barbell back squat", "barbell front squat", "goblet squat", "jumping squat", "sumo squat", "overhead squat", "single leg squat", "box squat"]

lunge_exercise = ["forward lunge", "backward lunge", "curtsy lunge", "dumbbell stepup", "rearfoot elevated split squat", "front foot elevated split squat", "side lunge", "walking lunge"]

carry_exercise = ["farmers carry", "frontrack carry", "overhead carry", "suitcase carry", "goblet carry", "zercher carry"]

hinge_exercise = ["conventional deadlift", "romanian deadlift", "sumo deadlift", "single leg romanian deadlift", "good morning", "hip thrust"]


def workout_gen():
    push = random.choice(push_exercise)
    pull = random.choice(pull_exercise)
    squat = random.choice(squat_exercise)
    lunge = random.choice(lunge_exercise)
    carry = random.choice(carry_exercise)
    hinge = random.choice(hinge_exercise)
	
    workout = {
        "Push exercise": push,
        "Pull exercise": pull,
        "Squat exercise": squat,
        "Lunge exercise": lunge,
        "Carry exercise": carry,
        "Hinge exercise": hinge
    }

    return workout

if __name__ == "__main__":
    workout = workout_gen()
    print(workout)


